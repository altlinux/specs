Name: kdiff3
Version: 0.9.97
Release: alt1.git

Summary: Compares and merges 2 or 3 files or directories
License: GPL
Group: Text tools
Url: http://kdiff3.sourceforge.net
Packager: Ilya Mashkin <oddity at altlinux dot ru>

Source0: %name-%version.tar.gz
# Our patches
Patch0:  kdiff3-post-0.9.97.patch
Patch1:  kdiff3-%version-%release-alt.patch


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

%patch0 -p1
%patch1 -p1

%build
%K4cmake
%K4make

%install
%K4install

%K4find_lang --with-kde %name
%K4find_lang --with-kde --append --output %name.lang %{name}plugin
%K4find_lang --with-kde --append --output %name.lang %{name}fileitemactionplugin

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
%_K4apps/%name
%_K4apps/kdiff3part
%_K4lib/kdiff3*.so
%_K4xdg_apps/%name.desktop
%_K4srv/*.desktop

%_iconsdir/*/*/apps/%name.png

%changelog
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
