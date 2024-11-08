Name: python3-module-mashumaro
Version: 3.14
Release: alt1

Summary: Fast and well tested serialization library
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/mashumaro/

Source0: %name-%version-%release.tar

BuildArch: noarch

BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-mock)
BuildRequires: python3(typing_extensions)
BuildRequires: python3(ciso8601)
BuildRequires: python3(pendulum)
BuildRequires: python3(tomli_w)
BuildRequires: python3(msgpack)
BuildRequires: python3(orjson)
BuildRequires: python3(yaml)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/mashumaro
%python3_sitelibdir/mashumaro-%version.dist-info

%changelog
* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.14-alt1
- 3.14 released
