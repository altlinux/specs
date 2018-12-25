%define _unpackaged_files_terminate_build 1

Name:           kdiff3
Version:        1.7.90
Release:        alt1.gitd59b742
Summary:        Compare + merge 2 or 3 files or directories
 
License:        GPLv2
Group: 		Text tools
URL:            https://github.com/KDE/kdiff3
Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-kf5 
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  glib-devel
BuildRequires:  kf5-kio-devel 
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kparts-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kbookmarks-devel
BuildRequires:  rpm-macros-cmake 
BuildRequires:  cmake-modules
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-ktextwidgets-devel

%description
KDiff3 is a program that
- compares and merges two or three input files or directories,
- shows the differences line by line and character by character (!),
- provides an automatic merge-facility and
- an integrated editor for comfortable solving of merge-conflicts
- has support for KDE-KIO (ftp, sftp, http, fish, smb)
- and has an intuitive graphical user interface.

%prep
%setup -n %name-%version

%build
%K5build

%install
%K5install
%K5install_move data appdata

%find_lang %name --with-kde --all-name

%files -f %name.lang

%doc AUTHORS ChangeLog INSTALL NEWS README
%_K5bin/%name
%_K5plug/kf5/kfileitemaction/kdiff3fileitemaction.so
%_K5plug/kf5/parts/kdiff3part.so
%_K5data/appdata/org.kde.%name.appdata.xml
%_K5xdgapp/org.kde.%name.desktop
%_K5icon/hicolor/*/apps/*.png
%_K5icon/hicolor/scalable/apps/kdiff3.svgz
%_K5srv/kdiff3part.desktop
%_K5xmlgui/%name
%_K5xmlgui/kdiff3part/kdiff3_part.rc

%changelog
* Thu Dec 20 2018 Alexey Melyashinsky <bip@altlinux.org> 1.7.90-alt1.gitd59b742
- Update to upstream snapshot d59b742

* Tue Nov 12 2013 Alexey Morozov <morozov@altlinux.org> 0.9.97-alt1.git
- built new git snapshot (4d116d1cb7e5ca0ed69a4c8e272253198bfbbb91),
  post-0.9.97.
- build scheme changed to off-source build, patches are migrated
  to the source tree.
- Russian translation updated

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9.95-alt2.qa1
- NMU: rebuilt for debuginfo.

* Sun Nov 14 2010 Alexey Morozov <morozov@altlinux.org> 0.9.95-alt2
- added kdiff3-0.9.95-alt-docbook_version.patch (#2) to fix build
  process

* Thu Mar 11 2010 Alexey Morozov <morozov@altlinux.org> 0.9.95-alt1
- NMU: new vesion (0.9.95)
- added kdiff3-0.9.95-localization.patch (#0):
  * fixed minor translation issues
  * Russian translation updated
- kdiff3-0.9.95-alt1-cumulative.patch (#1):
  * fixed desktop files
  * use 'kdiff3' as KDiff3Part component name to properly specify resources
- added several patches from KDiff3 SF.net tracker and Ubuntu package
- cleaned up the spec file

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.92-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for kdiff3
  * postclean-05-filetriggers for spec file

* Sat Apr 21 2007 Ilya Mashkin <oddity at altlinux dot ru> 0.9.92-alt1
- new version 0.9.92

* Wed Dec 20 2006 Ilya Mashkin <oddity at altlinux dot ru> 0.9.91-alt1
- new version 0.9.91
- fix #9917

* Thu Jul 20 2006 Ilya Mashkin <oddity at altlinux dot ru> 0.9.90-alt1
- new version 0.9.90

* Thu Apr 13 2006 Ilya Mashkin <oddity at altlinux dot ru> 0.9.89-alt1
- new version 0.9.89

* Wed Mar 30 2005 Ilya Mashkin <oddity at altlinux dot ru> 0.9.88-alt1
- new version 0.9.88

* Wed Feb 02 2005 Ilya Mashkin <oddity at altlinux dot ru> 0.9.87-alt1
- new version, add unicode support

* Tue Jan 11 2005 Ilya Mashkin <oddity at altlinux dot ru> 0.9.86-alt1
- New Version 0.9.86
- spec cleanup

* Tue Jun 10 2004 Dmitriy Porollo <spider@altlinux.ru> 0.9.84-alt1
- 0.9.84-alt1 0.9.84 Release
