%define pypi_name daphne

%def_with check

Name: python3-module-%pypi_name
Version: 4.2.2
Release: alt1

Summary: Django Channels HTTP/WebSocket server
License: BSD-3-Clause
Group: Development/Python3
URL: https://github.com/django/daphne

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-twisted
BuildRequires: python3-module-autobahn
BuildRequires: python3-module-asgiref
BuildRequires: python3-module-django
%endif

%description
Daphne is a HTTP, HTTP2 and WebSocket protocol server for ASGI and ASGI-HTTP,
developed to power Django Channels.

It supports automatic negotiation of protocols; there's no need for URL
prefixing to determine WebSocket endpoints versus HTTP endpoints.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/twisted
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 08 2026 Andrey Kovalev <ded@altlinux.org> 4.2.2-alt1
- Updated to upstream version 4.2.2.

* Tue Mar 10 2026 Andrey Kovalev <ded@altlinux.org> 4.2.1-alt1
- Updated to upstream version 4.2.1.

* Fri Aug 01 2025 Alexandr Shashkin <dutyrok@altlinux.org> 4.1.2-alt3
- Built with Hypothesis supplied without numerous redundant dependencies.

* Mon Oct 28 2024 Anton Vyatkin <toni@altlinux.org> 4.1.2-alt2
- Fixed FTBFS.

* Mon Jul 22 2024 Anton Vyatkin <toni@altlinux.org> 4.1.2-alt1
- Initial build for Sisyphus.
