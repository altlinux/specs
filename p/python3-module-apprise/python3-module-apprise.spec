%define pypi_name apprise
Name:    python3-module-%pypi_name
Version: 1.9.5
Release: alt1
Summary: Push Notifications that work with just about every platform!
License: BSD-2-Clause
URL:     https://pypi.org/project/apprise
VCS:     https://github.com/caronc/apprise
Source:  %name-%version.tar
Group:   Development/Python3

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-yaml
BuildRequires: python3-module-markdown
BuildRequires: python3-module-requests
BuildRequires: python3-module-click
BuildRequires: python3-module-requests-oauthlib

%description
Apprise allows you to send a notification to almost all of the most popular
notification services available to us today such as:
Telegram, Discord, Slack, Amazon SNS, Gotify, etc.

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -q --disable-warnings --maxfail=1 tests

%files
%doc README* LICENSE*
%python3_sitelibdir/apprise-%version.dist-info
%python3_sitelibdir/apprise

%changelog
* Fri Oct 31 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 1.9.5-alt1
- Initial build.
