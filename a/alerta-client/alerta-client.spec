%define pypi_name alerta

Name:       alerta-client
Version:    8.5.3
Release:    alt1

Summary:    Alerta unified command-line tool and SDK
License:    Apache-2.0
Group:      Monitoring
Url:        https://github.com/alerta/python-alerta-client

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-requests-mock
BuildRequires: python3-module-requests-hawk
BuildRequires: python3-module-click
BuildRequires: python3-module-pytz
BuildRequires: python3-module-tabulate

%description
Alerta is a monitoring tool used to consolidate and de-duplicate alerts
from multiple sources for quick at-a-glance visualisation.

This package provides the unified command-line tool (alerta) and the
Python SDK (alertaclient) for the Alerta API. The tool allows you to
send, query, tag, acknowledge, close and delete alerts, manage API keys,
blackouts, users, customers and heartbeats from the command line.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install --exclude-paths 'tests/*'

%check
# tests/integration requires a live instanse of alerta so we are not running them for hasher
%pyproject_run_pytest -vra tests/unit

%files
%doc NOTICE README.md
%_bindir/%pypi_name
%python3_sitelibdir_noarch/alertaclient
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 07 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 8.5.3-alt1
- Initial build for ALT.

