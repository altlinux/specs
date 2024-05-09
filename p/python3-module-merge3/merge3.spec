%define _unpackaged_files_terminate_build 1
%define pypi_name merge3

Name: python3-module-%pypi_name
Version: 0.0.15
Release: alt1
License: GPLv2
Source: %pypi_name-%version.tar
Group: Development/Python3
BuildArch: noarch
Summary: A Python implementation of 3-way merge of texts
Url: https://pypi.org/project/%pypi_name/

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%py3_provides %pypi_name

%description
A Python implementation of 3-way merge of texts.

Given BASE, OTHER, THIS, tries to produce a combined text incorporating the
changes from both BASE->OTHER and BASE->THIS. All three will typically be
sequences of lines.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%doc *.rst COPYING AUTHORS
%_bindir/%{pypi_name}
%python3_sitelibdir/%{pypi_name}/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 09 2024 L.A. Kostis <lakostis@altlinux.ru> 0.0.15-alt1
- Initial build for ALTLinux.

