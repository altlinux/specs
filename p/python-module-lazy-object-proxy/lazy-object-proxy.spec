%define _unpackaged_files_terminate_build 1
%define oname lazy-object-proxy

%def_with check

Name: python-module-%oname
Version: 1.3.1
Release: alt1

Summary: A fast and thorough lazy object proxy
License: BSD
Group: Development/Python
# Source-git: https://github.com/ionelmc/python-lazy-object-proxy.git
Url: https://pypi.org/project/lazy-object-proxy/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python-module-pytest
BuildRequires: python-module-pytest-benchmark
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-benchmark
%endif

%description
This Python module is based on wrapt's ObjectProxy with one big change: it
calls a function the first time the proxy object is used, while
wrapt.ObjectProxy just forwards the method calls to the target object.

%package -n python3-module-%oname
Summary: A fast and thorough lazy object proxy
Group: Development/Python3

%description -n python3-module-%oname
This Python3 module is based on wrapt's ObjectProxy with one big change: it
calls a function the first time the proxy object is used, while
wrapt.ObjectProxy just forwards the method calls to the target object.

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%build
%add_optflags -fno-strict-aliasing
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
pushd ../python3
%python3_install
popd

%check
python setup.py clean --all build_ext --force --inplace
py.test -v

pushd ../python3
python3 setup.py clean --all build_ext --force --inplace
py.test3 -v
popd

%files
%doc AUTHORS.rst README.rst CHANGELOG.rst
%python_sitelibdir/lazy_object_proxy/
%python_sitelibdir/lazy_object_proxy-*.egg-info/
%exclude %python_sitelibdir/lazy_object_proxy/cext.c

%files -n python3-module-%oname
%doc AUTHORS.rst README.rst CHANGELOG.rst
%python3_sitelibdir/lazy_object_proxy/
%python3_sitelibdir/lazy_object_proxy-*.egg-info/
%exclude %python3_sitelibdir/lazy_object_proxy/cext.c

%changelog
* Mon Sep 03 2018 Stanislav Levin <slev@altlinux.org> 1.3.1-alt1
- Initial build.
