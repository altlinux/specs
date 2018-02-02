%define oname aiokafka

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt2.1
Summary: asyncio client for kafka
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiokafka/

# https://github.com/aio-libs/aiokafka.git
Source0: https://pypi.python.org/packages/d4/ff/f440264776a1dc0d869d66197a0b74903206880c1c5d32c99ae5c9f9a337/%{oname}-%{version}.tar.gz
Patch1: %oname-%version-alt-deps.patch
BuildArch: noarch

%if_with python2
BuildRequires: python-dev python-module-setuptools
BuildRequires: python2.7(asyncio) python2.7(kafka)
BuildRequires: python2.7(snappy) python2.7(flake8)
BuildRequires: python2.7(nose)
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(asyncio) python3(kafka)
BuildRequires: python3(snappy) python3(flake8)
BuildRequires: python3(nose)
%endif

%py_provides %oname
%py_requires asyncio kafka snappy

%description
Kafka integration with asyncio.

%package -n python3-module-%oname
Summary: asyncio client for kafka
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio kafka snappy

%description -n python3-module-%oname
Kafka integration with asyncio.

%prep
%setup -q -n %{oname}-%{version}
%patch1 -p2

%if_with python3
cp -fR . ../python3
#sed -i 's|flake8|python3-flake8|' ../python3/Makefile
#sed -i 's|nosetests|nosetests3|' ../python3/Makefile
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
#nosetests -s -v ./tests/
%endif
%if_with python3
pushd ../python3
python3 setup.py test
#nosetests3 -s -v ./tests/
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
#exclude %python_sitelibdir/tests
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
#exclude %python3_sitelibdir/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt2
- Fixed build.

* Tue Jan 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.git20150207.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1.git20150207.1
- NMU: Use buildreq for BR.

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20150207
- New snapshot

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141230
- Initial build for Sisyphus

