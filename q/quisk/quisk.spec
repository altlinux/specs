Name: quisk
Version: 4.2.28
Release: alt1
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
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

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

# Drop dependency on distutils
grep -rl "distutils.core" | xargs sed -i 's/distutils.core/setuptools/'

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.txt CHANGELOG.txt *.html
%_bindir/quisk
%_bindir/quisk_vna
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version.dist-info

%changelog
* Thu Dec 21 2023 Andrey Cherepanov <cas@altlinux.org> 4.2.28-alt1
- New version 4.2.28.

* Sat Dec 09 2023 Andrey Cherepanov <cas@altlinux.org> 4.2.27-alt1
- New version 4.2.27.

* Thu Dec 07 2023 Andrey Cherepanov <cas@altlinux.org> 4.2.26-alt1
- New version 4.2.26.

* Thu Nov 30 2023 Andrey Cherepanov <cas@altlinux.org> 4.2.25-alt1
- New version 4.2.25.

* Thu Nov 23 2023 Andrey Cherepanov <cas@altlinux.org> 4.2.24-alt1
- New version 4.2.24.

* Tue Oct 17 2023 Grigory Ustinov <grenka@altlinux.org> 4.2.23-alt2
- Dropped dependency on distutils.

* Sun Sep 17 2023 Andrey Cherepanov <cas@altlinux.org> 4.2.23-alt1
- New version 4.2.23.

* Wed Sep 06 2023 Andrey Cherepanov <cas@altlinux.org> 4.2.22-alt1
- New version 4.2.22.

* Thu Nov 24 2022 Andrey Cherepanov <cas@altlinux.org> 4.2.12-alt1
- new version 4.2.12

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
