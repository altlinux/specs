%define _unpackaged_files_terminate_build 1

Name: qtm
Version: 0.7.1.3
Release: alt1.qa2

Summary: Qt4 blogging client
License: GPLv2+
Group: Networking/Other

Url: http://qtm.blogistan.co.uk/
Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: %name-%version.tar.gz
Patch0: %name-0.7.3.1-alt-desktop-fixes.patch

BuildPreReq: cmake gcc-c++ libqt4-devel
BuildRequires: desktop-file-utils

%description
QTM is a blogging client which is presently capable of composing,
formatting and submitting blog entries to a weblog. QTM will work with
blogs based on most of the major blogging systems available today:
Wordpress (including wordpress.com), Movable Type, Drupal and so on.

%prep
%setup
%patch0 -p1
mkdir build/
cd build
cmake ../ \
        -DCMAKE_INSTALL_PREFIX=%_prefix \
%ifarch x86_64
        -DLIB_SUFFIX=64 \
%endif
        -DCMAKE_BUILD_TYPE="Release" \
        -DCMAKE_CXX_FLAGS:STRING="%optflags" \
        -DCMAKE_SKIP_RPATH=YES

%build
cd build
%make_build VERBOSE=1

%install
cd build
%makeinstall DESTDIR=%buildroot

mkdir -p %buildroot%_pixmapsdir
mv %buildroot%_iconsdir/* %buildroot%_pixmapsdir/
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=WebDevelopment \
	%buildroot%_desktopdir/qtm.desktop

%files
%doc Changelog INSTALL README
%_bindir/*
%_desktopdir/*.desktop
%_pixmapsdir/*.png
%_man1dir/%name.*

%changelog
* Tue May 17 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.7.1.3-alt1.qa2
- NMU (by repocop): the following fixes applied:
  * freedesktop-desktop-file-proposed-patch for qtm

* Sun Nov 08 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.7.1.3-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for qtm
  * postclean-05-filetriggers for spec file

* Thu Jan 15 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.7.1.3-alt1
- 0.7.1.3
- remove obsolete macros

* Sat Nov 01 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.7-alt1
- 0.7

* Sun Jun 15 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Thu May 01 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.0.1-alt1
- 0.6.0.1

* Sun Mar 23 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.5.8.2-alt1
- initial build
