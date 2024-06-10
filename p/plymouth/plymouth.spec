%define _unpackaged_files_terminate_build 1
%define _allowed_nonstrict_interdeps plymouth-system-theme,plymouth-theme-fade-in
%add_findreq_skiplist %_unitdir/systemd-ask-password-plymouth.service
%add_findreq_skiplist %_datadir/plymouth/themes/spinfinity/header-image.png

%define plymouthdaemon_execdir /sbin
%define plymouthclient_execdir /bin
%define plymouth_libdir /%_libdir
%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

Name: plymouth
Version: 24.004.60
Release: alt5.20240608
Epoch: 1

Summary: Graphical Boot Animation and Logger
License: GPL-2.0-or-later
Group: System/Base

Url: http://www.freedesktop.org/wiki/Software/Plymouth

Source: %name-%version.tar

Patch: %name-%version-%release.patch

Requires(post): plymouth-scripts
Requires: lib%name = %EVR

BuildRequires: /proc
BuildRequires: meson
BuildRequires: pkgconfig(libevdev)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: pkgconfig(libpng) >= 1.2.16
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(pangocairo) >= 1.21.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires: pkgconfig(libdrm)
BuildRequires: xsltproc docbook-dtds docbook-style-xsl intltool

Conflicts: bootsplash
Conflicts: systemd < 186-alt1
Provides: %name-utils = %EVR
Obsoletes: %name-utils < %EVR

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
Requires: %name = %EVR
BuildArch: noarch

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
Requires: lib%name = %EVR

%description -n lib%name-graphics
This package contains the libply-splash-graphics library
used by graphical Plymouth splashes.

%package devel
Summary: Libraries and headers for writing Plymouth splash plugins
Group: System/Libraries
Requires: %name = %EVR
Requires: lib%name-graphics = %EVR
Requires: lib%name = %EVR

%description devel
This package contains the libply and libplybootsplash libraries
and headers needed to develop 3rd party splash plugins for Plymouth.

%package scripts
Summary: Plymouth related scripts
Group: System/Base
# Requires: make-initrd > 0.3.9-alt1
Requires: %name = %EVR

%description scripts
This package contains scripts that help integrate Plymouth with
the system.

%package plugin-label
Summary: Plymouth label plugin
Group: System/Base
Requires: lib%name = %EVR

%description plugin-label
This package contains the label control plugin for
Plymouth. It provides the ability to render text on
graphical boot splashes using pango and cairo.

%package plugin-fade-throbber
Summary: Plymouth "Fade-Throbber" plugin
Group: System/Base
Requires: lib%name = %EVR
Requires: lib%name-graphics = %EVR

%description plugin-fade-throbber
This package contains the "Fade-In" boot splash plugin for
Plymouth. It features a centered image that fades in and out
while other images pulsate around during system boot up.

%package theme-fade-in
Summary: Plymouth "Fade-In" theme
Group: System/Base
Requires: %name-plugin-fade-throbber = %EVR
Requires(post): %name-scripts = %version-%release
Provides: plymouth(system-theme) = %version-%release
BuildArch: noarch

%description theme-fade-in
This package contains the "Fade-In" boot splash theme for
Plymouth. It features a centered logo that fades in and out
while stars twinkle around the logo during system boot up.

%package theme-spinfinity
Summary: Plymouth "Spinfinity" theme
Group: System/Base
Requires: %name-plugin-two-step = %EVR
Requires(post): %name-scripts = %version-%release
BuildArch: noarch

%description theme-spinfinity
This package contains the "Spinfinity" boot splash theme for
Plymouth. It features a centered logo and animated spinner that
spins in the shape of an infinity sign.

%package plugin-space-flares
Summary: Plymouth "space-flares" plugin
Group: System/Base
Requires: lib%name = %EVR
Requires: lib%name-graphics = %EVR
Requires: plymouth-plugin-label = %EVR

%description plugin-space-flares
This package contains the "space-flares" boot splash plugin for
Plymouth. It features a corner image with animated flares.

