%define oname nose-docstring-modifier

%def_with python3

Name: python-module-%oname
Version: 0.0.6
Release: alt1.git20141126.1.1
Summary: Add attributes next to the original docstring
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/nose-docstring-modifier/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/taykey/nose-docstring.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides nose_docstring_modifier

%description
This plugin enables you to modify docstring of tests based on their
attributes.

%package -n python3-module-%oname
Summary: Add attributes next to the original docstring
Group: Development/Python3
%py3_provides nose_docstring_modifier

%description -n python3-module-%oname
This plugin enables you to modify docstring of tests based on their
attributes.

%prep
%setup

ln -s README.rst README.md

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%endif
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.6-alt1.git20141126.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.6-alt1.git20141126.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20141126
- Version 0.0.6

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20141124
- Version 0.0.5

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20141106
- Version 0.0.4

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20141105
- Initial build for Sisyphus

