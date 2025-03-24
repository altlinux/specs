%define pypi_name griffe

%def_with check

Name:    python3-module-%pypi_name
Version: 1.6.2
Release: alt1

Summary: Signatures for entire Python programs. Extract the structure, the frame, the skeleton of your project, to generate API documentation or find breaking changes in your API
License: ISC
Group:   Development/Python3
URL:     https://pypi.org/project/griffe
VCS:     https://github.com/mkdocstrings/griffe

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pdm-backend

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-colorama
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-mkdocstrings
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/_%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Mar 25 2025 Grigory Ustinov <grenka@altlinux.org> 1.6.2-alt1
- Automatically updated to 1.6.2.

* Thu Mar 20 2025 Grigory Ustinov <grenka@altlinux.org> 1.6.1-alt1
- Automatically updated to 1.6.1.

* Tue Mar 04 2025 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1
- Automatically updated to 1.6.0.

* Tue Feb 25 2025 Grigory Ustinov <grenka@altlinux.org> 1.5.7-alt1
- Automatically updated to 1.5.7.

* Tue Dec 19 2023 Alexander Burmatov <thatman@altlinux.org> 0.38.1-alt1
- Update version to 0.38.1.

* Wed Oct 25 2023 Alexander Burmatov <thatman@altlinux.org> 0.36.7-alt1
- Initial build for Sisyphus.