%package theme-solar
Summary: Plymouth "Solar" theme
Group: System/Base
Requires: %name-plugin-space-flares = %EVR
Requires(post): %name-scripts = %version-%release
Requires: plymouth-system-theme
BuildArch: noarch

%description theme-solar
This package contains the "Solar" boot splash theme for
Plymouth. It features a blue flamed sun with animated solar flares.

%package plugin-two-step
Summary: Plymouth "two-step" plugin
Group: System/Base
Requires: lib%name = %EVR
Requires: lib%name-graphics = %EVR
Requires: plymouth-plugin-label = %EVR

%description plugin-two-step
This package contains the "two-step" boot splash plugin for
Plymouth. It features a two phased boot process that starts with
a progressing animation synced to boot time and finishes with a
short, fast one-shot animation.

%package theme-charge
Summary: Plymouth "Charge" plugin
Group: System/Base
Requires: %name-plugin-two-step = %EVR
Requires(post): %name-scripts = %version-%release
BuildArch: noarch

%description theme-charge
This package contains the "charge" boot splash theme for
Plymouth. It features the shadowy hull of a Fedora logo charge up and
and finally burst into full form.

%package theme-glow
Summary: Plymouth "Glow" plugin
Group: System/Base
Requires: %name-plugin-two-step = %EVR
Requires(post): %name-scripts = %version-%release
BuildArch: noarch

%description theme-glow
This package contains the "Glow" boot splash theme for Plymouth.

%package plugin-script
Summary: Plymouth "script" plugin
Group: System/Base
Requires: lib%name = %EVR
Requires: lib%name-graphics = %EVR

%description plugin-script
This package contains the "script" boot splash plugin for
Plymouth. It features an extensible, scriptable boot splash
language that simplifies the process of designing custom
boot splash themes.

%package theme-script
Summary: Plymouth "Script" plugin
Group: System/Base
Requires: %name-plugin-script = %EVR
Requires(post): %name-scripts = %version-%release
BuildArch: noarch

%description theme-script
This package contains the "script" boot splash theme for
Plymouth. It it is a simple example theme the uses the "script"
plugin.

%package theme-spinner
Summary: Plymouth "Spinner" theme
Group: System/Base
Requires: %name-plugin-two-step = %EVR
Requires(post): %name-scripts = %version-%release
BuildArch: noarch

%description theme-spinner
This package contains the "spinner" boot splash theme for
Plymouth. It features a small spinner on a dark background.

%package theme-bgrt
Summary: Plymouth "BGRT" theme
Group: System/Base
Requires: %name-plugin-two-step = %EVR
Requires(post): %name-scripts = %version-%release
BuildArch: noarch

%description theme-bgrt
This package contains the "bgrt" boot splash theme for
Plymouth.
Jimmac's spinner theme using the ACPI BGRT graphics as background.

%package theme-bgrt-alt
Summary: Plymouth "BGRT-ALT" theme
Group: System/Base
Requires: %name-plugin-two-step = %EVR
Requires(post): %name-scripts = %version-%release
BuildArch: noarch

%description theme-bgrt-alt
This package contains the "bgrt-alt" boot splash theme for
Plymouth.
It is a cusomized Jimmac's spinner theme using the ACPI BGRT graphics as
background and featuring ALT logo.

%prep
%setup -q
%patch -p1

# Change the default theme
# sed -i 's/fade-in/charge/g' src/plymouthd.defaults

%build
export SYSTEMD_ASK_PASSWORD_AGENT="systemd-tty-ask-password-agent"
export UDEVADM="/sbin/udevadm"
%meson \
	-Dtracing=true \
	-Dlogo=%_datadir/design/current/icons/system-logo.png \
	-Dbackground-start-color-stop=0x0073B3 \
	-Dbackground-end-color-stop=0x00457E \
	-Dbackground-color=0x3391cd \
	-Dsystemd-integration=true \
	-Dsystemd-system-unitdir=%_unitdir \
	-Dsystemd-ask-password-agent=systemd-tty-ask-password-agent \
	-Ddocs=true

