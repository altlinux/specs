%define _unpackaged_files_terminate_build 1
%define pypi_name Flask-Cors
%define mod_name flask_cors

%def_with check

Name: python3-module-flask-cors
Version: 5.0.0
Release: alt1

Summary: Cross Origin Resource Sharing (CORS) support for Flask
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/Flask-Cors/
Vcs: https://github.com/corydolphin/flask-cors

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
# well-known PyPI name
Provides: python3-module-%pypi_name = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
A Flask extension for handling Cross Origin Resource Sharing (CORS), making
cross-origin AJAX possible.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra -o=addopts=-Wignore

%files
%doc CHANGELOG.md LICENSE README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/Flask_Cors-%version.dist-info/

%changelog
* Thu Dec 12 2024 Anton Zhukharev <ancieg@altlinux.org> 5.0.0-alt1
- Updated to 5.0.0 (closes CVE-2024-6221).
- Built from upstream VCS.

* Wed Sep 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.0.9-alt1
- Initial build.
