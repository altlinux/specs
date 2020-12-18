Name: dosbox-staging
Version: 0.76.0
Release: alt1
License: GPLv2
Summary: An attempt to revitalize DOSBox, an emulator that recreates a MS-DOS compatible environment
Group: Emulators
Source: %name-%version.tar.gz
%ifarch %ix86
%set_verify_elf_method textrel=relaxed
%endif

# Automatically added by buildreq on Fri Dec 18 2020
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libSDL2-devel libglvnd-devel libgpg-error libogg-devel libopus-devel libstdc++-devel perl pkg-config python2-base sh4 zlib-devel
BuildRequires: gcc-c++ libSDL2-devel libSDL2_net-devel libalsa-devel libfluidsynth-devel libopusfile-devel libpng-devel

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
sed -i 's/=dosbox$/=dosbox-staging/' contrib/linux/dosbox-staging.desktop

%build
%autoreconf
%configure --program-suffix=-staging
%make_build CXXFLAGS=-pthread

%install
%makeinstall_std
install -D contrib/icons/dosbox-staging.svg %buildroot%_iconsdir/hicolor/scalable/apps/dosbox-staging.svg
install -D contrib/linux/dosbox-staging.desktop %buildroot/%_desktopdir/dosbox-staging.desktop

%files
%doc docs
%_bindir/*
%_man1dir/*
%_iconsdir/hicolor/scalable/apps/*
%_desktopdir/*

%changelog
* Fri Dec 18 2020 Fr. Br. George <george@altlinux.ru> 0.76.0-alt1
- Autobuild version bump to 0.76.0
- Fix build on i686 (allow textrel)

* Wed May 13 2020 Fr. Br. George <george@altlinux.ru> 0.75.0-alt1
- Initial build for ALT

