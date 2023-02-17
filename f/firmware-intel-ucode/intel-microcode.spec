%define orig_name intel-microcode
%define orig_timestamp 20230214
%define orig_rev %nil

Name: firmware-intel-ucode
Version: 20
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
%doc license changelog releasenote.md security.md
%dir /lib/firmware/intel-ucode
/lib/firmware/intel-ucode/*

%changelog
* Fri Feb 17 2023 L.A. Kostis <lakostis@altlinux.ru> 2:20-alt1.20230214
- Updated to upstream microcode datafile 20230214:
  + Security updates for INTEL-SA-00767 INTEL-SA-00738 INTEL-SA-00700
  + Added new microcode for Xeon Scalable Gen4, Xeon Max and Core Gen13
    processors.
  + Updated firmware for Xeon Scalable Gen1/Gen2/Gen3, Xeon D-17xx/D-27xx
    Core Gen10 Mobile/Gen11/Gen12/Gen13/w/Hybrid Technology, Pentium
    and Celeron processors.
  + New Microcodes:
    sig 0x000806f8, pf_mask 0x87, 2022-12-27, rev 0x2b000181, size 561152
    sig 0x000806f7, pf_mask 0x87, 2022-12-27, rev 0x2b000181
    sig 0x000806f6, pf_mask 0x87, 2022-12-27, rev 0x2b000181
    sig 0x000806f5, pf_mask 0x87, 2022-12-27, rev 0x2b000181
    sig 0x000806f4, pf_mask 0x87, 2022-12-27, rev 0x2b000181
    sig 0x000806f8, pf_mask 0x10, 2022-12-19, rev 0x2c000170, size 600064
    sig 0x000806f6, pf_mask 0x10, 2022-12-19, rev 0x2c000170
    sig 0x000806f5, pf_mask 0x10, 2022-12-19, rev 0x2c000170
    sig 0x000806f4, pf_mask 0x10, 2022-12-19, rev 0x2c000170
    sig 0x000b06a2, pf_mask 0xc0, 2022-12-08, rev 0x410e, size 212992
    sig 0x000b06a3, pf_mask 0xc0, 2022-12-08, rev 0x410e
  + Updated Microcodes:
    sig 0x00050653, pf_mask 0x97, 2022-08-30, rev 0x1000161, size 36864
    sig 0x00050656, pf_mask 0xbf, 2022-08-26, rev 0x4003303, size 37888
    sig 0x00050657, pf_mask 0xbf, 2022-08-26, rev 0x5003303, size 37888
    sig 0x0005065b, pf_mask 0xbf, 2022-08-26, rev 0x7002503, size 29696
    sig 0x000606a6, pf_mask 0x87, 2022-10-09, rev 0xd000389, size 296960
    sig 0x000606c1, pf_mask 0x10, 2022-09-23, rev 0x1000211, size 289792
    sig 0x000706a1, pf_mask 0x01, 2022-09-16, rev 0x003e, size 75776
    sig 0x000706a8, pf_mask 0x01, 2022-09-20, rev 0x0022, size 76800
    sig 0x000706e5, pf_mask 0x80, 2022-08-31, rev 0x00b8, size 113664
    sig 0x000806a1, pf_mask 0x10, 2022-09-07, rev 0x0032, size 34816
    sig 0x00090672, pf_mask 0x07, 2023-01-04, rev 0x002c, size 219136
    sig 0x00090675, pf_mask 0x07, 2023-01-04, rev 0x002c
    sig 0x000b06f2, pf_mask 0x07, 2023-01-04, rev 0x002c
    sig 0x000b06f5, pf_mask 0x07, 2023-01-04, rev 0x002c
    sig 0x000906a3, pf_mask 0x80, 2023-01-11, rev 0x0429, size 218112
    sig 0x000906a4, pf_mask 0x80, 2023-01-11, rev 0x0429
    sig 0x000906c0, pf_mask 0x01, 2022-09-02, rev 0x24000024, size 20480
    sig 0x000a0671, pf_mask 0x02, 2022-08-31, rev 0x0057, size 103424
    sig 0x000b0671, pf_mask 0x32, 2022-12-19, rev 0x0112, size 207872

* Thu Dec 01 2022 L.A. Kostis <lakostis@altlinux.ru> 2:19-alt1.20221108
- Updated to upstream microcode datafile 20221108:
  + Fixes several errata (functional issues) on Xeon D-2700, 8th, 9th, 10th,
    11th and 12th generations Core processors.
  + Added new microcode for Xeon D-17xx, D-27xx and Core Gen13 processors.
  + New Microcodes:
    sig 0x000606c1, pf_mask 0x10, 2022-08-07, rev 0x1000201, size 286720
    sig 0x000b0671, pf_mask 0x32, 2022-09-07, rev 0x010e, size 204800
  + Updated Microcodes:
    sig 0x00050653, pf_mask 0x97, 2022-03-14, rev 0x100015e, size 34816
    sig 0x00050654, pf_mask 0xb7, 2022-03-08, rev 0x2006e05, size 44032
    sig 0x000606a6, pf_mask 0x87, 2022-04-07, rev 0xd000375, size 293888
    sig 0x000706a1, pf_mask 0x01, 2022-03-23, rev 0x003c, size 75776
    sig 0x000706a8, pf_mask 0x01, 2022-03-23, rev 0x0020, size 75776
    sig 0x000706e5, pf_mask 0x80, 2022-08-02, rev 0x00b6, size 113664
    sig 0x000806a1, pf_mask 0x10, 2022-03-26, rev 0x0031, size 34816
    sig 0x000806c1, pf_mask 0x80, 2022-06-28, rev 0x00a6, size 110592
    sig 0x000806c2, pf_mask 0xc2, 2022-03-19, rev 0x0028, size 97280
    sig 0x000806d1, pf_mask 0xc2, 2022-06-28, rev 0x0042, size 102400
    sig 0x000806ec, pf_mask 0x94, 2022-07-31, rev 0x00f4, size 105472
    sig 0x00090661, pf_mask 0x01, 2022-07-15, rev 0x0017, size 20480
    sig 0x00090672, pf_mask 0x07, 2022-09-19, rev 0x0026, size 218112
    sig 0x00090675, pf_mask 0x07, 2022-09-19, rev 0x0026, size 218112
    sig 0x000b06f2, pf_mask 0x07, 2022-09-19, rev 0x0026, size 218112
    sig 0x000b06f5, pf_mask 0x07, 2022-09-19, rev 0x0026, size 218112
    sig 0x000906a3, pf_mask 0x80, 2022-09-19, rev 0x0424, size 217088
    sig 0x000906a4, pf_mask 0x80, 2022-09-19, rev 0x0424, size 217088
    sig 0x000906ed, pf_mask 0x22, 2022-07-31, rev 0x00f4, size 104448
    sig 0x000a0652, pf_mask 0x20, 2022-07-31, rev 0x00f4, size 96256
    sig 0x000a0653, pf_mask 0x22, 2022-07-31, rev 0x00f4, size 97280
    sig 0x000a0655, pf_mask 0x22, 2022-07-31, rev 0x00f4, size 96256
    sig 0x000a0660, pf_mask 0x80, 2022-07-31, rev 0x00f4, size 97280
    sig 0x000a0661, pf_mask 0x80, 2022-07-31, rev 0x00f4, size 96256
    sig 0x000a0671, pf_mask 0x02, 2022-08-02, rev 0x0056, size 103424

* Mon May 16 2022 L.A. Kostis <lakostis@altlinux.ru> 2:18-alt1.20220510
- Sync with Debian 3.20220510.1:
  + New upstream microcode datafile 20220510
    + Fixes INTEL-SA-000617, CVE-2022-21151:
      Processor optimization removal or modification of security-critical
      code may allow an authenticated user to potentially enable information
      disclosure via local access (closes: #1010947)
    + Fixes several errata (functional issues) on Xeon Scalable, Atom C3000,
      Atom E3900
    + New Microcodes:
      sig 0x00090672, pf_mask 0x03, 2022-03-03, rev 0x001f, size 212992
      sig 0x00090675, pf_mask 0x03, 2022-03-03, rev 0x001f, size 212992
      sig 0x000906a3, pf_mask 0x80, 2022-03-24, rev 0x041c, size 212992
      sig 0x000906a4, pf_mask 0x80, 2022-03-24, rev 0x041c, size 212992
      sig 0x000b06f2, pf_mask 0x03, 2022-03-03, rev 0x001f, size 212992
      sig 0x000b06f5, pf_mask 0x03, 2022-03-03, rev 0x001f, size 212992
    + Updated Microcodes:
      sig 0x00030679, pf_mask 0x0f, 2019-07-10, rev 0x090d, size 52224
      sig 0x000406e3, pf_mask 0xc0, 2021-11-12, rev 0x00f0, size 106496
      sig 0x00050653, pf_mask 0x97, 2021-11-13, rev 0x100015d, size 34816
      sig 0x00050654, pf_mask 0xb7, 2021-11-13, rev 0x2006d05, size 43008
      sig 0x00050656, pf_mask 0xbf, 2021-12-10, rev 0x4003302, size 37888
      sig 0x00050657, pf_mask 0xbf, 2021-12-10, rev 0x5003302, size 37888
      sig 0x0005065b, pf_mask 0xbf, 2021-11-19, rev 0x7002501, size 29696
      sig 0x000506c9, pf_mask 0x03, 2021-11-16, rev 0x0048, size 17408
      sig 0x000506e3, pf_mask 0x36, 2021-11-12, rev 0x00f0, size 109568
      sig 0x000506f1, pf_mask 0x01, 2021-12-02, rev 0x0038, size 11264
      sig 0x000606a6, pf_mask 0x87, 2022-03-30, rev 0xd000363, size 294912
      sig 0x000706a1, pf_mask 0x01, 2021-11-22, rev 0x003a, size 75776
      sig 0x000706a8, pf_mask 0x01, 2021-11-22, rev 0x001e, size 75776
      sig 0x000706e5, pf_mask 0x80, 2022-03-09, rev 0x00b0, size 112640
      sig 0x000806a1, pf_mask 0x10, 2022-03-26, rev 0x0031, size 34816
      sig 0x000806c1, pf_mask 0x80, 2022-02-01, rev 0x00a4, size 109568
      sig 0x000806c2, pf_mask 0xc2, 2021-12-07, rev 0x0026, size 97280
      sig 0x000806d1, pf_mask 0xc2, 2021-12-07, rev 0x003e, size 102400
      sig 0x000806e9, pf_mask 0x10, 2021-11-12, rev 0x00f0, size 105472
      sig 0x000806e9, pf_mask 0xc0, 2021-11-12, rev 0x00f0, size 105472
      sig 0x000806ea, pf_mask 0xc0, 2021-11-12, rev 0x00f0, size 105472
      sig 0x000806eb, pf_mask 0xd0, 2021-11-15, rev 0x00f0, size 105472
      sig 0x000806ec, pf_mask 0x94, 2021-11-17, rev 0x00f0, size 105472
      sig 0x00090661, pf_mask 0x01, 2022-02-03, rev 0x0016, size 20480
      sig 0x000906c0, pf_mask 0x01, 2022-02-19, rev 0x24000023, size 20480
      sig 0x000906e9, pf_mask 0x2a, 2021-11-12, rev 0x00f0, size 108544
      sig 0x000906ea, pf_mask 0x22, 2021-11-15, rev 0x00f0, size 104448
      sig 0x000906eb, pf_mask 0x02, 2021-11-12, rev 0x00f0, size 105472
      sig 0x000906ec, pf_mask 0x22, 2021-11-15, rev 0x00f0, size 104448
      sig 0x000906ed, pf_mask 0x22, 2021-11-16, rev 0x00f0, size 104448
      sig 0x000a0652, pf_mask 0x20, 2021-11-16, rev 0x00f0, size 96256
      sig 0x000a0653, pf_mask 0x22, 2021-11-15, rev 0x00f0, size 97280
      sig 0x000a0655, pf_mask 0x22, 2021-11-16, rev 0x00f0, size 96256
      sig 0x000a0660, pf_mask 0x80, 2021-11-15, rev 0x00f0, size 96256
      sig 0x000a0661, pf_mask 0x80, 2021-11-16, rev 0x00f0, size 96256
      sig 0x000a0671, pf_mask 0x02, 2022-03-09, rev 0x0053, size 103424

* Mon Mar 21 2022 L.A. Kostis <lakostis@altlinux.ru> 2:17-alt1.20220207
- Sync with Debian 3.20220207:
    + new upstream datafile 20220207
      + Mitigates (*only* when loaded from UEFI firmware through the FIT)
        CVE-2021-0146, INTEL-SA-00528: VT-d privilege escalation through
        debug port, on Pentium, Celeron and Atom processors with signatures
        0x506c9, 0x506ca, 0x506f1, 0x706a1, 0x706a8
        https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/issues/57#issuecomment-1036363145
      + Mitigates CVE-2021-0127, INTEL-SA-00532: an unexpected code breakpoint
        may cause a system hang, on many processors.
      + Mitigates CVE-2021-0145, INTEL-SA-00561: information disclosure due
        to improper sanitization of shared resources (fast-store forward
        predictor), on many processors.
      + Mitigates CVE-2021-33120, INTEL-SA-00589: out-of-bounds read on some
        Atom Processors may allow information disclosure or denial of service
        via network access.
      + Fixes critical errata (functional issues) on many processors
      + Adds a MSR switch to enable RAPL filtering (default off, once enabled
        it can only be disabled by poweroff or reboot).  Useful to protect
        SGX and other threads from side-channel info leak.  Improves the
        mitigation for CVE-2020-8694, CVE-2020-8695, INTEL-SA-00389 on many
        processors.
      + Disables TSX in more processor models.
      + Fixes issue with WBINDV on multi-socket (server) systems which could
        cause resets and unpredictable system behavior.
      + Adds a MSR switch to 10th and 11th-gen (Ice Lake, Tiger Lake, Rocket
        Lake) processors, to control a fix for (hopefully rare) unpredictable
        processor behavior when HyperThreading is enabled.  This MSR switch
        is enabled by default on *server* processors.  On other processors,
        it needs to be explicitly enabled by an updated UEFI/BIOS (with added
        configuration logic).  An updated operating system kernel might also
        be able to enable it.  When enabled, this fix can impact performance.
      * Updated Microcodes:
        sig 0x000306f2, pf_mask 0x6f, 2021-08-11, rev 0x0049, size 38912
        sig 0x000306f4, pf_mask 0x80, 2021-05-24, rev 0x001a, size 23552
        sig 0x000406e3, pf_mask 0xc0, 2021-04-28, rev 0x00ec, size 105472
        sig 0x00050653, pf_mask 0x97, 2021-05-26, rev 0x100015c, size 34816
        sig 0x00050654, pf_mask 0xb7, 2021-06-16, rev 0x2006c0a, size 43008
        sig 0x00050656, pf_mask 0xbf, 2021-08-13, rev 0x400320a, size 35840
        sig 0x00050657, pf_mask 0xbf, 2021-08-13, rev 0x500320a, size 36864
        sig 0x0005065b, pf_mask 0xbf, 2021-06-04, rev 0x7002402, size 28672
        sig 0x00050663, pf_mask 0x10, 2021-06-12, rev 0x700001c, size 28672
        sig 0x00050664, pf_mask 0x10, 2021-06-12, rev 0xf00001a, size 27648
        sig 0x00050665, pf_mask 0x10, 2021-09-18, rev 0xe000014, size 23552
        sig 0x000506c9, pf_mask 0x03, 2021-05-10, rev 0x0046, size 17408
        sig 0x000506ca, pf_mask 0x03, 2021-05-10, rev 0x0024, size 16384
        sig 0x000506e3, pf_mask 0x36, 2021-04-29, rev 0x00ec, size 108544
        sig 0x000506f1, pf_mask 0x01, 2021-05-10, rev 0x0036, size 11264
        sig 0x000606a6, pf_mask 0x87, 2021-12-03, rev 0xd000331, size 291840
        sig 0x000706a1, pf_mask 0x01, 2021-05-10, rev 0x0038, size 74752
        sig 0x000706a8, pf_mask 0x01, 2021-05-10, rev 0x001c, size 75776
        sig 0x000706e5, pf_mask 0x80, 2021-05-26, rev 0x00a8, size 110592
        sig 0x000806a1, pf_mask 0x10, 2021-09-02, rev 0x002d, size 34816
        sig 0x000806c1, pf_mask 0x80, 2021-08-06, rev 0x009a, size 109568
        sig 0x000806c2, pf_mask 0xc2, 2021-07-16, rev 0x0022, size 96256
        sig 0x000806d1, pf_mask 0xc2, 2021-07-16, rev 0x003c, size 101376
        sig 0x000806e9, pf_mask 0x10, 2021-04-28, rev 0x00ec, size 104448
        sig 0x000806e9, pf_mask 0xc0, 2021-04-28, rev 0x00ec, size 104448
        sig 0x000806ea, pf_mask 0xc0, 2021-04-28, rev 0x00ec, size 103424
        sig 0x000806eb, pf_mask 0xd0, 2021-04-28, rev 0x00ec, size 104448
        sig 0x000806ec, pf_mask 0x94, 2021-04-28, rev 0x00ec, size 104448
        sig 0x00090661, pf_mask 0x01, 2021-09-21, rev 0x0015, size 20480
        sig 0x000906c0, pf_mask 0x01, 2021-08-09, rev 0x2400001f, size 20480
        sig 0x000906e9, pf_mask 0x2a, 2021-04-29, rev 0x00ec, size 106496
        sig 0x000906ea, pf_mask 0x22, 2021-04-28, rev 0x00ec, size 102400
        sig 0x000906eb, pf_mask 0x02, 2021-04-28, rev 0x00ec, size 104448
        sig 0x000906ec, pf_mask 0x22, 2021-04-28, rev 0x00ec, size 103424
        sig 0x000906ed, pf_mask 0x22, 2021-04-28, rev 0x00ec, size 103424
        sig 0x000a0652, pf_mask 0x20, 2021-04-28, rev 0x00ec, size 93184
        sig 0x000a0653, pf_mask 0x22, 2021-04-28, rev 0x00ec, size 94208
        sig 0x000a0655, pf_mask 0x22, 2021-04-28, rev 0x00ee, size 94208
        sig 0x000a0660, pf_mask 0x80, 2021-04-28, rev 0x00ea, size 94208
        sig 0x000a0661, pf_mask 0x80, 2021-04-29, rev 0x00ec, size 93184
        sig 0x000a0671, pf_mask 0x02, 2021-08-29, rev 0x0050, size 102400
      + Removed Microcodes:
        sig 0x00080664, pf_mask 0x01, 2021-02-17, rev 0xb00000f, size 130048
        sig 0x00080665, pf_mask 0x01, 2021-02-17, rev 0xb00000f, size 130048

* Mon Jun 14 2021 L.A. Kostis <lakostis@altlinux.ru> 2:16-alt1.20210608
- Sync with Debian 3.20210608.1:
  + New upstream microcode datafile 20210608:
    + Implements mitigations for CVE-2020-24511 CVE-2020-24512
      (INTEL-SA-00464), information leakage through shared resources,
      and timing discrepancy sidechannels
    + Implements mitigations for CVE-2020-24513 (INTEL-SA-00465),
      Domain-bypass transient execution vulnerability in some Intel Atom
      Processors, affects Intel SGX.
    + Implements mitigations for CVE-2021-24489 (INTEL-SA-00442), Intel
      VT-d privilege escalation
    + Fixes critical errata on several processors
    + New Microcodes:
      sig 0x00050655, pf_mask 0xb7, 2018-11-16, rev 0x3000010, size 47104
      sig 0x000606a5, pf_mask 0x87, 2021-03-08, rev 0xc0002f0, size 283648
      sig 0x000606a6, pf_mask 0x87, 2021-04-25, rev 0xd0002a0, size 283648
      sig 0x00080664, pf_mask 0x01, 2021-02-17, rev 0xb00000f, size 130048
      sig 0x00080665, pf_mask 0x01, 2021-02-17, rev 0xb00000f, size 130048
      sig 0x000806c1, pf_mask 0x80, 2021-03-31, rev 0x0088, size 109568
      sig 0x000806c2, pf_mask 0xc2, 2021-04-07, rev 0x0016, size 94208
      sig 0x000806d1, pf_mask 0xc2, 2021-04-23, rev 0x002c, size 99328
      sig 0x00090661, pf_mask 0x01, 2021-02-04, rev 0x0011, size 19456
      sig 0x000906c0, pf_mask 0x01, 2021-03-23, rev 0x001d, size 19456
      sig 0x000a0671, pf_mask 0x02, 2021-04-11, rev 0x0040, size 100352
    + Updated Microcodes:
      sig 0x000306f2, pf_mask 0x6f, 2021-01-27, rev 0x0046, size 34816
      sig 0x000306f4, pf_mask 0x80, 2021-02-05, rev 0x0019, size 19456
      sig 0x000406e3, pf_mask 0xc0, 2021-01-25, rev 0x00ea, size 105472
      sig 0x000406f1, pf_mask 0xef, 2021-02-06, rev 0xb00003e, size 31744
      sig 0x00050653, pf_mask 0x97, 2021-03-08, rev 0x100015b, size 34816
      sig 0x00050654, pf_mask 0xb7, 2021-03-08, rev 0x2006b06, size 36864
      sig 0x00050656, pf_mask 0xbf, 2021-03-08, rev 0x4003102, size 30720
      sig 0x00050657, pf_mask 0xbf, 2021-03-08, rev 0x5003102, size 30720
      sig 0x0005065b, pf_mask 0xbf, 2021-04-23, rev 0x7002302, size 27648
      sig 0x00050663, pf_mask 0x10, 2021-02-04, rev 0x700001b, size 24576
      sig 0x00050664, pf_mask 0x10, 2021-02-04, rev 0xf000019, size 24576
      sig 0x00050665, pf_mask 0x10, 2021-02-04, rev 0xe000012, size 19456
      sig 0x000506c9, pf_mask 0x03, 2020-10-23, rev 0x0044, size 17408
      sig 0x000506ca, pf_mask 0x03, 2020-10-23, rev 0x0020, size 15360
      sig 0x000506e3, pf_mask 0x36, 2021-01-25, rev 0x00ea, size 105472
      sig 0x000506f1, pf_mask 0x01, 2020-10-23, rev 0x0034, size 11264
      sig 0x000706a1, pf_mask 0x01, 2020-10-23, rev 0x0036, size 74752
      sig 0x000706a8, pf_mask 0x01, 2020-10-23, rev 0x001a, size 75776
      sig 0x000706e5, pf_mask 0x80, 2020-11-01, rev 0x00a6, size 110592
      sig 0x000806a1, pf_mask 0x10, 2020-11-06, rev 0x002a, size 32768
      sig 0x000806e9, pf_mask 0x10, 2021-01-05, rev 0x00ea, size 104448
      sig 0x000806e9, pf_mask 0xc0, 2021-01-05, rev 0x00ea, size 104448
      sig 0x000806ea, pf_mask 0xc0, 2021-01-06, rev 0x00ea, size 103424
      sig 0x000806eb, pf_mask 0xd0, 2021-01-05, rev 0x00ea, size 104448
      sig 0x000806ec, pf_mask 0x94, 2021-01-05, rev 0x00ea, size 104448
      sig 0x000906e9, pf_mask 0x2a, 2021-01-05, rev 0x00ea, size 104448
      sig 0x000906ea, pf_mask 0x22, 2021-01-05, rev 0x00ea, size 102400
      sig 0x000906eb, pf_mask 0x02, 2021-01-05, rev 0x00ea, size 104448
      sig 0x000906ec, pf_mask 0x22, 2021-01-05, rev 0x00ea, size 103424
      sig 0x000906ed, pf_mask 0x22, 2021-01-05, rev 0x00ea, size 103424
      sig 0x000a0652, pf_mask 0x20, 2021-02-07, rev 0x00ea, size 93184
      sig 0x000a0653, pf_mask 0x22, 2021-03-08, rev 0x00ea, size 94208
      sig 0x000a0655, pf_mask 0x22, 2021-03-08, rev 0x00ec, size 94208
      sig 0x000a0660, pf_mask 0x80, 2020-12-08, rev 0x00e8, size 94208
      sig 0x000a0661, pf_mask 0x80, 2021-02-07, rev 0x00ea, size 93184

* Thu Jun 03 2021 L.A. Kostis <lakostis@altlinux.ru> 2:15-alt1.20210216
- Sync with Debian 3.20210216.1:
  + New upstream microcode datafile 20210216
    + Mitigates an issue on Skylake Server (H0/M0/U0), Xeon-D 21xx,
      and Cascade Lake Server (B0/B1) when using an active JTAG
      agent like In Target Probe (ITP), Direct Connect Interface
      (DCI) or a Baseboard Management Controller (BMC) to take the
      CPU JTAG/TAP out of reset and then returning it to reset.
    + This issue is related to the INTEL-SA-00381 mitigation.
    + Updated Microcodes:
      sig 0x00050654, pf_mask 0xb7, 2020-12-31, rev 0x2006a0a, size 36864
      sig 0x00050656, pf_mask 0xbf, 2020-12-31, rev 0x4003006, size 53248
      sig 0x00050657, pf_mask 0xbf, 2020-12-31, rev 0x5003006, size 53248

* Tue Nov 17 2020 L.A. Kostis <lakostis@altlinux.ru> 2:14-alt1.20201110
- Sync with Debian 3.20201110.1:
  + New upstream microcode datafile 20201110:
    + Implements mitigation for CVE-2020-8696 and CVE-2020-8698,
      aka INTEL-SA-00381: AVX register information leakage;
      Fast-Forward store predictor information leakage
    + Implements mitigation for CVE-2020-8695, Intel SGX information
      disclosure via RAPL, aka INTEL-SA-00389
    + Fixes critical errata on several processor models
    + Reintroduces SRBDS mitigations(CVE-2020-0543, INTEL-SA-00320)
      for Skylake-U/Y, Skylake Xeon E3
    + New Microcodes:
      sig 0x0005065b, pf_mask 0xbf, 2020-08-20, rev 0x700001e, size 27648
      sig 0x000806a1, pf_mask 0x10, 2020-06-26, rev 0x0028, size 32768
      sig 0x000806c1, pf_mask 0x80, 2020-10-02, rev 0x0068, size 107520
      sig 0x000a0652, pf_mask 0x20, 2020-07-08, rev 0x00e0, size 93184
      sig 0x000a0653, pf_mask 0x22, 2020-07-08, rev 0x00e0, size 94208
      sig 0x000a0655, pf_mask 0x22, 2020-07-08, rev 0x00e0, size 93184
      sig 0x000a0661, pf_mask 0x80, 2020-07-02, rev 0x00e0, size 93184
    + Updated Microcodes:
      sig 0x000306f2, pf_mask 0x6f, 2020-05-27, rev 0x0044, size 34816
      sig 0x000406e3, pf_mask 0xc0, 2020-07-14, rev 0x00e2, size 105472
      sig 0x00050653, pf_mask 0x97, 2020-06-18, rev 0x1000159, size 33792
      sig 0x00050654, pf_mask 0xb7, 2020-06-16, rev 0x2006a08, size 35840
      sig 0x00050656, pf_mask 0xbf, 2020-06-18, rev 0x4003003, size 52224
      sig 0x00050657, pf_mask 0xbf, 2020-06-18, rev 0x5003003, size 52224
      sig 0x000506c9, pf_mask 0x03, 2020-02-27, rev 0x0040, size 17408
      sig 0x000506ca, pf_mask 0x03, 2020-02-27, rev 0x001e, size 15360
      sig 0x000506e3, pf_mask 0x36, 2020-07-14, rev 0x00e2, size 105472
      sig 0x000706a8, pf_mask 0x01, 2020-06-09, rev 0x0018, size 75776
      sig 0x000706e5, pf_mask 0x80, 2020-07-30, rev 0x00a0, size 109568
      sig 0x000806e9, pf_mask 0x10, 2020-05-27, rev 0x00de, size 104448
      sig 0x000806e9, pf_mask 0xc0, 2020-05-27, rev 0x00de, size 104448
      sig 0x000806ea, pf_mask 0xc0, 2020-06-17, rev 0x00e0, size 104448
      sig 0x000806eb, pf_mask 0xd0, 2020-06-03, rev 0x00de, size 104448
      sig 0x000806ec, pf_mask 0x94, 2020-05-18, rev 0x00de, size 104448
      sig 0x000906e9, pf_mask 0x2a, 2020-05-26, rev 0x00de, size 104448
      sig 0x000906ea, pf_mask 0x22, 2020-05-25, rev 0x00de, size 103424
      sig 0x000906eb, pf_mask 0x02, 2020-05-25, rev 0x00de, size 104448
      sig 0x000906ec, pf_mask 0x22, 2020-06-03, rev 0x00de, size 103424
      sig 0x000906ed, pf_mask 0x22, 2020-05-24, rev 0x00de, size 103424
      sig 0x000a0660, pf_mask 0x80, 2020-07-08, rev 0x00e0, size 94208
  + 0x806c1: remove the new Tiger Lake update: causes hang on cold/warm boot
    https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/issues/44
    INTEL-SA-00381 AND INTEL-SA-00389 MITIGATIONS ARE THEREFORE NOT INSTALLED
    FOR 0x806c1 TIGER LAKE PROCESSORS by this package update.  Contact your
    system vendor for a firmware update, or wait fo a possible fix in a future
    Intel microcode release.
  + source: update symlinks to reflect id of the latest release, 20201110
  + source: ship new upstream documentation (security.md, releasenote.md)

* Mon Jul 13 2020 L.A. Kostis <lakostis@altlinux.ru> 2:13-alt1.20200616
- Sync with Debian 3.20200616.1:
  + New upstream microcode datafile 20200616
    + Downgraded microcodes (to a previously shipped revision):
      sig 0x000406e3, pf_mask 0xc0, 2019-10-03, rev 0x00d6, size 101376
      sig 0x000506e3, pf_mask 0x36, 2019-10-03, rev 0x00d6, size 101376
  + Works around hangs on boot on Skylake-U/Y and Skylake Xeon E3,
  + https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/issues/31
  + This update *removes* the SRBDS mitigations from the above processors
- REGRESSION FIX: 0x406e3: rollback to rev 0xd6 and document regression
- Security fixes:
  + Implements mitigation for CVE-2020-0543 Special Register Buffer Data
    Sampling (SRBDS), aka INTEL-SA-00320
  + Implements mitigation for CVE-2020-0548 Vector Register Data Sampling
    (VRDS), INTEL-SA-00329
  + Implements mitigation for CVE-2020-0549 L1D Cache Eviction Sampling
    (L1DCES), INTEL-SA-00329
  + Known to fix the regression introduced in release 2019-11-12 (sig
    0x50564, rev. 0x2000065), which would cause several systems with
    Skylake Xeon, Skylake HEDT processors to hang while rebooting
  + Updated Microcodes:
    sig 0x000306c3, pf_mask 0x32, 2019-11-12, rev 0x0028, size 23552
    sig 0x000306d4, pf_mask 0xc0, 2019-11-12, rev 0x002f, size 19456
    sig 0x00040651, pf_mask 0x72, 2019-11-12, rev 0x0026, size 22528
    sig 0x00040661, pf_mask 0x32, 2019-11-12, rev 0x001c, size 25600
    sig 0x00040671, pf_mask 0x22, 2019-11-12, rev 0x0022, size 14336
    sig 0x000406e3, pf_mask 0xc0, 2020-04-27, rev 0x00dc, size 104448
    sig 0x00050653, pf_mask 0x97, 2020-04-24, rev 0x1000157, size 32768
    sig 0x00050654, pf_mask 0xb7, 2020-04-24, rev 0x2006906, size 34816
    sig 0x00050656, pf_mask 0xbf, 2020-04-23, rev 0x4002f01, size 52224
    sig 0x00050657, pf_mask 0xbf, 2020-04-23, rev 0x5002f01, size 52224
    sig 0x000806e9, pf_mask 0x10, 2020-04-27, rev 0x00d6, size 103424
    sig 0x000806e9, pf_mask 0xc0, 2020-04-27, rev 0x00d6, size 103424
    sig 0x000806ea, pf_mask 0xc0, 2020-04-27, rev 0x00d6, size 103424
    sig 0x000806eb, pf_mask 0xd0, 2020-04-27, rev 0x00d6, size 103424
    sig 0x000806ec, pf_mask 0x94, 2020-04-23, rev 0x00d6, size 103424
    sig 0x000906e9, pf_mask 0x2a, 2020-04-23, rev 0x00d6, size 103424
    sig 0x000906ea, pf_mask 0x22, 2020-04-27, rev 0x00d6, size 102400
    sig 0x000906eb, pf_mask 0x02, 2020-04-23, rev 0x00d6, size 103424
    sig 0x000906ec, pf_mask 0x22, 2020-04-27, rev 0x00d6, size 102400
    sig 0x000906ed, pf_mask 0x22, 2020-04-23, rev 0x00d6, size 103424

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
