%define _unpackaged_files_terminate_build 1
%define oname haven

%def_with python3

Name: python-module-%oname
Version: 1.1.88
Release: alt1
Summary: flask's style binary server framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/haven/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dantezhu/haven.git
Source0: https://pypi.python.org/packages/6e/37/cafac2c3b1a8ad24fb30b7866ac9198ac39c15c657c37b96a9ff14091ded/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-events python-module-netkit
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-events python3-module-netkit
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires events netkit

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-setuptools-tests python3-module-setuptools-tests rpm-build-python3 time

%description
flask's style binary server framework.

%package -n python3-module-%oname
Summary: flask's style binary server framework
Group: Development/Python3
%py3_provides %oname
%py3_requires events netkit

%description -n python3-module-%oname
flask's style binary server framework.

%prep
%setup -q -n %{oname}-%{version}

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.88-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.65-alt1.git20141127.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.65-alt1.git20141127.1
- NMU: Use buildreq for BR.

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.65-alt1.git20141127
- Version 1.1.65

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.60-alt1.git20141120
- Initial build for Sisyphus

