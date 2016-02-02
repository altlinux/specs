%define oname pies

%def_with python3

Name: python-module-%oname
Version: 2.6.3
Release: alt2.git20141225
Summary: The simplest way to write one program that runs on both Python 2 and Python 3
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pies/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/timothycrosley/pies.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-module-enum34 python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-enum34 python3-module-pytest
%endif

%py_provides %oname

%description
The simplest (and tastiest) way to write one program that runs on both
Python 2 and Python 3.

%package -n python3-module-%oname
Summary: The simplest way to write one program that runs on both Python 2 and Python 3
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The simplest (and tastiest) way to write one program that runs on both
Python 2 and Python 3.

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

%check
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
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
* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 2.6.3-alt2.git20141225
- cleanup buildreq

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.3-alt1.git20141225
- Version 2.6.3

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.1-alt1.git20140224
- Initial build for Sisyphus

