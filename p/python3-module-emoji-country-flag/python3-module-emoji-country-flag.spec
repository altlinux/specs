%define modname emoji-country-flag
%define pypi_name emoji_country_flag

%def_enable check

Name: python3-module-%modname
Version: 2.1.0
Release: alt1

Summary: En/Decode unicode country flags emoji
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/emoji-country-flag/

Vcs: https://github.com/cvzi/flag.git

Source: https://pypi.io/packages/source/e/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

BuildPreReq: rpm-build-python3
BuildRequires: python3(wheel) python3(setuptools)
%{?_enable_check:BuildRequires: python3(tox)
BuildRequires: python3(pytest) python3(emoji)}

%description
Converts flag emoji to ASCII and other way round.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
PYTHONPATH=%buildroot%python3_sitelibdir_noarch
py.test3


%files
%python3_sitelibdir/flag/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc README*

%changelog
* Fri Jan 09 2026 Yuri N. Sedunov <aris@altlinux.org> 2.1.0-alt1
- first build for Sisyphus

