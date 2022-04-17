Name: dosbox-staging
Version: 0.78.1
Release: alt1
License: GPLv2
Summary: An attempt to revitalize DOSBox, an emulator that recreates a MS-DOS compatible environment
Group: Emulators
Source: %name-%version.tar.gz
Patch: dosbox-staging-0.77.0-ne2000.patch

%ifarch %ix86
%set_verify_elf_method textrel=relaxed
%endif

# Automatically added by buildreq on Thu Apr 07 2022
# optimized out: glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libSDL2-devel libX11-devel libcrypt-devel libglvnd-devel libgmock-devel libgpg-error libogg-devel libopus-devel libp11-kit libstdc++-devel libxcb-devel ninja-build perl pkg-config python3 python3-base sh4 xz zlib-devel
BuildRequires: ctags gcc-c++ git-core libSDL2_net-devel libalsa-devel libfluidsynth-devel libgtest-devel libmt32emu-devel libopusfile-devel libpcap-devel libpng-devel libslirp-devel meson

%description
dosbox-staging is an attempt to revitalize DOSBox's development process.
It's not a rewrite, but a continuation and improvement on the existing
DOSBox codebase while leveraging modern development tools and practices.

Goals:
- Improve the out-of-the-box experience for new users.
- Encourage new contributors by removing barriers to entry.
- Fix, cleanup, and integrate several notable community-developed
patches that are not included in the SourceForge-hosted project.
- Implement new features and quality-of-life improvements.
- Prioritize DOS gaming, while welcoming general improvements (such as
for productivity software) that don't impact game emulation quality or
code-maintainability.
- Strike a balance between emulation quality, speed, and usability.
- Deliver a consistent cross-platform experience.
- Leverage ongoing DOSBox development.
- Focus on supporting up-to-date, current Operating Systems and modern
hardware.

%prep
%setup
%patch -p1
sed -i 's/=dosbox$/=dosbox-staging/' contrib/linux/dosbox-staging.desktop
sed -i 's/>dosbox</>dosbox-staging</' contrib/linux/dosbox-staging.metainfo.xml

%build
%meson
%meson_build

%install
%meson_install
install -D contrib/icons/dosbox-staging.svg %buildroot%_iconsdir/hicolor/scalable/apps/dosbox-staging.svg
install -D contrib/linux/dosbox-staging.desktop %buildroot/%_desktopdir/dosbox-staging.desktop
mv %buildroot/%_bindir/dosbox %buildroot/%_bindir/%name
mv %buildroot/%_man1dir/dosbox.1 %buildroot/%_man1dir/dosbox-staging.1

%files
%doc docs/*
%doc ?[A-Z]*
%_bindir/*
%_man1dir/*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*
%_datadir/metainfo/*
%_datadir/dosbox-staging

%exclude %_defaultdocdir/%name
%exclude %_datadir/licenses

%changelog
* Thu Apr 07 2022 Fr. Br. George <george@altlinux.org> 0.78.1-alt1
- Autobuild version bump to 0.78.1
- Introduce translations

* Wed Aug 25 2021 Fr. Br. George <george@altlinux.ru> 0.77.0-alt2
- Fix original DOSBox file conflicts

* Sun Aug 22 2021 Fr. Br. George <george@altlinux.ru> 0.77.0-alt1
- Autobuild version bump to 0.77.0
- Enable NE2000 emulation

* Fri Dec 18 2020 Fr. Br. George <george@altlinux.ru> 0.76.0-alt1
- Autobuild version bump to 0.76.0
- Fix build on i686 (allow textrel)

* Wed May 13 2020 Fr. Br. George <george@altlinux.ru> 0.75.0-alt1
- Initial build for ALT

