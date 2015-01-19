%define oname pre_commit

%def_without python3

Name: python-module-%oname
Version: 0.3.5
Release: alt1.git20150115
Summary: A framework for managing and maintaining multi-language pre-commit hooks
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pre_commit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pre-commit/pre-commit.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-argparse python-module-aspy.yaml
BuildPreReq: python-module-cached-property python-module-jsonschema
BuildPreReq: python-module-yaml
BuildPreReq: python-module-simplejson python-module-virtualenv
BuildPreReq: python-module-coverage python-module-flake8
BuildPreReq: python-module-mock pylint
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-argparse python3-module-aspy.yaml
BuildPreReq: python3-module-cached-property python3-module-jsonschema
BuildPreReq: python3-module-yaml
BuildPreReq: python3-module-simplejson python3-module-virtualenv
BuildPreReq: python3-module-coverage python3-module-flake8
BuildPreReq: python3-module-mock pylint-py3
%endif

%py_provides %oname
%py_requires argparse aspy.yaml cached_property jsonschema
%py_requires yaml simplejson virtualenv

%description
A framework for managing and maintaining multi-language pre-commit
hooks.

%package -n python3-module-%oname
Summary: A framework for managing and maintaining multi-language pre-commit hooks
Group: Development/Python3
%py3_provides %oname
%py3_requires argparse aspy.yaml cached_property jsonschema
%py3_requires yaml simplejson virtualenv

%description -n python3-module-%oname
A framework for managing and maintaining multi-language pre-commit
hooks.

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
%doc *.md *.yaml
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.yaml .*.yaml
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.git20150115
- Initial build for Sisyphus

