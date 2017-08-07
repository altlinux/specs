%define oname pydbus
%def_with python3

Name: python-module-pydbus
Version: 0.6.0
Release: alt1
Summary: Pythonic DBus library

License: LGPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/pydbus
Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar.gz
# Source-url: https://pypi.python.org/packages/58/56/3e84f2c1f2e39b9ea132460183f123af41e3b9c8befe222a35636baa6a5a/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%add_python3_req_skip gi.repository.GLib
%endif

%description
The pydbus module provides pythonic DBUS bindings.
It is based on PyGI, the Python GObject Introspection bindings,
which is the recommended way to use GLib from Python.

%package -n python3-module-%oname
Summary: %summary
Group: Development/Python3
#Requires: python3-gobject-base

%description -n python3-module-%oname
The pydbus module provides pythonic DBUS bindings.
It is based on PyGI, the Python GObject Introspection bindings,
which is the recommended way to use GLib from Python.

Python 3 version.

%prep
%setup -n %name-%version
%if_with python3
rm -rf ../python3-module-%oname-%version
cp -R . ../python3-module-%oname-%version
%endif

%build
%python_build
%if_with python3
pushd ../python3-module-%oname-%version
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3-module-%oname-%version
%python3_install
popd
%endif

%files
%doc LICENSE README.rst
%python_sitelibdir/%oname-*.egg-info
%python_sitelibdir/%oname

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.rst
%python3_sitelibdir/%oname-*.egg-info
%python3_sitelibdir/%oname
%endif

%changelog
* Mon Aug 07 2017 Anton Midyukov <antohami@altlinux.org> 0.6.0-alt1
- Initial build for ALT Sisyphus.
