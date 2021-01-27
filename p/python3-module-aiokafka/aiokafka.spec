%define oname aiokafka

Name: python3-module-%oname
Version: 0.7.0
Release: alt1

Summary: asyncio client for kafka

License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/aiokafka/

# https://github.com/aio-libs/aiokafka.git
# Source-url: https://pypi.io/packages/source/a/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

%py3_provides %oname
%py3_requires asyncio kafka snappy

# due _crecords
#BuildArch: noarch
BuildRequires: zlib-devel

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(asyncio) python3(kafka)
BuildRequires: python3(snappy) python3(flake8)
BuildRequires: python3(nose)

%description
Kafka integration with asyncio.

%prep
%setup
subst "s|kafka-python==|kafka-python>=|" setup.py

# Upstream tarballed compilated for python 3.7 libraries
find . -name "*.so" | xargs rm -f

#sed -i 's|flake8|python3-flake8|' ../python3/Makefile
#sed -i 's|nosetests|nosetests3|' ../python3/Makefile

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Wed Jan 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt1
- Build new version for python3 only.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- new version 0.5.1 (with rpmrb script)

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

