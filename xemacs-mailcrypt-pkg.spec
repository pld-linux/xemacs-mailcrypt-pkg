Summary:	Support for messaging encryption with PGP
Summary(pl.UTF-8):	Wsparcie dla szyfrowania wiadomości za pomocą PGP
Name:		xemacs-mailcrypt-pkg
%define 	srcname	mailcrypt
Version:	3.5.6
Release:	4
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://dl.sourceforge.net/mailcrypt/%{srcname}-%{version}.tar.gz
# Source0-md5:	3078e0674f70a345217799f623a5a436
Patch0:		%{name}-info.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://mailcrypt.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	texinfo
BuildRequires:	xemacs
BuildRequires:	xemacs-mail-lib-pkg
Requires:	xemacs
Requires:	xemacs-base-pkg
Requires:	xemacs-fsf-compat-pkg
Requires:	xemacs-mail-lib-pkg
Conflicts:	xemacs-sumo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Support for messaging encryption with PGP.

%description -l pl.UTF-8
Wsparcie dla szyfrowania wiadomości za pomocą PGP.

%prep
%setup -q -n %{srcname}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__autoconf}
%configure
%{__make} -j1 \
	MAKEINFO="%{_bindir}/makeinfo --no-split"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	INFOFILES=mailcrypt.info \
	lispdir=%{_datadir}/xemacs-packages/lisp/mailcrypt

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc README.gpg README ONEWS NEWS INSTALL ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/mailcrypt
%{_datadir}/xemacs-packages/lisp/mailcrypt/*.el*
%{_infodir}/*.info*
