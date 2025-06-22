%define _unpackaged_files_terminate_build 1

Name: rename-flac
Version: 2.3.0
Release: alt1

Summary: CLI tool to rename FLAC files
License: GPL-3.0
Group: Sound
URL: https://gitlab.com/baldurmen/rename-flac

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(flit-core)
BuildRequires: /usr/bin/rst2man

BuildArch: noarch

Source: %name-%version.tar

%description
rename-flac is a command-line tool that takes the information from FLAC
metadata to batch rename the files according to a filenaming scheme.

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install
mkdir -pv %buildroot/%_man1dir/
rst2man manpage.rst %buildroot/%_man1dir/rename-flac.1

%files
%doc CHANGELOG  LICENSE README.md
%_bindir/%name
%_man1dir/*
%exclude %python3_sitelibdir/__pycache__
%python3_sitelibdir/%{pyproject_distinfo rename_flac}
%python3_sitelibdir/rename_flac.py

%changelog
* Sun Jun 22 2025 Nikolay Strelkov <snk@altlinux.org> 2.3.0-alt1
- Initial build for Sisyphus
