%define _unpackaged_files_terminate_build 1
%define pypi_name liblore
%def_with check

Name: python3-module-%pypi_name
Version: 0.10.1
Release: alt1

Summary: Python library for public-inbox and lore.kernel.org access
License: GPL-2.0-or-later
Group: Development/Python3
Url: https://git.kernel.org/pub/scm/utils/liblore/liblore.git
Vcs: https://git.kernel.org/pub/scm/utils/liblore/liblore.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pyproject-installer
BuildRequires: python3-module-setuptools python3-module-wheel
%if_with check
BuildRequires: python3-module-requests
BuildRequires: python3-module-authheaders
BuildRequires: python3-module-pytest python3-module-pytest-asyncio
BuildRequires: python3-module-responses python3-module-typing_extensions
%endif

%description
liblore is a Python library for working with public-inbox servers,
particularly lore.kernel.org. It fetches email threads, parses mbox files,
summarises patch series, and provides utilities for working with email
messages from mailing list archives.

%prep
%setup -q

%build
%pyproject_build

%install
%pyproject_install

%check
%if_with check
%pyproject_run_pytest -vra tests
%endif

%files
%doc README.md CHANGELOG MIGRATIONS.md
%python3_sitelibdir/liblore/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Nov 16 2026 Vladislav Tatjanin <l27001@altlinux.org> 0.10.1-alt1
- Initial build.
