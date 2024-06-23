Name: eget
Version: 7.11
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
* Sun Jun 23 2024 Vitaly Lipatov <lav@altlinux.ru> 7.11-alt1
- eget: fix header quoting issue
- eget: don't add duplicate URL with the same CID
- eget: get latest CID entry from IPFS_DB
- eget: add EGET_IPFS_FORCE_LOAD enables downloading ever if the target is exists in IPFS DB

* Thu Apr 18 2024 Vitaly Lipatov <lav@altlinux.ru> 7.10-alt1
- added parameters needed to replace wget with eget in winetricks (eterbug #16749)
- eget: improve message about unaccessible ipfs
- eget: add pinata.cloud ipfs gateway, disable local Brave ipfs instance
- eget: use only selected ipfs gateway when EGET_IPFS_GATEWAY is set

* Mon Apr 08 2024 Vitaly Lipatov <lav@altlinux.ru> 7.9-alt1
- eget: decode &amp; html entity
- eget: add support square brackets as wildcards
- eget: select IPFS gateway if gateway mode is forced
- eget: add list url support for .md (markdown)
- eget: always use filter for separated mask
- eget: fix get response 404 from CloudFlare via range 0-0 downloading (#1)

* Thu Mar 28 2024 Vitaly Lipatov <lav@altlinux.ru> 7.8-alt1
- eget: replace --check with --check-url and --check-site
- eget: fix --check using (also allow --check for backward compatibility)
- eget: hide missed Brave's ipfs error
- eget: add support for a new IPFS gateways

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 7.7-alt1
- eget: put PROGNAME set to init_eget func
- eget: add hack for construct full url from related Location
- eget: add is_abs_path and use it
- eget: add have_end_slash and use it

* Sun Jul 02 2023 Vitaly Lipatov <lav@altlinux.ru> 7.6-alt1
- README.md: add commend about install with eepm
- eget: add --get-ipfs-cid to help, fix for case when IPFS is disabled (no accessible gateway)
- eget: get_cid_by_url(): return only correct CID
- eget: fix concatenate_url_and_filename()

* Fri May 12 2023 Vitaly Lipatov <lav@altlinux.ru> 7.5-alt1
- eget: allow download file from http://site/page/ URL (with latest slash)
- eget: print about unknown options

* Fri May 05 2023 Vitaly Lipatov <lav@altlinux.ru> 7.4-alt1
- eget: add -H (--header) support
- eget: fix for brave go-ipfs
- eget: add support for UTF-8 filename in Content-disposition
- eget: check filename in Content-Disposition in case insensivity
- eget: fix github json handling (some servers return optimized nonformatted answer)
- eget: use correct http download backend for ipfs via gateway

* Sat Apr 22 2023 Vitaly Lipatov <lav@altlinux.ru> 7.3-alt1
- eget: improve globbing symbol translation
- eget: disable checking for magic CID if IPFS is used
- eget: check Brave IPFS after local ipfs in IPFS auto mode
- eget: restore missed quotes after href

* Sat Apr 15 2023 Vitaly Lipatov <lav@altlinux.ru> 7.2-alt1
- eget: fix get real url again
- eget: fix embedded mode
- eget: don't return put error in gateway mode
- eget: add --compressed (send Accept-Encoding and decode result)

* Wed Apr 12 2023 Vitaly Lipatov <lav@altlinux.ru> 7.1-alt1
- eget: fix --check
- eget: add filename support in ipfs://Qm...filename=real.name
- eget: hide IPFS mode status when IPFS mode is disabled
- eget: add --quiet alias for -q
- eget: add --verbose support
- eget --check: allow --verbose
- eget: fix quiet mode

* Wed Apr 12 2023 Vitaly Lipatov <lav@altlinux.ru> 7.0-alt1
- eget: add --get-ipfs-cid, --get-real-url, --get-filename, --get-response
- eget: add ipfs mode support (EGET_IPFS={disabled,auto,brave,local,gateway)
- eget: add ipfs:// support
- eget: add EGET_IPFS_DB file support (save after download, get when download)
- eget: use scat only for get remote page content
- eget: add support for EGET_BACKEND={curl,wget}, refactoring wget/curl detection
- eget: stop recursion with EGET_ vars
- eget: add hack to get headers ever if HEAD is not allowed

* Mon Apr 10 2023 Vitaly Lipatov <lav@altlinux.ru> 6.1-alt1
- eget: improve is_url checking
- eget: disable checking for globbing symbol ? in URL
- eget: fix URL concatenation
- eget: add -4/-6 support (force use IPv4/6)
- eget: comment out set_quiet for --check
- eget: add support for single quote
- eget: update which workaround
- eget: update tty functions

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
