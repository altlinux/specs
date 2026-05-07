Name: tirith
Version: 1.0.5
Release: alt1

Summary: StackGuardian Policy as Code framework for IaC compliance scanning

License: Apache-2.0
Group: Development/Other
Url: https://github.com/StackGuardian/tirith

# Source-url: https://github.com/StackGuardian/tirith/archive/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Tirith (StackGuardian Policy Framework) scans declarative Infrastructure
as Code (IaC) configurations like Terraform plans against policies defined
using JSON. It simplifies defining Policy as Code for IaC compliance and
security checks across multiple providers including Terraform, Infracost,
StackGuardian Workflow, JSON, and Kubernetes.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md CHANGELOG.md
%_bindir/tirith
%python3_sitelibdir/%name/
%python3_sitelibdir/py_tirith-%version.dist-info/

%changelog
* Thu May 07 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- initial build for ALT Sisyphus
