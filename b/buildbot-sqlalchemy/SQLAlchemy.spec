%define oname SQLAlchemy
%define bbmodulesdir %_libexecdir/buildbot/modules

Name: buildbot-sqlalchemy
Version: 1.4.44
Release: alt1

Summary: Version for Buildbot of SQL toolkit and Object Relational Mapper

License: MIT
Group: Development/Python3
Url: http://www.sqlalchemy.org/

AutoReqProv: nopython

Source: SQLAlchemy-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

# Make sure that at least the Python built-in sqlite driver
# is present (and can be used by SQLAlchemy--among other things--
# in various tests, like in the tests for sphinx).
Requires: python3-modules-sqlite3

%description
%summary.

%prep
%setup -n SQLAlchemy-%version

%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install

mkdir -p %buildroot%bbmodulesdir
mv %buildroot%python3_sitelibdir/*  %buildroot%bbmodulesdir
rm -rf %buildroot%bbmodulesdir/*/testing

%files
%bbmodulesdir/*

%changelog
* Tue Sep 05 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.44-alt1
- Update to 1.4.44

* Sat Jul 03 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.23-alt1
- Build old version for buildbot
