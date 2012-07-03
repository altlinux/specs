%define plymouthdaemon_execdir /sbin
%define plymouthclient_execdir /bin
%define plymouth_libdir /%_lib
%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

%def_disable gdm

Summary: Graphical Boot Animation and Logger
Name: plymouth
Version: 0.8.3
Release: alt19.git20110406
License: GPLv2+
Group: System/Base

Url: http://freedesktop.org/software/plymouth/releases

Source: %name-%version.tar

Patch: %name-%version-%release.patch

Requires(post): plymouth-scripts

BuildRequires: libdrm-devel
Conflicts: bootsplash


%description
Plymouth provides an attractive graphical boot animation in
place of the text messages that normally get shown.  Text
messages are instead redirected to a log file for viewing
after boot.

%package system-theme
Summary: Plymouth default theme
Group: System/Base
Provides: %name-system-plugin = %version-%release
Requires: plymouth(system-theme)
Requires: %name = %version-%release

%description system-theme
This metapackage tracks the current distribution default theme.

%package -n lib%name
Summary: Plymouth core libraries
Group: System/Libraries

%description -n lib%name
This package contains the libply and libply-splash-core libraries
used by Plymouth.

%package -n lib%name-graphics
Summary: Plymouth graphics libraries
Group: System/Libraries
Requires: lib%name = %version-%release
BuildRequires: libpng-devel

%description -n lib%name-graphics
This package contains the libply-splash-graphics library
used by graphical Plymouth splashes.

%package devel
Summary: Libraries and headers for writing Plymouth splash plugins
Group: System/Libraries
Requires: %name = %version-%release
Requires: lib%name-graphics = %version-%release
Requires: lib%name = %version-%release

%description devel
This package contains the libply and libplybootsplash libraries
and headers needed to develop 3rd party splash plugins for Plymouth.

%package utils
Summary: Plymouth related utilities
Group: System/Base
Requires: %name = %version-%release
BuildRequires: libgtk+2-devel

%description utils
This package contains utilities that integrate with Plymouth
including a boot log viewing application.

%package scripts
Summary: Plymouth related scripts
Group: System/Base
# Requires: make-initrd > 0.3.9-alt1
Requires: %name = %version-%release

%description scripts
This package contains scripts that help integrate Plymouth with
the system.

%package gdm-hooks
Summary: Plymouth GDM integration
Group: System/Base
Requires: gdm >= 2.22.0
Requires: plymouth-utils
Requires: %name = %version-%release

%description gdm-hooks
This package contains support files for integrating Plymouth with GDM
Namely, it adds hooks to show boot messages at the login screen in the
event start-up services fail.

%package plugin-label
Summary: Plymouth label plugin
Group: System/Base
Requires: lib%name = %version-%release
BuildRequires: libpango-devel >= 1.21.0
BuildRequires: libcairo-devel

%description plugin-label
This package contains the label control plugin for
Plymouth. It provides the ability to render text on
graphical boot splashes using pango and cairo.

%package plugin-fade-throbber
Summary: Plymouth "Fade-Throbber" plugin
Group: System/Base
Requires: lib%name = %version-%release

%description plugin-fade-throbber
This package contains the "Fade-In" boot splash plugin for
Plymouth. It features a centered image that fades in and out
while other images pulsate around during system boot up.

%package theme-fade-in
Summary: Plymouth "Fade-In" theme
Group: System/Base
Requires: %name-plugin-fade-throbber = %version-%release
Requires(post): %name-scripts = %version-%release
Provides: plymouth(system-theme) = %version-%release

%description theme-fade-in
This package contains the "Fade-In" boot splash theme for
Plymouth. It features a centered logo that fades in and out
while stars twinkle around the logo during system boot up.

%package plugin-throbgress
Summary: Plymouth "Throbgress" plugin
Group: System/Base
Requires: lib%name = %version-%release
Requires: plymouth-plugin-label

%description plugin-throbgress
This package contains the "throbgress" boot splash plugin for
Plymouth. It features a centered logo and animated spinner that
spins repeatedly while a progress bar advances at the bottom of
the screen.

%package theme-spinfinity
Summary: Plymouth "Spinfinity" theme
Group: System/Base
Requires: %name-plugin-throbgress = %version-%release
Requires(post): %name-scripts = %version-%release

%description theme-spinfinity
This package contains the "Spinfinity" boot splash theme for
Plymouth. It features a centered logo and animated spinner that
spins in the shape of an infinity sign.

%package plugin-space-flares
Summary: Plymouth "space-flares" plugin
Group: System/Base
Requires: lib%name = %version-%release
Requires: plymouth-plugin-label

%description plugin-space-flares
This package contains the "space-flares" boot splash plugin for
Plymouth. It features a corner image with animated flares.

