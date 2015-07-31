%define oname hitchtest

%def_with python3

Name: python-module-%oname
Version: 0.6.6
Release: alt1.git20150730
Summary: Declarative test runner using YAML and jinja2
License: AGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/hitchtest
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hitchtest/hitchtest.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-hitch python-module-click
BuildPreReq: python-module-jinja2 python-module-yaml
BuildPreReq: python-module-colorama ipython python-module-psutil
BuildPreReq: python-module-patool python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-hitch python3-module-click
BuildPreReq: python3-module-jinja2 python3-module-yaml
BuildPreReq: python3-module-colorama ipython3 python3-module-psutil
BuildPreReq: python3-module-patool python3-module-requests
%endif

%py_provides %oname
%py_requires hitch click jinja2 yaml IPython colorama psutil patool
%py_requires requests

%description
HitchTest is a part of the hitch testing framework which compiles and
runs YAML (and optionally jinja2) tests.

%if_with python3
%package -n python3-module-%oname
Summary: Declarative test runner using YAML and jinja2
Group: Development/Python3
%py3_provides %oname
%py3_requires hitch click jinja2 yaml IPython colorama psutil patool
%py3_requires requests

%description -n python3-module-%oname
HitchTest is a part of the hitch testing framework which compiles and
runs YAML (and optionally jinja2) tests.
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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.6-alt1.git20150730
- Initial build for Sisyphus

