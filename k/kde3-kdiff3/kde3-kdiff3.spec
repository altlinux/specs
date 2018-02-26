%define origname kdiff3

%define qtdir %_qt3dir
%define kdedir %_K3prefix

Name: kde3-kdiff3
Version: 0.9.92
Release: alt2

Summary: Tool for Comparison and Merge of Files and Directories.
License: GPL
Group: Development/KDE and QT
Url: http://kdiff3.sourceforge.net
Packager: Lenar Shakirov <snejok at altlinux dot org>

Source0: %origname-%version.tar
Patch0: %origname-desktopfile.patch
Patch1: tde-3.5.13-build-defdir-autotool.patch
Patch2: cvs-auto_version_check.patch
BuildRequires: gcc-c++ kdelibs-devel

%description
Tool for Comparison and Merge of Files and Directories.
Shows the differences line by line and character by character,
provides an automatic merge-facility and an integrated editor
for comfortable solving of merge-conflicts.
Supports KIO on KDE (allows accessing ftp, sftp, fish, smb etc.),
and has an intuitive graphical user interface.

%prep
%setup -n %origname-%version
%patch0 -p2
%patch1
%patch2

%__subst 's/\(-Wl,--no-undefined\)/-Wl,--warn-unresolved-symbols \1/g' admin/acinclude.m4.in

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
make -f admin/Makefile.common

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%kdedir

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

%K3configure \
        --disable-rpath \
	--disable-debug \
	--disable-static \
	--enable-shared
%make

%install
%K3install
%K3find_lang --with-kde %origname

%files -f %origname.lang
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%_K3bindir/%origname
%_K3xdg_apps/%origname.desktop
%_K3apps/%origname/
%_K3srv/kdiff3part.desktop
%_datadir/man/man1/kdiff3.1.gz
%_K3lib/libkdiff3part.so
%_K3apps/kdiff3part/kdiff3_part.rc
%_K3doc/%origname/README
%_kde3_iconsdir/*/*/apps/%origname.png

%changelog
* Thu May 31 2012 Lenar Shakirov <snejok@altlinux.ru> 0.9.92-alt2
- Build from TDE 3.5.13 release

* Thu Apr 05 2012 Lenar Shakirov <snejok@altlinux.ru> 0.9.92-alt1
- rename to kde3-kdiff3 due original kdiff3 build for kde4
- spec cleaned and make it build for TDE 3.5.13
- build without arts
- BuildReqs cleaned

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
