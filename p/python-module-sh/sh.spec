%define oname sh

%def_with python3

Name: python-module-%oname
Version: 1.09
Release: alt1.git20130908
Summary: Python subprocess interface
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/sh/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/amoffat/sh.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
sh (previously pbs) is a full-fledged subprocess replacement for Python
2.6 - 3.2 that allows you to call any program as if it were a function:

  from sh import ifconfig
  print ifconfig("eth0")

sh is not a collection of system commands implemented in Python.

%package -n python3-module-%oname
Summary: Python subprocess interface
Group: Development/Python3
%py_provides %oname

%description -n python3-module-%oname
sh (previously pbs) is a full-fledged subprocess replacement for Python
2.6 - 3.2 that allows you to call any program as if it were a function:

  from sh import ifconfig
  print ifconfig("eth0")

sh is not a collection of system commands implemented in Python.

%prep
%setup

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

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.09-alt1.git20130908
- Initial build for Sisyphus

