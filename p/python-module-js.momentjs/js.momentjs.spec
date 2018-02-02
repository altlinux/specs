%define oname js.momentjs

%def_with python3

Name: python-module-%oname
Version: 2.13.1
Release: alt1.1
Summary: Fanstatic packaging of Moment.js
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.momentjs/

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-fanstatic
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-fanstatic
BuildRequires: python3-module-pytest
%endif

%py_provides %oname
%py_requires js

%description
This library packages Moment.js for fanstatic.

%if_with python3
%package -n python3-module-%oname
Summary: Fanstatic packaging of Moment.js
Group: Development/Python3
%py3_provides %oname
%py3_requires js

%description -n python3-module-%oname
This library packages Moment.js for fanstatic.
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
export PYTHONPATH=$PWD
python setup.py test
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.13.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13.1-alt1
- Updated to upstream version 2.13.1.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.3.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.8.3.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.8.3.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.3.1-alt1
- Version 2.8.3-1

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.3-alt1
- Initial build for Sisyphus

