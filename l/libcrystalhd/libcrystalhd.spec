# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary:        Broadcom Crystal HD device interface library
Name:           libcrystalhd
Version:        3.5.1
Release:        alt2_1
License:        LGPLv2
Group:          System/Libraries
#Source:         http://www.broadcom.com/docs/support/crystalhd/crystalhd_linux_20100703.zip
# This tarball and README are inside the above zip file...
Source0:        crystalhd_07032010.tbz2
Source1:        README_07032010
# We're going to use even newer firmware for now
Source2:        bcm70012fw.bin
Source3:        bcm70015fw.bin
# LICENSE file is copy-n-pasted from http://www.broadcom.com/support/crystal_hd/
Source4:        LICENSE
Requires:       firmware-crystalhd
URL:            http://www.broadcom.com/support/crystal_hd/
# Patch generated from http://git.wilsonet.com/crystalhd.git/
Patch0:         libcrystalhd-updates.patch
ExcludeArch:    s390 s390x
BuildRequires:  autoconf automake
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
Requires:      %{name} = %{version}-%{release}

%description devel
Development libraries needed to build applications against libcrystalhd.

%package -n firmware-crystalhd
Summary:       Firmware for the Broadcom Crystal HD video decoder
License:       Redistributable, no modification permitted
BuildArch:     noarch
Group:         System/Kernel and hardware
Requires:      %{name} = %{version}-%{release}

%description -n firmware-crystalhd
Firmwares for the Broadcom Crystal HD (bcm970012 and bcm970015)
video decoders.

%define        majorminor 0.10
%define        _gst 0.10.30
%define        _gstpb 0.10.30

%package -n gstreamer-plugin-crystalhd
Summary:       Gstreamer crystalhd decoder plugin
Group:         Sound
Requires:      %{name} = %{version}-%{release}
Requires:      gst-plugins-base
BuildRequires: gstreamer-devel >= %{_gst}
BuildRequires: gst-plugins-devel >= %{_gstpb}

%description -n gstreamer-plugin-crystalhd
Gstreamer crystalhd decoder plugin

%prep
%setup -q -n 07032010
%patch0 -p1
cp %{SOURCE1} %{SOURCE4} .

%build
pushd linux_lib/libcrystalhd/ > /dev/null 2>&1
# FIXME: this doesn't work just yet...
#make CPPFLAGS="%{optflags}" %{?_smp_mflags}
make %{?_smp_mflags}
popd > /dev/null 2>&1
pushd filters/gst/gst-plugin/ > /dev/null 2>&1
%configure
make %{?_smp_mflags}
popd > /dev/null 2>&1

%install
pushd linux_lib/libcrystalhd/ > /dev/null 2>&1
make install LIBDIR=%{_libdir} DESTDIR=$RPM_BUILD_ROOT
popd > /dev/null 2>&1
pushd filters/gst/gst-plugin/ > /dev/null 2>&1
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/libgstbcmdec.{a,la}
popd > /dev/null 2>&1
cp -p %{SOURCE2} $RPM_BUILD_ROOT/lib/firmware/
cp -p %{SOURCE3} $RPM_BUILD_ROOT/lib/firmware/

%files
%doc README_07032010 LICENSE
%{_libdir}/libcrystalhd.so.*

%files devel
%dir %{_includedir}/libcrystalhd
%{_includedir}/libcrystalhd/*
%{_libdir}/libcrystalhd.so

%files -n firmware-crystalhd
%doc LICENSE
/lib/firmware/bcm70012fw.bin
/lib/firmware/bcm70015fw.bin

%files -n gstreamer-plugin-crystalhd
%{_libdir}/gstreamer-%{majorminor}/*.so


%changelog
* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.1-alt2_1
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 3.5.1-alt1_1
- initial import by fcimport

