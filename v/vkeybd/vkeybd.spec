%def_with lash

Name: vkeybd
Version: 0.1.18c
Release: alt1
Epoch: 1

Summary: Virtual keyboard for MIDI and ALSA drivers
Summary(ru_RU.UTF-8): Эмулятор MIDI-клавиатуры для MIDI- и ALSA-драйверов
Group: Sound
License: GPLv2+
Url: http://www.alsa-project.org/~iwai/alsa.html
Packager: Alexander Myltsev <avm@altlinux.ru>

Source: ftp://ftp.suse.com/pub/people/tiwai/vkeybd/%name-%version.tar.gz
Source1: %name.png

%define tcl_ver 8.5.1-alt1
%define tk_ver 8.5.1-alt1

Requires: tcl >= %tcl_ver, tk >= %tk_ver

%if_with lash
BuildPreReq: liblash-devel
%endif

BuildPreReq: tcl-devel >= %tcl_ver
BuildPreReq: tk-devel >= %tk_ver

# Automatically added by buildreq on Fri Feb 16 2007
BuildRequires: tk-devel

%description
This is a virtual keyboard for MIDI and ALSA drivers.
It's a simple fake of a MIDI keyboard on X-windows system.
Enjoy a music with your mouse and "computer" keyboard :-)

This program supports:
  - ALSA sequencer
  - MIDI device on OSS and ALSA
  - LASH session management

%description -l ru_RU.UTF-8
Vkeybd — это виртуальная клавиатура для MIDI- и ALSA-драйверов.
Она эмулирует функциональность обычной MIDI-клавиатуры, позволяя
отправлять MIDI-события с клавиатуры или мыши.

%prep
%setup -q -n %name

%build
%add_optflags -DUSE_NON_CONST
%make PREFIX=%prefix TCLLIB=-ltcl TKLIB=-ltk USE_AWE=0 \
    COPTFLAGS="$RPM_OPT_FLAGS" \
%if_with lash
    USE_LASH=1
%endif

%install
%make_install PREFIX=%buildroot%prefix \
	      MAN_DIR=%buildroot%_mandir \
	      USE_AWE=0 \
	      install-all

%files
%_bindir/%name
%_bindir/sftovkb
%_man1dir/%name.1*
%_datadir/applications/*
%_datadir/%name
%_datadir/pixmaps/*
%doc README

%changelog
* Tue Aug 25 2009 Alexander Myltsev <avm@altlinux.ru> 1:0.1.18c-alt1
- New version.
- Move from LADCCA to LASH.

* Sat Dec 27 2008 Alexander Myltsev <avm@altlinux.ru> 1:0.1.17a-alt3
- Fix placement of vkeybd.1 and a couple of repocop warnings.

* Wed Jun 18 2008 Alexander Myltsev <avm@altlinux.ru> 1:0.1.17a-alt2
- Rebuild with fresh Tcl/Tk (closes #15601).
- Disable AWE support (thanks lav@).
- Add additional categories to the desktop entry.

* Fri Feb 16 2007 Alex V. Myltsev <avm@altlinux.ru> 1:0.1.17a-alt1
- New version (added French keyboard layout)
- Fixed build, removed menu file.

* Sat Sep 25 2004 Yuri N. Sedunov <aris@altlinux.ru> 1:0.1.17-alt1
- 0.1.17
- .desktop, menu files (thaqnks Suse for vkeybd.png)

* Wed Jan 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 1:0.1.15-alt1
- 0.1.15
- ladcca support enabled, required libladcca >= 0.4.0

* Sat Nov 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 1:0.1.14-alt1
- 0.1.14
- disable ladcca support, not ready for 0.4 yet.

* Tue Jul 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 1:0.1.13a-alt1
- 0.1.13a
- ladcca support enabled.
- summary, description by avp.

* Sun Dec 29 2002 Yuri N. Sedunov <aris@altlinux.ru> 1:0.1.12-alt1
- new version.

* Wed Dec 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.1.11-alt1
- new version. 

* Mon Oct  7 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.1.11a-alt3
- rebuilt with tcl 8.4

* Mon Jun 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.1.11a-alt2
- rebuilt with new tcl/tk environment.

* Fri May 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.1.11a-alt1
- First build for Sisyphus.
