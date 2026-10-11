Name: flamerobin
Summary: Graphical client for Firebird
Version: 1.0.0
Release: alt1
License: MIT
Group: Databases

URL: http://www.flamerobin.org/
VCS: https://github.com/mariuz/flamerobin.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: firebird-devel
BuildRequires: libwxGTK3.2-devel
BuildRequires: ImageMagick-tools

%description
FlameRobin is a database administration tool for Firebird DBMS based on wxgtk
toolkit.

%prep
%setup
%autopatch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

install -d %buildroot{%_niconsdir,%_miconsdir,%_liconsdir}
magick -size 16x16 ./res/fricon128.png %buildroot%_miconsdir/%name.png
magick -size 32x32 ./res/fricon128.png %buildroot%_niconsdir/%name.png
magick -size 48x48 ./res/fricon128.png %buildroot%_liconsdir/%name.png

%files
%doc docs
%_man1dir/flamerobin.1.*
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_pixmapsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png

%changelog
* Sun Oct 11 2026 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- New version 1.0.0.

* Mon Oct 23 2023 Anton Midyukov <antohami@altlinux.org> 0.9.9-alt1
- New version 0.9.9.

* Thu Mar 16 2023 Anton Midyukov <antohami@altlinux.org> 0.9.6-alt1
- New version 0.9.6.
- Build with libwxGTK3.2.

* Sun Sep 26 2021 Anton Midyukov <antohami@altlinux.org> 0.9.3.9-alt1
- New version 0.9.3.9.
- Build with libwxGTK3.0.
- Update License tag.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9.0-alt2.qa2
- NMU: rebuilt for debuginfo.

* Tue Nov 17 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.0-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for flamerobin
  * postclean-05-filetriggers for spec file

* Mon May 25 2009 Boris Savelev <boris@altlinux.org> 0.9.0-alt2
- fix build with new toolchain

* Sat Oct 04 2008 Boris Savelev <boris@altlinux.org> 0.9.0-alt1
- initial build for Sisyphus from Mandriva
