%define pypi_name owlrl

%def_with check

Name:    python3-module-%pypi_name
Version: 7.6.2
Release: alt1

Summary: OWL 2 RL profile and basic RDFS inference implementation for RDFLib
License: W3C-20150513
Group:   Development/Python3
URL:     https://github.com/RDFLib/OWL-RL
VCS:     https://github.com/RDFLib/OWL-RL

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-rdflib
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
OWL-RL provides an implementation of the OWL 2 RL profile and basic RDFS
inference on top of RDFLib using forward chaining.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc LICENSE.txt *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Oct 06 2026 Evgeniy Serov <scala@altlinux.org> 7.6.2-alt1
- Initial build for Sisyphus.
