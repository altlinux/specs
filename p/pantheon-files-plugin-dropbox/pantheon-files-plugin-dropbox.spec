Name: pantheon-files-plugin-dropbox
Version: 0.1
Release: alt2.revno22

Summary: Dropbox integration for Files
License: GPLv3+
Group: Graphical desktop/Other
Url: https://launchpad.net/pantheon-files

# bzr branch lp:~elementary-apps/pantheon-files/pantheon-files-plugin-dropbox-luna
Source0: %name.tar.xz

Packager: Igor Zubkov <icesik@altlinux.org>

Requires: pantheon-files

BuildRequires: cmake pantheon-files-devel libpixman-devel libexpat-devel
BuildRequires: libXdmcp-devel libXdamage-devel libXxf86vm-devel
BuildRequires: libharfbuzz-devel libpng-devel libXinerama-devel libXi-devel
BuildRequires: libXrandr-devel libXcursor-devel libXcomposite-devel
BuildRequires: libxkbcommon-devel libwayland-cursor-devel at-spi2-atk-devel
BuildRequires: gcc-c++

%description
Files Plugin Dropbox is an extension that integrates the Dropbox web service
with your Desktop.

%prep
%setup -q -n %name

%build
%cmake_insource
%make_build VERBOSE=1

%install
%make_install DESTDIR=%buildroot install

%ifarch x86_64
mkdir -p %buildroot%_libdir/
mv %buildroot/usr/lib/* %buildroot%_libdir/
%endif

%files
%_libdir/pantheon-files/plugins/*

%changelog
* Sat Sep 14 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt2.revno22
- Fix build on x86_64

* Sat Sep 14 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt1.revno22
- build for Sisyphus