%package theme-solar
Summary: Plymouth "Solar" theme
Group: System/Base
Requires: %name-plugin-space-flares = %version-%release
Requires(post): %name-scripts = %version-%release
Requires: plymouth-system-theme

%description theme-solar
This package contains the "Solar" boot splash theme for
Plymouth. It features a blue flamed sun with animated solar flares.

%package plugin-two-step
Summary: Plymouth "two-step" plugin
Group: System/Base
Requires: lib%name = %version-%release
Requires: plymouth-plugin-label

%description plugin-two-step
This package contains the "two-step" boot splash plugin for
Plymouth. It features a two phased boot process that starts with
a progressing animation synced to boot time and finishes with a
short, fast one-shot animation.

%package theme-charge
Summary: Plymouth "Charge" plugin
Group: System/Base
Requires: %name-plugin-two-step = %version-%release
Requires(post): %name-scripts = %version-%release

%description theme-charge
This package contains the "charge" boot splash theme for
Plymouth. It features the shadowy hull of a Fedora logo charge up and
and finally burst into full form.

%package theme-glow
Summary: Plymouth "Glow" plugin
Group: System/Base
Requires: %name-plugin-two-step = %version-%release
Requires(post): %name-scripts = %version-%release

%description theme-glow
This package contains the "Glow" boot splash theme for Plymouth.

%package plugin-script
Summary: Plymouth "script" plugin
Group: System/Base
Requires: lib%name = %version-%release

%description plugin-script
This package contains the "script" boot splash plugin for
Plymouth. It features an extensible, scriptable boot splash
language that simplifies the process of designing custom
boot splash themes.

%package theme-script
Summary: Plymouth "Script" plugin
Group: System/Base
Requires: %name-plugin-script = %version-%release
Requires(post): %name-scripts = %version-%release

%description theme-script
This package contains the "script" boot splash theme for
Plymouth. It it is a simple example theme the uses the "script"
plugin.

%prep
%setup -q
%patch -p1

# Change the default theme
# %__subst 's/fade-in/charge/g' src/plymouthd.defaults

%build
%autoreconf
%configure \
	--enable-tracing				\
	--disable-libkms				\
	--disable-tests					\
	--without-default-plugin			\
	--with-logo=%_pixmapsdir/altlinux.png		\
	--with-background-start-color-stop=0x0073B3	\
	--with-background-end-color-stop=0x00457E	\
	--with-background-color=0x3391cd		\
%if_enabled gdm
	--enable-gdm-transition				\
	--with-gdm-autostart-file			\
%else
	--disable-gdm-transition			\
	--without-gdm-autostart-file			\
%endif
	--without-rhgb-compat-link			\
	--with-system-root-install			\
	--with-log-viewer				\
	--with-release-file=/etc/altlinux-release

#	--with-boot-tty=tty7				\
#	--with-shutdown-tty=tty1			\


%make

%install
%makeinstall_std

# Glow isn't quite ready for primetime
rm -rf %buildroot%_datadir/plymouth/glow/
rm -f %buildroot%_libdir/plymouth/glow.so

find %buildroot -name '*.a' -exec rm -f {} \;
find %buildroot -name '*.la' -exec rm -f {} \;

# Temporary symlink until rc.sysinit is fixed
(cd %buildroot%_bindir; ln -s ../../bin/plymouth)

mkdir -p %buildroot%_localstatedir/lib/plymouth
cp boot-duration %buildroot%_datadir/plymouth/default-boot-duration
touch %buildroot%_localstatedir/lib/plymouth/{boot,shutdown}-duration
cp shutdown-duration %buildroot%_datadir/plymouth/default-shutdown-duration
cp install-duration %buildroot%_datadir/plymouth/default-install-duration
touch %buildroot%_localstatedir/lib/plymouth/{boot,shutdown}-duration

# Add charge, our new default
mkdir -p %buildroot%_datadir/plymouth/themes/charge
cp charge.plymouth %buildroot%_datadir/plymouth/themes/charge
cp %buildroot%_datadir/plymouth/themes/glow/{box,bullet,entry,lock}.png %buildroot%_datadir/plymouth/themes/charge

# add startup integration
mkdir -p %buildroot/%_sysconfdir/sysconfig
install -m 0640 sysconfig %buildroot/%_sysconfdir/sysconfig/bootsplash
install plymouth-update %buildroot/%plymouthdaemon_execdir/
mkdir -p %buildroot/%_initdir/init.d/
install init %buildroot/%_initdir/plymouth

%post
if [ $1 = 1 ]; then
         /sbin/chkconfig --add %name
fi
[ -f %_localstatedir/lib/plymouth/boot-duration ] || cp -f %_datadir/plymouth/default-boot-duration %_localstatedir/lib/plymouth/boot-duration
[ -f %_localstatedir/lib/plymouth/shutdown-duration ] || cp -f %_datadir/plymouth/default-shutdown-duration %_localstatedir/lib/plymouth/shutdown-duration


