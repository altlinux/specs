%define _unpackaged_files_terminate_build 1

# checks don't work, because pytz in repo is too old
%def_without check

Name: python3-module-dirty-equals
Version: 0.4
Release: alt1

Summary: Doing dirty (but extremely useful) things with equals
License: MIT
Group: Development/Python3
Url: https://github.com/samuelcolvin/dirty-equals

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(poetry)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
%summary

dirty-equals is a python library that (mis)uses the __eq__ method to make
python code (generally unit tests) more declarative and therefore easier
to read and write.

dirty-equals can be used in whatever context you like, but it comes into
its own when writing unit tests for applications where you're commonly
checking the response to API calls and the contents of a database.

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
%doc README.md LICENSE
%python3_sitelibdir/*

%changelog
* Tue Jul 26 2022 Anton Zhukharev <ancieg@altlinux.org> 0.4-alt1
- initial build for Sisyphus

