Name: pnmixer
Version: 0.5.1
Release: alt2

Summary: Volume mixer for the system tray
License: %gpl3only
Group: Graphical desktop/Other
Url: https://github.com/nicklan/pnmixer
Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Patches from Fedora:
# Set default mouse scroll step to 5
Patch1: pnmixer-0.5.0-volume-steps.patch
# Small fixes for the desktop file
Patch2: pnmixer-0.5.1-desktop-file.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: libgtk+2-devel libalsa-devel

%description
PNMixer is system tray sound mixer.
PNMixer integrates nicely into desktop environments that don't have a
panel that supports applets, and therefore can't run a mixer applet.
In particular it's been used quite a lot with fbpanel and tint2, but
should run fine in any system tray.
PNMixer currently supports ALSA and Pulse audio.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
find /usr/share/automake-* -name mkinstalldirs -type f | head -1 | xargs ln -s -t .

# Fix icon in launcher
sed -i 's/^Icon=pnmixer/Icon=multimedia-volume-control/' data/pnmixer.desktop

%build
%autoreconf
%configure

# CFLAGS... is only needed because of
# https://github.com/nicklan/pnmixer/issues/19
%make_build CFLAGS='%optflags'

%install
%makeinstall_std

# Don't show PNMixer in the menu,
# just autostart it instead.
mkdir -p %buildroot%_sysconfdir/xdg/autostart/
mv %buildroot%_desktopdir/%name.desktop %buildroot%_sysconfdir/xdg/autostart/

%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README
%config %_sysconfdir/xdg/autostart/%name.desktop
%_bindir/%name
%_datadir/%name/

%changelog
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
