%define oname js.angular_ui_sortable

%def_with python3

Name: python-module-%oname
Version: 0.13.4
Release: alt1.1
Summary: Fanstatic packaging of Angular UI Sortable
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.angular_ui_sortable/

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-fanstatic python-module-js.jquery
BuildRequires: python-module-js.jqueryui python-module-js.angular
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-fanstatic python3-module-js.jquery
BuildRequires: python3-module-js.jqueryui python3-module-js.angular
BuildRequires: python3-module-pytest
%endif

%py_provides %oname
%py_requires js js.jquery js.jqueryui js.angular

%description
This library packages Angular UI Sortable for fanstatic.

%if_with python3
%package -n python3-module-%oname
Summary: Fanstatic packaging of Angular UI Sortable
Group: Development/Python3
%py3_provides %oname
%py3_requires js js.jquery js.jqueryui js.angular

%description -n python3-module-%oname
This library packages Angular UI Sortable for fanstatic.
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

%if "%_lib" == "lib64"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
rm -fR build
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR build
export PYTHONPATH=$PWD
py.test3
popd
%endif

%files
%doc *.txt
%python_sitelibdir/js/*
%python_sitelibdir/*.egg-info
%python_sitelibdir/*-nspkg.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.13.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.13.4-alt1
- Updated to upstream version 0.13.4.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13.0-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1
- Initial build for Sisyphus

