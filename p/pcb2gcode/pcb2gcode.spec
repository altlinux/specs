Name: pcb2gcode
Version: 1.3.2
Release: alt1
Summary: Command-line software for the isolation, routing and drilling of PCBs

Group: Engineering
License: GPLv3+
Url: https://github.com/pcb2gcode/pcb2gcode/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: boost-program_options-devel boost-geometry-devel
BuildRequires: pkgconfig(glibmm-2.4) >= 2.8
BuildRequires: pkgconfig(gdkmm-2.4) >= 2.8
BuildRequires: pkgconfig(libgerbv) >= 2.1.0

%description
pcb2gcode is a command-line software for the isolation, routing and drilling of
PCBs. It takes Gerber files as input and it outputs gcode files, suitable for
the milling of PCBs. It also includes an Autoleveller, useful for the automatic
dynamic calibration of the milling depth.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/pcb2gcode
%_man1dir/pcb2gcode.1*
%doc AUTHORS README.md
%doc COPYING

%changelog
* Tue Jul 25 2017 Anton Midyukov <antohami@altlinux.org> 1.3.2-alt1
- Initial build for ALT Sisyphus.
