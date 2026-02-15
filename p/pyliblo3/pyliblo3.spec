%define _unpackaged_files_terminate_build 1

%define oname pyliblo3

Name: %oname
Version: 0.16.4
Release: alt1
Summary: Python bindings for the liblo OSC library

License: GPLv2+
Group: Development/Python3
URL: https://pypi.org/project/pyliblo3/

VCS: https://github.com/bonktree/pyliblo
Source0:        %name-%version.tar

BuildRequires:  gcc
BuildRequires:  liblo-devel
BuildRequires:  python3-module-Cython
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-wheel

%description
pyliblo is a Python wrapper for the liblo Open Sound Control library.
It supports almost the complete functionality of liblo, allowing you
to send and receive OSC messages using a nice and simple Python API.

Also included are the command line utilities send_osc and dump_osc.

%package -n python3-module-%oname
Summary: Python bindings for the liblo OSC library
Group: Development/Python3

%description -n python3-module-%oname
pyliblo is a Python wrapper for the liblo Open Sound Control library.
It supports almost the complete functionality of liblo, allowing you
to send and receive OSC messages using a nice and simple Python API.

This package contains the Python module.

%package -n %oname-utils
Summary: Utilities to accompany the liblo OSC library
Group: Sound

%description -n %oname-utils
pyliblo is a Python wrapper for the liblo Open Sound Control library.
It supports almost the complete functionality of liblo, allowing you
to send and receive OSC messages using a nice and simple Python API.

This package contains the command line utilities send_osc and dump_osc.

%prep
%setup
%autopatch -p1
chmod -c ugo-x COPYING NEWS PKG-INFO README.md
find -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

# Remove hashbang and executable bit from example scripts.
find examples/ -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?==' {} +
chmod -x examples/*

%build
%pyproject_build

%install
%pyproject_install

%files -n %oname-utils
%_bindir/*_osc.py

%files -n python3-module-%oname
%doc NEWS README.md examples/ COPYING
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Thu Sep 18 2025 Arseny Maslennikov <arseny@altlinux.org> 0.16.4-alt1
- Initial build for ALT Sisyphus.
  This is a continuation of pyliblo from nasophon.de, but under a different
  module name.
