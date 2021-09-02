
Name: acpica
Version: 20201113
Release: alt2
Summary: ACPICA tools for the development and debug of ACPI tables

Group: System/Kernel and hardware
License: GPLv2
Url: https://www.acpica.org/

#vcs-git https://github.com/acpica/acpica.git
Source: %name-%version.tar
Source3: iasl.1
Source4: acpibin.1
Source5: acpidump.1
Source6: acpiexec.1
Source7: acpihelp.1
Source8: acpinames.1
Source9: acpisrc.1
Source10: acpixtract.1
Source11: acpiexamples.1
Source12: badcode.asl.result
Source13: grammar.asl.result
Source14: converterSample.asl.result
Source15: run-misc-tests.sh

# the big-endian patch set (from fedora)
Patch0: 0001-Add-in-basic-infrastructure-for-big-endian-support.patch
Patch1: 0002-Modify-utility-functions-to-be-endian-agnostic.patch
Patch2: 0003-Always-display-table-header-content-in-human-readabl.patch
Patch3: 0004-Re-enable-support-for-big-endian-machines.patch
Patch4: 0005-Support-MADT-aka-APIC-in-a-big-endian-world.patch
Patch5: 0006-Support-ASF-tables-in-a-big-endian-world.patch
Patch6: 0007-Support-CPEP-tables-in-a-big-endian-world.patch
Patch7: 0008-Support-DBG2-table-in-a-big-endian-world.patch
Patch8: 0009-Support-DMAR-in-a-big-endian-world.patch
Patch9: 0010-Support-DRTM-in-a-big-endian-world.patch
Patch10: 0011-Support-EINJ-in-a-big-endian-world.patch
Patch11: 0012-Support-ERST-in-a-big-endian-world.patch
Patch12: 0013-Support-FADT-aka-FACP-in-a-big-endian-world.patch
Patch13: 0014-Support-most-FPDTs-in-a-big-endian-world.patch
Patch14: 0015-Support-GTDT-in-a-big-endian-world.patch
Patch15: 0016-Support-HEST-in-a-big-endian-world.patch
Patch16: 0017-Support-RSDT-RSD-PTR-in-a-big-endian-world.patch
Patch17: 0018-Support-XSDT-in-a-big-endian-world.patch
Patch18: 0019-Support-SRAT-in-a-big-endian-world.patch
Patch19: 0020-Support-SLIT-in-a-big-endian-world.patch
Patch20: 0021-Support-MSCT-in-a-big-endian-world.patch
Patch21: 0022-Support-MPST-in-a-big-endian-world.patch
Patch22: 0023-Support-NFIT-in-a-big-endian-world.patch
Patch23: 0024-Support-SDEV-in-a-big-endian-world.patch
Patch24: 0025-Support-HMAT-in-a-big-endian-world.patch
Patch25: 0026-Support-PDTT-in-a-big-endian-world.patch
Patch26: 0027-Support-PPTT-in-a-big-endian-world.patch
Patch27: 0028-Support-PCCT-in-a-big-endian-world.patch
Patch28: 0029-Support-WDAT-in-a-big-endian-world.patch
Patch29: 0030-Support-TCPA-in-a-big-endian-world.patch
Patch30: 0031-Support-STAO-in-a-big-endian-world.patch
Patch31: 0032-Support-SLIC-and-MSDM-in-a-big-endian-world.patch
Patch32: 0033-Support-MCFG-in-a-big-endian-world.patch
Patch33: 0034-Support-LPIT-in-a-big-endian-world.patch
Patch34: 0035-Support-PMTT-in-a-big-endian-world.patch
Patch35: 0036-Support-IORT-in-a-big-endian-world.patch
Patch36: 0037-Support-IVRS-in-a-big-endian-world.patch
Patch37: 0038-Support-TPM2-in-a-big-endian-world.patch
Patch38: 0039-Add-partial-big-endian-support-for-WPBT-tables.patch
Patch39: 0040-Support-DSDT-SSDT-in-a-big-endian-world.patch
Patch40: 0041-Support-MTMR-in-a-big-endian-world.patch
Patch41: 0042-Support-VRTC-in-a-big-endian-world.patch
Patch42: 0043-Support-S3PT-in-a-big-endian-world.patch
Patch43: 0044-Correct-an-endian-ness-problem-when-converting-ASL-t.patch
Patch44: 0045-Correct-a-couple-of-endianness-issues-previously-uns.patch


