Summary:	Support for messaging encryption with PGP
Summary(pl):	Wsparcie dla szyfrowania wiadomo¶ci za pomoc± PGP
Name:		xemacs-mailcrypt-pkg
%define 	srcname	mailcrypt
Version:	3.5.6
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://prdownloads.sourceforge.net/mailcrypt/%{srcname}-%{version}.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://mailcrypt.sourceforge.net/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-mail-lib-pkg
Requires:	xemacs-fsf-compat-pkg
Requires:	xemacs-base-pkg
BuildRequires:	xemacs
BuildRequires:	autoconf
BuildRequires:	xemacs-mail-lib-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Support for messaging encryption with PGP.

%description -l pl
Wsparcie dla szyfrowania wiadomo¶ci za pomoc± PGP.

%prep
%setup -q -n %{srcname}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	lispdir=%{_datadir}/xemacs-packages/lisp/mailcrypt


# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README.gpg README ONEWS NEWS INSTALL ChangeLog
%{_infodir}/*info*
%dir %{_datadir}/xemacs-packages/lisp/mailcrypt
%{_datadir}/xemacs-packages/lisp/mailcrypt/*.el*
