Name: xlibinput-calibrator
Version: 0.13.1
Release: alt1

Summary: Touch screen calibrator for X11 with libinput

License: MIT
Group: System/X11
Url: https://github.com/kreijack/xlibinput_calibrator

# Source-url: https://github.com/kreijack/xlibinput_calibrator/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++ libX11-devel libXi-devel libXrandr-devel txt2man

%description
xlibinput-calibrator calibrates a touch screen when the X server relies on
libinput. It sets the "libinput Calibration Matrix" property of the device
and can print the matrix, an xorg.conf.d snippet or an xinput command.
It is derived from xinput_calibrator, which does not work with libinput.

%prep
%setup

%build
%make_build all

%install
%makeinstall_std prefix=%_prefix/

%files
%doc README.md Changelog
%_bindir/xlibinput_calibrator
%_man8dir/xlibinput_calibrator.8*

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 0.13.1-alt1
- initial build for Sisyphus
