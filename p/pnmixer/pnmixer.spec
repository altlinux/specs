Name: pnmixer
Version: 0.7
Release: alt1

%def_without	gtk3

Summary: Volume mixer for the system tray
License: %gpl3only
Group: Graphical desktop/Other
Url: https://github.com/nicklan/pnmixer
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: intltool libalsa-devel libnotify-devel
%if_without gtk3
BuildRequires: libgtk+2-devel
%else
BuildRequires: libgtk+3-devel
%endif

%define _unpackaged_files_terminate_build 1

%description
PNMixer is a simple mixer application designed to run in your system
tray. It integrates nicely into desktop environments that don't have
a panel that supports applets and therefore can't run a mixer applet.
In particular it's been used quite a lot with fbpanel and tint2, but
should run fine in any system tray.

PNMixer is designed to work on systems that use ALSA for sound
management.
Any other sound driver like OSS or FFADO are currently not supported
(patches welcome). There is no *official* PulseAudio support
at the moment, but it seems that PNMixer behaves quite well anyway when
PA is running.
Feel free to try and to give some feedback.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--with-libnotify \
	%subst_with gtk3

%make_build

%install
%makeinstall_std

# Don't show PNMixer in the menu,
# just autostart it instead.
mkdir -p %buildroot%_sysconfdir/xdg/autostart/
mv %buildroot%_desktopdir/%name.desktop %buildroot%_sysconfdir/xdg/autostart/

%find_lang %name

%files -f %name.lang
%doc AUTHORS README.md
%config %_sysconfdir/xdg/autostart/%name.desktop
%_iconsdir/hicolor/128x128/apps/%name.png
%_bindir/%name
%_datadir/%name/
%_man1dir/*

%changelog
* Tue Sep 20 2016 Mikhail Efremov <sem@altlinux.org> 0.7-alt1
- Updated description.
- Updated to 0.7.

* Mon Sep 28 2015 Mikhail Efremov <sem@altlinux.org> 0.6.1-alt1
- Updated description.
- Drop old Fedora patches.
- Updated to 0.6.1.

* Wed Jan 15 2014 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt2
- Bump release because of the release in the autoimport
  repository is greater then alt1. Make robots happy.

* Tue Jan 14 2014 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1
- Fix segfault if no channels found.
- Fix icon in launcher.
- Don't show PNMixer in the menu.
- Add patches from Fedora.
- Fix configure.in for current autotools.
- Initial build.
