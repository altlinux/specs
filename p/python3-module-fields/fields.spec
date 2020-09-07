%define _unpackaged_files_terminate_build 1
%define oname fields

%def_with full_tests

Name: python3-module-%oname
Version: 5.0.0
Release: alt3
Summary: Container class boilerplate killer
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/fields

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with full_tests
BuildRequires: python3(attr) python3(characteristic) python3(pytest_benchmark)
%endif

%description
Container class boilerplate killer.

%prep
%setup
# Pytest4.x compatibility
grep -qsF '[pytest]' setup.cfg || exit 1
sed -i 's/\[pytest\]/[tool:pytest]/g' setup.cfg

# this file is not needed in python3
rm src/fields/py2ordereddict.py

%build
%python3_build_debug

%install
%python3_install

%check
%if_with full_tests
py.test3
%endif

%files
%doc LICENSE *.rst
%python3_sitelibdir/*

%changelog
* Mon Sep 07 2020 Stanislav Levin <slev@altlinux.org> 5.0.0-alt3
- Stopped Python2 package build.

* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 5.0.0-alt2
- Fixed Pytest4.x compatibility error.

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.0.0-alt1
- Initial build for ALT.
