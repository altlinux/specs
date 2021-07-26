%define oname clize

Name: python3-module-%oname
Version: 4.1.1
Release: alt2

Summary: Command-line argument parsing for Python, without the effort

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/clize/

# https://github.com/epsy/clize.git
# Source-url: https://pypi.io/packages/source/c/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sigtools >= 2.0
BuildRequires: python3-module-attrs >= 17.4.0
BuildRequires: python3-module-six
BuildRequires: python3-module-od
BuildRequires: python3(dateutil)
BuildRequires: python3(unittest2) python3(repeated_test) python3(pygments)

%py3_provides %oname
%py3_requires sigtools six

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx

%description
Clize procedurally turns your functions into convenient command-line
interfaces.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Clize procedurally turns your functions into convenient command-line
interfaces.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Clize procedurally turns your functions into convenient command-line
interfaces.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build

%install
%python3_install
rm -rf %buildroot%python3_sitelibdir/clize/tests/

export PYTHONPATH=$PWD
#make SPHINXBUILD="sphinx-build-3" -C docs pickle
#make SPHINXBUILD="sphinx-build-3" -C docs html

#cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
#exclude %python3_sitelibdir/*/pickle

%files pickles
#python3_sitelibdir/*/pickle

%files docs
#doc docs/_build/html examples

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 4.1.1-alt2
- Drop python2 support.

* Mon Apr 20 2020 Pavel Vasenkov <pav@altlinux.org> 4.1.1-alt1
- new version 4.1.1

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 4.0.3-alt1
- new version 4.0.3 (with rpmrb script)
- build python3 module only

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt1.a2.git20150111.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0-alt1.a2.git20150111.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.0-alt1.a2.git20150111.1
- NMU: Use buildreq for BR.

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1.a2.git20150111
- Initial build for Sisyphus

