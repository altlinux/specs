%define origname xmms-defx

Name: xmms-eff-defx
Version: 0.9.9
Release: alt3

Epoch: 20071220

Summary: Multi effects plugin for XMMS
License: GPL
Group: Sound

Url: http://defx.sourceforge.net
Source: %origname-%version.tar.gz
Patch: xmms-defx-0.9.9-alt-makefile.patch
Packager: Michael Shigorin <mike@altlinux.ru>

Obsoletes: xmms-defx < 0.9.9
Provides: xmms-defx = %version

# Automatically added by buildreq on Thu Dec 20 2007
BuildRequires: libxmms-devel

# need new macros
BuildRequires: libxmms-devel >= 1.2.8-alt2

%set_verify_elf_method textrel=relaxed
%add_optflags %optflags_shared

%description
Multi Effects plugin for XMMS.  Use this plugin if you want to
add simple but cool effects to your favorite songs.

Current effects include: karaoke, panning, flanger, chorus,
phaser and reverberation.

%prep
%setup -q -n %origname-%version
%patch -p1

%build
%make CC="gcc %optflags"

%install
install -pD -m755 lib/libdefx.so %buildroot%xmms_effectdir/libdefx.so

%files
%doc doc/AUTHORS README
%xmms_effectdir/libdefx.so

%changelog
* Thu Dec 20 2007 Michael Shigorin <mike@altlinux.ru> 20071220:0.9.9-alt3
- fixed x86_64 build

* Thu Dec 20 2007 Michael Shigorin <mike@altlinux.org> 20071220:0.9.9-alt2
- added patch by icesik@ to fix up plugin linking (#11435)
- spec macro abuse cleanup

* Sun Jan 04 2004 Michael Shigorin <mike@altlinux.ru> 20040104:0.9.9-alt1
- updated for new plugin policy
- renamed to %name

* Thu Aug 21 2003 Michael Shigorin <mike@altlinux.ru> 0.9.9-alt1
- built for ALT Linux

* Sat Oct 19 2002 Franco Catrin <fcatrin@tuxpan.cl>
- Initial RPM release.

