%define unpackaged_files_terminate_build 1

Name: qtl866
Version: 1.0.0
Release: alt1

Summary: GUI driver for minipro EPROM/Device programmer software
License: %gpl3plus

Requires: minipro

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-macros-cmake

Group: Other
Url: https://github.com/wd5gnr/qtl866
Source0: %name-%version.tar

BuildRequires: cmake
BuildRequires: cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-tools-devel

%description
GUI driver for minipro EPROM/Device programmer software

%prep
%setup -q

%build
%cmake
%install
%cmakeinstall_std
install -v -p -m 655 -D ./binhexedit %buildroot%_bindir/binhexedit

%files
%_bindir/qtl866
%_bindir/binhexedit

%changelog
* Tue Feb 10 2023 Aleksey Saprunov <sav@altlinux.org> 1.0.0-alt1
- Initial release

