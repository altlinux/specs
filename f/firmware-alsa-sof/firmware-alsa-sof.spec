%global _firmwarepath  /lib/firmware
%define version_major 2.2.4
Summary: Firmware and topology files for Sound Open Firmware project
Name: firmware-alsa-sof
Version: %version_major
Release: alt1
# See later in the spec for a breakdown of licensing
License: BSD
Group: Sound
Url: https://github.com/thesofproject/sof-bin
BuildRequires: alsa-utils alsa-topology-conf
Source: %name-%version.tar
Source2: sof-glk-es8336-ssp0.tplg
Source3: sof-cml-es8336.tplg
Source4: sof-tgl-es8326.tplg
# part of upstream development stage topology set for ES8336 codec
# https://github.com/thesofproject/linux/files/8076329/es8336-topologies-3.tar.gz
Source5: sof-cml-es8336-ssp0.tplg
Provides: alsa-sof-firmware = %EVR
# noarch, since the package is firmware
BuildArch: noarch

%description
This package contains the firmware binaries for the Sound Open Firmware project.

%package debug
Requires: alsa-sof-firmware
Summary: Debug files for Sound Open Firmware project
Group: Sound

%description debug
This package contains the debug files for the Sound Open Firmware project.

%prep
%setup

%build
# build generic topology file from alsa-topology
alsatplg -c /usr/share/alsa/topology/hda-dsp/skl_hda_dsp_generic-tplg.conf \
         -o skl_hda_dsp_generic-tplg.bin

%install
mkdir -p  %buildroot%_firmwarepath/intel/
cp -a sof-tplg-v%version  %buildroot%_firmwarepath/intel/sof-tplg-v%version
install %SOURCE2 %buildroot%_firmwarepath/intel/sof-tplg-v%version/
install %SOURCE3 %buildroot%_firmwarepath/intel/sof-tplg-v%version/
install %SOURCE4 %buildroot%_firmwarepath/intel/sof-tplg-v%version/
install %SOURCE5 %buildroot%_firmwarepath/intel/sof-tplg-v%version/
cp -a sof-v%version  %buildroot%_firmwarepath/intel/sof
ln -s sof-tplg-v%version %buildroot%_firmwarepath/intel/sof-tplg
install -m0644 skl_hda_dsp_generic-tplg.bin %buildroot%_firmwarepath/

# gather files and directories
FILEDIR=$(pwd)
pushd %buildroot/%_firmwarepath
find -P . -name "*.ri" | sed -e '/^.$/d' > $FILEDIR/alsa-sof-firmware.files
find -P . -name "*.tplg" | sed -e '/^.$/d' >> $FILEDIR/alsa-sof-firmware.files
find -P . -name "*.ldc" | sed -e '/^.$/d' > $FILEDIR/alsa-sof-firmware.debug-files
find -P . -type d | sed -e '/^.$/d' > $FILEDIR/alsa-sof-firmware.dirs
popd
sed -i -e 's:^./::' alsa-sof-firmware.{files,debug-files,dirs}
sed -i -e 's!^!/lib/firmware/!' alsa-sof-firmware.{files,debug-files,dirs}
sed -e 's/^/%%dir /' alsa-sof-firmware.dirs >> alsa-sof-firmware.files
cat alsa-sof-firmware.files

%files -f alsa-sof-firmware.files
%doc LICENCE*  README*
%dir %_firmwarepath
%_firmwarepath/skl_hda_dsp_generic-tplg.bin
%dir %_firmwarepath/intel
%_firmwarepath/intel/sof-tplg

%files debug -f alsa-sof-firmware.debug-files

%changelog
* Fri Jan 13 2023 Anton Farygin <rider@altlinux.ru> 2.2.4-alt1
- 2.2.3 -> 2.2.4

* Wed Dec 14 2022 Anton Farygin <rider@altlinux.ru> 2.2.3-alt1
- 2.2.2 -> 2.2.3

* Thu Nov 03 2022 Anton Farygin <rider@altlinux.ru> 2.2.2-alt1
- 2.0 -> 2.2.2

* Thu Apr 07 2022 Nikolai Kostrigin <nickel@altlinux.org> 2.0-alt2
- added extra topologies for es83x6, from upstream and OEM patners

* Wed Dec 22 2021 Anton Farygin <rider@altlinux.ru> 2.0-alt1
- 1.9.3 -> 2.0

* Fri Dec 17 2021 Anton Farygin <rider@altlinux.ru> 1.9.3-alt1
- 1.9.2 -> 1.9.3

* Thu Nov 25 2021 Anton Farygin <rider@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Mon Oct 04 2021 Anton Farygin <rider@altlinux.ru> 1.8-alt4
- added topology for es8336, received from our OEM partners

* Sun Oct 03 2021 Anton Farygin <rider@altlinux.ru> 1.8-alt3
- reverted back to using directory for /lib/firmware/alsa/sof (closes: #41045)

* Fri Oct 01 2021 Anton Farygin <rider@altlinux.ru> 1.8-alt2
- RPM does not know how to replace the symlinks to the directory.
  Switched to symlink back (for sof and sof-tplg).
- Added generic SST topology file for Skylake SST driver.

* Thu Sep 30 2021 Anton Farygin <rider@altlinux.ru> 1.8-alt1
- 1.8

* Sun Apr 25 2021 Anton Farygin <rider@altlinux.ru> 1.7-alt1
- 1.7

* Fri Feb 05 2021 Anton Farygin <rider@altlinux.org> 1.6.1-alt1
- 1.6.1

* Mon Apr 27 2020 Anton Farygin <rider@altlinux.ru> 1.4.2-alt1
- first build for ALT, based on Fedora package

