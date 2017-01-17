%define _unpackaged_files_terminate_build 1
%define oname ipyroute

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0.36
Release: alt1
Summary: Yet another interface for iproute2
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/ipyroute/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jta/ipyroute.git
Source0: https://pypi.python.org/packages/3c/cf/98fd398c0a1393700514fd1f90e825444ae5c2787d4f92e4b1814bf44b12/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-sh python-module-netaddr
#BuildPreReq: python-module-six python-module-nose
#BuildPreReq: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-sh python3-module-netaddr
#BuildPreReq: python3-module-six python3-module-nose
#BuildPreReq: python3-module-mock
%endif

%py_provides %oname
Requires: iproute2
%py_requires sh netaddr six

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-netaddr python-module-nose python-module-pbr python-module-pytest python-module-sh python-module-unittest2 python3-module-html5lib python3-module-netaddr python3-module-nose python3-module-pbr python3-module-pytest python3-module-sh python3-module-unittest2 rpm-build-python3

%description
Yet another interface for iproute2.

%package -n python3-module-%oname
Summary: Yet another interface for iproute2
Group: Development/Python3
%py3_provides %oname
Requires: iproute2
%py3_requires sh netaddr six

%description -n python3-module-%oname
Yet another interface for iproute2.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
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
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 -v
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
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.36-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.23-alt1.git20150214.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.23-alt1.git20150214.1
- NMU: Use buildreq for BR.

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.23-alt1.git20150214
- Version 0.0.23

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.18-alt1.git20150211
- Version 0.0.18

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.16-alt1.git20150210
- Version 0.0.16

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.13-alt1.git20150202
- Initial build for Sisyphus

