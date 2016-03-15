%define oname orderedmultidict

%def_with python3

Name: python-module-%oname
Version: 0.7.4
Release: alt1.git20141118.1
Summary: Ordered Multivalue Dictionary - omdict
License: Public domain
Group: Development/Python
Url: https://pypi.python.org/pypi/orderedmultidict/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gruns/orderedmultidict.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six
%endif

%py_provides %oname

%description
A multivalue dictionary is a dictionary that can store multiple values
for the same key. An ordered multivalue dictionary is a multivalue
dictionary that retains the order of insertions and deletions.

omdict retains method parity with dict.

%package -n python3-module-%oname
Summary: Ordered Multivalue Dictionary - omdict
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A multivalue dictionary is a dictionary that can store multiple values
for the same key. An ordered multivalue dictionary is a multivalue
dictionary that retains the order of insertions and deletions.

omdict retains method parity with dict.

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
touch tests/__init__.py
python setup.py test
%if_with python3
pushd ../python3
touch tests/__init__.py
python3 setup.py test
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.4-alt1.git20141118.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1.git20141118
- Version 0.7.4
- Added module for Python 3

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1.git20140705
- Initial build for Sisyphus

