Name: quisk
Version: 4.1.96
Release: alt1.1
Summary: QUISK is a Software Defined Radio (SDR) transceiver that can control various radio hardware

License: GPL-2.0
Group: Communications
URL: http://james.ahlstrom.name/quisk/

# Download latest version from https://pypi.org/project/quisk/#files
Source: %name-%version.tar.gz
Source1: %name.watch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: libfftw3-devel
BuildRequires: libportaudio2-devel
BuildRequires: libpulseaudio-devel

%filter_from_requires /^python3(\(_quisk\|ftd2xx\))/d
%py3_requires usb PIL

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%name/

%description
QUISK is a Software Defined Radio (SDR) transceiver. You supply radio hardware
that converts signals at the antenna to complex (I/Q) data at an intermediate
frequency (IF). Data can come from a sound card, Ethernet or USB. Quisk then
filters and demodulates the data and sends the audio to your speakers or
headphones. For transmit, Quisk takes the microphone signal, converts it to I/Q
data and sends it to the hardware.

Quisk can be used with SoftRock, Hermes Lite 2, HiQSDR, Odyssey and many radios
that use the Hermes protocol. Quisk can connect to digital programs like Fldigi
and WSJT-X. Quisk can be connected to other software like N1MM+ and software
that uses Hamlib.

%prep
%setup

# Fix python3 shebangs
subst 's|#!.*python$|#!%__python3|' $(grep -Rl '#!.*python$' *)

# Remove precompiled executables
find . -name \*.pyc -o -name \*.pyd -o -name \*.so -o -name \*.dll | xargs rm -f

# Remove executable bit from any files
find . -type f -exec chmod a-x '{}' ';'

%build
%python3_build

%install
%python3_install

%files
%doc docs.html defaults.html help.html help_conf.html help_vna.html
%_bindir/*
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info

%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 4.1.96-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Fri May 13 2022 Andrey Cherepanov <cas@altlinux.org> 4.1.96-alt1
- new version 4.1.96

* Mon May 09 2022 Andrey Cherepanov <cas@altlinux.org> 4.1.95-alt1
- new version 4.1.95

* Thu Apr 14 2022 Andrey Cherepanov <cas@altlinux.org> 4.1.94-alt1
- new version 4.1.94

* Tue Feb 08 2022 Andrey Cherepanov <cas@altlinux.org> 4.1.93-alt2
- Requires python3(usb) and python3(PIL).

* Mon Jan 24 2022 Andrey Cherepanov <cas@altlinux.org> 4.1.93-alt1
- Initial build in Sisyphus.
