%define pypi_name griffe

%def_with check

Name:    python3-module-%pypi_name
Version: 2.0.0
Release: alt1

Summary: Signatures for entire Python programs. Extract the structure, the frame, the skeleton of your project, to generate API documentation or find breaking changes in your API
License: ISC
Group:   Development/Python3
URL:     https://pypi.org/project/griffe
VCS:     https://github.com/mkdocstrings/griffe

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-uv-dynamic-versioning
BuildRequires: python3-module-pdm-backend

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-gitconfig
BuildRequires: python3-module-colorama
BuildRequires: python3-module-jsonschema
BuildRequires: python3-module-mkdocstrings
BuildRequires: python3-module-griffe-inherited-docstrings
%endif

Requires: python3-module-%pypi_name-lib

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%package cli
Summary: Signatures for entire Python programs. Extract the structure, the frame, the skeleton of your project, to generate API documentation or find breaking changes in your API
Group: Development/Python3
Requires: %name = %EVR

%description cli
%summary.

%package lib
Summary: Signatures for entire Python programs. Extract the structure, the frame, the skeleton of your project, to generate API documentation or find breaking changes in your API
Group: Development/Python3

%description lib
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
pushd packages/griffecli
%pyproject_build
popd
pushd packages/griffelib
%pyproject_build
popd

%install
%pyproject_install
pushd packages/griffecli
%pyproject_install
popd
pushd packages/griffelib
%pyproject_install
popd

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%files cli
%doc *.md
%_bindir/griffecli
%python3_sitelibdir/griffecli
%python3_sitelibdir/griffecli-%version.dist-info

%files lib
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/griffelib-%version.dist-info

%changelog
* Wed Mar 04 2026 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Automatically updated to 2.0.0.

* Wed Jan 21 2026 Grigory Ustinov <grenka@altlinux.org> 1.15.0-alt1
- Automatically updated to 1.15.0.

* Mon Sep 08 2025 Grigory Ustinov <grenka@altlinux.org> 1.14.0-alt1
- Automatically updated to 1.14.0.

* Tue Sep 02 2025 Grigory Ustinov <grenka@altlinux.org> 1.13.0-alt1
- Automatically updated to 1.13.0.

* Tue Aug 19 2025 Grigory Ustinov <grenka@altlinux.org> 1.12.1-alt1
- Automatically updated to 1.12.1.

* Sun Aug 03 2025 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt1
- Automatically updated to 1.9.0.

* Thu Jul 24 2025 Grigory Ustinov <grenka@altlinux.org> 1.8.0-alt1
- Automatically updated to 1.8.0.

* Thu Apr 24 2025 Grigory Ustinov <grenka@altlinux.org> 1.7.3-alt1
- Automatically updated to 1.7.3.

* Tue Apr 01 2025 Grigory Ustinov <grenka@altlinux.org> 1.7.2-alt1
- Automatically updated to 1.7.2.

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
