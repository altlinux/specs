Name: kdiff3
Version: 0.9.95
Release: alt2

Summary: Compares and merges 2 or 3 files or directories
License: GPL
Group: Text tools
Url: http://kdiff3.sourceforge.net
Packager: Ilya Mashkin <oddity at altlinux dot ru>

Source0: %name-%version.tar.gz
# Our patches
Patch0:  kdiff3-0.9.95-localization.patch
Patch1:  kdiff3-%version-%release-cumulative.patch
Patch2: kdiff3-0.9.95-alt-docbook_version.patch
# Patches from KDiff3 Tracker
Patch10: kdiff3-0.9.95_log10.diff
Patch11: kdiff3-0.9.95_mimatched_delete.diff
Patch12: kdiff3-0.9.95_avoid_equal_files_dialog.diff
Patch13: kdiff3-avoid-dirmerge-dialog.patch

# Patches from Ubuntu package
Patch20: create_qm_files.patch
Patch21: kdiff3.pro.patch


BuildRequires: gcc-c++ kde4base-workspace-devel kde4base-devel cmake cmake-modules

%description
KDiff3 is a program that
- compares and merges two or three input files or directories,
- shows the differences line by line and character by character (!),
- provides an automatic merge-facility and
  an integrated editor for comfortable solving of merge-conflicts
- has support for KDE-KIO (ftp, sftp, http, fish, smb...)
- and has an intuitive graphical user interface.

%prep
%setup -q

%patch0 -p2
%patch1 -p2
%patch2 -p1

%patch10 -p1
%patch11 -p0
%patch12 -p5
%patch13 -p1

%patch20 -p0
%patch21 -p1

%build
%K4cmake
%K4make

%install
%K4install

%K4find_lang --with-kde %name
%K4find_lang --with-kde --append --output %name.lang %{name}plugin

# Fix absolute links
pushd %buildroot
for l in .%_K4doc/*/%name/common; do
  t=$(readlink $l)
  # unfortunately ${var:pos} is a bash'ism
  r=$(relative $t $(echo $l | cut -c 2-))
  rm -f $l
  ln -s $r $l
done

%files -f %name.lang
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%_bindir/%name
%_K4lib/libkdiff3*.so
%_K4apps/%name
%_K4xdg_apps/%name.desktop
%_K4srv/*.desktop

%_iconsdir/*/*/apps/%name.png

%changelog
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