%meson_build

%install
# workaround for create symlink with meson
mkdir -p %buildroot/%_datadir/design/current/icons
touch %buildroot/%_datadir/design/current/icons/system-logo.png

%meson_install

rm -r %buildroot/%_datadir/design

# Glow isn't quite ready for primetime
rm -rf %buildroot%_datadir/plymouth/glow/
rm -f %buildroot%_libdir/plymouth/glow.so

find %buildroot -name '*.a' -exec rm -f {} \;
find %buildroot -name '*.la' -exec rm -f {} \;

mkdir -p %buildroot%_localstatedir/lib/plymouth
cp boot-duration %buildroot%_datadir/plymouth/default-boot-duration
cp shutdown-duration %buildroot%_datadir/plymouth/default-shutdown-duration
cp install-duration %buildroot%_datadir/plymouth/default-install-duration
touch %buildroot%_localstatedir/lib/plymouth/{boot,shutdown}-duration

# Add charge, our new default
mkdir -p %buildroot%_datadir/plymouth/themes/charge
cp charge.plymouth %buildroot%_datadir/plymouth/themes/charge
cp %buildroot%_datadir/plymouth/themes/glow/{box,bullet,entry,lock}.png %buildroot%_datadir/plymouth/themes/charge

# don't put plymouth client and daemon in the prefix
mkdir -p %buildroot/sbin
mv %buildroot%_sbindir/plymouthd %buildroot/sbin/
mkdir -p %buildroot/bin
mv %buildroot%_bindir/plymouth %buildroot/bin/

# add startup integration
mkdir -p %buildroot%_sysconfdir/sysconfig
install -m 0640 sysconfig %buildroot%_sysconfdir/sysconfig/bootsplash
install plymouth-update %buildroot%plymouthdaemon_execdir/
mkdir -p %buildroot%_initdir
install init %buildroot%_initdir/plymouth
ln -s plymouth-quit.service %buildroot%_unitdir/plymouth.service

%find_lang %name

%post
if [ $1 = 1 ]; then
         /sbin/chkconfig --add %name
fi
if [ $1 = 2 ]; then
         /sbin/chkconfig %name resetpriorities
fi

[ -f %_localstatedir/lib/plymouth/boot-duration ] || cp -f %_datadir/plymouth/default-boot-duration %_localstatedir/lib/plymouth/boot-duration
[ -f %_localstatedir/lib/plymouth/shutdown-duration ] || cp -f %_datadir/plymouth/default-shutdown-duration %_localstatedir/lib/plymouth/shutdown-duration

%preun
if [ $1 = 0 ]; then
         /sbin/chkconfig --del %name
fi

%define theme_scripts() \
%post -n %name-theme-%{1} \
if [ -x %_sbindir/plymouth-set-default-theme ]; then \
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


