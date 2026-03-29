%define _unpackaged_files_terminate_build 1
%define pypi_name enrich
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.7
Release: alt1.1
Summary: Enriched extends rich library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/enrich
Vcs: https://github.com/pycontribs/enrich
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: git
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pip

%if_with check
BuildRequires: python3-module-rich
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-xdist
%endif

%description
Enriched extends rich library functionality with a set of changes that were not
accepted to rich itself.

%prep
%setup
%autopatch -p1
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m "release"
    git tag "%version"
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
# don't ship tests
%exclude %python3_sitelibdir/%mod_name/test/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 1.2.7-alt1.1
- Demodernized packaging.

* Wed Aug 16 2023 Stanislav Levin <slev@altlinux.org> 1.2.7-alt1
- Initial build for Sisyphus.
