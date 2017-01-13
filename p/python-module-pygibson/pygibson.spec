%define _unpackaged_files_terminate_build 1
%define oname pygibson

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.1
Release: alt1
Summary: Python client for gibson cache server
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pygibson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bak1an/pygibson.git
Source0: https://pypi.python.org/packages/49/ce/18e324897ae11b3a9f271e3780fe5ffa169ac980a47eb9c14077f586ebda/%{oname}-%{version}.tar.gz

#BuildPreReq: libgibsonclient-devel
#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: libgibsonclient-devel python-devel python3-devel rpm-build-python3

%description
Python client for gibson cache server.

%package -n python3-module-%oname
Summary: Python client for gibson cache server
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python client for gibson cache server.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
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

%check
python -m tests.run
%if_with python3
pushd ../python3
python3 -m tests.run
popd
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20131001.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20131001.1
- NMU: Use buildreq for BR.

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20131001
- Initial build for Sisyphus

