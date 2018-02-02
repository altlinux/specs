%define _unpackaged_files_terminate_build 1
%define oname robotframework-debuglibrary

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt1.1
Summary: RobotFramework debug library and an interactive shell
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/robotframework-debuglibrary/

# https://github.com/xyb/robotframework-debuglibrary.git
Source: %name-%version.tar

BuildRequires: python-module-setuptools
BuildRequires: python-module-robotframework
BuildRequires: python2.7(pygments) python2.7(prompt_toolkit)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-robotframework
BuildRequires: python3(pygments) python3(prompt_toolkit)
%endif

%description
Robotframework-DebugLibrary is A debug library for RobotFramework, which
can be used as an interactive shell(REPL) also.

%if_with python3
%package -n python3-module-%oname
Summary: RobotFramework debug library and an interactive shell
Group: Development/Python3

%description -n python3-module-%oname
Robotframework-DebugLibrary is A debug library for RobotFramework, which
can be used as an interactive shell(REPL) also.
%endif

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt1
- Updated to upstream version 1.0.2.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt2.git20130806.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2.git20130806
- Added module for Python 3

* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20130806
- Initial build for Sisyphus

