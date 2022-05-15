%define oname liblo

Name: pyliblo
Version: 0.10.0
Release: alt1
Summary: Python bindings for the liblo OSC library

License: GPLv2+
Group: Development/Python3
URL: http://das.nasophon.de/pyliblo/

Source0:        %name-%version.tar

BuildRequires:  gcc
BuildRequires:  liblo-devel
BuildRequires:  python3-dev
BuildRequires:  python3-module-Cython

%description
pyliblo is a Python wrapper for the liblo Open Sound Control library.
It supports almost the complete functionality of liblo, allowing you
to send and receive OSC messages using a nice and simple Python API.

Also included are the command line utilities send_osc and dump_osc.

%package -n python3-module-%name
Summary: Python bindings for the liblo OSC library
Group: Development/Python3

%description -n python3-module-%name
pyliblo is a Python wrapper for the liblo Open Sound Control library.
It supports almost the complete functionality of liblo, allowing you
to send and receive OSC messages using a nice and simple Python API.

Also included are the command line utilities send_osc and dump_osc.

%prep
%setup
find -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

# Remove hashbang and executable bit from example scripts.
find examples/ -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?==' {} +
chmod -x examples/*

%build
%python3_build

%install
%python3_install

%files -n python3-module-%name
%doc NEWS README examples/ COPYING
%_mandir/man*/*.*
%_bindir/*_osc
%python3_sitelibdir/liblo*.so
%python3_sitelibdir/%{name}*.egg-info

%changelog
* Fri Jun 25 2021 Arseny Maslennikov <arseny@altlinux.org> 0.10.0-alt1
- Initial build for ALT Sisyphus.
