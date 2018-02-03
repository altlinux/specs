%define oname colibri

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20140917.1.1.1
Summary: Colibri - asyncio-based AMQP client
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/colibri/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/malinoff/colibri.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname
%py_requires asyncio

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python3-module-setuptools rpm-build-python3

%description
asyncio-based implementation of AMQP client.

%package -n python3-module-%oname
Summary: Colibri - asyncio-based AMQP client
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
asyncio-based implementation of AMQP client.

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
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc *.rst docs/*.rst spec
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst spec
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.1-alt1.git20140917.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.git20140917.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.git20140917.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20140917
- Initial build for Sisyphus

