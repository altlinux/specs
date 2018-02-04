%define oname setproctitle

%def_with python3
#%%def_with check

Name: python-module-%oname
Version: 1.1.10
Release: alt1.1
Summary: A library to allow customization of the process title
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/setproctitle/
Packager: Python Development Team <python@packages.altlinux.org>

# https://github.com/dvarrazzo/py-setproctitle.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools /proc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif
%if_with check
BuildRequires: python-module-Cython-tests
%if_with python3
BuildRequires: python3-module-Cython-tests
%endif
%endif

%py_provides %oname

%description
The library allows a process to change its title (as displayed by system
tools such as ps and top).

%package -n python3-module-%oname
Summary: A library to allow customization of the process title
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The library allows a process to change its title (as displayed by system
tools such as ps and top).

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if_with check
%check
export PYTHONPATH=%buildroot%python_sitelibdir
%make tests/pyrun2
%py.test
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
export LC_ALL=en_US.UTF-8
%make tests/pyrun3 PYCONFIG=python3-config PYTHON=python3
py.test-%_python3_version
popd
%endif
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 03 2017 Anton Midyukov <antohami@altlinux.org> 1.1.10-alt1
- New version 1.1.10
- Disable check

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.9-alt1.dev0.git20140903.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.9-alt1.dev0.git20140903
- Initial build for Sisyphus

