# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libcrystalhd-devel
# END SourceDeps(oneline)
%global date 20120405

Summary:        Broadcom Crystal HD device interface library
Name:           libcrystalhd
Version:        3.10.0
Release:        alt1_2
License:        LGPLv2
Group:          System/Libraries
#Source:         http://www.broadcom.com/docs/support/crystalhd/crystalhd_linux_20100703.zip
# This tarball and README are inside the above zip file...
# Patch generated from http://git.linuxtv.org/jarod/crystalhd.git
Source0:        libcrystalhd-%{date}.tar.bz2
Source1:        README_07032010
# We're going to use even newer firmware for now
Source2:        bcm70012fw.bin
Source3:        bcm70015fw.bin
# LICENSE file is copy-n-pasted from http://www.broadcom.com/support/crystal_hd/
Source4:        LICENSE
Source9:        libcrystalhd-snapshot.sh
Patch0:         libcrystalhd-nosse2.patch
URL:            http://www.broadcom.com/support/crystal_hd/
ExcludeArch:    s390 s390x
BuildRequires:  autoconf automake libtool
Requires:       firmware-crystalhd
Source44: import.info

%description
The libcrystalhd library provides userspace access to Broadcom Crystal HD
video decoder devices. The device supports hardware decoding of MPEG-2,
h.264 and VC1 video codecs, up to 1080p at 40fps for the first-generation
bcm970012 hardware, and up to 1080p at 60fps for the second-generation
bcm970015 hardware.

%package devel
Summary:       Development libs for libcrystalhd
Group:         Development/C
Requires:      libcrystalhd = %{version}-%{release}

%description devel
Development libraries needed to build applications against libcrystalhd.

%package -n firmware-crystalhd
Summary:       Firmware for the Broadcom Crystal HD video decoder
License:       Redistributable, no modification permitted
BuildArch:     noarch
Group:         System/Kernel and hardware
Requires:      libcrystalhd = %{version}-%{release}

%description -n firmware-crystalhd
Firmwares for the Broadcom Crystal HD (bcm970012 and bcm970015)
video decoders.

%define        majorminor 0.10
%define        _gst 0.10.30
%define        _gstpb 0.10.30

%package -n gstreamer-plugin-crystalhd
Summary:       Gstreamer crystalhd decoder plugin
Group:         Sound
Requires:      libcrystalhd = %{version}-%{release}
Requires:      gst-plugins-base
BuildRequires: gstreamer-devel >= %{_gst}
BuildRequires: gst-plugins-devel >= %{_gstpb}

%description -n gstreamer-plugin-crystalhd
Gstreamer crystalhd decoder plugin

%prep
%setup -q -n libcrystalhd-%{date}
cp %{SOURCE1} %{SOURCE4} .
%ifnarch %{ix86} ia64 x86_64
%patch0 -p1 -b .nosse2
sed -i -e 's|-msse2||' linux_lib/libcrystalhd/Makefile
%endif

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
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/libgstbcmdec.{a,la}
popd > /dev/null 2>&1
rm -rf $RPM_BUILD_ROOT/lib/firmware/
mkdir -p $RPM_BUILD_ROOT/lib/firmware/
cp -p %{SOURCE2} $RPM_BUILD_ROOT/lib/firmware/
cp -p %{SOURCE3} $RPM_BUILD_ROOT/lib/firmware/
#Install udev rule
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d
install -pm 0644 driver/linux/20-crystalhd.rules \
  $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d


%files
%doc README_07032010 LICENSE
%{_libdir}/libcrystalhd.so.*

%files devel
%dir %{_includedir}/libcrystalhd
%{_includedir}/libcrystalhd/*
%{_libdir}/libcrystalhd.so

%files -n firmware-crystalhd
%doc LICENSE
%config %{_sysconfdir}/udev/rules.d/20-crystalhd.rules
/lib/firmware/bcm70012fw.bin
/lib/firmware/bcm70015fw.bin

%files -n gstreamer-plugin-crystalhd
%{_libdir}/gstreamer-%{majorminor}/*.so


%changelog
* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 3.10.0-alt1_2
- new release

* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt2_1.1
- Fixed build

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.1-alt2_1
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.1-alt1_1
- initial import by fcimport

