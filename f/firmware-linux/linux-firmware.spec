Name: firmware-linux
Version: 20180222
Release: alt1

Summary: Firmware files used by the Linux kernel
License: GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
Group: System/Kernel and hardware

Url: git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
Provides: linux-firmware
Provides: firmware-iwl1000 
Provides: firmware-iwl3945 firmware-iwl4965 firmware-iwl5000 firmware-iwl5150 
Provides: firmware-iwl6000 firmware-iwl6050 
Obsoletes: firmware-iwl1000 
Obsoletes: firmware-iwl3945 firmware-iwl4965 firmware-iwl5000 firmware-iwl5150 
Obsoletes: firmware-iwl6000 firmware-iwl6050 
#Requires: firmware-ipw2200 firmware-ipw2100 firmware-ipw3945
Provides:  firmware-carl9170-1.9.4 firmware-i2400m firmware-rt2870 firmware-rt3090
Obsoletes: firmware-carl9170-1.9.4 firmware-i2400m firmware-rt2870 firmware-rt3090
Provides: firmware-amd-ucode
Obsoletes: firmware-amd-ucode <= 2.0

Requires: udev
AutoReqProv: no

%add_verify_elf_skiplist /lib/firmware/*

%description
Kernel-firmware includes firmware files
required for some devices to operate.

%prep
%setup -n %name-%version 
%patch -p1

%build
# Remove firmware shipped in separate packages already
# Perhaps these should be built as subpackages of linux-firmware?
## firmware-ql*
rm ql2???_fw.bin LICENCE.qla2xxx
## *TODO* check these too
rm -rf ess korg sb16 yamaha
# We have _some_ ralink firmware in separate packages already.
rm rt73.bin rt2561.bin rt2561s.bin rt2661.bin

# Remove source files we don't need to install
rm -f usbdux/*dux */*.asm *spec

# Fallback symlink in case kernel driver lags behind
# TODO: drop it when we move to 3.19+ or so
ln -s fw_sst_0f28.bin-48kHz_i2s_master intel/fw_sst_0f28.bin-i2s_master

%install
mkdir -p %buildroot/lib/firmware
cp -a * %buildroot/lib/firmware
rm %buildroot/lib/firmware/{WHENCE,LICENCE.*,*.py}

