# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: real-ucode
Version: 20260322
Release: alt1
Summary: Actually provides the latest CPU microcode for AMD and Intel
License: Redistributable, no modification permitted
Group: System/Kernel and hardware
Url: https://github.com/divestedcg/real-ucode/

Source: %name-%version.tar
BuildArch: noarch

ExclusiveArch: x86_64
%{?!_without_check:%{?!_disable_check:
BuildRequires: iucode_tool
}}

%define disclaimer %{expand:
DISCLAIMER: All the microcodes below come only from official BIOS/UEFI updates,
Intel/AMD Linux Microcode Updates, Linux Distributions, Windows Updates etc
which were provided and made public by various manufacturers.

It is generally advised to request and/or wait for your OEM to release newer
fixes. Latest is not always better or tested! Manufacturers usually have some
insider/confidential info from microcode vendors on what got changed/fixed at
newer microcode releases so if they ship older microcodes, it could be that
newer versions have not been thoroughly tested, have been retracted/downgraded
by the microcode vendor or not contain anything important enough to warrant an
update. The microcodes here are gathered and provided with the sole purpose of
helping people who are out of other viable solutions. Thus, they can be
extremely helpful to those who have major problems with their systems for which
their manufacturer refuses to assist due to indifference and/or system age.
}

%define amd_notice %{expand:
SPECIAL NOTICE (2026-01-12)

AMD ucode loading for both -official and -resigned is now broken on entrysign
affected machines after 6.18.4 or newer please switch back to linux-firmware
}

%description
Please see the README for details.
The actual microcodes are from https://github.com/platomav/CPUMicrocodes

%package -n firmware-amd-real-ucode
Summary: Latest microcode for AMD
Group: System/Kernel and hardware
RemovePathPostfixes: .official

# Kernel filters patch ID in arch/x86/kernel/cpu/microcode/amd_shas.c
%define amd_sha_check_note \
NOTE: You will need to add microcode.amd_sha_check=off to the kernel command \
line for the new microcode to be loadable. This will taint the kernel. \
Verify the dmesg that the new microcode is loaded correctly.

%description -n firmware-amd-real-ucode
Microcode updates for AMD CPUs (for new BIOS). If it's not loadable on old
BIOS you may try to install firmware-amd-real-ucode-resigned.

%amd_sha_check_note

%disclaimer

%amd_notice

%package -n firmware-amd-real-ucode-resigned
Summary: Latest microcode for AMD, resigned
Group: System/Kernel and hardware
RemovePathPostfixes: .resigned
Conflicts: firmware-amd-real-ucode

%description -n firmware-amd-real-ucode-resigned
After the recent AMD microcode signature verification vulnerability
(CVE-2024-56161), microcode dated after 2024-11 will fail to load on pre
2025-01 BIOS! The vulnerability can be utilized to resign new ucodes for the
old loaders.

This is microcode updates for AMD CPUs, resigned for vulnerable old loaders.

%amd_sha_check_note

These may fail to load upon resume from suspend when using s3 sleep, please use
s2idle instead.

%disclaimer

%amd_notice

%package -n firmware-intel-real-ucode
Summary: Latest microcode for Intel
Group: System/Kernel and hardware

%description -n firmware-intel-real-ucode
Microcode updates for Intel CPUs.

%disclaimer

%prep
%setup

%install
install -Dm644 microcode/amd-ucode/*   -t %buildroot/lib/firmware/updates/amd-ucode
install -Dm644 microcode/intel-ucode/* -t %buildroot/lib/firmware/updates/intel-ucode
# iucode_tool is incompatible with non-microcode files.
rm %buildroot/lib/firmware/updates/*-ucode/LICENSE.*

%check
/usr/sbin/iucode_tool --write-earlyfw=ucode.cpio %buildroot/lib/firmware/updates/intel-ucode
cpio -t < ucode.cpio
rm ucode.cpio

%files -n firmware-amd-real-ucode
%doc LICENSE LICENSE.amd-ucode README.md index-amd-official.txt index-amd.txt
%dir /lib/firmware/updates/amd-ucode
/lib/firmware/updates/amd-ucode/*.bin.official

%files -n firmware-amd-real-ucode-resigned
%doc LICENSE LICENSE.amd-ucode README.md index-amd-official.txt index-amd.txt
%dir /lib/firmware/updates/amd-ucode
/lib/firmware/updates/amd-ucode/*.bin.resigned

%files -n firmware-intel-real-ucode
%doc LICENSE LICENSE.intel-ucode README.md index-intel-official.txt index-intel.txt
/lib/firmware/updates/intel-ucode

%changelog
* Fri Mar 27 2026 Vitaly Chikunov <vt@altlinux.org> 20260322-alt1
- Update to 56eccff (2026-03-22).

* Wed Feb 18 2026 Vitaly Chikunov <vt@altlinux.org> 20260214-alt1
- Update to 2510ae8 (2026-02-14).
- Notice: AMD ucode loading for both -official and -resigned is now broken on
  entrysign affected machines after 6.18.4 or newer please switch back to
  linux-firmware.

* Sat Dec 20 2025 Vitaly Chikunov <vt@altlinux.org> 20251219-alt1
- Update to 5e46e06 (2025-12-19).

* Mon Dec 15 2025 Vitaly Chikunov <vt@altlinux.org> 20251211-alt1
- Update to 68384b9 (2025-12-11).

* Mon Dec 08 2025 Vitaly Chikunov <vt@altlinux.org> 20251207-alt1
- Update to a86da0a (2025-12-07).

* Sun Dec 07 2025 Vitaly Chikunov <vt@altlinux.org> 20251205-alt1
- Update to dec6830 (2025-12-05).

* Sat Nov 22 2025 Vitaly Chikunov <vt@altlinux.org> 20251116-alt1
- Update to ea1ed78 (2025-11-16).

* Sat Nov 08 2025 Vitaly Chikunov <vt@altlinux.org> 20251106-alt1
- Update to b3c46a4 (2025-11-06).

* Sun Oct 05 2025 Vitaly Chikunov <vt@altlinux.org> 20251004-alt1
- Update to 9dcabd3 (2025-10-04).

* Wed Sep 24 2025 Vitaly Chikunov <vt@altlinux.org> 20250922-alt1
- Update to b08b470 (2025-09-22).
- Fix install of firmware-intel-real-ucode (ALT#56076).

* Sun Sep 14 2025 Vitaly Chikunov <vt@altlinux.org> 20250913-alt1
- Update to c471526 (2025-09-13).

* Tue Sep 02 2025 Vitaly Chikunov <vt@altlinux.org> 20250831-alt1
- Update to 8dd5b74 (2025-08-31).

* Thu Aug 21 2025 Vitaly Chikunov <vt@altlinux.org> 20250818-alt1
- Update to d2a075f (2025-08-18).

* Thu Aug 14 2025 Vitaly Chikunov <vt@altlinux.org> 20250813-alt1
- First import e53b04e (2025-08-13).
