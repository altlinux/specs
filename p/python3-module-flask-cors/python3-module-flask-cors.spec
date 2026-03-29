%define _unpackaged_files_terminate_build 1
%define pypi_name Flask-Cors
%define pypi_nname flask-cors
%define mod_name flask_cors

%def_with check

Name: python3-module-%pypi_nname
Version: 6.0.2
Release: alt1.1

Summary: Cross Origin Resource Sharing (CORS) support for Flask
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Flask-Cors/
Vcs: https://github.com/corydolphin/flask-cors

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

# well-known PyPI name
Provides: python3-module-%pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-mkdocs
BuildRequires: python3-module-mkdocs-material
BuildRequires: python3-module-mkdocstrings
BuildRequires: python3-module-mypy
BuildRequires: python3-module-pre-commit
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-ruff

BuildRequires: python3-module-flask
BuildRequires: python3-module-werkzeug
%endif

%description
A Flask extension for handling Cross Origin Resource Sharing (CORS), making
cross-origin AJAX possible.

%prep
%setup
%autopatch -p1
echo '__version__ = "%version"' > flask_cors/version.py
sed -i 's/^version =.*$/version = "%version"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc CHANGELOG.md LICENSE README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 6.0.2-alt1.1
- Demodernized packaging.

* Mon Dec 22 2025 Anton Zhukharev <ancieg@altlinux.org> 6.0.2-alt1
- Updated to 6.0.2.

* Mon Jun 23 2025 Anton Zhukharev <ancieg@altlinux.org> 6.0.1-alt1
- Updated to 6.0.1.

* Thu May 22 2025 Anton Zhukharev <ancieg@altlinux.org> 6.0.0-alt1
- Updated to 6.0.0 (fixes CVE-2024-6839, CVE-2024-6844, CVE-2024-6866).

* Mon Feb 24 2025 Anton Zhukharev <ancieg@altlinux.org> 5.0.1-alt1
- Updated to 5.0.1.

* Thu Dec 12 2024 Anton Zhukharev <ancieg@altlinux.org> 5.0.0-alt1
- Updated to 5.0.0 (closes CVE-2024-6221).
- Built from upstream VCS.

* Wed Sep 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.0.9-alt1
- Initial build.
