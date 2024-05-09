%define _unpackaged_files_terminate_build 1
%define pypi_name setuptools-gettext

Name: python3-module-%pypi_name
Version: 0.1.13
Release: alt1
License: GPLv2
Source: %pypi_name-%version.tar
Patch: alt-drop-distutils.patch
Group: Development/Python3
BuildArch: noarch
Summary: setuptools plugin for building mo files
Url: https://pypi.org/project/%pypi_name/

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%py3_provides %pypi_name

%description
This plugin adds build_mo, clean_mo and install_mo subcommands for setup.py as
well as hooking those into standard commands.

%prep
%setup -n %pypi_name-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/setuptools_gettext/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed May 08 2024 L.A. Kostis <lakostis@altlinux.ru> 0.1.13-alt1
- Initial build for ALTLinux.

