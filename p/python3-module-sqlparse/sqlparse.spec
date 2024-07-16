%define _unpackaged_files_terminate_build 1
%define oname sqlparse

Name: python3-module-%oname
Version: 0.5.1
Release: alt1
Summary: Non-validating SQL parser
License: BSD
Group: Development/Python3
URL: https://pypi.org/project/sqlparse
VCS: https://github.com/andialbrecht/sqlparse
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-sphinx

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
sqlparse is a non-validating SQL parser module. It provides support for
parsing, splitting and formatting SQL statements.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
sqlparse is a non-validating SQL parser module. It provides support for
parsing, splitting and formatting SQL statements.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
sqlparse is a non-validating SQL parser module. It provides support for
parsing, splitting and formatting SQL statements.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/

%build
%pyproject_build

%install
%pyproject_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/

install -d %buildroot%_man1dir
install -p -m644 docs/*.1 %buildroot%_man1dir/

%files
%doc AUTHORS *.rst TODO CHANGELOG docs
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/build/html
%_man1dir/*

%changelog
* Tue Jul 16 2024 Grigory Ustinov <grenka@altlinux.org> 0.5.1-alt1
- Automatically updated to 0.5.1.

* Tue Apr 16 2024 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt1
- Automatically updated to 0.5.0.

* Mon Apr 24 2023 Grigory Ustinov <grenka@altlinux.org> 0.4.4-alt1
- Automatically updated to 0.4.4.

* Sat Sep 24 2022 Grigory Ustinov <grenka@altlinux.org> 0.4.3-alt1
- Automatically updated to 0.4.3.

* Tue Oct 12 2021 Grigory Ustinov <grenka@altlinux.org> 0.4.2-alt1
- Automatically updated to 0.4.2.

* Tue Jun 29 2021 Grigory Ustinov <grenka@altlinux.org> 0.4.1-alt1
- Build new version.

* Tue Jun 08 2021 Grigory Ustinov <grenka@altlinux.org> 0.2.2-alt2
- Drop python2 support.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.12-alt1.git20140920.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.12-alt1.git20140920.1
- NMU: Use buildreq for BR.

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.12-alt1.git20140920
- Initial build for Sisyphus

