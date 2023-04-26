%define  modulename doc8

%def_with docs
%def_with check

Name:    python3-module-%modulename
Version: 1.1.1
Release: alt1

Summary: Style checker for sphinx (or other) rst documentation.

License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/openstack/doc8

BuildArch: noarch

Source:  %modulename-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_with docs
BuildRequires: python3-module-sphinx_rtd_theme
%endif

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-stevedore
BuildRequires: python3-module-restructuredtext_lint
%endif

Requires: python3-module-tomli

%description
Doc8 is an opinionated style checker for rst_ (with basic support for
plain text) styles of documentation.

%if_with docs
%package doc
Summary: Documentation for %modulename
Group: Development/Documentation

%description doc
Documentation for %modulename.
%endif

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install

%if_with docs
export PYTHONPATH="$PWD"

# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%check
%pyproject_run_pytest

%files
%_bindir/*
%python3_sitelibdir/%modulename
%python3_sitelibdir/%{pyproject_distinfo %modulename}
%exclude %python3_sitelibdir/%modulename/tests

%if_with docs
%files doc
%doc LICENSE html
%endif

%changelog
* Wed Apr 26 2023 Anton Vyatkin <toni@altlinux.org> 1.1.1-alt1
- NMU: New version 1.1.1 (Fix BuildRequires)

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt2
- NMU: fix build (add missed mock)

* Mon Jun 29 2020 Grigory Ustinov <grenka@altlinux.org> 0.8.1-alt1
- Build new version.
- Add docs.
- Add check.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt2
- Build without python2.

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus.
