%define oname js.nvd3

%def_with python3

Name: python-module-%oname
Version: 1.8.1
Release: alt1
Summary: Fanstatic packaging of NVD3
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.nvd3/

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-js.d3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-js.d3
%endif

%py_provides %oname
%py_requires js js.d3

%description
This library packages NVD3 for fanstatic.

%if_with python3
%package -n python3-module-%oname
Summary: Fanstatic packaging of NVD3
Group: Development/Python3
%py3_provides %oname
%py3_requires js js.d3

%description -n python3-module-%oname
This library packages NVD3 for fanstatic.
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
* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.1-alt1
- Updated to upstream version 1.8.1.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.15-alt1.beta.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.15-alt1.beta.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.15-alt1.beta.1
- NMU: Use buildreq for BR.

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.15-alt1.beta
- Initial build for Sisyphus

