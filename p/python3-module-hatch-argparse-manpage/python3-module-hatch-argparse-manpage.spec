%define _unpackaged_files_terminate_build 1
%define _name hatch-argparse-manpage
%define pypi_name hatch_argparse_manpage

# no tests defined
%def_disable check

Name: python3-module-%_name
Version: 1.0.1
Release: alt1

Summary: Hatch Argparse Manpage plugin
License: GPL-3.0-or-later
Group: Development/Python3
Url: https://pypi.org/project/hatch-argparse-manpage

Vcs: https://github.com/damonlynch/hatch-argparse-manpage.git

Source: https://pypi.io/packages/source/h/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch
%py3_provides %pypi_name

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(hatchling)
%{?_enable_check: BuildRequires:python3(pytest)
BuildRequires: python3(rich) python3(argparse-manpage)}

%description
%pypi_name provides a build hook plugin for Hatch to automatically
generate a manual page from an ArgumentParser object, using
argparse-manpage package.

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
* Wed Apr 29 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- first build for Sisyphus


