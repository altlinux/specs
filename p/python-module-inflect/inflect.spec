%define oname inflect

%def_with python3

Name: python-module-%oname
Version: 0.2.5
Release: alt1.pre1.git20140708
Summary: Correctly generate plurals, singular nouns, ordinals, indefinite articles
License: AGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/inflect/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pwdyson/inflect.py.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose
%endif

%py_provides %oname

%description
inflect.py - Correctly generate plurals, singular nouns, ordinals,
indefinite articles; convert numbers to words.

%package -n python3-module-%oname
Summary: Correctly generate plurals, singular nouns, ordinals, indefinite articles
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
inflect.py - Correctly generate plurals, singular nouns, ordinals,
indefinite articles; convert numbers to words.

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
%doc *.txt *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.pre1.git20140708
- Initial build for Sisyphus

