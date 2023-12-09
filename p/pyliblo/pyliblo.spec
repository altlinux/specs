%define oname pyliblo

Name: %oname
Version: 0.10.0
Release: alt5
Summary: Python bindings for the liblo OSC library

License: GPLv2+
Group: Development/Python3
URL: http://das.nasophon.de/pyliblo/

Source0:        %name-%version.tar

BuildRequires:  gcc
BuildRequires:  liblo-devel
BuildRequires:  python3-dev
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
find -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

# Remove hashbang and executable bit from example scripts.
find examples/ -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?==' {} +
chmod -x examples/*

%build
%pyproject_build

%install
%pyproject_install

%files -n %oname-utils
%_bindir/*_osc
%_mandir/man*/*_osc.*

%files -n python3-module-%oname
%doc NEWS README examples/ COPYING
%python3_sitelibdir/liblo*.so
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Sat Dec 09 2023 Arseny Maslennikov <arseny@altlinux.org> 0.10.0-alt5
- Split out the example utilities to a new subpackage: pyliblo-utils.

* Wed Jul 20 2022 Arseny Maslennikov <arseny@altlinux.org> 0.10.0-alt4
- Rebuilt for the following reasons:
  + to use %%pyproject_* in spec file;
  + for the Sisyphus package EVR to be greater than the one in autoimports.

* Fri Jun 25 2021 Arseny Maslennikov <arseny@altlinux.org> 0.10.0-alt1
- Initial build for ALT Sisyphus.
