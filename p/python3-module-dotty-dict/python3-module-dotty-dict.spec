%define _unpackaged_files_terminate_build 1
%define pypi_name dotty-dict
%define mod_name dotty_dict

Name: python3-module-%pypi_name
Version: 1.3.1
Release: alt1

Summary: Dictionary wrapper for quick access to deeply nested keys
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/dotty-dict/
Vcs: https://github.com/pawelzny/dotty_dict

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%description
Simple wrapper around python dictionary and dict like objects.
Two wrappers with the same dict are considered equal. Create,
read, update and delete nested keys of any length

%prep
%setup 

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jan 21 2026 Tatyana Gagina <treza@altlinux.org> 1.3.1-alt1
- Packaged for ALT Sisyphus.
