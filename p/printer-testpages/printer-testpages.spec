Name: printer-testpages
Version: 2.0
Release: alt3

Summary: Test pages for printers
Source: %name.tar.bz2

License: GPL-2.0-only
Group: Publishing
Url: https://www.cups.org

BuildArch: noarch

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
* Wed Sep 16 2026 Anton Farygin <rider@altlinux.org> 2.0-alt3
- updated CUPS test page to the last upstream PS version (CUPS 1.3.11)
- fixed License tag (GPL -> GPL-2.0-only)
- added Url tag
- dropped unused BuildRequires (spec installs prebuilt pages, no build step)

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


