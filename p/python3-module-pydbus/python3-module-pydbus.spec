%define oname pydbus

Name: python3-module-pydbus
Version: 0.6.0
Release: alt2
Summary: Pythonic DBus library

License: LGPLv2+
Group: Development/Python3
Url: https://pypi.python.org/pypi/pydbus
Source: %oname-%version.tar
# Source-url: https://pypi.python.org/packages/58/56/3e84f2c1f2e39b9ea132460183f123af41e3b9c8befe222a35636baa6a5a/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%add_python3_req_skip gi.repository.GLib

%description
The pydbus module provides pythonic DBUS bindings.
It is based on PyGI, the Python GObject Introspection bindings,
which is the recommended way to use GLib from Python.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/%oname-*.egg-info
%python3_sitelibdir/%oname

%changelog
* Sat Oct 08 2022 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt2
- build python3 module only

* Mon Aug 07 2017 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt1
- Initial build for ALT Sisyphus.
