%set_verify_elf_method no

Summary: bootloader and GPU firmware for Raspberry Pi
Name: raspberrypi-firmware
Version: 20221214
Release: alt3
Url: https://github.com/raspberrypi/firmware
License: distributable
Group: System/Kernel and hardware

BuildArch: noarch

Source0: %name-%version.tar

%description
%summary

%install
mkdir -p %buildroot%_datadir
tar -xf %SOURCE0 -C %buildroot%_datadir

%files
%_datadir/%name

%changelog
* Mon Feb 13 2023 Anton Midyukov <antohami@altlinux.org> 20221214-alt3
- BuildArch: noarch (Closes: 44652)
- do'nt require u-boot-rpi3

* Thu Dec 15 2022 Anton Midyukov <antohami@altlinux.org> 20221214-alt2
- do'nt create hardlinks in u-boot directories

* Thu Dec 15 2022 Anton Midyukov <antohami@altlinux.org> 20221214-alt1
- New snapshot (Closes: 44641)

* Sun Apr 25 2021 Anton Midyukov <antohami@altlinux.org> 20210421-alt1
- New snapshot

* Mon Feb 22 2021 Anton Midyukov <antohami@altlinux.org> 20210216-alt1
- New snapshot
- Add new dtb:
  + bcm2711-rpi-cm4.dtb
  + bcm2711-rpi-400.dtb
- Add option hdmi_ignore_edid_audio=1 to config.txt for fix audio

* Thu Jul 30 2020 Anton Midyukov <antohami@altlinux.org> 20200730-alt1
- New snapshot
- Added overlays and dtb for all boards

* Tue Jun 02 2020 Dmitry Terekhin <jqt4@altlinux.org> 20200527-alt1
- Added parameter in config.txt for RPi4:
- dtoverlay=vc4-fkms-v3d
- New snapshot

* Thu Apr 16 2020 Anton Midyukov <antohami@altlinux.org> 20200228-alt3
- Also added parameters in config.txt for RPi3:
- disable_overscan=1
- dtparam=audio=on

* Wed Apr 01 2020 Dmitry Terekhin <jqt4@altlinux.org> 20200228-alt2
- Added parameters in config.txt for RPi4:
- disable_overscan=1
- dtparam=audio=on

* Wed Mar 04 2020 Dmitry Terekhin <jqt4@altlinux.org> 20200228-alt1
- new snapshot

* Thu Nov 14 2019 Dmitry Terekhin <jqt4@altlinux.org> 20191105-alt2
- Added bcm2711-rpi-4-b.dtb for the RasPi4 firmware's work

* Tue Nov 05 2019 Dmitry Terekhin <jqt4@altlinux.org> 20191105-alt1
- new snapshot

* Tue Oct 08 2019 Anton Midyukov <antohami@altlinux.org> 20190926-alt2
- Add support u-boot-rpi3-2019.10

* Thu Sep 26 2019 Dmitry Terekhin <jqt4@altlinux.org> 20190926-alt1
- new snapshot

* Sat Jul 20 2019 Anton Midyukov <antohami@altlinux.org> 20190716-alt1
- new snapshot

* Sat Feb 16 2019 Anton Midyukov <antohami@altlinux.org> 20190213-alt1
- Initial build
