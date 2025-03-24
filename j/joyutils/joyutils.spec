Name: joyutils
Version: 1.8.1
Release: alt1

Summary: Joystick utilities
License: GPLv2
Group: System/Configuration/Hardware
Url: http://sf.net/projects/linuxconsole/

Source: %name-%version.tar

BuildRequires: libSDL2-devel libudev-devel

%description
The following utilities are provided to calibrate and test joysticks:
* evdev-joystick - calibrate joystick devices (including dead zones
  and fuzz)
* ffcfstress, ffmvforce, fftest - test force-feedback devices
* ffset - set force-feedback device parameters
* jscal - calibrate joystick devices, reconfigure the axes and buttons
* jscal-store, jscal-restore - store and retrieve joystick device
  settings as configured using jscal
* jstest - test joystick devices

The typical scenario when configuring a new device is as follows:
1. Check the basic functions using jstest (number of buttons, axes,
   etc.).
2. Calibrate the joystick using jscal (this can be useful even if the
   device functions correctly, if only to configure the dead-zone at
   the centre).
3. Repeat steps 1 and 2 until the joystick is configured to the user's
   satisfaction.
4. Store the device's setup using jscal-store.

%define defs PREFIX=%_prefix DISABLE_INPUTATTACH=1

%prep
%setup

%build
make %defs CFLAGS='%optflags' -C utils

%install
%make_install %defs DESTDIR=%buildroot install -C utils
install -pm0644 -D /dev/null %buildroot%_localstatedir/joystick/joystick.state

%files
%doc COPYING README
%_bindir/*
%_datadir/joystick
%_udevdir/js-set-enum-leds
%_udevdir/rules.d/80-stelladaptor-joystick.rules
%dir %_localstatedir/joystick
%ghost %_localstatedir/joystick/joystick.state

%changelog
* Mon Mar 24 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.1-alt1
- 1.8.1 released
