%define orig_name intel-microcode
%define orig_timestamp 20191115
%define orig_rev .2

Name: firmware-intel-ucode
Version: 12
Release: alt1.%{orig_timestamp}%{?orig_rev}
Epoch: 2

Packager: L.A. Kostis <lakostis@altlinux.org>

Summary: Microcode definitions for Intel processors
License: INTEL SOFTWARE LICENSE AGREEMENT
Group: System/Kernel and hardware
Provides: microcode-data-intel = %version-%release
Obsoletes: microcode-data-intel <= 20130222-alt2

URL: https://salsa.debian.org/hmh/intel-microcode.git
Source0: %{orig_name}-%{orig_timestamp}%{?orig_rev}.tar

BuildRequires: iucode_tool

# beware that this probably should be ix86
# but who cares about intel on ARM?
BuildArch: noarch
ExclusiveArch: %ix86 x86_64

%description
The microcode data file for Linux contains the latest microcode
definitions for all Intel processors.

%prep
%setup -q -n %orig_name-%{orig_timestamp}%{?orig_rev}

%build
%make_build

%install
mkdir -p %buildroot/lib/firmware/intel-ucode
UCODE=intel-microcode
%ifarch %ix86
# use stripped down version for x86_64 and ia32
UCODE=${UCODE}-64
%endif
mv ${UCODE}.bin %buildroot/lib/firmware/intel-ucode/%{orig_name}.bin

