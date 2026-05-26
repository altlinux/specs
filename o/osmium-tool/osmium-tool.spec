%define _unpackaged_files_terminate_build 1

%def_with check

Name:    osmium-tool
Version: 1.19.1
Release: alt1

Summary: Command line tool for working with OpenStreetMap data based on the Osmium library
License: GPL-3.0
Group:   System/Libraries
URL:     https://osmcode.org/osmium-tool/
VCS:     https://github.com/osmcode/osmium-tool

Source:  %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: boost-program_options-devel
BuildRequires: libosmium-devel
BuildRequires: nlohmann-json-devel
BuildRequires: liblz4-devel
BuildRequires: pandoc
%if_with check
BuildRequires: ctest
%endif

%description
Command line tool for working with OpenStreetMap data
based on the Osmium library.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_datadir/zsh/site-functions
install -p -m644 zsh_completion/* %buildroot%_datadir/zsh/site-functions

%check
OSMIUM_PAGER=cat %ctest

%files
%_bindir/osmium
%_mandir/man1/osmium*.1*
%_mandir/man5/osmium*.5*
%_datadir/zsh/site-functions/_osmium

%changelog
* Mon May 25 2026 Alexey Volkov <qualimock@altlinux.org> 1.19.1-alt1
- Initial build for ALT
