%define oname js.angular_nvd3_directives

%def_with python3

Name: python-module-%oname
Version: 2.3.11
Release: alt2
Summary: Fanstatic packaging of angularjs-nvd3-directives
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.angular_nvd3_directives/

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-js.angular
BuildRequires: python-module-js.nvd3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-js.angular
BuildRequires: python3-module-js.nvd3
%endif

%py_provides %oname
%py_requires js js.angular js.nvd3

%description
This library packages angularjs-nvd3-directives for fanstatic.

%if_with python3
%package -n python3-module-%oname
Summary: Fanstatic packaging of angularjs-nvd3-directives
Group: Development/Python3
%py3_provides %oname
%py3_requires js js.angular js.nvd3

%description -n python3-module-%oname
This library packages angularjs-nvd3-directives for fanstatic.
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
* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.11-alt2
- Fixed build.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.11-alt1.2.1
- (AUTO) subst_x86_64.

* Tue Mar 15 2016 Denis Medvedev <nbr@altlinux.org> 2.3.11-alt1.2
- NMU just rebuild.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.11-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.11-alt1
- Initial build for Sisyphus

