%define pypi_name proglog

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.10
Release: alt1

Summary: Logs and progress bars manager for Python

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/proglog
Vcs: https://github.com/Edinburgh-Genome-Foundry/Proglog

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-tqdm
%endif

%description
Proglog is a progress logging system for Python. It allows to build complex
libraries while giving your users control over logs, callbacks and progress bars.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.rst logo.png docs examples
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 26 2024 Alexander Kovalev <alexvk@altlinux.org> 0.1.10-alt1
- Initial build for ALT.
