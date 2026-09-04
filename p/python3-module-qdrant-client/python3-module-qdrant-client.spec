%define _unpackaged_files_terminate_build 1
%define pypi_name qdrant-client
%define pypi_name_snake qdrant_client

Name: python3-module-%pypi_name
Version: 1.19.0
Release: alt1

Summary: Client library for the Qdrant vector search engine
License: Apache-2.0
Group: Development/Python3

URL: https://pypi.org/project/qdrant-client
VCS: https://github.com/qdrant/qdrant-client
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(poetry.core)

BuildArch: noarch

%description
Client library and SDK for the Qdrant vector search engine.

Library contains type definitions for all Qdrant API and allows to make both
Sync and Async requests.

Client allows calls for all  directly. It also provides some additional helper
methods for frequently required operations, e.g. initial collection uploading.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir_noarch/%pypi_name_snake
%python3_sitelibdir_noarch/%pypi_name_snake-%version.dist-info
%doc README.md

%changelog
* Fri Sep 04 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.19.0-alt1
- Updated to version 1.19.0.

* Wed May 13 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.18.0-alt1
- Updated to version 1.18.0.

* Sat Mar 14 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.17.1-alt1
- Updated to version 1.17.1.

* Mon Feb 16 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.16.2-alt1
- Updated to version 1.16.2.
- Excluded tests from package to avoid pytest dependency.

* Mon Apr 14 2025 David Sultaniiazov <x1z53@altlinux.org> 1.13.3-alt1
- Initial build
