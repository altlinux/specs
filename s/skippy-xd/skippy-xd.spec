Name: skippy-xd
Version: 0.10.7.1
Release: alt1

Summary: Full-screen task-switcher for X11
License: %gpl2plus
Group: Graphical desktop/Other

# URL: http://code.google.com/p/skippy-xd/
# git://github.com/richardgv/skippy-xd.git
VCS: https://github.com/felixfung/skippy-xd
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses rpm-build-xdg

# Automatically added by buildreq on Sun Aug 30 2026
# optimized out: bash5 fontconfig-devel glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libXau-devel libXext-devel libXfixes-devel libXrender-devel libcairo-devel libcrypt-devel libfreetype-devel libgcc15-devel libgpg-error libgraphite2-devel libharfbuzz-devel libicu-devel libp11-kit libpng-devel libxcb-devel ninja-build openssl-config p11-kit-trust perl pkg-config python3 python3-base sh5 xorg-proto-devel xz zlib-devel
BuildRequires: ctags git-core libXcomposite-devel libXdamage-devel libXft-devel libXinerama-devel libgif-devel libjpeg-devel meson

%description
Standalone composited window picker (displays all your windows at once,
with live previews).

%prep
%setup

%build
export CFLAGS="%optflags"
%meson
%meson_build

%install
%meson_install

%files
%doc CHANGELOG README.*
%_xdgconfigdir/*.rc
%_bindir/*
%_man1dir/*

%changelog
* Sun Aug 30 2026 Fr. Br. George <george@altlinux.org> 0.10.7.1-alt1
- Update to 0.10.7.1

* Sun Aug 30 2026 Fr. Br. George <george@altlinux.org> 0.10.7-alt1
- Change upstream, many releases are passed

* Tue Mar 05 2019 Fr. Br. George <george@altlinux.ru> 0.5-alt1.git20150224
- Upstream git snapshot

* Thu Nov 28 2013 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20131106
- Upstream git snapshot.

* Wed Jun 19 2013 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20130602
- Initial build.

