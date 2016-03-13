%define oname robotframework-debuglibrary

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt2.git20130806.1
Summary: RobotFramework debug library and an interactive shell
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/robotframework-debuglibrary/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/xyb/robotframework-debuglibrary.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-robotframework
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools-tests
BuildPreReq: python3-module-robotframework
%endif

%description
Robotframework-DebugLibrary is A debug library for RobotFramework, which
can be used as an interactive shell(REPL) also.

%package -n python3-module-%oname
Summary: RobotFramework debug library and an interactive shell
Group: Development/Python3

%description -n python3-module-%oname
Robotframework-DebugLibrary is A debug library for RobotFramework, which
can be used as an interactive shell(REPL) also.

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc ChangeLog *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt2.git20130806.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2.git20130806
- Added module for Python 3

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20130806
- Initial build for Sisyphus

