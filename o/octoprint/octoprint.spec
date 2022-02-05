%define _localstatedir %_var
%define  srcname OctoPrint
#%%def_disable check

Name:    octoprint
Version: 1.6.1
Release: alt5

Summary: OctoPrint is the snappy web interface for your 3D printer
License: AGPL-3.0
Group:   Development/Python3
URL:     https://github.com/OctoPrint/OctoPrint

Packager: Anton Midyukov <antohami@altlinux.org>

BuildArch: noarch

# Source-url: https://github.com/OctoPrint/OctoPrint/archive/refs/tags/%version.tar.gz
Source: %srcname-%version.tar
Source1: octoprint.service
Source2: octoprint.init
Source3: octoprint-16x16.png
Source4: octoprint-32x32.png
Source5: octoprint-48x48.png
Source6: octoprint.desktop
Source7: octoprint.conf

Patch: octoprint-1.6.1-alt-fix.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-markdown

%if_disabled check
%else
BuildRequires: python3-module-pytest
BuildRequires: python3-module-ddt
BuildRequires: python3-module-flask
BuildRequires: python3-module-flask-assets
BuildRequires: python3-module-flask-babel
BuildRequires: python3-module-flask-login
BuildRequires: python3-module-future
BuildRequires: python3-module-netaddr
BuildRequires: python3-module-netifaces
BuildRequires: python3-module-yaml
BuildRequires: python3-module-mock
BuildRequires: python3-module-wrapt
BuildRequires: python3-module-pkginfo
BuildRequires: python3-module-frozendict
BuildRequires: python3-module-sarge
BuildRequires: python3-module-serial
BuildRequires: python3-module-watchdog
BuildRequires: python3-module-pylru
BuildRequires: python3-module-emoji
BuildRequires: python3-module-unidecode
BuildRequires: python3-module-regex
BuildRequires: python3-module-tornado
BuildRequires: python3-module-cachelib
BuildRequires: python3-module-blinker
BuildRequires: python3-module-psutil
BuildRequires: python3-module-filetype
BuildRequires: python3-module-pip
BuildRequires: python3-module-requests
BuildRequires: python3-module-immutabledict
%endif

%py3_requires frozendict websocket blinker

AutoProv:no

%description
%summary.

%prep
%setup -n %srcname-%version
%autopatch -p2

%build
%python3_build

%install
%python3_install

install -pD -m644 %SOURCE1 %buildroot/lib/systemd/system/octoprint.service
install -pD -m755 %SOURCE2 %buildroot/%_sysconfdir/rc.d/init.d/octoprint
install -pD -m644 %SOURCE3 %buildroot/%_miconsdir/octoprint.png
install -pD -m644 %SOURCE4 %buildroot/%_niconsdir/octoprint.png
install -pD -m644 %SOURCE5 %buildroot/%_liconsdir/octoprint.png
install -pD -m644 %SOURCE6 %buildroot/%_desktopdir/octoprint.desktop
install -pD -m644 %SOURCE7 %buildroot/%_tmpfilesdir/octoprint.conf
rm %buildroot/%python3_sitelibdir/*egg-info/requires.txt
mkdir -p %buildroot%_localstatedir/lib/octoprint

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v tests

%pre
%_sbindir/groupadd -r -f octoprint 2>/dev/null ||:
%_sbindir/useradd -c 'Web interface for 3D printer' \
	-d %_localstatedir/lib/octoprint -g octoprint -s '/dev/null' \
	-r octoprint 2>/dev/null || :

%post
%post_service octoprint

%preun
%preun_service octoprint

%files
%_bindir/%name
%python3_sitelibdir/*
%_unitdir/octoprint.service
%_tmpfilesdir/octoprint.conf
%_sysconfdir/rc.d/init.d/octoprint
%attr(1770, octoprint, octoprint) %dir %_localstatedir/lib/octoprint
%_miconsdir/octoprint.png
%_niconsdir/octoprint.png
%_liconsdir/octoprint.png
%_desktopdir/octoprint.desktop
%doc *.md

%changelog
* Sat Feb 05 2022 Anton Midyukov <antohami@altlinux.org> 1.6.1-alt5
- add buildrequires to python3-module-immutabledict

* Sat Aug 21 2021 Anton Midyukov <antohami@altlinux.org> 1.6.1-alt4
- add BR: python3-module-requests (for tests)

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt3
- NMU: drop pip python module require
- NMU: disable provides, octoprint is a program, not a public module

* Thu Aug 12 2021 Anton Midyukov <antohami@altlinux.org> 1.6.1-alt2
- Add octoprint.service and octoprint.init
- Add desktop and icons files

* Wed Jul 28 2021 Anton Midyukov <antohami@altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus
