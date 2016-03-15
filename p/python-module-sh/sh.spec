%define oname sh

%def_with python3

Name: python-module-%oname
Version: 1.11
Release: alt1.git20150211.1
Summary: Python subprocess interface
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sh/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/amoffat/sh.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests /dev/pts
buildprereq: python-module-coverage python-module-py
buildprereq: python-module-tox python-module-virtualenv
buildprereq: python-module-nose
%if_with python3
buildrequires(pre): rpm-build-python3
buildprereq: python3-devel python3-module-setuptools-tests
buildprereq: python3-module-coverage python3-module-py
buildprereq: python3-module-tox python3-module-virtualenv
buildprereq: python3-module-nose
%endif

%py_provides %oname

%description
sh (previously pbs) is a full-fledged subprocess replacement for python
2.6 - 3.2 that allows you to call any program as if it were a function:

  from sh import ifconfig
  print ifconfig("eth0")

sh is not a collection of system commands implemented in python.

%package -n python3-module-%oname
summary: python subprocess interface
Group: Development/Python3
%py_provides %oname

%description -n python3-module-%oname
sh (previously pbs) is a full-fledged subprocess replacement for python
2.6 - 3.2 that allows you to call any program as if it were a function:

  from sh import ifconfig
  print ifconfig("eth0")

sh is not a collection of system commands implemented in python.

%prep
%setup

%if_with python3
cp -fr . ../python3
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
#py.test
nosetests -v
%if_with python3
pushd ../python3
py.test-%_python3_version
nosetests3 -v
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11-alt1.git20150211.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.git20150211
- Version 1.11

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt2.git20141230
- Fixed Group

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt1.git20141230
- Version 1.10

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.09-alt1.git20130908
- Initial build for Sisyphus

