%define mname aspy
%define oname %mname.yaml

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.1
Summary: Some extensions to pyyaml
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/aspy.yaml/

# https://github.com/asottile/aspy.yaml.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-yaml python-module-coverage
BuildRequires: python-module-flake8 pylint
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-yaml python3-module-coverage
BuildRequires: python3-module-flake8 pylint-py3
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires yaml

%description
A few extensions to pyyaml.

%if_with python3
%package -n python3-module-%oname
Summary: Some extensions to pyyaml
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires yaml

%description -n python3-module-%oname
A few extensions to pyyaml.
%endif

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%if_with python3
%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/
%if_with python3
install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/
%endif

%check
python setup.py test
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test3 -vv
popd
%endif

%files
%doc *.md
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%python_sitelibdir/*-nspkg.pth
%exclude %python_sitelibdir/%mname/__init__.py*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20150111.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20150111.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150111
- Initial build for Sisyphus

