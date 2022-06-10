%define oname yaql
# Version 2.0.0 doesn't support recent sphinx
%def_without docs

Name: python3-module-%oname
Version: 2.0.0
Release: alt1

Summary: YAQL - Yet Another Query Language

Group: Development/Python3
License: Apache-2.0
Url: https://pypi.org/project/yaql

Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr
BuildRequires: python3-module-babel
BuildRequires: python3-module-ply
BuildRequires: python3-module-dateutil

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
%endif

BuildArch: noarch

%description
YAQL (Yet Another Query Language) is an embeddable and extensible query language,
that allows performing complex queries against arbitrary objects.
It has a vast and comprehensive standard library of frequently 
used querying functions and can be extend even further with user-specified functions.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: yaql documentation
Group: Development/Documentation

%description doc
Documentation for yaql
%endif

%prep
%setup -n %oname-%version
# Remove bundled egg-info
rm -rf %oname.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%python3_build

%if_with docs
# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo
%endif

%install
%python3_install

%files
%doc README.rst
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%if_with docs
%files doc
%doc doc/build/html
%endif

%changelog
* Fri Jun 10 2022 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Build new version.

* Thu May 21 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt3
- Fixed FTBFS.
- Fixed Url.

* Fri Jan 10 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt2
- Build without python2.
- Fix license.

* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 1.1.3-alt1
- 1.1.3

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- Initial Package
