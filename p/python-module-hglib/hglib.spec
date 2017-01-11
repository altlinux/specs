%define _unpackaged_files_terminate_build 1
%define oname hglib

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 2.3
Release: alt1
Summary: Mercurial Python library
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/python-hglib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/80/9c/1618281fc1ef0df4436b1435de6276452fefb46b111b3b00d3e20fcf5e17/python-%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: mercurial
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose
BuildRequires: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose
#BuildPreReq: python-tools-2to3
BuildRequires: python3 python-tools-2to3
%endif

%py_provides %oname

%description
python-hglib is a library with a fast, convenient interface to
Mercurial. It uses Mercurial's command server for communication with hg.

%if_with python3
%package -n python3-module-%oname
Summary: Mercurial Python library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
python-hglib is a library with a fast, convenient interface to
Mercurial. It uses Mercurial's command server for communication with hg.
%endif

%prep
%setup -q -n python-%{oname}-%{version}

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
python test.py
%if_with python3
pushd ../python3
python3 test.py
popd
%endif

%files
%doc README examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README examples
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1
- automated PyPI update

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 1.5-alt3
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2
- Fixed build

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Initial build for Sisyphus