%files -f %name.lang
%doc AUTHORS README.md
%dir %_datadir/plymouth
%dir %_datadir/plymouth/themes
%dir %_libdir/plymouth/renderers
%dir %_libexecdir/plymouth
%dir %_localstatedir/lib/plymouth
%config(noreplace) %_sysconfdir/plymouth/plymouthd.conf
%config(noreplace) %_sysconfdir/logrotate.d/bootlog
%config %_sysconfdir/sysconfig/bootsplash
%_initdir/plymouth
%plymouthdaemon_execdir/plymouthd
%plymouthdaemon_execdir/plymouth-update
%plymouthclient_execdir/plymouth
%_libdir/plymouth/details.so
%_libdir/plymouth/text.so
%_libdir/plymouth/tribar.so
%_libdir/plymouth/renderers/drm*
%_libdir/plymouth/renderers/frame-buffer*
%_libexecdir/plymouth/plymouthd-fd-escrow
%_datadir/plymouth/default-boot-duration
%_datadir/plymouth/default-shutdown-duration
%_datadir/plymouth/default-install-duration
%dir %_datadir/plymouth/themes/details
%_datadir/plymouth/themes/details/details.plymouth
%dir %_datadir/plymouth/themes/text
%_datadir/plymouth/themes/text/text.plymouth
%dir %_datadir/plymouth/themes/tribar
%_datadir/plymouth/themes/tribar/tribar.plymouth
%_datadir/plymouth/plymouthd.defaults
%_localstatedir/spool/plymouth
%_mandir/man?/*
%ghost %_localstatedir/lib/plymouth/boot-duration
%ghost %_localstatedir/lib/plymouth/shutdown-duration
%_unitdir/*

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
%_libexecdir/plymouth/plymouth-generate-initrd
%_libexecdir/plymouth/plymouth-populate-initrd

%files plugin-label
%_libdir/plymouth/label-pango.so
%_libdir/plymouth/label-freetype.so

%files plugin-fade-throbber
%_libdir/plymouth/fade-throbber.so

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

%files theme-spinner
%_datadir/plymouth/themes/spinner

%files theme-bgrt
%_datadir/plymouth/themes/bgrt

%files theme-bgrt-alt
%_datadir/plymouth/themes/bgrt-alt

%files system-theme

%changelog
* Sun Jun 09 2024 Anton Midyukov <antohami@altlinux.org> 1:24.004.60-alt5.20240608
- new snapshot

* Thu Jun 06 2024 Anton Midyukov <antohami@altlinux.org> 1:24.004.60-alt4
- do not use full PATH for systemd-tty-ask-password-agent

* Tue Apr 16 2024 Anton Midyukov <antohami@altlinux.org> 1:24.004.60-alt3
- don't put plymouth client and daemon in the prefix

* Mon Apr 15 2024 Anton Midyukov <antohami@altlinux.org> 1:24.004.60-alt2
- Set paths for systemd via meson options

* Mon Jan 08 2024 Anton Midyukov <antohami@altlinux.org> 1:24.004.60-alt1
- New version
- build with meson

* Tue Aug 29 2023 Anton Midyukov <antohami@altlinux.org> 1:22.02.122-alt3.20221016
- Add upstream commit:
  "drm: Use first output for panel info if there is no builtin display"

* Mon May 22 2023 Anton Midyukov <antohami@altlinux.org> 1:22.02.122-alt2.20221016
- Revert "Revert "Revert "drm: Remove explicit set_scan_out_buffer() from
  activate()"""

* Fri Apr 28 2023 Anton Midyukov <antohami@altlinux.org> 1:22.02.122-alt1.20221016
- snapshot 4bd41a355fa017afa4db86282b90eb67bbf9db59 (Closes: 44297)
- Revert "Revert "drm: Remove explicit set_scan_out_buffer() from activate()""
- src/main.c: set ignore_serial_consoles = true (Closes: 39326)
- bgrt-alt: add bgrt-fallback.png
- Revert "Fix daemon install ignoring configured runstatedir"
- Revert "Use standard runstatedir vs custom flag"

* Mon Feb 28 2022 Oleg Solovyov <mcpain@altlinux.org> 1:0.9.5-alt9
- bgrt-alt: move text block further

* Fri Feb 18 2022 Oleg Solovyov <mcpain@altlinux.org> 1:0.9.5-alt8
- Fix overlap in bgrt-alt theme
- Fetch russian translation from upstream

* Thu Jan 27 2022 Nikolai Kostrigin <nickel@altlinux.org> 1:0.9.5-alt7
- introduce bgrt-alt customized theme

* Wed Dec 08 2021 Oleg Solovyov <mcpain@altlinux.org> 1:0.9.5-alt6
- revert commit 3b75b66 (doesn't show splash on boot when using pve)

* Wed Nov 03 2021 Sergey V Turchin <zerg@altlinux.org> 1:0.9.5-alt5
- fix requires (closes: 39837)
- using /usr/share/design/current/icons/system-logo.png as special://logo

* Sun Jul 11 2021 Alexey Shabalin <shaba@altlinux.org> 1:0.9.5-alt4
- KillMode=mixed in plymouth-start.service
- kernel cmdline should contain splash for run plymouth
- filter requires on systemd-tty-ask-password-agent

* Sat Nov 07 2020 Alexey Shabalin <shaba@altlinux.org> 1:0.9.5-alt3
- plymouth-update-initrd: Adapt for make-initrd and dracut

* Mon Nov 02 2020 Alexey Shabalin <shaba@altlinux.org> 1:0.9.5-alt2
- Adapt for dracut

* Tue Sep 08 2020 Alexey Shabalin <shaba@altlinux.org> 1:0.9.5-alt1
- 0.9.5
- cleanup plymouth-start.service.

* Fri May 01 2020 Alexey Shabalin <shaba@altlinux.org> 1:0.9.4-alt4
- Add RemainAfterExit=yes to plymouth's systemd service files.
- Fix type plymouth-start.service.

* Tue Mar 31 2020 Anton Midyukov <antohami@altlinux.org> 1:0.9.4-alt3
- plymouth-start.service: ExecStart=/bin/true (Closes: 38229)

* Sun Nov 03 2019 Alexey Shabalin <shaba@altlinux.org> 1:0.9.4-alt2
- snapshot d18086efcc6aff16d510cfdbddad81421175a917
- remove the throbgress plugin
- build with --with-logo=%%_pixmapsdir/system-logo.png
- drop gdm-hooks package
- define runtimedir as /run
- use /etc/os-release for define release

* Sun Feb 24 2019 Alexey Shabalin <shaba@altlinux.org> 1:0.9.4-alt1
- 0.9.4
- add bgrt theme

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.8.8-alt6.git.37d2e4.qa1
- NMU: applied repocop patch

* Tue Apr 26 2016 Michael Shigorin <mike@altlinux.org> 1:0.8.8-alt6.git.37d2e4
- rollback to 0.8: 0.9 isn't included even in fedora (closes: #31379)

* Fri Mar 25 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.9.2-alt3.git.g5188f19
- upstream snapshot 5188f19416a60f801b46600503dd02926b4d9f33

* Tue Jun 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.9.2-alt2.git.ed5aa69
- upstream snapshot ed5aa69d4aa336898ebd2755d6222343f7cc2050

* Wed Apr 15 2015 Alexey Shabalin <shaba@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Thu Jun 19 2014 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Wed Mar 26 2014 Alexey Shabalin <shaba@altlinux.ru> 0.8.8-alt5.git.37d2e4
- upstream snapshot 37d2e400d25e6b4716d77d26fb7d40de8a8c1a8a

* Mon Apr 08 2013 Alexey Shabalin <shaba@altlinux.ru> 0.8.8-alt4.git.054d29
- upstream snapshot 054d29019d03fe787eeb26267774743d2a849777
- revert buggy commit "move to daemon in real system"
- remove systemd-vconsole-setup.service from plymouth-start.service

* Thu Mar 21 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8.8-alt3.git.b1140c
- fixed progress calculation while run in vesa framebuffer

* Fri Jan 25 2013 Alexey Shabalin <shaba@altlinux.ru> 0.8.8-alt2.git.b1140c
- build themes as noarch

* Wed Jan 23 2013 Alexey Shabalin <shaba@altlinux.ru> 0.8.8-alt1.git.b1140c
- upstream git snapshot b1140c1936adfd074d2a4db886cb26129e14f3a7

* Thu Sep 27 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.7-alt1
- 0.8.7
- disable libdrm_intel, libdrm_radeon too

* Sat Sep 15 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.8.6.1-alt2
- disabled libdrm_nouveau

* Tue Jul 17 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.6.1-alt1
- 0.8.6.1
- ship systemd service files
- add theme-spinner
- change stop level (ALT#27444)

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

