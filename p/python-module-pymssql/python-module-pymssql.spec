Name: python-module-pymssql
Version: 2.0.0b1_dev_20130611
Release: alt2
Url: http://code.google.com/p/pymssql/
Summary: A simple database interface to MS-SQL for Python
License: LGPL-2.1
Group: Development/Python
Packager: Evgenii Terechkov <evg@altlinux.org>
Source0: %name-%version.tar
Patch0: setup.py.diff

BuildRequires: python-module-setuptools
BuildRequires: python-module-Cython
BuildRequires: libfreetds-devel

%description

pymssql is the Python language extension module that provides access
to Microsoft SQL Servers from Python scripts. It is compliant with
Python DB-API 2.0 Specification and works on most popular operating
systems.

The pymssql package consists of two modules:

    pymssql -- use it if you care about DB-API compliance, or if you
    are accustomed to DB-API syntax,
    _mssql -- use it if you care about performance and ease of use
    (_mssql module is easier to use than pymssql).

%prep
%setup -n %name-%version
%patch0

%build
rm -rf freetds                   # wipe bundled freetds binaries
%python_build

%install
%python_install --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc README ChangeLog

%changelog
* Sun Aug 17 2014 Terechkov Evgenii <evg@altlinux.org> 2.0.0b1_dev_20130611-alt2
- Build from git, not srpm

* Tue Oct  8 2013 Terechkov Evgenii <evg@altlinux.org> 2.0.0b1_dev_20130611-alt1
- Initial build for ALT Linux Sisyphus
