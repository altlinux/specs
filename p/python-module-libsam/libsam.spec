%define oname libsam

%def_with python3

Name: python-module-%oname
Version: 0.1.4
Release: alt1.git20150206.1
Summary: Bio-Informatics sam file libraries
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/libsam/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dlmeduLi/libsam.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Libsam is a collection of SAM/BAM file related python library. Packaged
included in this library include:

    samparser: A robust sam file format checker and parser

%package -n python3-module-%oname
Summary: Bio-Informatics sam file libraries
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Libsam is a collection of SAM/BAM file related python library. Packaged
included in this library include:

    samparser: A robust sam file format checker and parser

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150206.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150206
- Version 0.1.4

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20150204
- Initial build for Sisyphus

