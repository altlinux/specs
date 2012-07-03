%def_without scglib
%def_disable xdao

%define cvsdate 20020925
%undefine cvsdate
%define rc_ver %nil

Name: cdrdao
Version: 1.2.3
%define release alt2%rc_ver

%ifdef cvsdate
Release: %{release}cvs%cvsdate
%else
Release: %release
%endif

Summary: Cdrdao - Write audio CD-Rs in disk-at-once mode
Group: Archiving/Cd burning
License: GPLv2
Url: http://cdrdao.sourceforge.net

%ifndef cvsdate
#Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.bz2
Source: %name-%version%rc_ver.tar.bz2
%else
Source: %name-%version-%cvsdate.tar.bz2
%endif

Source1: %name.control
Patch: %name-1.1.9-alt-locale.patch
# from Fedora
Patch2:    cdrdao-1.2.2-desktop.patch
Patch3:    cdrdao-1.2.3-version.patch

PreReq: control

# Added by buildreq2 on Wed Feb 01 2006
#BuildRequires: gcc-c++ gnome-libs-devel libacl-devel libao-devel libgnome-vfsmm-devel libgnomemm-devel libgnomeui-devel libgnomeuimm-devel liblame-devel libmad-devel libpopt-devel libvorbis-devel pccts-devel

BuildRequires: gcc-c++ libacl-devel libao-devel liblame-devel libmad-devel libvorbis-devel
BuildRequires: libGConf-devel

%description
Writes audio CD-Rs in disc-at-once (DAO) mode allowing
control over pre-gaps (length down to 0, nonzero audio data)
and sub-channel information like ISRC codes. All data that
is written to the disc must be specified with a text file.
Audio data may be in WAVE or raw format.

%package -n gcdmaster
Summary: Graphical front end to cdrdao for composing audio CDs
Group: Archiving/Cd burning
Requires: %name = %version-%release

%description -n gcdmaster
gcdmaster allows the creation of toc-files for cdrdao and
can control the recording process. Its main application is
the composition of audio CDs from one or more audio files.
It supports PQ-channel editing, entry of meta data like
ISRC codes/CD-TEXT and non destructive cut of the audio data.

%prep

%ifndef cvsdate
#%setup -q -n %name-%version
%setup -q -n %name-%version%rc_ver
%else
%setup -q -n %name-%version-%cvsdate
%endif
#%%patch -p1
%patch2 -p1 -b .desktop
%patch3 -p1 -b .version

subst 's,<linux/../scsi/scsi.h>,<scsi/scsi.h>,' dao/sg_err.h

%build
%ifdef cvsdate
find -type d -name CVS -print0 | xargs -r0 %__rm -rf --
%define __autoconf autoconf_2.5
%__subst 's@autoconf@%__autoconf@' autogen.sh
./autogen.sh
%endif

%autoreconf

%configure \
	--with-mp3-support \
	--with-ogg-support \
	%{?_disable_xdao:--without-xdao} \
	%{subst_with scglib}

%make_build

%install
%makeinstall

# control support
install -pD -m755 %SOURCE1 %buildroot%_controldir/%name
chmod 700 %buildroot%_bindir/%name

%pre
%pre_control %name

%post
%post_control %name

%files
%_bindir/*
%_datadir/%name
%_man1dir/*
%config /etc/control.d/facilities/%name
%doc README CREDITS ChangeLog NEWS

%if_enabled xdao
%exclude %_bindir/gcdmaster
%exclude %_man1dir/gcdmaster*

%files -n gcdmaster
%_bindir/gcdmaster
%_datadir/applications/*
%_datadir/pixmaps/*
%_man1dir/gcdmaster*
%_menudir/gcdmaster
%endif

%changelog
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
