%define _unpackaged_files_terminate_build 1
%define pypi_name telert
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.5
Release: alt1
Summary: Commandline and Python utility that alerts on command completion.
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/telert/
Vcs: https://github.com/navig-me/telert
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(requests)
BuildRequires: python3-module-beautifulsoup4
BuildRequires: python3(psutil)
BuildRequires: python3(ping3)

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
%summary

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
#package don't have tests
#tox_create_default_config
#tox_check_pyproject

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jul 22 2025 Pavel Shilov <zerospirit@altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus.
