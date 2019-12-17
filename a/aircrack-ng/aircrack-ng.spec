%define _unpackaged_files_terminate_build 1

Name: aircrack-ng
Version: 1.5.2
Release: alt2

Summary: 802.11 WEP and WPA-PSK key recovery program
License: GPLv2+
Group: Networking/Other

Url: http://aircrack-ng.org

# https://github.com/aircrack-ng/aircrack-ng.git
Source: %name-%version.tar
Patch0: %name-%version-alt-build.patch

BuildRequires: gcc-c++
BuildRequires: libssl-devel libsqlite3-devel
BuildRequires: libnl-devel
BuildRequires: libpcre-devel
BuildRequires: libpcap-devel
BuildRequires: zlib-devel
BuildRequires: ethtool
BuildRequires: python2.7(distutils)

Requires: iw rfkill ethtool

%description
Aircrack is an 802.11 WEP and WPA-PSK keys cracking program that can
recover keys once enough data packets have been captured.
It implements the standard FMS attack along with some optimizations
like KoreK attacks, thus making the attack much faster compared to
other WEP cracking tools. In fact aircrack is a set of tools for
auditing wireless networks.

%prep
%setup
%patch0 -p1

# change python shebangs to python2
find . -name '*.py' | xargs sed -i \
	-e '1s|^#!/usr/bin/env python$|#!/usr/bin/env python2|' \
	-e '1s|^#!/usr/bin/python$|#!/usr/bin/python2|' \
	%nil

find scripts -type f | xargs sed -i \
	-e '1s|^#!/usr/bin/env python$|#!/usr/bin/env python2|' \
	-e '1s|^#!/usr/bin/python$|#!/usr/bin/python2|' \
	%nil

%build
%autoreconf
%configure --with-sqlite3 --with-experimental --with-ext-scripts
%make_build

%install
%makeinstall_std

%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
mkdir -pv %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* %buildroot%python_sitelibdir/
%endif

%files
%_bindir/*
%_sbindir/*
%_libdir/*.so*
%_man1dir/*
%_man8dir/*
%python_sitelibdir/*
%_defaultdocdir/%name

%changelog
* Tue Dec 17 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.2-alt2
- Fixed build with python.

* Tue Jan 22 2019 Egor Zotov <egorz@altlinux.org> 1.5.2-alt1
- Update to upstream version 1.5.2
- Don't install airgraph-ng

* Thu Sep 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt1
- Updated to upstream version 1.3.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1-alt2.qa1
- NMU: rebuilt for debuginfo.

* Tue Dec 21 2010 Timur Aitov <timonbl4@altlinux.org> 1.1-alt2
- Add iw in dependence

* Tue Oct 12 2010 Timur Aitov <timonbl4@altlinux.org> 1.1-alt1
- new version

* Sun Oct 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.0-alt3
- fix installing of airolib-ng

* Tue Sep 08 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.0-alt2
- 1.0

* Sat Aug 15 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.0-alt1.rc4
- 1.0-rc4

* Thu May 28 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.0-alt1.rc3
- 1.0-rc3

* Sun Mar 01 2009 Maxim Ivaniv <redbaron at altlinux.org> 1.0-alt1.rc2
- Version bump to 1.0-rc2

* Mon Jul 30 2007 Alex V. Myltsev <avm@altlinux.ru> 0.9.1-alt1
- new version: critical security fix (remote execution), please upgrade
- more attacks, better SMP handling, bug fixes

* Thu Apr 12 2007 Alex V. Myltsev <avm@altlinux.ru> 0.7-alt1
- 0.7: many new features/attacks, bug fixes.

* Wed Nov 22 2006 Alex V. Myltsev <avm@altlinux.ru> 0.6.2-alt1
- 0.6.2: bug fixes. arpforge-ng is replaced by packetforge-ng.

* Fri Sep 22 2006 Alex V. Myltsev <avm@altlinux.ru> 0.6.1-alt1
- Initial build for Sisyphus.

