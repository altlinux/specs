%define  oname MaxMindDB

Name:    python3-module-%oname
Version: 1.5.1
Release: alt1

Summary: Python MaxMind DB reader extension

License: ASLv2
Group:   Development/Python3
URL:     https://github.com/maxmind/MaxMind-DB-Reader-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: libmaxminddb-devel

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

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/maxminddb
%python3_sitelibdir/*.egg-info

%files doc
%doc docs/*

%changelog
* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt1
- Build new version 1.5.1.
- Build without python2.
- Added docs.

* Thu Dec 20 2018 Grigory Ustinov <grenka@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
