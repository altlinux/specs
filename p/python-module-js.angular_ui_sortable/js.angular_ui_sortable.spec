%define oname js.angular_ui_sortable

%def_with python3

Name: python-module-%oname
Version: 0.13.0
Release: alt1.1
Summary: Fanstatic packaging of Angular UI Sortable
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.angular_ui_sortable/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-fanstatic python-module-js.jquery
BuildPreReq: python-module-js.jqueryui python-module-js.angular
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-fanstatic python3-module-js.jquery
BuildPreReq: python3-module-js.jqueryui python3-module-js.angular
%endif

%py_provides %oname
%py_requires js js.jquery js.jqueryui js.angular

%description
This library packages Angular UI Sortable for fanstatic.

%package -n python3-module-%oname
Summary: Fanstatic packaging of Angular UI Sortable
Group: Development/Python3
%py3_provides %oname
%py3_requires js js.jquery js.jqueryui js.angular

%description -n python3-module-%oname
This library packages Angular UI Sortable for fanstatic.

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

%ifarch x86_64
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
py.test-%_python3_version
popd
%endif

%files
%doc *.txt
%python_sitelibdir/js/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1
- Initial build for Sisyphus

