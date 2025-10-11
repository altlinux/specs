%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: buffybox
Version: 3.2.0
Release: alt2.gc683350

Summary: A suite of graphical applications for the terminal
License: GPL-3.0-or-later
Group: Accessibility
URL: https://gitlab.com/postmarketOS/buffybox.git

Source0: %name-%version.tar
Source1: lvgl.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libinih-devel
BuildRequires: libinput-devel
BuildRequires: libxkbcommon-devel
BuildRequires: scdoc

%description
%summary.

%package -n buffyboard
Summary: Touch-enabled framebuffer keyboard
Group: Accessibility

%description -n buffyboard
Buffyboard is a touch-enabled on-screen keyboard running
on Linux framebuffer.

%package -n unl0kr
Summary: Disk unlocker for the initramfs based on LVGL
Group: Accessibility
Requires: xkeyboard-config

%description -n unl0kr
Unl0kr is an osk-sdl clone written in LVGL and rendering
directly to the Linux framebuffer. As a result, it doesn't
depend on GPU hardware acceleration.

%prep
%setup -a1
%patch0 -p1

%build
%meson
%meson_build

%install
%meson_install

%files -n unl0kr
%config(noreplace) %_sysconfdir/unl0kr.conf
%_bindir/unl0kr
%_man1dir/unl0kr*
%_man5dir/unl0kr*

%files -n buffyboard
%config(noreplace) %_sysconfdir/buffyboard.conf
%_bindir/buffyboard
%_man1dir/buffyboard*
%_man5dir/buffyboard*

%changelog
* Mon Oct 06 2025 Anton Midyukov <antohami@altlinux.org> 3.2.0-alt2.gc683350
- unl0kr: add runtime dependencies on xkeyboard-config

* Mon Sep 29 2025 Egor Shestakov <ved@altlinux.org> 3.2.0-alt1.gc683350
- Initial build:
  + unl0kr package has become part of the buffybox suite
