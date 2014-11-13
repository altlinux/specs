%define oname zetup

%def_with python3

Name: python-module-%oname
Version: 0.2.3
Release: alt1.git20141013
Summary: Zimmermann's Python package setup
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/zetup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/userzimmermann/zetup.py.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-hgdistver python-module-conda
BuildPreReq: python-module-path
#BuildPreReq: python-module-jinjatools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-hgdistver python3-module-conda
BuildPreReq: python3-module-path
#BuildPreReq: python3-module-jinjatools
%endif

%py_provides %oname
%add_python_req_skip jinjatools

%description
Zimmermann's Python package setup.

%package -n python3-module-%oname
Summary: Zimmermann's Python package setup
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip jinjatools

%description -n python3-module-%oname
Zimmermann's Python package setup.

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
%doc README*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README*
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.3-alt1.git20141013
- Initial build for Sisyphus

