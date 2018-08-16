%define _unpackaged_files_terminate_build 1

%define oname fake-factory

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.8.17
Release: alt1
Summary: Faker is a Python package that generates fake data for you
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/fake-factory/

# https://github.com/joke2k/faker.git
Source: %name-%version.tar

Patch1: %oname-%version-alt-docs.patch
Patch2: %oname-%version-alt-unidecode.patch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pytest
BuildRequires: python2.7(mock) python2.7(unidecode) python2.7(dateutil)
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
BuildRequires: python3(mock) python3(unidecode) python3(dateutil)
%endif

%py_provides faker

%description
Faker is a Python package that generates fake data for you. Whether you
need to bootstrap your database, create good-looking XML documents,
fill-in your persistence to stress test it, or anonymize data taken from
a production service, Faker is for you.

%if_with python3
%package -n python3-module-%oname
Summary: Faker is a Python package that generates fake data for you
Group: Development/Python3
%py3_provides faker

%description -n python3-module-%oname
Faker is a Python package that generates fake data for you. Whether you
need to bootstrap your database, create good-looking XML documents,
fill-in your persistence to stress test it, or anonymize data taken from
a production service, Faker is for you.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Faker is a Python package that generates fake data for you. Whether you
need to bootstrap your database, create good-looking XML documents,
fill-in your persistence to stress test it, or anonymize data taken from
a production service, Faker is for you.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
Faker is a Python package that generates fake data for you. Whether you
need to bootstrap your database, create good-looking XML documents,
fill-in your persistence to stress test it, or anonymize data taken from
a production service, Faker is for you.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1
%patch2 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8

rm -f tests/providers/test_address.py
rm -f tests/providers/test_internet.py
py.test

%if_with python3
pushd ../python3

rm -f tests/providers/test_address.py
rm -f tests/providers/test_internet.py
py.test3
popd
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Aug 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.17-alt1
- Updated to upstream version 0.8.17.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20150222.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20150222.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.git20150222.1
- NMU: Use buildreq for BR.

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20150222
- Version 0.5.0

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20141015
- Initial build for Sisyphus