%files
%doc WHENCE LICEN?E.*
/lib/firmware/*
%exclude /lib/firmware/carl9170fw

%changelog
* Sat Feb 24 2018 L.A. Kostis <lakostis@altlinux.ru> 20180222-alt1
- configuration changes:
  +  update changelog rules
- upstream changes (GIT 7344ec9):
  + ath10k: QCA9984 hw1.0: update firmware-5.bin to 10.4-3.5.3-00053 (thx Kalle Valo)
  + ath10k: QCA988X hw2.0: update firmware-5.bin to 10.2.4-1.0-00037 (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update firmware-5.bin to 10.4-3.5.3-00053 (thx Kalle Valo)
  + ath10k: QCA9887 hw1.0: update firmware-5.bin to 10.2.4-1.0-00037 (thx Kalle Valo)
  + ath10k: QCA9377 hw1.0: update firmware-5.bin to
    WLAN.TF.1.0-00002-QCATFSWPZ-5 (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update firmware-6.bin to
    WLAN.RM.4.4.1-00079-QCARMSWPZ-1 (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update firmware-5.bin to 10.4-3.5.3-00053 (thx Kalle Valo)
  + rtl_bt: Add firmware and configuration files for the Bluetooth
    parts of RTL8821C and RTL8723D (thx Larry Finger)
  + qed: Add firmwares 8.30.12.0 and 8.10.9.0 (thx Rasesh Mody)
  + nfp: update Agilio SmartNIC firmware to rev 2.0.4 (thx Edwin Peer)

* Fri Feb 02 2018 L.A. Kostis <lakostis@altlinux.ru> 20180201-alt1
- configuration changes:
  + changelog.sh: get pkg name from specfile
  + cronbuild: initial config
- upstream changes (GIT 2aa2ac2):
  + linux-firmware: Add firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + linux-firmware: Add firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + linux-firmware: Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + wl127x/wl128x: update PLT firmwares (thx Guy Mishol)
  + linux-firmware: intel: Update Kabylake audio firmware (thx Guneshwor Singh)
  + .gear: simplify cronbuild scripts

* Tue Jan 23 2018 Konstantin A. Lepikhov <lakostis@altlinux.ru> 20180118-alt1
- Update 65b1c68 GIT:
  + amdgpu: update uvd firmware for polaris asics (thx Alex Deucher).
  + amdgpu: update vce firmware for Fiji (thx Alex Deucher).
  + amdgpu: update vcn firmware for raven (thx Alex Deucher).
  + amdgpu: update vce and uvd firmware for Vega10 (thx Alex Deucher).
  + mediatek: update MT8173 VPU firmware to 1.0.8 [decoder h264]
    Fix h264 decoder output delay for some low latency bitstreams
    (thx pochun.lin).
  + cxgb4: update firmware to revision 1.17.14.0 (thx Ganesh Goudar).
  + linux-firmware: update Marvell PCIe-USB8897/8997 firmware image
    to add WPA2 vulnerability fix (thx Xinming Hu).
  + LICENSE.nouveau-firmware: added.
  + linux-firmware: intel: Update Geminilake audio firmware
    (thx Pradeep Tewani).

* Sat Jan 13 2018 L.A. Kostis <lakostis@altlinux.ru> 20180104-alt1.2
- prepare .spec for cronbuild.

* Fri Jan 05 2018 L.A. Kostis <lakostis@altlinux.ru> 20180104-alt1.1
- amd-ucode: Add microcode_amd_fam17h.bin (bsc#1068032 CVE-2017-5715)

* Fri Jan 05 2018 L.A. Kostis <lakostis@altlinux.ru> 20180104-alt1
- Updated to 65b1c68 GIT.

* Mon Dec 04 2017 Michael Shigorin <mike@altlinux.org> 20171128-alt1
- updated from git

* Mon Oct 30 2017 Michael Shigorin <mike@altlinux.org> 20171009-alt1
- updated from git

* Mon Sep 11 2017 Michael Shigorin <mike@altlinux.org> 20170901-alt1
- updated from git

* Mon Jun 26 2017 Michael Shigorin <mike@altlinux.org> 20170622-alt1
- updated from git

* Mon Jun 05 2017 Michael Shigorin <mike@altlinux.org> 20170531-alt1
- updated from git

* Mon May 22 2017 Michael Shigorin <mike@altlinux.org> 20170517-alt2
- disable attempts to find R:/P: or ELF bugs automatically

* Mon May 22 2017 Michael Shigorin <mike@altlinux.org> 20170517-alt1
- updated from git

* Wed Mar 22 2017 Michael Shigorin <mike@altlinux.org> 20170314-alt1
- updated from git

* Mon Jan 23 2017 Michael Shigorin <mike@altlinux.org> 20170113-alt1
- updated from git (closes: #33022)

* Tue Nov 15 2016 Michael Shigorin <mike@altlinux.org> 20160927-alt2
- dropped /lib/firmware/check_whence.py (closes: #32754)

* Mon Oct 24 2016 Michael Shigorin <mike@altlinux.org> 20160927-alt1
- updated from git

* Wed Aug 03 2016 Michael Shigorin <mike@altlinux.org> 20160728-alt1
- updated from git

* Wed Jun 15 2016 Michael Shigorin <mike@altlinux.org> 20160608-alt1
- updated from git

* Tue Mar 01 2016 Michael Shigorin <mike@altlinux.org> 20160219-alt1
- updated from git

* Tue Feb 16 2016 Michael Shigorin <mike@altlinux.org> 20160216-alt1
- updated from git

* Sun Nov 29 2015 Michael Shigorin <mike@altlinux.org> 20151129-alt1
- updated from git

* Fri Nov 06 2015 Michael Shigorin <mike@altlinux.org> 20151104-alt1
- updated from git

* Thu Sep 10 2015 Michael Shigorin <mike@altlinux.org> 20150824-alt1
- updated from git
  + NB: amdgpu* have arrived (thx lakostis@ for the notice)

* Thu Aug 13 2015 Michael Shigorin <mike@altlinux.org> 20150811-alt1
- updated from git
- dropped Requires: firmware-ipw* (closes: #30308)

* Mon Jun 01 2015 Michael Shigorin <mike@altlinux.org> 20150506-alt1
- updated from git

* Tue Apr 28 2015 Michael Shigorin <mike@altlinux.org> 20150410-alt1
- updated from git

* Fri Dec 26 2014 Michael Shigorin <mike@altlinux.org> 20141222-alt1
- updated from git

* Tue Nov 11 2014 Michael Shigorin <mike@altlinux.org> 20141009-alt1
- updated from git

* Mon Oct 06 2014 Michael Shigorin <mike@altlinux.org> 20140926-alt1
- updated from git

* Tue Sep 30 2014 Michael Shigorin <mike@altlinux.org> 20140902-alt1
- updated from git

* Wed Sep 10 2014 Michael Shigorin <mike@altlinux.org> 20140828-alt2
- add P:/O: firmware-amd-ucode

* Sat Aug 30 2014 Michael Shigorin <mike@altlinux.org> 20140828-alt1
- updated from git

* Wed May 21 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20140521-alt1
- updated from git

* Thu Jan 23 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20140123-alt1
- updated from git

* Wed Nov 06 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20131106-alt1
- updated from git

* Wed Sep 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130904-alt1
- updated from git

* Thu Jun 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130613-alt1
- updated from git

* Tue Apr 23 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130423-alt1
- updated from git
- added prov/obs firmware-carl9170-1.9.4 firmware-i2400m firmware-rt2870
  firmware-rt3090 (closes #27624)

* Fri Mar 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130313-alt2
- sources exluded (closes: #28682)

* Wed Mar 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130313-alt1
- updated from git

* Wed Jan 09 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130109-alt1
- updated from git

* Wed Sep 05 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20120905-alt1
- updated from git

* Wed Apr 04 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20120304-alt1
- updated from g.k.o/pub/scm/linux/kernel/git/firmware/linux-firmware.git

* Wed Dec 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20111228-alt1
- updated from git

* Fri Aug 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110819-alt1
- updated from git

* Tue Jul 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110726-alt1
- updated from git

* Fri May 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110520-alt3
- requires for firmware-ipw* added

* Thu May 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110520-alt2
- false ipw* provedes/obsoletes deleted (closes #25669)

* Fri May 20 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110520-alt1
- updated from git
- iwl* included and provided/obsoleted

* Thu Mar 31 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110331-alt1
- updated from git

* Fri Jan 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110114-alt1
- updated from git

* Fri Dec 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101217-alt1
- updated from git

* Fri Sep 24 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20100924-alt1
- updated from git

* Tue Jun 29 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20100629-alt1
- updated from git
- provides of linux-firmware added

* Fri May 21 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20100521-alt1
- build to Sisyphus
- updated from git
- radeon and nouveau added to tree directly

* Mon Apr 12 2010 Michael Shigorin <mike@altlinux.org> 20100106-alt1
- adapted fedora spec for ALT Linux (thanks lakostis@ for proposal)

* Fri Apr 09 2010 Dave Airlie <airlied@redhat.com> 20100106-4
- Add further radeon firmwares

* Wed Feb 10 2010 Dave Airlie <airlied@redhat.com> 20100106-3
- add radeon RLC firmware - submitted upstream to dwmw2 already.

* Tue Feb 09 2010 Ben Skeggs <bskeggs@redhat.com> 20090106-2
- Add firmware needed for nouveau to operate correctly (this is Fedora
  only - do not upstream yet - we just moved it here from Fedora kernel)

* Wed Jan 06 2010 David Woodhouse <David.Woodhouse@intel.com> 20090106-1
- Update

* Fri Aug 21 2009 David Woodhouse <David.Woodhouse@intel.com> 20090821-1
- Update, fix typos, remove some files which conflict with other packages.

* Thu Mar 19 2009 David Woodhouse <David.Woodhouse@intel.com> 20090319-1
- First standalone kernel-firmware package.