%files
%doc changelog releasenote
%dir /lib/firmware/intel-ucode
/lib/firmware/intel-ucode/*

%changelog
* Mon Jan 20 2020 L.A. Kostis <lakostis@altlinux.ru> 2:12-alt1.20191115.2
- Sync with Debian 3.20191115.2:
  + New upstream microcode datafile 20191115
  + Microcode rollbacks (closes: debian #946515, LP#1854764):
    sig 0x00050654, pf_mask 0xb7, 2019-07-31, rev 0x2000064, size 33792
  + Avoids hangs on warm reboots (cold boots work fine) on HEDT and
    Xeon processors with signature 0x50654.
    https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/issues/21
  + Updated Microcodes:
    sig 0x000406e3, pf_mask 0xc0, 2019-10-03, rev 0x00d6, size 101376
    sig 0x000506e3, pf_mask 0x36, 2019-10-03, rev 0x00d6, size 101376
    sig 0x000806e9, pf_mask 0x10, 2019-10-15, rev 0x00ca, size 100352
    sig 0x000806e9, pf_mask 0xc0, 2019-09-26, rev 0x00ca, size 100352
    sig 0x000806ea, pf_mask 0xc0, 2019-10-03, rev 0x00ca, size 100352
    sig 0x000806eb, pf_mask 0xd0, 2019-10-03, rev 0x00ca, size 100352
    sig 0x000806ec, pf_mask 0x94, 2019-10-03, rev 0x00ca, size 100352
    sig 0x000906e9, pf_mask 0x2a, 2019-10-03, rev 0x00ca, size 100352
    sig 0x000906ea, pf_mask 0x22, 2019-10-03, rev 0x00ca, size 99328
    sig 0x000906eb, pf_mask 0x02, 2019-10-03, rev 0x00ca, size 100352
    sig 0x000906ec, pf_mask 0x22, 2019-10-03, rev 0x00ca, size 99328
    sig 0x000906ed, pf_mask 0x22, 2019-10-03, rev 0x00ca, size 100352
    sig 0x000a0660, pf_mask 0x80, 2019-10-03, rev 0x00ca, size 91136

* Mon Oct 07 2019 L.A. Kostis <lakostis@altlinux.ru> 2:11-alt1.20190918
- Sync with Debian 3.20190918.1:
  + New upstream microcode datafile 20190918
  + SECURITY UPDATE
    *Might* contain mitigations for INTEL-SA-00247 (RAMBleed), given
    the set of processors being updated.
  + Updated Microcodes:
    sig 0x000306d4, pf_mask 0xc0, 2019-06-13, rev 0x002e, size 19456
    sig 0x000306f4, pf_mask 0x80, 2019-06-17, rev 0x0016, size 18432
    sig 0x00040671, pf_mask 0x22, 2019-06-13, rev 0x0021, size 14336
    sig 0x000406f1, pf_mask 0xef, 2019-06-18, rev 0xb000038, size 30720
    sig 0x00050654, pf_mask 0xb7, 2019-07-31, rev 0x2000064, size 33792
    sig 0x00050657, pf_mask 0xbf, 2019-08-12, rev 0x500002b, size 51200
    sig 0x00050662, pf_mask 0x10, 2019-06-17, rev 0x001c, size 32768
    sig 0x00050663, pf_mask 0x10, 2019-06-17, rev 0x7000019, size 24576
    sig 0x00050664, pf_mask 0x10, 2019-06-17, rev 0xf000017, size 24576
    sig 0x00050665, pf_mask 0x10, 2019-06-17, rev 0xe00000f, size 19456

* Mon Sep 09 2019 L.A. Kostis <lakostis@altlinux.ru> 2:10-alt1.20190618.1
- Sync with Debian 3.20190618.1:
  + New upstream microcode datafile 20190618
  + SECURITY UPDATE
    Implements MDS mitigation (RIDL, Fallout, Zombieload), INTEL-SA-00223
    CVE-2018-12126, CVE-2018-12127, CVE-2018-12130, CVE-2019-11091
    for Sandybridge server and Core-X processors
  + Updated Microcodes:
    sig 0x000206d6, pf_mask 0x6d, 2019-05-21, rev 0x061f, size 18432
    sig 0x000206d7, pf_mask 0x6d, 2019-05-21, rev 0x0718, size 19456

* Mon May 20 2019 L.A. Kostis <lakostis@altlinux.ru> 2:9-alt1.20190514
- Sync with Debian 3.20190514.1:
  + New upstream microcode datafile 20190514
  + SECURITY UPDATE
    Implements MDS mitigation (RIDL, Fallout, Zombieload), INTEL-SA-00223
    CVE-2018-12126, CVE-2018-12127, CVE-2018-12130, CVE-2019-11091
  + New Microcodes:
    sig 0x00030678, pf_mask 0x02, 2019-04-22, rev 0x0838, size 52224
    sig 0x00030678, pf_mask 0x0c, 2019-04-22, rev 0x0838, size 52224
    sig 0x00030679, pf_mask 0x0f, 2019-04-23, rev 0x090c, size 52224
    sig 0x000406c3, pf_mask 0x01, 2019-04-23, rev 0x0368, size 69632
    sig 0x000406c4, pf_mask 0x01, 2019-04-23, rev 0x0411, size 68608
    sig 0x00050657, pf_mask 0xbf, 2019-02-27, rev 0x5000021, size 47104
  + Updated Microcodes:
    sig 0x000206a7, pf_mask 0x12, 2019-02-17, rev 0x002f, size 12288
    sig 0x000306a9, pf_mask 0x12, 2019-02-13, rev 0x0021, size 14336
    sig 0x000306c3, pf_mask 0x32, 2019-02-26, rev 0x0027, size 23552
    sig 0x000306d4, pf_mask 0xc0, 2019-03-07, rev 0x002d, size 19456
    sig 0x000306e4, pf_mask 0xed, 2019-03-14, rev 0x042e, size 16384
    sig 0x000306e7, pf_mask 0xed, 2019-03-14, rev 0x0715, size 17408
    sig 0x000306f2, pf_mask 0x6f, 2019-03-01, rev 0x0043, size 34816
    sig 0x000306f4, pf_mask 0x80, 2019-03-01, rev 0x0014, size 18432
    sig 0x00040651, pf_mask 0x72, 2019-02-26, rev 0x0025, size 21504
    sig 0x00040661, pf_mask 0x32, 2019-02-26, rev 0x001b, size 25600
    sig 0x00040671, pf_mask 0x22, 2019-03-07, rev 0x0020, size 14336
    sig 0x000406e3, pf_mask 0xc0, 2019-04-01, rev 0x00cc, size 100352
    sig 0x000406f1, pf_mask 0xef, 2019-03-02, rev 0xb000036, size 30720
    sig 0x00050654, pf_mask 0xb7, 2019-04-02, rev 0x200005e, size 32768
    sig 0x00050662, pf_mask 0x10, 2019-03-23, rev 0x001a, size 32768
    sig 0x00050663, pf_mask 0x10, 2019-03-23, rev 0x7000017, size 24576
    sig 0x00050664, pf_mask 0x10, 2019-03-23, rev 0xf000015, size 23552
    sig 0x00050665, pf_mask 0x10, 2019-03-23, rev 0xe00000d, size 19456
    sig 0x000506c9, pf_mask 0x03, 2019-01-15, rev 0x0038, size 17408
    sig 0x000506ca, pf_mask 0x03, 2019-03-01, rev 0x0016, size 15360
    sig 0x000506e3, pf_mask 0x36, 2019-04-01, rev 0x00cc, size 100352
    sig 0x000506f1, pf_mask 0x01, 2019-03-21, rev 0x002e, size 11264
    sig 0x000706a1, pf_mask 0x01, 2019-01-02, rev 0x002e, size 73728
    sig 0x000806e9, pf_mask 0x10, 2019-04-01, rev 0x00b4, size 98304
    sig 0x000806e9, pf_mask 0xc0, 2019-04-01, rev 0x00b4, size 99328
    sig 0x000806ea, pf_mask 0xc0, 2019-04-01, rev 0x00b4, size 99328
    sig 0x000806eb, pf_mask 0xd0, 2019-03-30, rev 0x00b8, size 98304
    sig 0x000806ec, pf_mask 0x94, 2019-03-30, rev 0x00b8, size 97280
    sig 0x000906e9, pf_mask 0x2a, 2019-04-01, rev 0x00b4, size 99328
    sig 0x000906ea, pf_mask 0x22, 2019-04-01, rev 0x00b4, size 98304
    sig 0x000906eb, pf_mask 0x02, 2019-04-01, rev 0x00b4, size 99328
    sig 0x000906ec, pf_mask 0x22, 2019-02-14, rev 0x00ae, size 98304
    sig 0x000906ed, pf_mask 0x22, 2019-03-17, rev 0x00b8, size 97280

* Thu Apr 11 2019 L.A. Kostis <lakostis@altlinux.ru> 2:8-alt1.20190312
- Sync with Debian 3.20190312.1:
  + Removed Microcodes:
    sig 0x00050653, pf_mask 0x97, 2018-01-29, rev 0x1000140, size 30720
  + New Microcodes:
    sig 0x000806e9, pf_mask 0x10, 2018-10-18, rev 0x009e, size 98304
    sig 0x000806eb, pf_mask 0xd0, 2018-10-25, rev 0x00a4, size 99328
    sig 0x000806ec, pf_mask 0x94, 2019-02-12, rev 0x00b2, size 98304
    sig 0x000906ec, pf_mask 0x22, 2018-09-29, rev 0x00a2, size 98304
    sig 0x000906ed, pf_mask 0x22, 2019-02-04, rev 0x00b0, size 97280
  + Updated Microcodes:
    sig 0x000306f2, pf_mask 0x6f, 2018-11-20, rev 0x0041, size 34816
    sig 0x000306f4, pf_mask 0x80, 2018-11-06, rev 0x0013, size 17408
    sig 0x00050654, pf_mask 0xb7, 2019-01-28, rev 0x200005a, size 33792
    sig 0x00050662, pf_mask 0x10, 2018-12-06, rev 0x0019, size 32768
    sig 0x00050663, pf_mask 0x10, 2018-12-06, rev 0x7000016, size 23552
    sig 0x00050664, pf_mask 0x10, 2018-11-17, rev 0xf000014, size 23552
    sig 0x00050665, pf_mask 0x10, 2018-11-17, rev 0xe00000c, size 19456
    sig 0x000506c9, pf_mask 0x03, 2018-09-14, rev 0x0036, size 17408
    sig 0x000506ca, pf_mask 0x03, 2018-09-20, rev 0x0010, size 15360
    sig 0x000706a1, pf_mask 0x01, 2018-09-21, rev 0x002c, size 73728
    sig 0x000806e9, pf_mask 0xc0, 2018-07-16, rev 0x009a, size 98304
    sig 0x000806ea, pf_mask 0xc0, 2018-10-18, rev 0x009e, size 98304
    sig 0x000906e9, pf_mask 0x2a, 2018-07-16, rev 0x009a, size 98304
    sig 0x000906ea, pf_mask 0x22, 2018-12-12, rev 0x00aa, size 98304
    sig 0x000906eb, pf_mask 0x02, 2018-12-12, rev 0x00aa, size 99328

* Thu Aug 30 2018 L.A. Kostis <lakostis@altlinux.ru> 2:7-alt2.20180807.a
- Update url.

* Thu Aug 30 2018 L.A. Kostis <lakostis@altlinux.ru> 2:7-alt1.20180807.a
- Sync with Debian 3.20180807a1:
  + New Microcodes:
    sig 0x000206c2, pf_mask 0x03, 2018-05-08, rev 0x001f, size 11264
    sig 0x000206e6, pf_mask 0x04, 2018-05-15, rev 0x000d, size 9216
    sig 0x000506c2, pf_mask 0x01, 2018-05-11, rev 0x0014, size 15360
    sig 0x000506ca, pf_mask 0x03, 2018-05-11, rev 0x000c, size 14336
    sig 0x000506f1, pf_mask 0x01, 2018-05-11, rev 0x0024, size 10240
  + Updated Microcodes:
    sig 0x000106a5, pf_mask 0x03, 2018-05-11, rev 0x001d, size 12288
    sig 0x000106e5, pf_mask 0x13, 2018-05-08, rev 0x000a, size 9216
    sig 0x00020652, pf_mask 0x12, 2018-05-08, rev 0x0011, size 9216
    sig 0x00020655, pf_mask 0x92, 2018-04-23, rev 0x0007, size 4096
    sig 0x000206a7, pf_mask 0x12, 2018-04-10, rev 0x002e, size 12288
    sig 0x000206f2, pf_mask 0x05, 2018-05-16, rev 0x003b, size 14336
    sig 0x000306a9, pf_mask 0x12, 2018-04-10, rev 0x0020, size 13312
    sig 0x000306c3, pf_mask 0x32, 2018-04-02, rev 0x0025, size 23552
    sig 0x000306d4, pf_mask 0xc0, 2018-03-22, rev 0x002b, size 18432
    sig 0x00040651, pf_mask 0x72, 2018-04-02, rev 0x0024, size 22528
    sig 0x00040661, pf_mask 0x32, 2018-04-02, rev 0x001a, size 25600
    sig 0x00040671, pf_mask 0x22, 2018-04-03, rev 0x001e, size 13312
    sig 0x000406e3, pf_mask 0xc0, 2018-04-17, rev 0x00c6, size 99328
    sig 0x00050662, pf_mask 0x10, 2018-05-25, rev 0x0017, size 31744
    sig 0x00050663, pf_mask 0x10, 2018-04-20, rev 0x7000013, size 22528
    sig 0x00050664, pf_mask 0x10, 2018-04-20, rev 0xf000012, size 22528
    sig 0x000506c9, pf_mask 0x03, 2018-05-11, rev 0x0032, size 16384
    sig 0x000506e3, pf_mask 0x36, 2018-04-17, rev 0x00c6, size 99328
    sig 0x000706a1, pf_mask 0x01, 2018-05-22, rev 0x0028, size 73728
    sig 0x000806e9, pf_mask 0xc0, 2018-03-24, rev 0x008e, size 98304
    sig 0x000806ea, pf_mask 0xc0, 2018-05-15, rev 0x0096, size 98304
    sig 0x000906e9, pf_mask 0x2a, 2018-03-24, rev 0x008e, size 98304
    sig 0x000906ea, pf_mask 0x22, 2018-05-02, rev 0x0096, size 97280
    sig 0x000906eb, pf_mask 0x02, 2018-03-24, rev 0x008e, size 98304
  + Implements L1D_FLUSH support (L1TF "Foreshadow/-NG" mitigation)
    Intel SA-00161, CVE-2018-3615, CVE-2018-3620, CVE-2018-3646
  + Implements SSBD support (Spectre v4 mitigation),
    Disable speculation for (some) RDMSR/WRMSR (Spectre v3a fix)
    Intel SA-00115, CVE-2018-3639, CVE-2018-3640
  + Implements IBRS/IBPB/STIPB support, Spectre v2 mitigation for older
    processors with signatures 0x106a5, 0x106e5, 0x20652, 0x20655.
    Intel SA-0088, CVE-2017-5753, CVE-2017-5754
  - source: update symlinks to reflect id of the latest release, 20180807a

* Mon Aug 06 2018 L.A. Kostis <lakostis@altlinux.ru> 2:6-alt1.20180703
- Sync with Debian 3.20180703.2:
  + Updated Microcodes:
      sig 0x000206d6, pf_mask 0x6d, 2018-05-08, rev 0x061d, size 18432
      sig 0x000206d7, pf_mask 0x6d, 2018-05-08, rev 0x0714, size 19456
      sig 0x000306e4, pf_mask 0xed, 2018-04-25, rev 0x042d, size 15360
      sig 0x000306e7, pf_mask 0xed, 2018-04-25, rev 0x0714, size 17408
      sig 0x000306f2, pf_mask 0x6f, 2018-04-20, rev 0x003d, size 33792
      sig 0x000306f4, pf_mask 0x80, 2018-04-20, rev 0x0012, size 17408
      sig 0x000406f1, pf_mask 0xef, 2018-04-19, rev 0xb00002e, size 28672
      sig 0x00050654, pf_mask 0xb7, 2018-05-15, rev 0x200004d, size 31744
      sig 0x00050665, pf_mask 0x10, 2018-04-20, rev 0xe00000a, size 18432
  + First batch of fixes for: Intel SA-00115, CVE-2018-3639, CVE-2018-3640
  + SSBD support (Spectre-v4 mitigation) and fix Spectre-v3a for:
      Sandybridge server, Ivy Bridge server, Haswell server, Skylake server,
      Broadwell server, a few HEDT Core i7/i9 models that are actually gimped
      server dies.
  - source: update symlinks to reflect id of the latest release, 20180703

* Mon Jun 18 2018 L.A. Kostis <lakostis@altlinux.ru> 2:5-alt2.20180425
- Make package %%ix86/x86_64 only.

* Mon Jun 18 2018 L.A. Kostis <lakostis@altlinux.ru> 2:5-alt1.20180425
- Update 20180425 (debian changelog below):
  + Updated Microcodes:
    sig 0x000406f1, pf_mask 0xef, 2018-03-21, rev 0xb00002c, size 27648
    sig 0x000706a1, pf_mask 0x01, 2017-12-26, rev 0x0022, size 73728
  + Implements IBRS/IBPB/STIPB support, Spectre-v2 mitigation
  - source: remove undesired list files from microcode directories
  - source: switch to microcode-<id>.d/ since Intel dropped .dat
    support.

* Tue Mar 20 2018 L.A. Kostis <lakostis@altlinux.ru> 2:4-alt1.20180312
- Update to 20180312.
  + New Microcodes:
    sig 0x00050653, pf_mask 0x97, 2018-01-29, rev 0x1000140, size 30720
    sig 0x00050665, pf_mask 0x10, 2018-01-22, rev 0xe000009, size 18432
  + Updated Microcodes:
    sig 0x000206a7, pf_mask 0x12, 2018-02-07, rev 0x002d, size 12288
    sig 0x000206d6, pf_mask 0x6d, 2018-01-30, rev 0x061c, size 18432
    sig 0x000206d7, pf_mask 0x6d, 2018-01-26, rev 0x0713, size 19456
    sig 0x000306a9, pf_mask 0x12, 2018-02-07, rev 0x001f, size 13312
    sig 0x000306c3, pf_mask 0x32, 2018-01-21, rev 0x0024, size 23552
    sig 0x000306d4, pf_mask 0xc0, 2018-01-18, rev 0x002a, size 18432
    sig 0x000306e4, pf_mask 0xed, 2018-01-25, rev 0x042c, size 15360
    sig 0x000306e7, pf_mask 0xed, 2018-02-16, rev 0x0713, size 16384
    sig 0x000306f2, pf_mask 0x6f, 2018-01-19, rev 0x003c, size 33792
    sig 0x000306f4, pf_mask 0x80, 2018-01-22, rev 0x0011, size 17408
    sig 0x00040651, pf_mask 0x72, 2018-01-18, rev 0x0023, size 21504
    sig 0x00040661, pf_mask 0x32, 2018-01-21, rev 0x0019, size 25600
    sig 0x00040671, pf_mask 0x22, 2018-01-21, rev 0x001d, size 12288
    sig 0x000406e3, pf_mask 0xc0, 2017-11-16, rev 0x00c2, size 99328
    sig 0x00050654, pf_mask 0xb7, 2018-01-26, rev 0x2000043, size 28672
    sig 0x00050662, pf_mask 0x10, 2018-01-22, rev 0x0015, size 31744
    sig 0x00050663, pf_mask 0x10, 2018-01-22, rev 0x7000012, size 22528
    sig 0x00050664, pf_mask 0x10, 2018-01-22, rev 0xf000011, size 22528
    sig 0x000506c9, pf_mask 0x03, 2017-03-25, rev 0x002c, size 16384
    sig 0x000506e3, pf_mask 0x36, 2017-11-16, rev 0x00c2, size 99328
    sig 0x000706a1, pf_mask 0x01, 2017-10-31, rev 0x001e, size 72704
    sig 0x000806e9, pf_mask 0xc0, 2018-01-21, rev 0x0084, size 98304
    sig 0x000806ea, pf_mask 0xc0, 2018-01-21, rev 0x0084, size 97280
    sig 0x000906e9, pf_mask 0x2a, 2018-01-21, rev 0x0084, size 98304
    sig 0x000906ea, pf_mask 0x22, 2018-01-21, rev 0x0084, size 96256
    sig 0x000906eb, pf_mask 0x02, 2018-01-21, rev 0x0084, size 98304

* Thu Feb 08 2018 Konstantin A. Lepikhov <lakostis@altlinux.ru> 2:3-alt3.20171117
- Rollback microcode files back to 20171117 (debian changelog below):
  + Revert to release 20171117, as per Intel instructions issued to
    the public in 2018-01-22 (closes: #886998)
  + This effectively removes IBRS/IBPB/STIPB microcode support for
    Spectre variant 2 mitigation.

* Wed Jan 10 2018 L.A. Kostis <lakostis@altlinux.ru> 2:3-alt2.20180108
- bump epoch (again) and restore old versioning.
- removed external microcode files:
  + sig 0x000306f2, pf_mask 0x6f, 2017-11-17, rev 0x003b (merged)
  + sig 0x000406f1, pf_mask 0xef, 2017-11-18, rev 0xb000025 (downgraded)
  + sig 0x00050654, pf_mask 0xb7, 2017-11-21, rev 0x200003a (obsoleted).

* Wed Jan 10 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:3.20180108-alt1
- Update to 20180108 (adapted debian changelog is below):
  * New upstream microcode data file 20180108
    + Updated Microcodes:
      sig 0x000306c3, pf_mask 0x32, 2017-11-20, rev 0x0023, size 23552
      sig 0x000306d4, pf_mask 0xc0, 2017-11-17, rev 0x0028, size 18432
      sig 0x000306e4, pf_mask 0xed, 2017-12-01, rev 0x042a, size 15360
      sig 0x000306f2, pf_mask 0x6f, 2017-11-17, rev 0x003b, size 33792
      sig 0x000306f4, pf_mask 0x80, 2017-11-17, rev 0x0010, size 17408
      sig 0x00040651, pf_mask 0x72, 2017-11-20, rev 0x0021, size 22528
      sig 0x00040661, pf_mask 0x32, 2017-11-20, rev 0x0018, size 25600
      sig 0x00040671, pf_mask 0x22, 2017-11-17, rev 0x001b, size 13312
      sig 0x000406e3, pf_mask 0xc0, 2017-11-16, rev 0x00c2, size 99328
      sig 0x00050654, pf_mask 0xb7, 2017-12-08, rev 0x200003c, size 27648
      sig 0x00050662, pf_mask 0x10, 2017-12-16, rev 0x0014, size 31744
      sig 0x00050663, pf_mask 0x10, 2017-12-16, rev 0x7000011, size 22528
      sig 0x000506e3, pf_mask 0x36, 2017-11-16, rev 0x00c2, size 99328
      sig 0x000706a1, pf_mask 0x01, 2017-12-26, rev 0x0022, size 73728
      sig 0x000806e9, pf_mask 0xc0, 2018-01-04, rev 0x0080, size 98304
      sig 0x000806ea, pf_mask 0xc0, 2018-01-04, rev 0x0080, size 98304
      sig 0x000906e9, pf_mask 0x2a, 2018-01-04, rev 0x0080, size 98304
      sig 0x000906ea, pf_mask 0x22, 2018-01-04, rev 0x0080, size 97280
      sig 0x000906eb, pf_mask 0x02, 2018-01-04, rev 0x0080, size 98304
    + Implements IBRS/IBPB support and enhances LFENCE: mitigation
      against Spectre (fixes CVE-2017-5715)
    + Very likely fixes several other errata on some of the processors
  * supplementary-ucode-CVE-2017-5715.d/: remove.
    + Downgraded microcodes:
      sig 0x000406f1, pf_mask 0xef, 2017-03-01, rev 0xb000021, size 26624
      sig 0x000506c9, pf_mask 0x03, 2017-03-25, rev 0x002c, size 16384
    + This removes IBRS/IBPB support for these two platforms when compared
      with the previous (and unofficial) release, 20171215.  We don't know
      why Intel declined to include these microcode updates (as well as
      several others) in the release.
  * source: remove superseded upstream data file: 20171117

* Thu Jan 04 2018 L.A. Kostis <lakostis@altlinux.ru> 1:3-alt1.20171121
- Added new CPU microcodes (microcode counterpart of the CVE-2017-5715
  kernel mitigation):
  + sig 0x000306f2, pf_mask 0x6f, 2017-11-17, rev 0x003b, size 33792
  + sig 0x000406f1, pf_mask 0xef, 2017-11-18, rev 0xb000025, size 27648
  + sig 0x00050654, pf_mask 0xb7, 2017-11-21, rev 0x200003a, size 27648

* Fri Nov 24 2017 L.A. Kostis <lakostis@altlinux.ru> 1:3-alt0.20171117.1
- Update to 20171117.1 (debian changelog below):
  * New upstream microcode data file 20171117
    + New Microcodes:
      sig 0x000506c9, pf_mask 0x03, 2017-03-25, rev 0x002c, size 16384
      sig 0x000706a1, pf_mask 0x01, 2017-10-31, rev 0x001e, size 72704
      sig 0x000906ea, pf_mask 0x22, 2017-08-23, rev 0x0070, size 95232
      sig 0x000906eb, pf_mask 0x02, 2017-09-20, rev 0x0072, size 97280
    + Updated Microcodes:
      sig 0x00050654, pf_mask 0xb7, 2017-10-17, rev 0x2000035, size 26624
      sig 0x000806ea, pf_mask 0xc0, 2017-08-03, rev 0x0070, size 96256
  * source: remove superseded upstream data file: 20170707.
  * source: remove unneeded intel-ucode/ directory for 20171117.
- TODO: we need to implement ucode blacklisting as well as debian does.


* Mon Sep 04 2017 L.A. Kostis <lakostis@altlinux.ru> 1:3-alt0.20170707.1
- Rebased to Debian package (because Fedora version is outdated):
  * New upstream microcode datafile 20170707
    + New Microcodes:
      sig 0x00050654, pf_mask 0x97, 2017-06-01, rev 0x2000022, size 25600
      sig 0x000806e9, pf_mask 0xc0, 2017-04-27, rev 0x0062, size 97280
      sig 0x000806ea, pf_mask 0xc0, 2017-05-23, rev 0x0066, size 95232
      sig 0x000906e9, pf_mask 0x2a, 2017-04-06, rev 0x005e, size 97280
    + This release fixes the nightmare-level errata SKZ7/SKW144/SKL150/
      SKX150 (Skylake) KBL095/KBW095 (Kaby Lake) for all affected Kaby
      Lake and Skylake processors: Skylake D0/R0 were fixed since the
      previous upstream release (20170511).  This new release adds the
      fixes for Kaby Lake Y0/B0/H0 and Skylake H0 (Skylake-E/X).
    + Fix undisclosed errata in Skylake H0 (0x50654), Kaby Lake Y0
      (0x806ea), Kaby Lake H0 (0x806e9), Kaby Lake B0 (0x906e9)
  * source: remove unneeded intel-ucode/ directory
  * source: remove superseded upstream data file: 20170511

* Thu Dec 08 2016 L.A. Kostis <lakostis@altlinux.ru> 1:2.1-alt0.3
- Updated to 2.1-11 version:
  + Intel CPU microcode 20161104 update.

* Wed Jun 08 2016 L.A. Kostis <lakostis@altlinux.ru> 1:2.1-alt0.2
- Updated to 2.1-8 version:
  + Intel CPU microcode 20151106 update.

* Mon Aug 12 2013 L.A. Kostis <lakostis@altlinux.ru> 1:2.1-alt0.1
- 2.1.
- remove amd-ucode (now part of linux-firmware).

* Mon Apr 08 2013 L.A. Kostis <lakostis@altlinux.ru> 1:2.0-alt0.2
- Get rid of versioning mess.

* Mon Apr 08 2013 L.A. Kostis <lakostis@altlinux.ru> 2.0-alt0.1
- 2.0 release from fedora.
- it's just a helper for seamless in-kernel firmware management.
- combine separate firmware files.

* Tue Nov 09 2010 Victor Forsiuk <force@altlinux.org> 1.17-alt2
- Package only utility. Microcode data will be in separate packages.
- Move utility from %_sbindir to /sbin.
- Use /lib/microcode for microcode data instead of /etc.

* Wed May 02 2007 Victor Forsyuk <force@altlinux.org> 1.17-alt1
- 1.17

* Mon Apr 02 2007 Victor Forsyuk <force@altlinux.org> 1.16-alt2
- Comment ExclusiveArch for now.

* Tue Mar 27 2007 Victor Forsyuk <force@altlinux.org> 1.16-alt1
- 1.16

* Mon Nov 13 2006 Denis Smirnov <mithraen@altlinux.ru> 1.14-alt1
- Update to 1.14

* Mon Dec 12 2005 Victor Forsyuk <force@altlinux.ru> 1.12-alt2
- Shift service start priority to run after udev is up.
- Remove microcode kernel module after microcode uploading.

* Wed Oct 19 2005 Victor Forsyuk <force@altlinux.ru> 1.12-alt1
- Initial build.
