%define _unpackaged_files_terminate_build 1
%define appname PE-bear

Name: pe-bear
Version: 0.7.2
Release: alt1

Summary: Portable Executable reversing tool with a friendly GUI
License: GPL-2.0-or-later
Group: Development/Tools
Url: https://hshrzd.wordpress.com/pe-bear
VCS: https://github.com/hasherezade/pe-bear.git

# Source-url: https://github.com/hasherezade/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: bearparser.tar
Source2: capstone.tar
Source3: sig_finder.tar

BuildRequires: qt6-base-devel

%description
PE-bear is a multiplatform reversing tool for PE files. Its objective
is to deliver fast and flexible "first view" for malware analysts,
stable and capable to handle malformed PE files.

%prep
%setup -a1 -a2 -a3

# use lowercase project name
sed -i 's;\(add_dependencies(\)%appname\(.*\)$;\1%name\2;' CMakeLists.txt
sed -i 's;\(project\s\?(\).*\()\);\1%name\2;' pe-bear/CMakeLists.txt

%build
%cmake
%cmake_build

%install
sed -i 's;\(Name=\).*;\1%appname;' %_cmake__builddir/%name/%name.desktop
%cmake_install

%files
%doc README.md
%_bindir/%name
%_desktopdir/net.hasherezade.pe-bear.desktop
%_datadir/metainfo/net.hasherezade.pe-bear.metainfo.xml
%_pixmapsdir/net.hasherezade.pe-bear.png

%changelog
* Tue Jun 23 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.7.2-alt1
- new version

* Fri Mar 13 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.7.1-alt1
- initial build for ALT Linux
