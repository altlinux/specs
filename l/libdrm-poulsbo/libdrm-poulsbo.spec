%global oname libdrm

# Do not provide libdrm.so.*
%add_findprov_skiplist %_libdir/psb/*

Summary: Direct Rendering Manager runtime library (for Poulsbo)
Name: libdrm-poulsbo
Version: 2.3.0
Release: alt1.3
License: MIT
Group: System/Libraries
Url: http://ppa.launchpad.net/ubuntu-mobile/ubuntu/pool/main/libd/libdrm-poulsbo/
Packager: Anton V. Boyarshinov <boyarsh@altlinux.ru>

Source0: http://ppa.launchpad.net/ubuntu-mobile/ubuntu/pool/main/libd/libdrm-poulsbo/%{name}_%version.orig.tar.gz
# Extra sources are extracted from Ubuntu diff
Source1: psb_drm.h
Source2: psb_drv.h
Source3: psb_reg.h
Source4: psb_schedule.h
Patch0: libdrm-poulsbo_configure_debian.patch
Patch1: libdrm-poulsbo_headers_debian.patch
Patch2: libdrm-poulsbo-relocate_headers.patch
Patch3: libdrm-poulsbo_symbols.patch

ExclusiveArch: i586

BuildRequires: pkgconfig
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: kernel-headers
BuildRequires: libxcb-devel
BuildRequires: libudev-devel
# For the file we can't carry in both
Requires: libdrm

%description
Direct Rendering Manager runtime library. This build is specifically
for the xorg-drv-psb driver, for Intel Poulsbo graphics chipsets.

%package devel
Summary: Direct Rendering Manager development package
Group: Development/C

Requires: %name = %version-%release
Requires: pkgconfig

%description devel
Direct Rendering Manager development package. This build is
specifically for the xorg--drv-psb driver, for Intel Poulsbo
graphics chipsets.

%prep
%setup -q -n %oname-%version
install -m 0644 %SOURCE1 shared-core/
install -m 0644 %SOURCE2 shared-core/
install -m 0644 %SOURCE3 shared-core/
install -m 0644 %SOURCE4 shared-core/
%patch0 -p1
%patch1 -p1 -b .headers
%patch2 -p1 -b .relocate
%patch3 -p2

%build
autoreconf -i
%configure --libdir=%_libdir/psb
make %{?_smp_mflags}

%install
rm -rf %buildroot
make install DESTDIR=%buildroot
# SUBDIRS=libdrm
mkdir -p %buildroot%_sysconfdir/udev/rules.d/

# NOTE: We intentionally don't ship *.la files
find %buildroot -type f -name '*.la' | xargs rm -f -- || :
for i in i915 mach64 mga nouveau r128 radeon savage sis via; do rm -f %buildroot%_includedir/psb/drm/$i"_drm.h"; done
for i in drm_sarea.h r300_reg.h via_3d_reg.h
do
rm -f %buildroot%_includedir/psb/drm/$i
done

# clean up for relocation
mkdir -p %buildroot%_libdir/pkgconfig
mv %buildroot%_libdir/psb/pkgconfig/libdrm.pc %buildroot%_libdir/pkgconfig/libdrm-poulsbo.pc
mkdir -p %buildroot%_sysconfdir/ld.so.conf.d
cat > %buildroot%_sysconfdir/ld.so.conf.d/psb.conf << EOF
%_libdir/psb
EOF


%files
%doc MIT_License.txt README
%_libdir/psb/libdrm.so.2
%_libdir/psb/libdrm.so.2.3.0
%config %_sysconfdir/ld.so.conf.d/psb.conf

%files devel
%doc MIT_License.txt
%_includedir/psb
%_libdir/psb/libdrm.so
%_libdir/pkgconfig/libdrm-poulsbo.pc

%changelog
* Wed Jul 14 2010 Alexey I. Froloff <raorn@altlinux.org> 2.3.0-alt1.3
- NMU:
  + REALLY do not provide libdrm.so.2

* Mon Jun 28 2010 Alexey I. Froloff <raorn@altlinux.org> 2.3.0-alt1.2
- NMU:
  + Do not provide libdrm.so.2 (conflicts with libdrm package)

* Thu Jun 24 2010 Alexey I. Froloff <raorn@altlinux.org> 2.3.0-alt1.1
- NMU:
  + Add version information to libdrm.so.2 (closes: #23653)

* Fri Jun 04 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.3.0-alt1
- build for Sisyphus

* Mon Aug 24 2009 Adam Williamson <awilliam@redhat.com> 2.3.0-9
- correct exclusivearch for rpmfusion buildsystem
- don't install 91-drm-modeset.rules only to delete it later

* Thu Aug 20 2009 Adam Williamson <awilliam@redhat.com> 2.3.0-8
- exclusivearch ix86 (there's no 64-bit poulsbo hardware)
- mark config file as config

* Wed Aug 19 2009 Adam Williamson <awilliam@redhat.com> 2.3.0-7
- put the license in as documentation

* Tue Aug 11 2009 Adam Williamson <awilliam@redhat.com> 2.3.0-6
- The Let's Stop Smoking Crack release: move the library to libdir/psb
  and use an ld.so.conf.d file, thus avoiding all the obsoletes /
  provides tomfoolery and co-existing peacefully with main libdrm
  thanks lkundrak for the suggestion

* Mon Aug 10 2009 Adam Williamson <awilliam@redhat.com> 2.3.0-5
- more outrageous lies in the -devel package

* Mon Aug 10 2009 Adam Williamson <awilliam@redhat.com> 2.3.0-4
- use ldconfig -X in %post and %postun to (hopefully) work around the
  nasty #513224 in normal use of these packages (this should be the
  only library installed in the initial transaction people use)

* Mon Aug 10 2009 Adam Williamson <awilliam@redhat.com> 2.3.0-3
- lie outrageously about what we provide to satisfy some dependencies

* Mon Aug 10 2009 Adam Williamson <awilliam@redhat.com> 2.3.0-2
- obsolete / provide regular libdrm

* Wed May 13 2009 Adam Williamson <awilliam@redhat.com> 2.3.0-1
- initial poulsbo libdrm package (from ubuntu-mobile repos)

