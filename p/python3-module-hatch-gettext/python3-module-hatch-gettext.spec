%define _unpackaged_files_terminate_build 1
%define _name hatch-gettext
%define pypi_name hatch_gettext

# no tests defined
%def_disable check

Name: python3-module-%_name
Version: 1.1.1
Release: alt1

Summary: Hatch Gettext plugin
License: GPL-3.0-or-later
Group: Development/Python3
Url: https://pypi.org/project/hatch-gettext

Vcs: https://github.com/damonlynch/hatch-gettext.git

Source: https://pypi.io/packages/source/h/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch
%py3_provides %pypi_name

Requires: gettext-tools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(hatchling)
%{?_enable_check: BuildRequires:python3(pytest)
BuildRequires: python3(rich)}

%description
%pypi_name provides a build hook plugin for Hatch that compiles
multi-lingual messages with GNU gettext's tools msgfmt. It can also
(optionally) use intltool.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Apr 29 2026 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- first build for Sisyphus