# other miscellaneous patches
Patch100: unaligned.patch
Patch101: OPT_LDFLAGS.patch
Patch102: int-format.patch
Patch103: f23-harden.patch
Patch104: template.patch
Patch105: arm7hl.patch
Patch106: simple-64bit.patch
Patch107: mips-be-fix.patch
Patch108: cve-2017-13693.patch
Patch109: cve-2017-13694.patch
Patch110: cve-2017-13695.patch
Patch111: str-trunc-warn.patch
Patch112: ptr-cast.patch
Patch113: facp.patch
Patch114: armv7-str-fixes.patch
Patch115: dbtest.patch
Patch116: ull-32bit.patch

BuildRequires: bison flex

Provides: %name-tools = %version-%release

# The previous iasl package contained only a very small subset of these tools
# and it produced only the iasl package listed below; further, the pmtools
# package -- which provides acpidump -- also provides a /usr/sbin/acpixtract
# that we don't really want to collide with
Provides: acpixtract = %version-%release
Provides: iasl = %version-%release
Obsoletes: iasl < %version-%release

# The pmtools package provides an obsolete and deprecated version of the
# acpidump command from lesswatts.org which has now been taken off-line.
# ACPICA, however, is providing a new version and we again do not want to
# conflict with the command name.
Provides: acpidump = %version-%release
Provides: pmtools = %version-%release
Obsoletes: pmtools < %version-%release

%description
The ACPI Component Architecture (ACPICA) project provides an OS-independent
reference implementation of the Advanced Configuration and Power Interface
Specification (ACPI).  ACPICA code contains those portions of ACPI meant to
be directly integrated into the host OS as a kernel-resident subsystem, and
a small set of tools to assist in developing and debugging ACPI tables.

This package contains only the user-space tools needed for ACPI table
development, not the kernel implementation of ACPI.  The following commands
are installed:
   -- iasl: compiles ASL (ACPI Source Language) into AML (ACPI Machine
      Language), suitable for inclusion as a DSDT in system firmware.
      It also can disassemble AML, for debugging purposes.
   -- acpibin: performs basic operations on binary AML files (e.g.,
      comparison, data extraction)
   -- acpidump: write out the current contents of ACPI tables
   -- acpiexec: simulate AML execution in order to debug method definitions
   -- acpihelp: display help messages describing ASL keywords and op-codes
   -- acpinames: display complete ACPI name space from input AML
   -- acpisrc: manipulate the ACPICA source tree and format source files
      for specific environments
   -- acpixtract: extract binary ACPI tables from acpidump output (see
      also the pmtools package)

This version of the tools is being released under GPLv2 license.

%prep
%setup

%patch0 -p1 -b .big-endian
%patch1 -p1 -b .unaligned
%patch2 -p1 -b .OPT_LDFLAGS
%patch3 -p1 -b .int-format
%patch4 -p1 -b .f23-harden
# do not preserve a backup for this patch; it alters the results
# of the template test case and forces it to fail
%patch5 -p1
%patch6 -p1 -b .ppc64le
%patch7 -p1 -b .arm7hl
%patch8 -p1 -b .big-endian-v2
%patch9 -p1 -b .simple-64bit
%patch10 -p1 -b .mips-be-fix
%patch11 -p1 -b .cve-2017-13693
%patch12 -p1 -b .cve-2017-13694
%patch13 -p1 -b .cve-2017-13695
%patch14 -p1 -b .str-trunc-warn
%patch15 -p1 -b .ptr-cast
%patch16 -p1 -b .aslcodegen
%patch17 -p1 -b .facp
%patch18 -p1 -b .badexit

cp -p %SOURCE3 iasl.1
cp -p %SOURCE4 acpibin.1
cp -p %SOURCE5 acpidump.1
cp -p %SOURCE6 acpiexec.1
cp -p %SOURCE7 acpihelp.1
cp -p %SOURCE8 acpinames.1
cp -p %SOURCE9 acpisrc.1
cp -p %SOURCE10 acpixtract.1
cp -p %SOURCE11 acpiexamples.1
cp -p %SOURCE12 badcode.asl.result
cp -p %SOURCE13 grammar.asl.result
cp -p %SOURCE14 converterSample.asl.result
cp -p %SOURCE15 tests/run-misc-tests.sh
chmod a+x tests/run-misc-tests.sh

%ifarch %e2k
sed -i 's,-Werror ,,' generate/unix/iasl/Makefile
%endif

