%define pypi_name sphinx-autobuild

%def_with check

Name:    python3-module-%pypi_name
Version: 2024.9.3
Release: alt1

Summary: Watch a Sphinx directory and rebuild the documentation when a change is detected

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/sphinx-autobuild
VCS:     https://github.com/executablebooks/sphinx-autobuild

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit

%if_with check
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-livereload
BuildRequires: python3-module-colorama
BuildRequires: python3-module-starlette
BuildRequires: python3-module-uvicorn
BuildRequires: python3-module-httpx
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
Watch a Sphinx directory and rebuild the documentation when a change is detected.
Also includes a livereload enabled web server.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.rst
%_bindir/sphinx-autobuild
%python3_sitelibdir/sphinx_autobuild
%python3_sitelibdir/sphinx_autobuild-%version.dist-info

%changelog
* Wed Sep 11 2024 Grigory Ustinov <grenka@altlinux.org> 2024.9.3-alt1
- Automatically updated to 2024.9.3.

* Fri Apr 19 2024 Grigory Ustinov <grenka@altlinux.org> 2024.4.16-alt1
- Automatically updated to 2024.4.16.

* Tue Apr 16 2024 Grigory Ustinov <grenka@altlinux.org> 2024.04.13-alt1
- Automatically updated to 2024.04.13.

* Sat Feb 10 2024 Grigory Ustinov <grenka@altlinux.org> 2024.02.04-alt1
- Automatically updated to 2024.02.04.

* Tue Sep 19 2023 Grigory Ustinov <grenka@altlinux.org> 2021.03.14-alt1
- Initial build for Sisyphus.
