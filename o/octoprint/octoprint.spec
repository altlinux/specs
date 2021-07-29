%define  srcname OctoPrint

Name:    octoprint
Version: 1.6.1
Release: alt1

Summary: OctoPrint is the snappy web interface for your 3D printer
License: AGPL-3.0
Group:   Development/Python3
URL:     https://github.com/OctoPrint/OctoPrint

Packager: Anton Midyukov <antohami@altlinux.org>

BuildArch: noarch

# Source-url: https://github.com/OctoPrint/OctoPrint/archive/refs/tags/%version.tar.gz
Source: %srcname-%version.tar

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
%endif

%py3_requires frozendict websocket

%description
%summary.

%prep
%setup -n %srcname-%version
%autopatch -p2

%build
%python3_build

%install
%python3_install

rm %buildroot/%python3_sitelibdir/*egg-info/requires.txt

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v tests

%files
%_bindir/%name
%python3_sitelibdir/*
%doc *.md

%changelog
* Wed Jul 28 2021 Anton Midyukov <antohami@altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus
