Summary: NoScript extension for Firefox
Name: firefox-addon-noscript
Version: 11.2.11
Release: alt1
Source: {73a6fe31-595d-460b-a920-fcc0f8843232}.xpi
License: GPLv3+
Group: Networking/WWW
Url: https://noscript.net
BuildArch: noarch
BuildRequires: rpm-build-firefox
Provides: firefox-noscript = %EVR
Obsoletes: firefox-noscript < %EVR

%description
This package contains %summary.

%install
mkdir -p %buildroot%firefox_noarch_extensionsdir
install -pm644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/

%files
%firefox_noarch_extensionsdir/*.xpi

%changelog
* Thu Aug 12 2021 Dmitry V. Levin <ldv@altlinux.org> 11.2.11-alt1
- 10.1.7.2 -> 11.2.11.
- Overhauled packaging, renamed to firefox-addon-noscript.

* Wed Oct 02 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 10.1.7.2-alt2
- Fixed build without rpm-build-palemoon.

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 10.1.7.2-alt1
- New version (ALT #34305)

* Mon May 23 2016 Andrey Cherepanov <cas@altlinux.org> 2.9.0.11-alt1
- New version (supports Firefox <= 48.0)

* Sun Mar 20 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2.9.0.7-alt2
- Fix errors in spec

* Sun Mar 20 2016 Hihin Ruslan <ruslandh@altlinux.ru> 2.9.0.7-alt1
- Version 2.9.0.7

* Sat Jun 06 2015 Andrey Cherepanov <cas@altlinux.org> 2.6.9.26-alt1
- New version

* Wed Oct 30 2013 Andrey Cherepanov <cas@altlinux.org> 2.6.8.4-alt1
- New version

* Wed Dec 19 2012 Andrey Cherepanov <cas@altlinux.org> 2.6.4.1-alt1
- New version 2.6.4.1

* Wed Jan 18 2012 Alexey Gladkov <legion@altlinux.ru> 2.2.6-alt1
- New version (2.2.6).

* Thu Aug 04 2011 Alexey Gladkov <legion@altlinux.ru> 2.1.2.5-alt1
- New version (2.1.2.5).

* Fri Apr 08 2011 Alexey Gladkov <legion@altlinux.ru> 2.1.0.1-alt1
- New version (2.1.0.1)

* Sun Jan 24 2010 Alexey Gladkov <legion@altlinux.ru> 1.9.9.39-alt1
- New version (1.9.9.39)

* Thu Jun 04 2009 Alexey Gladkov <legion@altlinux.ru> 1.9.3.3-alt1
- New version (1.9.3.3)

* Mon Jul 07 2008 Alexey Gladkov <legion@altlinux.ru> 1.7.6-alt1
- first build for ALT Linux.
