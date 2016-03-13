%define oname clip

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1.git20150225.1
Summary: Embeddable, composable command line interface parsing
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/clip.py/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/willyg302/clip.py.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mkdocs
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Embeddable, composable [c]ommand [l]ine [i]nterface [p]arsing.

%package -n python3-module-%oname
Summary: Embeddable, composable command line interface parsing
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Embeddable, composable [c]ommand [l]ine [i]nterface [p]arsing.

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

mkdocs build
mv site doc

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
%doc *.md clip-logo.* examples doc
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md clip-logo.* examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20150225.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150225
- Initial build for Sisyphus

