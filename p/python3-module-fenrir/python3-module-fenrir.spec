%define _unpackaged_files_terminate_build 1
%define pypi_name fenrir

%def_without check

Name:    python3-module-%pypi_name
Version: 1.9.8
Release: alt1

Summary: Python3 module for %pypi_name
License: LGPL-3.0
Group:   Development/Python3
URL:     https://github.com/chrys87/fenrir
Requires: python3-module-espeak
Requires: python3-module-evdev
Requires: sox
Requires: speech-dispatcher
Requires: python3-module-pyenchant
Requires: python3-module-daemonize

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%package -n %pypi_name
Summary: An TTY screenreader for Linux.
Group: Accessibility
BuildArch: noarch
Requires: %name = %EVR

%description -n %pypi_name
A modern, modular, flexible and fast console screenreader.
It should run on any operating system. If you want to help, or write drivers to make it work on other systems, just let me know.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install
mv %buildroot%python3_sitelibdir%_sysconfdir %buildroot
cp -r %buildroot%python3_sitelibdir/usr/* %buildroot/usr/
rm -r %buildroot%python3_sitelibdir/usr

install -Dm 755 autostart/systemd/Arch/%pypi_name.service %buildroot%_systemd_dir/system/%pypi_name

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/fenrir_screenreader-1.9.7.post1.dist-info
%python3_sitelibdir/fenrirscreenreader
%_datadir/sounds/fenrirscreenreader/*
%_datadir/fenrirscreenreader/*


%files -n %pypi_name
%_bindir/%pypi_name
%_bindir/%pypi_name-daemon
%config(noreplace) %_sysconfdir/fenrirscreenreader/*
%_systemd_dir/system/%pypi_name
%_man1dir/%pypi_name.1.xz

%changelog
* Sat Nov 02 2024 Artem Semenov <savoptik@altlinux.org> 1.9.8-alt1
- Initial build for Sisyphus (ALT bug: 51707)
