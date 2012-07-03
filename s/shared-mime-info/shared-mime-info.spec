%def_enable updatedb

Name: shared-mime-info
Version: 0.91
Release: alt1

Summary: Shared MIME-Info Specification
Group: System/Libraries
License: %gpl2plus
Url: http://www.freedesktop.org/wiki/Software/%name

Source: http://www.freedesktop.org/~hadess/%name-%version.tar.xz
Source2: %name.filetrigger
Patch: %name-0.19-alt-cachedir-param.patch

Requires: rpm-build-xdg

BuildPreReq: rpm-build-licenses rpm-build-xdg
BuildPreReq: intltool xml-utils
# for build test programs
BuildPreReq: libgio-devel

# Automatically added by buildreq on Sun Jun 08 2008
BuildRequires: glib2-devel libxml2-devel perl-XML-Parser xml-utils

%description
This is the freedesktop.org shared MIME info database.

Many programs and desktops use the MIME system to represent the types of
files. Frequently, it is necessary to work out the correct MIME type for
a file. This is generally done by examining the file's name or contents,
and looking up the correct MIME type in a database.

For interoperability, it is useful for different programs to use the
same database so that different programs agree on the type of a file,
and new rules for determining the type apply to all programs.

This specification attempts to unify the type-guessing systems currently
in use by GNOME, KDE and ROX. Only the name-to-type and contents-to-type
mappings are covered by this spec; other MIME type information, such as
the default handler for a particular type, or the icon to use to display
it in a file manager, are not covered since these are a matter of style.

In addition, freedesktop.org provides a shared database in this format
to avoid inconsistencies between desktops. This database has been
created by converting the existing KDE and GNOME databases to the new
format and merging them together.

%prep
%setup -q
%patch

rm -f freedesktop.org.xml

%build
%configure %{?_disable_updatedb:--disable-update-mimedb}
# SMP-incompatible build
%make

%install
%makeinstall

cat <<__SH__ >%name.sh
export XDG_DATA_DIRS="\${XDG_DATA_DIRS-%_datadir}"
__SH__

cat <<__CSH__ >%name.csh
setenv XDG_DATA_DIRS "%_datadir"
__CSH__

install -pD -m755 %name.sh %buildroot%_sysconfdir/profile.d/%name.sh
install -pD -m755 %name.csh %buildroot%_sysconfdir/profile.d/%name.csh

# posttrans filetrigger
install -pD -m 755 %SOURCE2 %buildroot%_rpmlibdir/mime-database.filetrigger

# do empty db files and create file list
find %buildroot%_xdgmimedir -type f |fgrep -v "/packages/" > db.files
cat db.files| while read f; do echo -n > $f; done
find %buildroot%_xdgmimedir -mindepth 1 -type d |sed -e "s,^,%%dir ," >> db.files
subst 's,%buildroot,,' db.files

%triggerpostun -- %name < 0.13-alt2
rm -rf %_xdgmimedir/{application,audio,globs,image,inode,magic,message,model,\
multipart,text,video,XMLnamespaces}

