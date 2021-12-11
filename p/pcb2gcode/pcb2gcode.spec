Name: pcb2gcode
Version: 2.4.0
Release: alt3
Summary: Command-line software for the isolation, routing and drilling of PCBs

Group: Engineering
License: GPLv3+
Url: https://github.com/pcb2gcode/pcb2gcode/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

# Tests fails
ExcludeArch: %ix86 %arm

BuildRequires: gcc-c++
BuildRequires: boost-program_options-devel boost-geometry-devel
BuildRequires: pkgconfig(glibmm-2.4) >= 2.8
BuildRequires: pkgconfig(gdkmm-2.4) >= 2.8
BuildRequires: pkgconfig(libgerbv) >= 2.1.0
BuildRequires: pkgconfig(librsvg-2.0)

%description
pcb2gcode is a command-line software for the isolation, routing and drilling of
PCBs. It takes Gerber files as input and it outputs gcode files, suitable for
the milling of PCBs. It also includes an Autoleveller, useful for the automatic
dynamic calibration of the milling depth.

%prep
%setup

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS -I%_includedir/librsvg-2.0"
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%_bindir/*
%_man1dir/*.1*
%doc AUTHORS README.md

%changelog
* Sat Dec 11 2021 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt3
- add -I%_includedir/librsvg-2.0 to CXXFLAGS (fix FTBFS)

* Sat Sep 25 2021 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt2
- add compiler flag '-std=c++14' (fix build with gcc-c++ >= 11)
- ExcludeArch: %ix86 %arm (tests fails)

* Thu May 13 2021 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Sun Jul 08 2018 Anton Midyukov <antohami@altlinux.org> 1.3.2-alt1.2
- Rebuilt for aarch64

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.2-alt1.1
- NMU: rebuilt with boost-1.67.0

* Tue Jul 25 2017 Anton Midyukov <antohami@altlinux.org> 1.3.2-alt1
- Initial build for ALT Sisyphus.