%build
CWARNINGFLAGS="\
    -std=c99 \
    -Wall \
    -Wbad-function-cast \
    -Wdeclaration-after-statement \
%ifnarch %e2k
    -Werror \
%endif
    -Wformat=2 \
    -Wmissing-declarations \
    -Wmissing-prototypes \
    -Wstrict-aliasing \
    -Wstrict-prototypes \
    -Wswitch-default \
    -Wpointer-arith \
    -Wundef \
    -Waddress \
    -Waggregate-return \
    -Winit-self \
    -Winline \
    -Wmissing-declarations \
    -Wmissing-field-initializers \
    -Wnested-externs \
    -Wold-style-definition \
    -Wno-format-nonliteral \
    -Wredundant-decls \
    -Wempty-body \
    -Woverride-init \
    -Wlogical-op \
    -Wmissing-parameter-type \
    -Wold-style-declaration \
    -Wtype-limits"

OPT_CFLAGS="%optflags $CWARNINGFLAGS"
export OPT_CFLAGS

%make HOST=_LINUX

%install
# Install the binaries
mkdir -p %buildroot%_bindir
install -pD -m0755 generate/unix/bin*/* %buildroot%_bindir/

# Install the man pages
mkdir -p %buildroot%_man1dir
install -pD -m0644 *.1 %buildroot%_man1dir/

%check
cd tests

# ASL tests
./aslts.sh                         # relies on non-zero exit
[ $? -eq 0 ] || exit 1

# misc tests
./run-misc-tests.sh %buildroot%_bindir %version

%files
%doc documents/changes.txt source/compiler/new_table.txt
%_bindir/*
%_man1dir/*

%changelog
* Wed Sep 01 2021 Michael Shigorin <mike@altlinux.org> 20201113-alt2
- fix -Wstrict-aliasing use; see also mcst#4656 and the suggested
  http://gcc.gnu.org/onlinedocs/gcc-7.5.0/gcc/Warning-Options.html#Warning-Options
- E2K: ftbfs workarounds (still the warnings might be real)

* Sat Dec 12 2020 Alexey Shabalin <shaba@altlinux.org> 20201113-alt1
- 20201113

* Fri Dec 13 2019 Alexey Shabalin <shaba@altlinux.org> 20190816-alt1
- 20190816

* Thu Aug 01 2019 Alexey Shabalin <shaba@altlinux.org> 20190509-alt1
- 20190509

* Wed Jan 16 2019 Alexey Shabalin <shaba@altlinux.org> 20181213-alt1
- 20181213

* Fri Aug 24 2018 Alexey Shabalin <shaba@altlinux.org> 20180810-alt1
- 20180810

* Wed May 23 2018 Alexey Shabalin <shaba@altlinux.ru> 20180508-alt1
- 20180508

* Mon Apr 02 2018 Alexey Shabalin <shaba@altlinux.ru> 20180209-alt1
- 20180209
- Fixes:
  + CVE-2017-13693
  + CVE-2017-13694
  + CVE-2017-13695

* Wed Feb 07 2018 Alexey Shabalin <shaba@altlinux.ru> 20180105-alt1
- 20180105
- Pulled in a mips32/BE patch from Debian, for completeness sake

* Wed Dec 13 2017 Alexey Shabalin <shaba@altlinux.ru> 20171110-alt1
- 20171110
- Add patch for mips64el build, should it ever be needed; it also cleans
  up all 64-bit arches, so nice to have regardless
- Add new patch for a TPM2 big-endian issue.

* Fri Nov 10 2017 Alexey Shabalin <shaba@altlinux.ru> 20170929-alt1
- 20170929

* Tue Aug 08 2017 Alexey Shabalin <shaba@altlinux.ru> 20170728-alt1
- 20170728

* Mon Dec 26 2016 Alexey Shabalin <shaba@altlinux.ru> 20161222-alt1
- 20161222

* Tue Aug 23 2016 Alexey Shabalin <shaba@altlinux.ru> 20160729-alt1
- 20160729

* Thu Jul 07 2016 Alexey Shabalin <shaba@altlinux.ru> 20160527-alt1
- 20160527

* Fri May 13 2016 Alexey Shabalin <shaba@altlinux.ru> 20160422-alt1
- 20160422

* Thu Dec 10 2015 Alexey Shabalin <shaba@altlinux.ru> 20150930-alt1
- Initial build
- Replace iasl and pmtools packages
