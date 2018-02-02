%define oname js.bootstrap_select

%def_with python3

Name: python-module-%oname
Version: 1.5.2
Release: alt1.git20140516.2.1
Summary: Fanstatic packaging of bootstrap-select.js
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.bootstrap_select/

# https://github.com/tmassman/js.bootstrap_select.git
Source: %name-%version.tar

BuildRequires: python-module-js.bootstrap python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-js.bootstrap python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%py_requires js js.bootstrap

%description
This library packages bootstrap select for fanstatic.

%package -n python3-module-%oname
Summary: Fanstatic packaging of bootstrap-select.js
Group: Development/Python3
%py3_requires js js.bootstrap

%description -n python3-module-%oname
This library packages bootstrap select for fanstatic.

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

%check
python setup.py test
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/js/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.2-alt1.git20140516.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.2-alt1.git20140516.2
- Fixed build.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.2-alt1.git20140516.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.2-alt1.git20140516.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.2-alt1.git20140516.1
- NMU: Use buildreq for BR.

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.git20140516
- Initial build for Sisyphus

