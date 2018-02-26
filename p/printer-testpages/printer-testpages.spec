Name: printer-testpages
Version: 2.0
Release: alt2

Summary: Test pages for printers
Source: %name.tar.bz2

License: GPL
Group: Publishing

BuildArch: noarch

# Automatically added by buildreq on Fri May 26 2006
BuildRequires: fonts-type1-urw ghostscript-classic ghostscript-module-X ghostscript-utils transfig

%description
This package contains some example PS pages for printer testing

%prep
%setup -q -n %name

%install
%__install -d $RPM_BUILD_ROOT%_datadir/%name
cp -a * $RPM_BUILD_ROOT%_datadir/%name

%files
%_datadir/%name

%changelog
* Fri May 26 2006 Stanislav Ievlev <inger@altlinux.org> 2.0-alt2
- fixed testpage printing on new ghostscript

* Mon Aug 09 2004 Stanislav Ievlev <inger@altlinux.org> 2.0-alt1
- replace bitmap based logo with vector based.

* Thu Feb 13 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt3.1
- fixed text on testpage again (testpage.fig also)

* Mon Feb 10 2003 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt3
- fixed testpage.ps (testpage.fig unchanged)

* Mon Oct 21 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt2
- change URL

* Thu Nov 15 2001 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt1
- Initial release for ALT


