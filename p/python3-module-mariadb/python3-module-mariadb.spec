%define _unpackaged_files_terminate_build 1
%define pypi_name mariadb

Name: python3-module-%pypi_name
Version: 1.1.10
Release: alt1

Summary: MariaDB Connector/Python
License: LGPL-2.1-or-later
Group: Development/Python3
Url: https://pypi.org/project/mariadb/
Vcs: https://github.com/mariadb-corporation/mariadb-connector-python

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: libmariadb-devel

%description
MariaDB Connector/Python enables python programs to access MariaDB and
MySQL databases, using an API which is compliant with the Python
DB API 2.0 (PEP-249). It is written in C and uses MariaDB Connector/C
client library for client server communication.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Feb 09 2024 Anton Zhukharev <ancieg@altlinux.org> 1.1.10-alt1
- Updated to 1.1.10.

* Wed Dec 27 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.9-alt1
- Updated to 1.1.9.
- Distributed under LGPL-2.1-or-later license.

* Fri Oct 13 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.8-alt1
- Updated to 1.1.8.

* Thu Jul 20 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.7-alt1
- Updated to 1.1.7.

* Sun Jun 18 2023 Anton Zhukharev <ancieg@altlinux.org> 1.1.6-alt1
- Initial build for ALT Sisyphus.

