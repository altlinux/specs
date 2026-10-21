%define pypi_name spdx-tools
%define mod_name spdx_tools

%def_with check

Name:    python3-module-%pypi_name
Version: 0.8.5
Release: alt1

Summary: A Python library to parse, validate and create SPDX documents
License: Apache-2.0
Group:   Development/Python3
URL:     http://spdx.org/
VCS:     https://github.com/spdx/tools-python

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildREquires: python3-module-wheel

%if_with check
BuildRequires: python3-module-semantic_version
BuildRequires: python3-module-beartype
BuildRequires: python3-module-license-expression
BuildRequires: python3-module-pyshacl
BuildRequires: python3-module-ply
BuildRequires: python3-module-uritools
BuildRequires: python3-module-xmltodict
BuildRequires: python3-module-click
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
SPDX is an open standard for communicating software bill of material
information, including provenance, license, security, and other related
information. SPDX reduces redundant work by providing common formats for
organizations and communities to share important data, thereby streamlining
and improving compliance, security, and dependability. The SPDX specification
is recognized as the international open standard for security, license
compliance, and other software supply chain artifacts as ISO/IEC 5962:2021.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc *.md
%_bindir/pyspdxtools
%_bindir/pyspdxtools3
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Oct 07 2026 Evgeniy Serov <scala@altlinux.org> 0.8.5-alt1
- Initial build for Sisyphus.
