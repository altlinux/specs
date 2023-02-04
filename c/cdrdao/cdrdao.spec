%def_without scglib
%def_enable gcdmaster

Name: cdrdao
Version: 1.2.5
Release: alt1

Summary: Cdrdao - Write audio CD-Rs in disk-at-once mode
Group: Archiving/Cd burning
License: GPLv2
Url: http://cdrdao.sourceforge.net

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.bz2
Source1: %name.control
Requires(pre,postun): control

%define lame_ver 3.100

BuildRequires: gcc-c++ libacl-devel libao-devel liblame-devel >= %lame_ver
BuildRequires: libmad-devel libvorbis-devel
BuildRequires: libGConf-devel
%{?_enable_gcdmaster:BuildRequires: libgtkmm3-devel}

%description
Writes audio CD-Rs in disc-at-once (DAO) mode allowing
control over pre-gaps (length down to 0, nonzero audio data)
and sub-channel information like ISRC codes. All data that
is written to the disc must be specified with a text file.
Audio data may be in WAVE or raw format.

%package -n gcdmaster
Summary: Graphical front end to cdrdao for composing audio CDs
Group: Archiving/Cd burning
Requires: %name = %EVR

%description -n gcdmaster
gcdmaster allows the creation of toc-files for cdrdao and
can control the recording process. Its main application is
the composition of audio CDs from one or more audio files.
It supports PQ-channel editing, entry of meta data like
ISRC codes/CD-TEXT and non destructive cut of the audio data.

%prep
%setup
# AC_CHECK_INCLUDES_DEFAULT available in 2.70 as compatibility macro
sed -i 's|\(AC_\)CHECK_\(INCLUDES_DEFAULT\)|\1\2|' configure.ac

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure \
	--with-mp3-support \
	--with-ogg-support \
	%{?_disable_gcdmaster:--without-gcdmaster} \
	%{subst_with scglib}
%nil
%make_build

%install
%makeinstall_std

# control support
install -pD -m755 %SOURCE1 %buildroot%_controldir/%name
chmod 700 %buildroot%_bindir/%name

%pre
%pre_control %name

%post
%post_control %name

%files
%_bindir/%name
%_bindir/cue2toc
%_bindir/toc2cddb
%_bindir/toc2cue
%_bindir/toc2mp3
%_datadir/%name
%_man1dir/*
%{?_enable_gcdmaster:%exclude %_man1dir/gcdmaster*}
%config /etc/control.d/facilities/%name
%doc README CREDITS ChangeLog

%if_enabled gcdmaster
%files -n gcdmaster
%_bindir/gcdmaster
%_desktopdir/gcdmaster.desktop
%_datadir/glib-2.0/schemas/org.gnome.gcdmaster.gschema.xml
%_datadir/pixmaps/gcdmaster*.png
%_man1dir/gcdmaster*
%_datadir/application-registry/gcdmaster.applications
%_datadir/mime-info/gcdmaster.*
%_datadir/mime/packages/gcdmaster.xml
%_datadir/gcdmaster/glade/Preferences.glade
%_datadir/gcdmaster/glade/ProjectChooser.glade
%endif

%changelog
* Sat Feb 04 2023 Yuri N. Sedunov <aris@altlinux.org> 1.2.5-alt1
- 1.2.5 (GCDMaster ported to GTKMM 3)

* Tue May 22 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Mon Jan 16 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt4
- fc patches: cdrdao-1.2.3-narrowing.patch
              cdrdao-1.2.3-format_security.patch

* Wed Apr 13 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.2.3-alt3.qa1
- Rebuilt for gcc5 C++11 ABI.

* Tue Sep 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt3
- fixed build (patch from fedora)

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt2
- 1.2.3 release
- upstreamed patches removed

* Fri May 08 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1rc2
- updated to 1.2.3rc2
- removed upstreamed patches
- cdrdao-1.2.2-gcc44.patch from Fedora
- updated buildreqs

* Thu Oct 30 2008 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt4
- updated cdrdao-1.2.2-gcc43.patch

* Tue Oct 14 2008 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt3
- change license to GPLv2
- fedora patches (1,2,9,23,30)
- don't build gcdmaster
- use internal pccts and scglib
- updated buildreqs

* Fri Jul 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2.2-alt2
- Set default control to public (fixes #7481, #12272).

* Thu Nov 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.2.2-alt1
- 1.2.2 release.
- Removed patch2 (merged upstream).

* Mon May 15 2006 Anton Farygin <rider@altlinux.ru> 1.2.1-alt2
- fixed build by gcc-4.1

* Tue Jan 31 2006 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- new version
- updated buildrequires
- fixed build for x86_64

* Fri Jan 21 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.1.9-alt0.8
- patch for some gcc 3.4 fixes. (MDK).
- fix ambigous operator cast (P4 from fedora).

* Wed Jun 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.9-alt0.7
- new version.
- fix to build with new gtkmm2-2.4.1
- FIXME: Use "C" locale to temporaly fix #3906 with menu.

* Fri Feb 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.8-alt0.5
- new version.

* Tue May 20 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.7-alt0.6
- added control support

* Sat Oct 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.7-alt0.5
- 1.1.7 without gcdmaster (it requires old gnome).

* Thu Sep 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.6-alt0.5cvs20020925
- built lastest cvs snapshot with gcc-3.2
- updated buildrequires.

* Thu Jan 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.1.5-alt1
- First build for Sisyphus
