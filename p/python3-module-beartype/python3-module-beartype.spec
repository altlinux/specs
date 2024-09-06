%define _unpackaged_files_terminate_build 1

%define oname beartype

%def_with check

Name: python3-module-%oname
Version: 0.18.5
Release: alt2

Summary: Unbearably fast near-real-time hybrid runtime-static type-checking in pure Python.
License: MIT
Group: Development/Python3
Url: https://github.com/beartype/beartype
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox)
%endif

%description
Beartype is an open-source pure-Python PEP-compliant near-real-time hybrid
runtime-static third-generation type checker emphasizing efficiency, usability,
unsubstantiated jargon we just made up, and thrilling puns.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Fri Sep 06 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 0.18.5-alt2
- fix URL address in spec file

* Wed Jun 19 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 0.18.5-alt1
- Initial build for ALT Linux