%define theme_scripts() \
%post -n %name-theme-%{1} \
if [ -x %_sbindir/plymouth-set-default-theme ]; then \
  export LIB=%_lib \
  if [ $1 -eq 1 ]; then \
      %{_sbindir}/plymouth-set-default-theme %{1} \
  else \
      THEME=$(%_sbindir/plymouth-set-default-theme) \
      if [ "$THEME" == "text" -o "$THEME" == "%{1}" ]; then \
          %_sbindir/plymouth-set-default-theme %{1} \
      fi \
  fi \
fi \
\
%postun -n %name-theme-%{1} \
export LIB=%_lib \
if [ $1 -eq 0 -a -x %_sbindir/plymouth-set-default-theme ]; then \
    if [ "$(%_sbindir/plymouth-set-default-theme)" == "%{1}" ]; then \
        %_sbindir/plymouth-set-default-theme --reset \
    fi \
fi \

%theme_scripts spinfinity
%theme_scripts fade-in
%theme_scripts solar
%theme_scripts charge
%theme_scripts glow
%theme_scripts script


%files
%doc AUTHORS NEWS README
%dir %_datadir/plymouth
%dir %_datadir/plymouth/themes
%dir %_libdir/plymouth/renderers
%dir %_libexecdir/plymouth
%dir %_localstatedir/lib/plymouth
%config(noreplace) %_sysconfdir/plymouth/plymouthd.conf
%config %_sysconfdir/sysconfig/bootsplash
%_initdir/plymouth
%plymouthdaemon_execdir/plymouthd
%plymouthdaemon_execdir/plymouth-update
%plymouthclient_execdir/plymouth
%_libdir/plymouth/details.so
%_libdir/plymouth/text.so
%_libdir/plymouth/renderers/drm*
%_libdir/plymouth/renderers/frame-buffer*
%_datadir/plymouth/default-boot-duration
%_datadir/plymouth/default-shutdown-duration
%_datadir/plymouth/default-install-duration
%dir %_datadir/plymouth/themes/details
%_datadir/plymouth/themes/details/details.plymouth
%dir %_datadir/plymouth/themes/text
%_datadir/plymouth/themes/text/text.plymouth
%_datadir/plymouth/plymouthd.defaults
%_localstatedir/run/plymouth
%_localstatedir/spool/plymouth
%_mandir/man?/*
%ghost %_localstatedir/lib/plymouth/boot-duration

%files devel
%plymouth_libdir/libply.so
%plymouth_libdir/libply-splash-core.so
%_libdir/libply-splash-graphics.so
%_libdir/libply-boot-client.so
%_pkgconfigdir/ply-splash-core.pc
%_pkgconfigdir/ply-splash-graphics.pc
%_pkgconfigdir/ply-boot-client.pc
%_libdir/plymouth/renderers/x11*
%_includedir/plymouth-1

%files -n lib%name
%plymouth_libdir/libply.so.*
%plymouth_libdir/libply-splash-core.so.*
%_libdir/libply-boot-client.so.*
%dir %_libdir/plymouth

%files -n lib%name-graphics
%_libdir/libply-splash-graphics.so.*

%files scripts
%_sbindir/plymouth-set-default-theme
%_libexecdir/plymouth/plymouth-update-initrd
# %_libexecdir/plymouth/plymouth-generate-initrd
# %_libexecdir/plymouth/plymouth-populate-initrd

%files utils
%_bindir/plymouth-log-viewer

%if_enabled gdm
%files gdm-hooks
%_datadir/gdm/autostart/LoginWindow/plymouth-log-viewer.desktop
%endif

%files plugin-label
%_libdir/plymouth/label.so

%files plugin-fade-throbber
%_libdir/plymouth/fade-throbber.so

%files plugin-throbgress
%_libdir/plymouth/throbgress.so

%files plugin-space-flares
%_libdir/plymouth/space-flares.so

%files plugin-two-step
%_libdir/plymouth/two-step.so

%files plugin-script
%_libdir/plymouth/script.so

%files theme-fade-in
%_datadir/plymouth/themes/fade-in

%files theme-spinfinity
%_datadir/plymouth/themes/spinfinity

%files theme-solar
%_datadir/plymouth/themes/solar

%files theme-charge
%_datadir/plymouth/themes/charge

%files theme-script
%_datadir/plymouth/themes/script

%files theme-glow
%_datadir/plymouth/themes/glow

%files system-theme

%changelog
* Wed Aug 24 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt19.git20110406
- changed 'unexpectedly disconnected' from error to trace (closes: 25817)

* Thu Jun 16 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt18.git20110406
- run setsysfont on all ttys

* Wed Jun 15 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt17.git20110406
- setsysfont after deactivating

* Wed Apr 06 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt16.git20110406
- update from git
- should be buildable on ARM

* Mon Jan 17 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt15.git20110117
- install-duration changes

* Mon Jan 17 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt14.git20110117
- update from git

* Fri Dec 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt13.git20101007
- use details.plymouth as fallback instead of text.plymouth

* Tue Dec 07 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt12.git20101007
- non-zero value for first install-duration entry

* Thu Dec 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt11.git20101007
- add "normal" entryes into install-duration for livecd

* Thu Dec 02 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt10.git20101007
- install-duration added

* Mon Nov 22 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt9.git20101007
- no initrd rebuild after install/uninstall themes
- minor spec cleanup

* Mon Nov 22 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt8.git20101007
- config file for make-initrd removed (initrd.mk.d have strange sematics)

* Fri Nov 19 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt7.git20101007
- config file for make-initrd added

* Tue Nov 16 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt6.git20101007
- fix console state after boot
- paths added to init script
- chkconfig --add added

* Mon Nov 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt5.git20101007
- init script fixed

* Mon Nov 15 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt4.git20101007
- init script for hiding splash at boot and and starting on shutdown

* Fri Nov 12 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt3.git20101007
- ALT Linux startup integration
- minor spec cleanup

* Wed Nov 10 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.3-alt2.git20101007
- set default device in framebuffer plugin to /dev/fb0

* Thu Oct 07 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.3-alt1.git20101007
- git snapshot  ace1c6675c3320e5e80d8da226df517fbcfc3c9a
- define _localstatedir as /var
- set fade-in as default theme
- add glow theme
- update files for themes
- update boot-duration

* Sat Sep 18 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.3-alt1.git20100918
- git snapshot 784fbcfb096d756a63cd42a1efad1413c1ed8903
- do not package plymouth-populate-initrd and plymouth-generate-initrd

* Sat Aug 21 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.3-alt1.git20100819
- git snapshot dff1924448a20fa68de575aecaf4679b2ca88381
- drop fedora specifics

* Tue May 04 2010 Alexandra Panyukova <mex3@altlinux.org> 0.8.2-alt1
- build for altlinux

* Mon Apr 19 2010 Ray Strode <rstrode@redhat.com> 0.8.2-2
- Lock tty into raw mode
  Resolves: #579686

* Tue Apr 13 2010 Ray Strode <rstrode@redhat.com> 0.8.2-1
- Update to 0.8.2

* Wed Mar 31 2010 Ray Strode <rstrode@redhat.com> 0.8.1-3
- Fix assertion failure.  May fix bug 578633
- Fix things up to work with new drm header file locations

* Thu Mar 25 2010 Ray Strode <rstrode@redhat.com> 0.8.1-2
- Add debug statements to help debug transition
  problem

* Wed Mar 24 2010 Ray Strode <rstrode@redhat.com> 0.8.1-1
- Update to 0.8.1

* Wed Mar 24 2010 Ray Strode <rstrode@redhat.com> 0.8.0-1
- Update to 0.8.0

* Fri Mar 05 2010 Ray Strode <rstrode@redhat.com> 0.8.0-0.20100305.2
- Fix plymouth-update-initrd to work with dracut

* Fri Mar 05 2010 Ray Strode <rstrode@redhat.com> 0.8.0-0.20100305.1
- More crash fixes when booting into runlevel 3

* Thu Feb 25 2010 Ray Strode <rstrode@redhat.com> 0.8.0-0.20100225.1
- Fix crash when booting into runlevel 3

* Thu Jan 14 2010 Ray Strode <rstrode@redhat.com> 0.8.0-0.20100114.2
- Don't link plymouthd against libpng either

* Thu Jan 14 2010 Ray Strode <rstrode@redhat.com> 0.8.0-0.20100114.1
- Make it possible to do a basic plymouth installations without
  libpng

* Thu Jan 07 2010 Ray Strode <rstrode@redhat.com> 0.8.0-0.2009129.2
- Drop nash dep

* Tue Dec 22 2009 Dave Airlie <airlied@redhat.com> 0.8.0-0.2009129.1
- rebuild for API bump in libdrm

* Wed Dec 09 2009 Ray Strode <rstrode@redhat.com> 0.8.0-0.2009129
- Update to latest snapshot

* Tue Sep 29 2009 Ray Strode <rstrode@redhat.com> 0.8.0-0.2009.10.05
- Add new x11-renderer plugin from Charlie Brej for debugging

* Tue Sep 29 2009 Ray Strode <rstrode@redhat.com> 0.8.0-0.2009.29.09
- Fix escape and ask-for-password

* Mon Sep 28 2009 Ray Strode <rstrode@redhat.com> 0.8.0-0.2009.28.09
- Add prerelease of 0.8.0 for multihead support

* Fri Sep 11 2009 Ray Strode <rstrode@redhat.com> 0.7.1-7
- Go back to blue charge background (bug 522460)

* Fri Sep 11 2009 Ray Strode <rstrode@redhat.com> 0.7.1-6
- Remove duplicate Provides: plymouth(system-theme)

* Thu Sep 10 2009 Ray Strode <rstrode@redhat.com> 0.7.1-5
- Fix set_verbose error reported by yaneti.

* Wed Sep  9 2009 Ray Strode <rstrode@redhat.com> 0.7.1-4
- Look for inst() in dracut as well as mkinitrd bash source file
- Drop plymouth initrd for now.

* Fri Aug 28 2009 Ray Strode <rstrode@redhat.com> 0.7.1-3
- Create plymouth supplementary initrd in post (bug 515589)

* Tue Aug 25 2009 Ray Strode <rstrode@redhat.com> 0.7.1-2
- Get plugin path from plymouth instead of trying
  to guess.  Should fix bug 502667

* Tue Aug 25 2009 Ray Strode <rstrode@redhat.com> 0.7.1-1
- Update to 0.7.1

* Mon Aug 24 2009 Adam Jackson <ajax@redhat.com> 0.7.0-2
- Set charge bgcolor to black. (#519052)

* Tue Aug 11 2009 Ray Strode <rstrode@redhat.com> 0.7.0-1
- Update to 0.7.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-0.2010.05.15.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 15 2009 Ray Strode <rstrode@redhat.com> 0.7.0-0.2009.05.15.1
- Fix spinfinity theme to point to the right image directory
  (bug 500994)

* Thu May 14 2009 Ray Strode <rstrode@redhat.com> 0.7.0-0.2009.05.14.1
- Update to new snapshot that renames plugins to fix upgrades
  somewhat (bug 499940)

* Fri May 08 2009 Ray Strode <rstrode@redhat.com> 0.7.0-0.2009.05.08.1
- Add some fixes for shutdown

* Fri May 08 2009 Ray Strode <rstrode@redhat.com> 0.7.0-0.2009.05.06.4
- Don't slow down progress updating at the end of boot

* Thu May 07 2009 Ray Strode <rstrode@redhat.com> 0.7.0-0.2009.05.06.3
- Change colors to transition better to gdm

* Wed May 06 2009 Ray Strode <rstrode@redhat.com> 0.7.0-0.2009.05.06.2
- Make "charge" theme require two-step plugin instead of solar (oops)

* Wed May 06 2009 Ray Strode <rstrode@redhat.com> 0.7.0-0.2009.05.06.1
- Update to "plugin-rework" branch from git

* Wed Apr 08 2009 Jesse Keating <jkeating@redhat.com> - 0.7.0-0.2009.03.10.3
- Drop the version on system-logos requires for now, causing hell with
  other -logos providers not having the same version.

* Wed Mar 18 2009 Ray Strode <rstrode@redhat.com> 0.7.0-0.2009.03.10.2
- Destroy terminal on detach (may help with bug 490965)

* Tue Mar 10 2009 Ray Strode <rstrode@redhat.com> 0.7.0-0.2009.03.10.1
- Address one more issue with password handling.  It wasn't working
  well for secondary devices when using the "details" plugin.

* Mon Mar  9 2009 Ray Strode <rstrode@redhat.com> 0.7.0-0.2009.03.09.1
- Attempt to address some problems with password handling in the
  0.7.0 snapshots

* Fri Mar  6 2009 Ray Strode <rstrode@redhat.com> 0.7.0-0.2009.03.06.2
- Fix set default script

* Fri Mar  6 2009 Ray Strode <rstrode@redhat.com> 0.7.0-0.2009.03.06.1
- more scriptlet changes to move from solar to spinfinity

* Fri Mar  6 2009 Ray Strode <rstrode@redhat.com> 0.7.0-0.2009.03.06
- Updated to development snapshot
- Guess progress better on second boot of persistent live images
- Drop upstream patches
- swap "solar" and "spinfinity" scriptlet behavior

* Tue Feb 24 2009 Ray Strode <rstrode@redhat.com> 0.6.0-3
- Add fix-heap-corruptor patch from master.  Problem
  spotted by Mr. McCann.

* Wed Dec 17 2008 Ray Strode <rstrode@redhat.com> 0.6.0-2
- Add patch from drop-nash branch for jeremy

* Wed Dec  3 2008 Ray Strode <rstrode@redhat.com> 0.6.0-1
- Update to 0.6.0

* Sat Nov 22 2008 Matthias Clasen <mclasen@redhat.com> 0.6.0-0.2008.11.17.3.1
- Strip %%name from %%summary

* Mon Nov 17 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.17.3
- don't give error about missing default.so
- rework packaging of boot-duration to prevent .rpmnew droppings
  (bug 469752)

* Mon Nov 17 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.17.2
- Don't tell gdm to transition unless booting into runlevel 3
  (bug 471785)

* Mon Nov 17 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.17.1
- Crawl progress bar if boot is way off course (Charlie, bug 471089)

* Fri Nov 14 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.14.2
- Don't loop forever when tty returns NUL byte (bug 471498)

* Fri Nov 14 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.14.1
- Generate solar background dynamically to reduce ondisk size, and
  look better at various resolutions (Charlie, bug 471227)

* Thu Nov 13 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.12.4
- Move Obsoletes: plymouth-text-and-details-only to base package
  so people who had it installed don't end up solar on upgrade

* Wed Nov 12 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.12.3
- Redo packaging to work better with minimal installs
  (bug 471314)

* Wed Nov 12 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.12.2
- Fix plymouth-set-default-plugin to allow external $LIB

* Wed Nov 12 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.12.1
- Fix star image (Charlie, bug 471113)

* Tue Nov 11 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.11.2
- Improve solar flares (Charlie)
- redirect tty again on --show-splash
- ignore subsequent --hide-splash calls after the first one
- turn off kernel printks during boot up

* Tue Nov 11 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.11.1
- Disconnect from tty when init=/bin/bash (bug 471007)

* Mon Nov 10 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.10.5
- Force the right arch when calling plymouth-set-default-plugin
  (bug 470732)

* Mon Nov 10 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.10.4
- Drop comet (bug 468705)
- make boot-duration config(noreplace)

* Mon Nov 10 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.10.3
- Don't abort if no splash when root is mounted
- Actually move patches upstream

* Mon Nov 10 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.10.1
- Fix feedback loop with plymouth:debug
- Move patches upstream
- Improve comet animation

* Sun Nov  9 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.06.4
- Fix up more-debug patch to not assert with plymouth:nolog
  (bug 470569)

* Fri Nov  7 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.06.3
- add some more debug spew to help debug a problem jlaska is having

* Thu Nov  6 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.06.2
- show details plugin on --hide-splash so people can see why the splash
  got hidden.

* Thu Nov  6 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.06.1
- Don't exit on plymouth --show-splash after sulogin
- Properly retake console after that --show-splash

* Wed Nov  5 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.11.05.1
- reset colors on quit --retain-splash
- fix off by one in damage calculation for label

* Tue Nov  4 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.30.5
- Add a sample boot-duration for livecds and first time boots
  (bug 469752)

* Mon Nov  3 2008 Jeremy Katz <katzj@redhat.com> - 0.6.0-0.2008.10.30.4
- Allow pre-setting the default plugin when calling plymouth-populate-initrd

* Fri Oct 31 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.30.3
- Add pango minimum version to buildrequires

* Thu Oct 30 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.30.2
- Update prompt text colors to be legible on new artwork

* Thu Oct 30 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.30.1
- Drop upstreamed patches
- Patch from Charlie to update artwork
- Patch from Charlie to make password screen match animation better
  (bug 468899)

* Thu Oct 30 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.27.8
- Fix escape at password prompt (bug 467533)

* Tue Oct 28 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.27.7
- Don't require /bin/plymouth before it's installed (bug 468925)

* Tue Oct 28 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.27.6
- Force raw mode for keyboard input with solar and fade-in
  (bug 468880)
- make sure windows get closed on exit

* Mon Oct 27 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.27.5
- Make "Solar" lock icon the same as the "Spinfinity" one.

* Mon Oct 27 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.27.4
- Make plymouth-libs own %_libdir/plymouth (bug 458071)

* Mon Oct 27 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.27.3
- Default to "Solar" instead of "Spinfinity"

* Mon Oct 27 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.27.2
- Don't set plymouth default plugin to text in %%post

* Mon Oct 27 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.27.1
- Add Charlie patch to dither in lower color modes (bug 468276)

* Sun Oct 26 2008 Jeremy Katz <katzj@redhat.com> - 0.6.0-0.2008.10.24.2
- More requires changing to avoid loops (#467356)

* Fri Oct 24 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.24.1
- Add updated progress bar for solar plugin from Charlie
- Log plymouth:debug output to boot log
- Ignore sigpipe signals in daemon

* Thu Oct 23 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.23.2
- Bump so name of libply to hopefully force plymouth to get installed
  before kernel (or at least make plymouth-libs and plymouth get installed
  on the same side of kernel in the transaction).

* Thu Oct 23 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.23.1
- Add patch from Charlie to align progress bar to milestones during boot up
- force tty to be sane on exit (bug 467207)

* Thu Oct 23 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.21.3
- add empty files section for text-and-details-only so the subpackage
  shows up.

* Wed Oct 22 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.21.2
- add text-and-details-only subpackage so davej can uninstall
  spinfinity, pango, cairo etc from his router.

* Tue Oct 21 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.21.1
- Minor event loop changes
- drop upstream patches
- Charlie Brej fix for progress bar resetting when escape gets pressed

* Tue Oct 21 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.17.4
- Don't make plymouth-libs require plymouth (more fun with 467356)

* Mon Oct 20 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.17.3
- Add initscripts requires (bug 461322)

* Mon Oct 20 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.17.2
- Put tty1 back in "cooked" mode when going into runlevel 3
  (bug 467207)

* Fri Oct 17 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.17.1
- Clear screen in details plugin when it's done
- Make plymouth-update-initrd a small wrapper around mkinitrd instead
  of the broken monstrosity it was before.

* Fri Oct 17 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.15.3
- Move plymouth-set-default-plugin, plymouth-update-initrd, and
  plymouth-populate-initrd to plymouth-scripts subpackage
  (the last fix didn't actually help with bug 467356)

* Fri Oct 17 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.15.2
- Move plymouth-set-default-plugin to -libs (might help with bug 467356)
- Fix up requires, provides and postun scripts

* Wed Oct 15 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.15.1
- Don't free windows on --hide-splash (fix from Jeremy)

* Tue Oct 14 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.14.1
- Solar fixes from Charlie Brej
- Better cpu usage from Charlie

* Fri Oct 10 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.08.2
- Add Requires(post): nash (bug 466500)

* Wed Oct 08 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.08.1
- Rework how "console=" args done again, to hopefully fix
  bug 460565

* Mon Oct 06 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.10.06.1
- Add "Solar" plugin from Charles Brej
- Move things around so computers with separate /usr boot
  (hopefully this won't break things, but it probably will)
- Make GDM show up on vt1 for all plugins

* Tue Sep 30 2008 Jeremy Katz <katzj@redhat.com> 0.6.0-0.2008.09.25.2
- Remove mkinitrd requires to break the dep loop and ensure things
  get installed in the right order

* Thu Sep 25 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.09.25.1
- Add new snapshot to fold in Will Woods progress bar, and
  move ajax's splash upstream, putting the old text splash
  in a "pulser" subpackage

* Tue Sep 23 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.09.23.1
- Last snapshot was broken

* Mon Sep 22 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.09.22.1
- Update to latest snapshot to get better transition support

* Fri Sep 19 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.09.15.2
- Turn on gdm trigger for transition

* Mon Sep 15 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.09.15.1
- add quit command with --retain-splash option to client

* Wed Sep 10 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.09.10.1
- Fix text rendering for certain machines

* Mon Sep  8 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.09.05.4
- More serial console fixes (bug 460565 again)

* Fri Sep  5 2008 Bill Nottingham <notting@redhat.com> 0.6.0-0.2008.09.05.3
- make the text plugin use the system release info rather than a hardcoded 'Fedora 10'

* Fri Sep  5 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.09.05.2
- Try to support multiple serial consoles better
  (bug 460565)

* Fri Sep  5 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.09.05.1
- Fix some confusion with password handling in details plugin

* Wed Aug 27 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.08.27.1
- Fix another crasher for users with encrypted disks (this time in
  the text plugin, not the client)

* Wed Aug 27 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.08.27
- Update to latest snapshot
- Add the ability to show text prompts in graphical plugin
- Fix crasher for users with encrypted disks

* Fri Aug 23 2008 Ray Strode <rstrode@redhat.com> 0.6.0-0.2008.08.22
- Update to latest snapshot

* Wed Aug 13 2008 Ray Strode <rstrode@redhat.com> 0.5.0-20.2008.08.13
- Update previous patch to remove some assertions

* Wed Aug 13 2008 Ray Strode <rstrode@redhat.com> 0.5.0-19.2008.08.13
- add a patch that may help serial console users

* Wed Aug 13 2008 Ray Strode <rstrode@redhat.com> 0.5.0-18.2008.08.13
- add spool directory to file list

* Wed Aug 13 2008 Ray Strode <rstrode@redhat.com> 0.5.0-17.2008.08.13
- Make plymouth-gdm-hooks require plymouth-utils

* Wed Aug 13 2008 Ray Strode <rstrode@redhat.com> 0.5.0-16.2008.08.13
- Add a boot failure viewer to login screen (written by Matthias)

* Tue Aug 12 2008 Adam Jackson <ajax@redhat.com> 0.5.0-15.2008.08.08
- plymouth-0.5.0-textbar-hotness.patch: Change the text plugin to a slightly
  more traditional progress bar, to maintain the illusion of progress better
  than the eternally oscillating cylon. Note: still incomplete.

* Fri Aug  8 2008 Ray Strode <rstrode@redhat.com> - 0.5.0-14.2008.08.08
- Don't require a modifiable text color map (may fix serial consoles)

* Thu Aug  7 2008 Ray Strode <rstrode@redhat.com> - 0.5.0-13.2008.08.07
- Update to new snapshot which when combined with a new mkinitrd should
  make unlocking encrypted root partitions work again

* Wed Aug  6 2008 Ray Strode <rstrode@redhat.com> - 0.5.0-12.2008.08.06
- Update to new snapshot which fixes some assertion failures in the
  client code

* Wed Aug  6 2008 Ray Strode <rstrode@redhat.com> - 0.5.0-11.2008.08.01
- Add Requires(post): plymouth to plugins so they get plymouth-set-default-plugin (bug 458071)

* Tue Aug  5 2008 Ray Strode <rstrode@redhat.com> - 0.5.0-10.2008.08.01
- Add plymouth dirs to file list (bug 457871)

* Fri Aug  1 2008 Ray Strode <rstrode@redhat.com> - 0.5.0-9.2008.08.01
- new plymout-populate-initrd features don't work with the set -e at the
  top of it.

* Thu Jul 31 2008 Ray Strode <rstrode@redhat.com> - 0.5.0-8.2008.08.01
- Update to another snapshot to actually get new
  plymouth-populate-initrd features

* Thu Jul 31 2008 Ray Strode <rstrode@redhat.com> - 0.5.0-8.2008.07.31
- Update to snapshot to get new plymouth-populate-initrd features
- Make removing rhgb use details plugin instead of exiting

* Thu Jul 31 2008 Peter Jones <pjones@redhat.com> - 0.5.0-7
- Make it a mkinitrd requires instead of a nash requires (that will
  still pull in nash, but we need mkinitrd for newer plymouth-populate-initrd)

* Wed Jul 30 2008 Ray Strode <rstrode@redhat.com> - 0.5.0-6
- Add nash requires

* Wed Jul  9 2008 Ray Strode <rstrode@redhat.com> - 0.5.0-5
- Use a new heuristic for finding libdir, since the old
  one falls over on ia64

* Wed Jul  9 2008 Ray Strode <rstrode@redhat.com> - 0.5.0-4
- add ctrl-r to rotate text color palette back to stock values

* Tue Jul  8 2008 Ray Strode <rstrode@redhat.com> - 0.5.0-3
- Fix populate script on ppc (bug 454353)

* Tue Jul  1 2008 Ray Strode <rstrode@redhat.com> - 0.5.0-2
- Pull in spinfinity by default.  This whole "figure out
  which plugin to use" set of scripts and scriptlets
  needs work.  We need to separate distro default from
  user choice.

* Thu Jul  1 2008 Ray Strode <rstrode@redhat.com> - 0.5.0-1
- Add new client "ask-for-password" command which feeds
  the user input to a program instead of standard output,
  and loops when the program returns non-zero exit status.

* Thu Jun 26 2008 Ray Strode <rstrode@redhat.com> - 0.4.5-1
- Update to version 0.4.5
- Make text plugin blue and less 80s

* Wed Jun 25 2008 Ray Strode <rstrode@redhat.com> - 0.4.0-4
- Make "Password: " show up correctly in text plugin

* Wed Jun 25 2008 Ray Strode <rstrode@redhat.com> - 0.4.0-3
- Require elfutils (bug 452797)

* Sun Jun 22 2008 Ray Strode <rstrode@redhat.com> - 0.4.0-2
- Make plymouth-set-default-plugin --reset choose the latest
  installed plugin, not the earliest

* Sun Jun 22 2008 Ray Strode <rstrode@redhat.com> - 0.4.0-1
- Update to version 0.4.0
- Only run if rhgb is on kernel command line
- Make text plugin more animated

* Mon Jun 16 2008 Ray Strode <rstrode@redhat.com> - 0.3.2-2
- dont go back to text mode on exit

* Mon Jun 16 2008 Ray Strode <rstrode@redhat.com> - 0.3.2-1
- Update to version 0.3.2
- show gradient in spinfinity plugin
- Drop fade out in spinfinity plugin
- fix throbber placement
- rename graphical.so to default.so

* Thu Jun 12 2008 Ray Strode <rstrode@redhat.com> - 0.3.1-3
- scriplet should be preun, not postun

* Thu Jun 12 2008 Ray Strode <rstrode@redhat.com> - 0.3.1-2
- Fix postun scriptlet

* Thu Jun 12 2008 Ray Strode <rstrode@redhat.com> - 0.3.1-1
- Update to version 0.3.1
- Don't ship generated initrd scripts in tarball

* Thu Jun 12 2008 Ray Strode <rstrode@redhat.com> - 0.3.0-1
- Update to version 0.3.0
- Better plugin handling
- Better integration with mkinitrd (pending mkinitrd changes)
- random bug fixes

* Mon Jun  9 2008 Ray Strode <rstrode@redhat.com> - 0.2.0-1
- Update to version 0.2.0
- Integrate more tightly with nash (pending nash changes)
- ship libs for out of tree splash plugins
- gradient support
- random bug fixes

* Fri May 30 2008 Ray Strode <rstrode@redhat.com> - 0.1.0-1
- Initial import, version 0.1.0
