%define _unpackaged_files_terminate_build 1
%define pypi_name sqids
%define mod_name sqids

Name: python3-module-%pypi_name
Version: 0.5.2
Release: alt1

Summary: This is a library for generating unique identifiers from numbers and also for shortening links
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/sqids/
Vcs: https://github.com/sqids/sqids-python

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
This is a small library that lets you generate unique IDs from
numbers. It's good for link shortening, fast & URL-safe ID
generation and decoding back into numbers for quicker database lookups

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc CHANGELOG.md LICENSE README*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Feb 04 2026 Tatyana Gagina <treza@altlinux.org> 0.5.2-alt1
- Packaged for ALT Sisyphus.
