%def_disable debug

Name: dmraid
Version: 1.0.0.rc16
Release: alt2

Summary: dmraid (Device-mapper RAID tool and library)
Group: System/Base
License: GPL
Url: http://people.redhat.com/heinzm/sw/dmraid

Source: dmraid-%version.tar.bz2
Patch: dmraid-1.0.0.rc16-alt-DSO.patch
Patch1: dmraid-1.0.0.rc16-alt-Makefile.patch
Patch2: dmraid-1.0.0.rc16-alt-fix-build-with-static-libdevmapper.patch

#fc
Patch10: dmraid-1.0.0.rc16-test_devices.patch
Patch11: ddf1_lsi_persistent_name.patch
Patch12: pdc_raid10_failure.patch
Patch13: return_error_wo_disks.patch
Patch14: fix_sil_jbod.patch
Patch15: avoid_register.patch
Patch16: move_pattern_file_to_var.patch
Patch17: libversion.patch
Patch18: libversion-display.patch
Patch19: bz635995-data_corruption_during_activation_volume_marked_for_rebuild.patch
Patch21: bz626417_19-enabling_registration_degraded_volume.patch
Patch22: bz626417_20-cleanup_some_compilation_warning.patch
Patch23: bz626417_21-add_option_that_postpones_any_metadata_updates.patch
Patch24: dmraid-fix-build-to-honour-cflags-var.patch

Requires: kpartx

BuildRequires: libdevmapper-devel libdevmapper-event-devel libdevmapper-devel-static

%description
DMRAID supports RAID device discovery, RAID set activation and display of
properties for ATARAID on Linux >= 2.4 using device-mapper.

%package devel
Summary: Development libraries and headers for dmraid.
Group: Development/C
Requires: %name = %version-%release

%description devel
dmraid-devel provides a library interface for RAID device discovery,
RAID set activation and display of properties for ATARAID volumes.


%prep
%setup
%patch
%patch1 -p1
%patch2 -p2

# fc
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1

%build
%define opt %{subst_enable debug} --sbindir=/sbin
%configure  %opt --enable-static_link
# SMP incompatible build
%make
mv tools/dmraid tools/dmraid.static
%make clean
%configure %opt --enable-shared_lib
%make

%install
%makeinstall_std
install -m 755 tools/dmraid.static %buildroot/sbin/dmraid.static

%files
/sbin/dmevent_tool
/sbin/dmraid
/sbin/dmraid.static
%_libdir/lib%name.so.*
%_libdir/lib%name-events-isw.so.*
%_man8dir/dmevent_tool.8.*
%_man8dir/dmraid.8.*
%doc CHANGELOG CREDITS KNOWN_BUGS LICENSE 
%doc README TODO doc/dmraid_design.txt

%exclude %_libdir/lib%name.a

%files devel
%_includedir/%name/
%_libdir/lib%name.so
%_libdir/lib%name-events-isw.so

%changelog
* Wed Mar 07 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.0.0.rc16-alt2
- NMU: fixed FTBFS with static libdevmapper

* Mon Oct 03 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.0.rc16-alt1
- 1.0.0.rc16
- applied fc patchset
- updated buildrequires
- new -devel subpackage

* Fri Feb 28 2014 Andrey Cherepanov <cas@altlinux.org> 1.0.0.rc14-alt1.qa2
- Fixed build

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.0.rc14-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Jun 11 2007 L.A. Kostis <lakostis@altlinux.ru> 1.0.0.rc14-alt1
- build for ALTLinux.

* Fri May 20 2005 Heinz Mauelshagen <heinzm@redhat.com> 1.0.0.rc8-FC4_2
- specfile change to build static and dynamic binray into one package
- rebuilt

* Thu May 19 2005 Heinz Mauelshagen <heinzm@redhat.com> 1.0.0.rc8-FC4_1
- nv.c: fixed stripe size
- sil.c: avoid incarnation_no in name creation, because the Windows
         driver changes it every time
- added --ignorelocking option to avoid taking out locks in early boot
  where no read/write access to /var is given

* Wed Mar 16 2005 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 15 2005 Heinz Mauelshagen <heinzm@redhat.com> 1.0.0.rc6.1-4_FC4
- VIA metadata format handler
- added RAID10 to lsi metadata format handler
- "dmraid -rD": file device size into {devicename}_{formatname}.size
- "dmraid -tay": pretty print multi-line tables ala "dmsetup table"
- "dmraid -l": display supported RAID levels + manual update
- _sil_read() used LOG_NOTICE rather than LOG_INFO in order to
  avoid messages about valid metadata areas being displayed
  during "dmraid -vay".
- isw, sil filed metadata offset on "-r -D" in sectors rather than in bytes.
- isw needed dev_sort() to sort RAID devices in sets correctly.
- pdc metadata format handler name creation. Lead to
  wrong RAID set grouping logic in some configurations.
- pdc RAID1 size calculation fixed (rc6.1)
- dos.c: partition table code fixes by Paul Moore
- _free_dev_pointers(): fixed potential OOB error
- hpt37x_check: deal with raid_disks = 1 in mirror sets
- pdc_check: status & 0x80 doesn't always show a failed device;
  removed that check for now. Status definitions needed.
- sil addition of RAID sets to global list of sets
- sil spare device memory leak
- group_set(): removal of RAID set in case of error
- hpt37x: handle total_secs > device size
- allow -p with -f
- enhanced error message by checking target type against list of
  registered target types

* Fri Jan 21 2005 Alasdair Kergon <agk@redhat.com> 1.0.0.rc5f-2
- Rebuild to pick up new libdevmapper.

* Fri Nov 26 2004 Heinz Mauelshagen <heinzm@redhat.com> 1.0.0.rc5f
- specfile cleanup

* Tue Aug 20 2004 Heinz Mauelshagen <heinzm@redhat.com> 1.0.0-rc4-pre1
- Removed make flag after fixing make.tmpl.in

* Tue Aug 18 2004 Heinz Mauelshagen <heinzm@redhat.com> 1.0.0-rc3
- Added make flag to prevent make 3.80 from looping infinitely

* Thu Jun 17 2004 Heinz Mauelshagen <heinzm@redhat.com> 1.0.0-pre1
- Created
