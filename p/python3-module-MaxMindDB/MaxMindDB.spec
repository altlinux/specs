%define  oname MaxMindDB
%define  fname maxminddb

Name:    python3-module-%oname
Version: 2.2.0
Release: alt1

Summary: Python MaxMind DB reader extension

License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/maxmind/MaxMind-DB-Reader-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: libmaxminddb-devel
BuildRequires: python3-module-sphinx

Source:  %oname-%version.tar

%description
This is a Python module for reading MaxMind DB files.  The module includes both
a pure Python reader and an optional C extension. MaxMind DB is a binary file
format that stores data indexed by IP address subnets (IPv4 or IPv6).

%package doc
Summary: Documentation for %oname
Group:   Development/Documentation

%description doc
This package provides the documentation for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
This package contains pickles for %oname.

%prep
%setup -n %oname-%version

%build
%python3_build

%make SPHINXBUILD="sphinx-build-3" -C docs man
%make SPHINXBUILD="sphinx-build-3" -C docs html
%make SPHINXBUILD="sphinx-build-3" -C docs pickle

%install
%python3_install

install -d %buildroot%_man1dir
cp -fR docs/_build/man/* %buildroot%_man1dir

install -d %buildroot%python3_sitelibdir/%fname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%fname/


%files
%doc README.rst
%python3_sitelibdir/%fname
%python3_sitelibdir/*.egg-info
%_man1dir/*
%exclude %python3_sitelibdir/%fname/pickle

%files doc
%doc LICENSE docs/_build/html

%files pickles
%python3_sitelibdir/%fname/pickle

%changelog
* Wed Oct 06 2021 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt1
- Automatically updated to 2.2.0.

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.3-alt1
- Automatically updated to 2.0.3.

* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt1
- Automatically updated to 2.0.2.

* Tue Jun 30 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.4-alt1
- Automatically updated to 1.5.4.

* Wed Feb 12 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.2-alt1
- Build new version 1.5.2.
- Add manpage.
- Build docs correctly.
- Add pickles subpackage.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt1
- Build new version 1.5.1.
- Build without python2.
- Added docs.

* Thu Dec 20 2018 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus.
