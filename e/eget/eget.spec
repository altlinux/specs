Name: eget
Version: 4.1
Release: alt1

Summary: wget like downloader wrapper with wildcard support

License: AGPLv3
Group: Networking/WWW
Url: https://github.com/Etersoft/eget

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/Etersoft/eget.git
Source: ftp://updates.etersoft.ru/pub/Korinf/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

#Requires: wget
#Requires: curl

%description
eget is a wget like downloader wrapper. It supports download urls with wildcard.

It supports wget or curl as backend.

%prep
%setup

%install
install -D eget %buildroot%_bindir/eget

%files
%_bindir/eget

%changelog
* Mon Aug 16 2021 Vitaly Lipatov <lav@altlinux.ru> 4.1-alt1
- eget: add hack for skip mask if there ?...= (some args)
- eget: fix get list of releases

* Mon Oct 26 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0-alt1
- full rewrite to support curl (and detect curl or wget is available)

* Fri Oct 23 2020 Vitaly Lipatov <lav@altlinux.ru> 3.4-alt1
- eget: add --latest support
- eget: add support for https://github.com/owner/project urls
- tools_eget: don't strict mask with begin of the line

* Mon Oct 19 2020 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt1
- eget: fix ? in sed

* Mon Jun 18 2018 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt1
- eget: fix href case accept

* Sun Dec 10 2017 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt1
- test_glob: add test for [ab]
- eget: add initial help

* Sat Nov 11 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt1
- improve test for eget, add check for globbing
- eget: full rewrite, use filter_glob

* Sat Nov 11 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- rewrite eget

* Fri Nov 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus
