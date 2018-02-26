Packager:	Alex Negulescu <alecs@altlinux.org>
Summary:	Advanced Linux Sound Architecture (ALSA) graphical mixer
Name:		alsamixergui
Version:	0.9.0
Release:	alt3
License:	GPL
Group:		Sound
URL:		http://www.iua.upf.es/~mdeboer/projects/alsamixergui/
Source0:	alsamixergui-0.9.0rc1-2.tar.bz2
Patch0:		alsamixergui-0.9.0rc1-fixes.patch
Patch1:		alsamixer-0.9.0rc1-2-fltk.patch
Patch2:		alsamixer-0.9.0rc1-2-fltk2.patch
Patch3:		alsamixergui-0.9.0rc1-memleak.patch
Patch4:		alsamisergui-fix-compile-gcc-3.4.patch
Patch5:		alsamixergui-0.9.0rc1-lock.patch
BuildRequires: gcc-c++ libX11-devel libalsa-devel libfltk-devel

%description
Alsamixergui is a FLTK based frontend for alsamixer. It is written
directly on top of the alsamixer source, leaving the original source
intact, only adding a couple of ifdefs, and some calls to the gui
part, so it provides exactly the same functionality, but with a 
graphical userinterface.

%prep
%setup -q -n %name-%{version}rc1-2
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1 -b .fix_gcc_3.4
%patch5 -p0

%build
autoconf
%configure
%make all

%install
rm -rf %buildroot
%makeinstall
# XDG menu
install -d %buildroot%_datadir/applnk/Multimedia
cat > %buildroot%_datadir/applnk/Multimedia/%name.desktop << EOF
[Desktop Entry]
Name=AlsaMixerGUI
Comment=%summary
Exec=%name
Icon=sound_section
Terminal=false
Type=Application
Categories=Audio;Mixer;
EOF

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc AUTHORS README
%_bindir/%name
%_datadir/applnk/Multimedia/%name.desktop

%changelog
* Sat Apr 21 2012 Alex Negulescu <alecs@altlinux.org> 0.9.0-alt3
- fixed build failure

* Fri Apr 15 2011 Alex Negulescu <alecs@altlinux.org> 0.9.0-alt2.1
- libfltk upped to 1.3.0.r8575

* Sun Feb 06 2011 Alex Negulescu <alecs@altlinux.org> 0.9.0-alt2
- updated spec to use libfltk13 and libfltk-devel
- fixed debuginfo build

* Sat Sep 05 2009 Alex Negulescu <alecs@altlinux.org> 0.9.0-alt1
- initial build for Sisyphus
- minor cleanup of spec

* Sun Dec 07 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9.0-0.14rc1_4mdv2009.1
+ Revision: 311681
- rebuild for new fltk

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.9.0-0.13rc1_4mdv2009.0
+ Revision: 218429
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Jan 16 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9.0-0.13rc1_4mdv2008.1
+ Revision: 153719
- remove useless kernel require
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 10 2007 Funda Wang <fundawang@mandriva.org> 0.9.0-0.12rc1_4mdv2008.1
+ Revision: 116837
- drop old menu

  + Thierry Vignaud <tvignaud@mandriva.com>
    - buildrequires X11-devel instead of XFree86-devel

* Wed May 23 2007 Christiaan Welvaart <spturtle@mandriva.org> 0.9.0-0.12rc1_3mdv2008.0
+ Revision: 30393
- sync with 0.9.0-0.12rc1_3mdv2007.1 src rpm
  o add xdg menu stuff


* Fri Sep 29 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-0.11rc1_3
- sync with mille-xterm

* Mon Dec 13 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.0-0.10rc1_3mdk
- rebuild
- spec cosmetics
- do parallell build

* Wed Jun 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.9.0-0.9rc1_3mdk
- Rebuild
