%define pypi_name cloudsplaining

%def_with check

Name:    python3-module-%pypi_name
Version: 0.7.0
Release: alt1

Summary: AWS IAM security assessment tool
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://cloudsplaining.readthedocs.io/
VCS:     https://github.com/salesforce/cloudsplaining

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-schema
BuildRequires: python3-module-yaml
BuildRequires: python3-module-policy_sentry
BuildRequires: python3-module-cached-property
BuildRequires: python3-module-boto3
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-click-option-group
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
Cloudsplaining identifies violations of least privilege in AWS IAM policies and
generates a pretty HTML report. It can scan all the policies in your AWS
account, across multiple AWS accounts, or it can scan a single policy file.

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
* Wed Oct 07 2026 Evgeniy Serov <scala@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
