Name: eget
Version: 5.3
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
* Wed Apr 06 2022 Vitaly Lipatov <lav@altlinux.ru> 5.3-alt1
- eget: add --no-check-certificate support
- eget: add --user-agent support

* Sun Apr 03 2022 Vitaly Lipatov <lav@altlinux.ru> 5.2-alt1
- eget: use sort --version-sort for ordering (fix 99 > 100)
- eget: use Content-disposition for downloaded filename

* Thu Oct 28 2021 Vitaly Lipatov <lav@altlinux.ru> 5.1-alt1
- eget: add / in the end of URL to avoid redirect

* Tue Aug 24 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0-alt1
- eget: make list always returns absolute URL
- eget: fix double slash in URL to download
- eget: don't fall in download by mask without a mask or if we have a direct url
- eget: allow separated mask for urls
- eget: concatenate filenames with base url if need

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
