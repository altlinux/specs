Name: eget
Version: 6.0
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
%doc README.md
%_bindir/eget

%changelog
* Thu Mar 30 2023 Vitaly Lipatov <lav@altlinux.ru> 6.0-alt1
- eget: add --second-latest support
- eget: add support -O when wildcards are used
- eget: parse data-file= too
- eget: implement --check-mirrors
- eget: rewrite mirror checking to minimize requests
- eget: add support for URL in form file:/ or /path
- eget: make correct URL if file part parsed by mask separately
- eget: improve options parsing
- eget: improve help text
- eget: fix list for direct URL without mask
- eget: add checking for extra args

* Sun Sep 04 2022 Vitaly Lipatov <lav@altlinux.ru> 5.9-alt1
- eget: add --check support for check url if accessible
- eget: improve UserAgent line
- eget: check for wildcard only if separated mask is missed
- eget: fix absolute path on a site

* Wed Apr 27 2022 Vitaly Lipatov <lav@altlinux.ru> 5.8-alt1
- eget: fix making file url from site url and filename

* Mon Apr 18 2022 Vitaly Lipatov <lav@altlinux.ru> 5.7-alt1
- eget: fix url from page filtering

* Sun Apr 17 2022 Vitaly Lipatov <lav@altlinux.ru> 5.6-alt1
- eget: clean warnings
- eget: add support for -O- and -O/dev/stdout
- add script to prepare patches for eepm

* Fri Apr 15 2022 Vitaly Lipatov <lav@altlinux.ru> 5.5-alt1
- eget: don't add latest slash, slit file to lines by tags
- eget: add examples to help

* Fri Apr 08 2022 Vitaly Lipatov <lav@altlinux.ru> 5.4-alt1
- add README.md
- eget: workaround quotes

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
