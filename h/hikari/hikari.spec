Name: hikari
Version: 2.2.2
Release: alt3

Summary: a stacking Wayland compositor

License: BSD-2-Clause
Group: Graphical desktop/Other
Url: https://hikari.acmelabs.space/

# repacked https://hikari.acmelabs.space/releases/hikari-%version.tar.gz
Source: %name-%version.tar
Source1: %name.watch
Patch1: 0001-ALT-fix-permissions.patch

Requires: xorg-xwayland
Requires: libdrmhelper

# Automatically added by buildreq on Thu Nov 12 2020
# optimized out: fontconfig glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libEGL-devel libcairo-devel libglvnd-devel libgpg-error libharfbuzz-devel libpixman-devel libudev-devel libwayland-client libwayland-egl libwayland-server libwayland-server-devel libxcb-devel libxcbutil-icccm pkg-config python2-base sh4 wayland-devel
BuildRequires: bmake libinput-devel libpam-devel libpango-devel libucl5-devel libwlroots-devel libxkbcommon-devel pkgsrc-mk-files wayland-protocols
# dependencies listed above do not requires libEGL-devel on armh for some reason
BuildRequires: libEGL-devel

%description
hikari is a stacking Wayland compositor with additional tiling capabilities, it
is heavily inspired by the Calm Window manager (cwm(1)).

%prep
%setup
%autopatch -p2

%define env \
  unset MAKEFLAGS; \
  export USE_NM=%_bindir/nm \
  export USE_INSTALL=%__install \
  export USE_AWK=%_bindir/awk \
  export USE_ID=%_bindir/id \
  export USE_CC_COMPILERS='%cc_compilers' \
  export USE_CXX_COMPILERS='%cxx_compilers' \
  export PREFIX=%_prefix \
  export SYSCONFDIR=%_sysconfdir \
  export MANDIR=%_mandir

%build
%env
bmake \
	WITH_POSIX_C_SOURCE=YES \
	WITH_XWAYLAND=YES \
	#

%install
%env
bmake \
	DESTDIR=%buildroot \
	ETC_PREFIX="" \
	PREFIX=%prefix \
	install

%files
%doc CHANGELOG.md LICENSE README.md

%dir %_sysconfdir/hikari
%config(noreplace) %_sysconfdir/hikari/hikari.conf
%config(noreplace) %_sysconfdir/pam.d/hikari-unlocker

%_bindir/hikari
%attr(2711,root,chkpwd) %_bindir/hikari-unlocker

%dir %_datadir/backgrounds
%dir %_datadir/backgrounds/hikari
%dir %_datadir/wayland-sessions
%_datadir/backgrounds/hikari/hikari_wallpaper.png
%_datadir/wayland-sessions/hikari.desktop

%_man1dir/hikari.1*

%changelog
* Wed Dec 30 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.2.2-alt3
- Fixed package group (ALT#39488).

* Tue Dec 29 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.2.2-alt2
- Fixed hikari and hikari-unlocker executables permissions (no more suid);
- Added dependency to libdrmhelper.

* Thu Nov 12 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.2.2-alt1
- Initial build for ALT Sisyphus.

