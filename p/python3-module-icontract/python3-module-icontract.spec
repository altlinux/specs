%define _unpackaged_files_terminate_build 1

%define oname icontract

%def_with check

Name: python3-module-%oname
Version: 2.6.6
Release: alt1

Summary: Design-by-contract in Python3 with informative violation messages and inheritance.
License: MIT
Group: Development/Python3
Url: https://github.com/Parquery/icontract.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(asttokens)
BuildRequires: python3(numpy)
BuildRequires: python3(typeguard)
BuildRequires: python3(astor)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox)
%endif

%description
Icontract provides design-by-contract to Python3 with informative
violation messages and inheritance.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject -vra tests

%files
%doc *.rst LICENSE.txt
%python3_sitelibdir/*

%changelog
* Wed Jun 19 2024 Dmitry Lyalyaev <fruktime@altlinux.org> 2.6.6-alt1
- Initial build for ALT Linux
