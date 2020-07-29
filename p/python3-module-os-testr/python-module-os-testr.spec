%define oname os-testr

Name: python3-module-os-testr
Version: 2.0.0
Release: alt1
Summary: A testr wrapper to provide functionality for OpenStack projects
Group: Development/Python3
License: Apache-2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Packager: Lenar Shakirov <snejok@altlinux.ru>
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-pbr
BuildRequires: python3-module-setuptools

Requires: python3-module-pbr
Requires: python3-module-babel
Requires: python3-module-testrepository
Requires: python3-module-subunit
Requires: python3-module-testtools
Requires: python3-module-setuptools

%description
ostestr is a testr wrapper that uses subunit-trace for output and builds
some helpful extra functionality around testr.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for ostestr module
Group: Development/Documentation

%description doc
Documentation for ostestr module

%prep
%setup -n %oname-%version

rm -f test-requirements.txt requirements.txt

%build
%python3_build

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
#sphinx-build-3 -b html -d build/doctrees source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%python3_install

%files
%doc README.rst
%_bindir/generate-subunit
%_bindir/ostestr
%_bindir/subunit-trace
%_bindir/subunit2html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

#%%files doc
#%%doc doc/build/html

%changelog
* Wed Jul 29 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Build new version.
- Fix license.

* Tue Oct 29 2019 Grigory Ustinov <grenka@altlinux.org> 0.8.2-alt2
- Build without python2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 0.8.2-alt1
- 0.8.2
- add test packages

* Mon Nov 14 2016 Lenar Shakirov <snejok@altlinux.ru> 0.6.0-alt1
- Initial build for ALT (based on CentOS 0.6.0-1.el7.src)

