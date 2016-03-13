%define oname aioirc

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1
Release: alt1.git20140929.1.1
Summary: AsyncIO IRC Library for >= Python 3.3
License: LGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/aioirc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/devunt/aioirc.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname
%py_requires asyncio

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-setuptools
BuildRequires: python3-module-pytest rpm-build-python3

%description
AsyncIO IRC Library for >= Python 3.3.

%package -n python3-module-%oname
Summary: AsyncIO IRC Library for >= Python 3.3
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
AsyncIO IRC Library for >= Python 3.3.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
python setup.py test
export PYTHONPATH=$PWD
python examples/test.py
%endif
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
python3 examples/test.py
popd
%endif

%if_with python2
%files
%doc *.rst docs/*.rst docs/aioirc/* examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst docs/aioirc/* examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20140929.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20140929.1
- NMU: Use buildreq for BR.

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140929
- Initial build for Sisyphus

