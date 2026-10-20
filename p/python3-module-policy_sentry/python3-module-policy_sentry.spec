%define pypi_name policy_sentry

%def_with check

Name:    python3-module-%pypi_name
Version: 0.13.2
Release: alt1

Summary: IAM Least Privilege Policy Generator
License: MIT
Group:   Development/Python3
URL:     https://policy-sentry.readthedocs.io/
VCS:     https://github.com/salesforce/policy_sentry

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-click
BuildRequires: python3-module-orjson
BuildRequires: python3-module-yaml
BuildRequires: python3-module-schema
BuildRequires: python3-module-requests
BuildRequires: python3-module-beautifulsoup4
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
Policy Sentry is an AWS IAM Least Privilege Policy Generator, auditor, and
analysis database. It compiles database tables based on the AWS IAM
Documentation on Actions, Resources, and Condition Keys and leverages that data
to create least-privilege IAM policies.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc LICENSE *.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 08 2026 Evgeniy Serov <scala@altlinux.org> 0.13.2-alt1
- Initial build for Sisyphus.
