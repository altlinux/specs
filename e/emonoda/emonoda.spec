%define modulename emonoda

Name: emonoda
Version: 2.1.36
Release: alt1

Summary: The set of tools to organize and management of your torrents

Group: File tools
License: GPLv3
Url: https://github.com/mdevaev/emonoda

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/mdevaev/emonoda/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

Provides: rtfetch
Obsoletes: rtfetch

# manually removed: python3-module-pycairo python3-module-pygobject3 python3-module-zmq pythonium python3-module-Cython0.18 libdb4-devel mailcap 
# manually removed:  ruby ruby-stdlibs
# Automatically added by buildreq on Sun Jul 19 2015
# optimized out: python3 python3-base python3-module-greenlet python3-module-pycparser 
BuildRequires: python3-module-chardet python3-module-nose python3-module-setuptools

BuildRequires: python3-dev python3-module-Cython 

# do not require by findreq...
Requires: python3-module-yaml

%description
The set of tools to organize and management of your torrents.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/emdiff
%_bindir/emfile
%_bindir/emfind
%_bindir/emload
%_bindir/emrm
%_bindir/emconfetti-demo
%_bindir/emconfetti-tghi
%_bindir/emupdate
%_bindir/emhook-rtorrent-collectd-stat
%_bindir/emhook-rtorrent-manage-trackers
%_bindir/emhook-transmission-redownload

%python3_sitelibdir/%modulename/
%python3_sitelibdir/%name-%version-*.egg-info

%changelog
* Sat Feb 25 2023 Vitaly Lipatov <lav@altlinux.ru> 2.1.36-alt1
- new version 2.1.36 (with rpmrb script)

* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 2.1.35-alt1
- new version 2.1.35 (with rpmrb script)

* Mon Feb 14 2022 Vitaly Lipatov <lav@altlinux.ru> 2.1.33-alt1
- new version 2.1.33 (with rpmrb script)

* Sun Feb 28 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.32-alt1
- new version 2.1.32 (with rpmrb script)

* Wed Jan 15 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.29-alt1
- new version 2.1.29 (with rpmrb script)

* Mon Mar 25 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.26-alt1
- new version 2.1.26 (with rpmrb script)

* Sun Mar 24 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.25-alt1
- new version 2.1.25 (with rpmrb script)

* Tue Dec 25 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.23-alt1
- new version 2.1.23 (with rpmrb script)

* Mon Nov 26 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.21-alt1
- new version 2.1.21 (with rpmrb script)

* Sat Jun 16 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.13-alt1
- new version 2.1.13 (with rpmrb script)

* Tue Mar 20 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.48-alt1
- new version 2.0.48 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.19-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 14 2015 Vitaly Lipatov <lav@altlinux.ru> 1.9.19-alt1
- fixed #34: cut short lines by terminal width
- implemented option emload.set_customs
- term conveyor: ordered summary lines

* Sat Jul 25 2015 Vitaly Lipatov <lav@altlinux.ru> 1.9.17-alt2
- fix buildreqs (for p7)

* Sat Jul 25 2015 Vitaly Lipatov <lav@altlinux.ru> 1.9.17-alt1
- new version
 + issue 33: fixed error messages about broken torrents
 + emfind: fixed behaviour on broken symlinks
 + verbose init errors
 + fixed #35: empty log on stdout/stderr redirection
 + dump config as yaml
 + fixed #36: Added option another_data_root_dirs for core/emfind

* Sun Jul 19 2015 Vitaly Lipatov <lav@altlinux.ru> 1.9.13-alt1
- initial build for ALT Linux Sisyphus (formely rtfetch)
