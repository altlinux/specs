%define pypi_name configshell-fb

Name: python3-module-%pypi_name
Version: 2.0.2
Release: alt1

Summary: A framework to implement simple but nice CLIs
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/configshell-fb
Vcs: https://github.com/open-iscsi/configshell-fb

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs

Obsoletes: python3-module-configshell < %EVR

%description
Configshell-fb is a Python library that provides a framework
for building simple but nice CLI-based applications.

%prep
%setup -n %pypi_name-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%files
%doc README.*
%python3_sitelibdir/__pycache__/configshell_fb.*
%python3_sitelibdir/configshell_fb.py
%python3_sitelibdir/configshell/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed May 21 2025 Anton Vyatkin <toni@altlinux.org> 2.0.2-alt1
- Initial build for Sisyphus.
