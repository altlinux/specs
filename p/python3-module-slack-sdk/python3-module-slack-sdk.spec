%define pypi_name slack-sdk

%def_with check

Name: python3-module-%pypi_name
Version: 3.33.0
Release: alt1

Summary: Slack Developer Kit for Python
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/slack-sdk
VCS: https://github.com/slackapi/python-slack-sdk

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-websockets
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-boto3
BuildRequires: python3-module-sqlalchemy
BuildRequires: python3-module-moto
BuildRequires: python3-module-websocket-client
%endif

%description
The Slack platform offers several APIs to build apps. Each Slack API delivers
part of the capabilities from the platform, so that you can pick just those that
fit for your needs. This SDK offers a corresponding package for each of
Slack's APIs. They are small and powerful when used independently, and work
seamlessly when used together, too.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v -k 'not TestRTMClient and not test_send_message_while_disconnection'

%files
%doc README.*
%python3_sitelibdir/slack
%python3_sitelibdir/slack_sdk
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Sep 17 2024 Anton Vyatkin <toni@altlinux.org> 3.33.0-alt1
- New version 3.33.0.

* Mon Sep 09 2024 Anton Vyatkin <toni@altlinux.org> 3.32.0-alt1
- New version 3.32.0.

* Sun Jul 21 2024 Anton Vyatkin <toni@altlinux.org> 3.31.0-alt1
- Initial build for Sisyphus.
