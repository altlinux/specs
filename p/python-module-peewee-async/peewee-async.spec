%define oname peewee-async

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0.2
Release: alt1.git20141030.1
Summary: Asynchronous interface for peewee ORM powered by asyncio
License: MIT
Group: Development/Python
Url: http://peewee-async.readthedocs.org/en/latest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/05bit/peewee-async.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-peewee
#BuildPreReq: python-module-aiopg
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-peewee
#BuildPreReq: python3-module-aiopg
%endif

%py_provides peewee_async
%py_requires asyncio peewee aiopg

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-jinja2 python3-module-setuptools
BuildRequires: python3-module-apsw python3-module-psycopg2 python3-module-pytest rpm-build-python3

%description
peewee-async is a library providing asynchronous interface powered by
asyncio for peewee ORM.

%package -n python3-module-%oname
Summary: Asynchronous interface for peewee ORM powered by asyncio
Group: Development/Python3
%py3_provides peewee_async
%py3_requires asyncio peewee aiopg

%description -n python3-module-%oname
peewee-async is a library providing asynchronous interface powered by
asyncio for peewee ORM.

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
%doc *.md docs/*.rst docs/peewee_async
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*.rst docs/peewee_async
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.2-alt1.git20141030.1
- NMU: Use buildreq for BR.

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141030
- Initial build for Sisyphus