%files -f db.files
%_bindir/update-mime-database
%_xdgmimedir/packages/freedesktop.org.xml
%_man1dir/*
%_datadir/pkgconfig/*

%exclude  %config(noreplace) %_sysconfdir/profile.d/*

# filetrigger
%_rpmlibdir/mime-database.filetrigger
%doc README shared-mime-info-spec.xml

%exclude %_datadir/locale

%changelog
* Fri Sep 30 2011 Yuri N. Sedunov <aris@altlinux.org> 0.91-alt1
- 0.91

* Thu Sep 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0.90-alt3
- XDG_DATA_DIRS variable is not exported any more, finally fixed
  (ALT #26194).

* Tue Aug 30 2011 Yuri N. Sedunov <aris@altlinux.org> 0.90-alt2
- %%_cachedir no more a part of XDG_DATA_DIRS variable (ALT #26194)

* Sat Dec 11 2010 Yuri N. Sedunov <aris@altlinux.org> 0.90-alt1
- 0.90

* Tue Nov 02 2010 Yuri N. Sedunov <aris@altlinux.org> 0.80-alt1
- 0.80

* Tue Apr 27 2010 Yuri N. Sedunov <aris@altlinux.org> 0.71-alt2
- modified %%name.{sh,csh} so permited to redefine XDG_DATA_DIRS variable

* Wed Feb 10 2010 Yuri N. Sedunov <aris@altlinux.org> 0.71-alt1
- new version

* Wed Jan 20 2010 Yuri N. Sedunov <aris@altlinux.org> 0.70-alt2
- removed obsolete %%{update,clean}_mimedb macros

* Thu Oct 08 2009 Yuri N. Sedunov <aris@altlinux.org> 0.70-alt1
- 0.70

* Tue Jun 09 2009 Alexey Rusakov <ktirf@altlinux.org> 0.60-alt5
- added rpm-build-xdg to Requires to fix building packages that use
  %%_xdgmimedir macro

* Mon Jun 01 2009 Alexey Rusakov <ktirf@altlinux.org> 0.60-alt4
- use rpm-build-xdg
- no more need in rpm-build-spec2macro package

* Wed Apr 22 2009 Yuri N. Sedunov <aris@altlinux.org> 0.60-alt3
- packaged lost directories under /usr/share/mime

* Fri Apr 17 2009 Yuri N. Sedunov <aris@altlinux.org> 0.60-alt2
- empty mime-database files added to filelist

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 0.60-alt1
- 0.60
- removed upstreamed patch

* Sat Nov 15 2008 Yuri N. Sedunov <aris@altlinux.org> 0.51-alt3
- use %%_rpmlibdir instead %%_libdir/rpm

* Fri Nov 14 2008 Yuri N. Sedunov <aris@altlinux.org> 0.51-alt2
- use posttrans filetrigger instead of {update,clean}_mimedb macros

* Tue Nov 11 2008 Yuri N. Sedunov <aris@altlinux.org> 0.51-alt1
- 0.51

* Sun Jun 08 2008 Yuri N. Sedunov <aris@altlinux.org> 0.30-alt1
- 0.30
- remove freedesktop.org.xml from source - use intltool to generate it
- Updated JavaScript detection patch and applied to freedesktop.org.xml.in
- Updated buildreqs

* Wed Mar 05 2008 Alexey Rusakov <ktirf@altlinux.org> 0.23-alt1
- New version (0.23).
- Use rpm-build-spec2macro and rpm-build-licenses.
- Added a patch from Debian to fix JavaScript detection
  (fd.o Bug 11837).

* Tue Oct 16 2007 Alexey Rusakov <ktirf@altlinux.org> 0.22-alt1
- new version (0.22)
- remove %%__ macros usage

* Sun Sep 10 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.19-alt1
- Updated to 0.19
- Abolished the cache directory and the extra parameter patch to
  update-mime-database as not following the spec
- Patch0: allow the extra directory parameter, but ignore it

* Sat Apr 09 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.16-alt1
- 0.16
- updated russian translation.

* Mon Mar 21 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.15-alt3.7
- ready russian translation (latest fixes by avp@).

* Wed Mar 16 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.15-alt3.6
- russian translation updated by vyt@ and avp@.

* Wed Mar 09 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.15-alt3.5
- russian translation.

* Tue Dec 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.15-alt3
- fixed %%{update,clean}_mimedb.

* Mon Nov 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.15-alt2
- %%{update,clean}_mimedb macros.

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.15-alt1
- 0.15

* Fri Mar 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.14-alt1
- 0.14

* Thu Mar 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.13-alt2
- put database cache in /var/cache/mime.

* Thu Feb 26 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.13-alt1
- 0.13
- --disable-update-mime-database added to configure.

* Mon Dec 09 2002 AVL <avl@altlinux.ru> 0.9-alt
- initial rpm for sisyphus

* Thu Jul 25 2002 Götz Waschk <waschk@linux-mandrake.com> 0.8-1mdk
- license changed to GPL
- removed noarch
- 0.8

* Mon Jun  3 2002 Götz Waschk <waschk@linux-mandrake.com> 0.7-1mdk
- set license from free to Public Domain
- adapt for Mandrake

* Fri May 31 2002 José Romildo Malaquias <romildo@iceb.ufop.br> 1.3.1-1
- First spec file for rox.
