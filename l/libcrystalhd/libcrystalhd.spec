# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libcrystalhd-devel
# END SourceDeps(oneline)
BuildRequires(pre): kernel-build-tools
%add_optflags %optflags_shared
%global majorminor 1.0
%global date 20120405
# Avoid to emit gstreamer provides - rhbz#1184975
%undefine __gstreamer1_provides

Summary:       Broadcom Crystal HD device interface library
Name:          libcrystalhd
Version:       3.10.0
Release:       alt3_12
License:       LGPLv2
Group:         System/Libraries
URL:           http://www.broadcom.com/support/crystal_hd/
ExcludeArch:   s390 s390x

#Source:       http://www.broadcom.com/docs/support/crystalhd/crystalhd_linux_20100703.zip
# This tarball and README are inside the above zip file...
# Patch generated from http://git.linuxtv.org/jarod/crystalhd.git
Source0:       libcrystalhd-%{date}.tar.bz2
Source1:       README_07032010
# We're going to use even newer firmware for now
Source2:       bcm70012fw.bin
Source3:       bcm70015fw.bin
# LICENSE file is copy-n-pasted from http://www.broadcom.com/support/crystal_hd/
Source4:       LICENSE
Source5:       libcrystalhd-snapshot.sh
Patch0:        libcrystalhd-nosse2.patch
# https://patchwork2.kernel.org/patch/2247431/
Patch1:        crystalhd-gst-Port-to-GStreamer-1.0-API.patch

BuildRequires: autoconf automake libtool
BuildRequires: gstreamer1.0-devel >= %{majorminor}
BuildRequires: gst-plugins1.0-devel >= %{majorminor}
Requires:      firmware-crystalhd
Source44: import.info
Patch33: libcrystalhd-alt-from-zerg-bug30916.patch

%description
The libcrystalhd library provides userspace access to Broadcom Crystal HD
video decoder devices. The device supports hardware decoding of MPEG-2,
h.264 and VC1 video codecs, up to 1080p at 40fps for the first-generation
bcm970012 hardware, and up to 1080p at 60fps for the second-generation
bcm970015 hardware.

%package devel
Summary:       Development libs for libcrystalhd
Group:         Development/C
Requires:      %{name} = %{version}

%description devel
Development libraries needed to build applications against libcrystalhd.

%package -n firmware-crystalhd
Summary:       Firmware for the Broadcom Crystal HD video decoder
License:       Redistributable, no modification permitted
BuildArch:     noarch
Group:         System/Kernel and hardware
Requires:      %{name} = %{version}

%description -n firmware-crystalhd
Firmwares for the Broadcom Crystal HD (bcm970012 and bcm970015)
video decoders.

%package -n gstreamer-plugin-crystalhd
Summary:       Gstreamer crystalhd decoder plugin
Group:         Sound
Requires:      %{name} = %{version}
Requires:      gst-plugins-base1.0

%description -n gstreamer-plugin-crystalhd
Gstreamer crystalhd decoder plugin

%package -n kernel-source-crystalhd
Summary: Linux crystalhd  Broadcom module sources
Group: Development/Kernel
BuildArch: noarch

%description -n kernel-source-crystalhd
Crystalhd module sources for Linux kernel.


%prep
%setup -q -n libcrystalhd-%{date}
cp %{SOURCE1} %{SOURCE4} .
%ifnarch %{ix86} ia64 x86_64
%patch0 -p1 -b .nosse2
sed -i -e 's|-msse2||' linux_lib/libcrystalhd/Makefile
%endif
%patch1 -p1 -b .gst1
%patch33 -p1

%build
pushd linux_lib/libcrystalhd/ > /dev/null 2>&1
# FIXME: this doesn't work just yet...
#make CPPFLAGS="%{optflags}" %{?_smp_mflags}
make %{?_smp_mflags}
popd > /dev/null 2>&1

pushd filters/gst/gst-plugin/ > /dev/null 2>&1
sh autogen.sh || :

%configure
make %{?_smp_mflags} \
  CFLAGS="-I%{_builddir}/%{buildsubdir}/include -I%{_builddir}/%{buildsubdir}/linux_lib/libcrystalhd" \
  BCMDEC_LDFLAGS="-L%{_builddir}/%{buildsubdir}/linux_lib/libcrystalhd -lcrystalhd"
popd > /dev/null 2>&1

%install
pushd linux_lib/libcrystalhd/ > /dev/null 2>&1
make install LIBDIR=%{_libdir} DESTDIR=$RPM_BUILD_ROOT
popd > /dev/null 2>&1

pushd filters/gst/gst-plugin/ > /dev/null 2>&1
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/libgstbcmdec.{a,la}
popd > /dev/null 2>&1

rm -rf $RPM_BUILD_ROOT/lib/firmware/
mkdir -p $RPM_BUILD_ROOT/lib/firmware/
cp -p %{SOURCE2} $RPM_BUILD_ROOT/lib/firmware/
cp -p %{SOURCE3} $RPM_BUILD_ROOT/lib/firmware/

#Install udev rule
mkdir -p $RPM_BUILD_ROOT%{_udevrulesdir}
install -pm 0644 driver/linux/20-crystalhd.rules \
  $RPM_BUILD_ROOT%{_udevrulesdir}

mv driver kernel-source-crystalhd-%version
%__mkdir_p %kernel_srcdir/
%__tar jcf %kernel_srcdir/kernel-source-crystalhd-%version.tar.bz2 kernel-source-crystalhd-%version/



%files
%doc README_07032010 LICENSE
%{_libdir}/libcrystalhd.so.*

%files devel
%dir %{_includedir}/libcrystalhd
%{_includedir}/libcrystalhd/*
%{_libdir}/libcrystalhd.so

%files -n firmware-crystalhd
%doc LICENSE
%{_udevrulesdir}/20-crystalhd.rules
/lib/firmware/bcm70012fw.bin
/lib/firmware/bcm70015fw.bin

%files -n gstreamer-plugin-crystalhd
%{_libdir}/gstreamer-%{majorminor}/*.so

%files -n kernel-source-crystalhd
/usr/src/kernel/sources/*



%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 3.10.0-alt3_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.10.0-alt3_11
- update to new release by fcimport

* Wed Apr 08 2015 Igor Vlasenko <viy@altlinux.ru> 3.10.0-alt3_8
- rules: MODE="0660", GROUP="video" (closes: #30916)

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.10.0-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.10.0-alt2_7
- update to new release by fcimport

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.10.0-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 3.10.0-alt2_5
- update to new release by fcimport

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 3.10.0-alt2_4
- merged kernel-source-crystalhd into hook

* Fri Jul 05 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.10.0-alt2
- packaging kernel-source-crystalhd added

* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 3.10.0-alt1_4.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * udev-files-in-etc for firmware-crystalhd

* Tue Apr 16 2013 Igor Vlasenko <viy@altlinux.ru> 3.10.0-alt1_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.10.0-alt1_3
- update to new release by fcimport

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 3.10.0-alt1_2
- new release

* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2_1.1
- Fixed build

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.1-alt2_1
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.1-alt1_1
- initial import by fcimport

