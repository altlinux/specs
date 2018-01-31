# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit 60170bfe8de166b2947ea2d604506f0bdfa0565c
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%ifarch x86_64
%global niarch x64
%endif
%ifarch %{ix86}
%global niarch x86
%endif
%ifarch %arm
%global niarch Arm
%endif


Name:           openni-primesense
Version:        5.1.6.6
Release:        alt2_9%{?gitrev}
Summary:        PrimeSensor/Kinect Modules for OpenNI
Group:          System/Libraries
License:        ASL 2.0
URL:            https://github.com/PrimeSense/Sensor

Source0:        https://github.com/PrimeSense/Sensor/archive/%{commit}/Sensor-%{commit}.tar.gz
Source1:        openni-primesense-55-primesense-usb.rules
Patch0:         openni-primesense-5.1.6.6-fedora.patch
Patch1:         openni-primesense-5.1.6.6-willowgarage.patch
Patch2:         openni-primesense-5.1.6.6-sse.patch
Patch3:         openni-primesense-5.1.6.6-softfloat.patch
ExclusiveArch:  %{ix86} x86_64 %{arm}

BuildRequires:  openni-devel >= 1.5.0.0, python
BuildRequires:  dos2unix
BuildRequires:  libjpeg-devel
Requires:       openni >= 1.5.0.0
Requires:       udev
Source44: import.info

%description
This modules enables OpenNI to make use of the PrimeSense, also known as
Kinect depth camera.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n Sensor-%{commit}
%patch0 -p0 -b .fedora
%patch1 -p0 -b .willow
%patch2 -p0 -b .sse
%patch3 -p0 -b .softfloat

#dos2unix LGPL.txt
rm -rf Source/External/LibJPEG
rm -rf Platform/Android Platform/Win32

%build
cd Platform/Linux/CreateRedist
# Add SSE_GENERATION=2 (or 3) to enable SSE
sed -i 's|make -j$(calc_jobs_number) -C ../Build|make -j$(calc_jobs_number) -C ../Build CFLAGS_EXT="%{optflags} -Wno-unknown-pragmas" LDFLAGS_EXT="%{optflags}" DEBUG=1|' RedistMaker
./RedistMaker


%install
pushd Platform/Linux/Redist/Sensor-Bin-Linux-%{niarch}-v%{version}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/
mkdir -p $RPM_BUILD_ROOT%{_bindir}
INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir}/ \
INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir}/ \
INSTALL_ETC=$RPM_BUILD_ROOT%{_sysconfdir}/openni/primesense/ \
SERVER_LOGS_DIR=$RPM_BUILD_ROOT%{_var}/log/primesense/ \
INSTALL_RULES=$RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/ \
./install.sh -n
popd

#mkdir $RPM_BUILD_ROOT%{_bindir}
#install -p -m 0755 Platform/Linux/Redist/Sensor-Bin-Linux-%{niarch}-v%{version}/Bin/XnSensorServer $RPM_BUILD_ROOT%{_bindir}/XnSensorServer

rm -rf $RPM_BUILD_ROOT%{_var}/log/primesense

rm $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/55-primesense-usb.rules
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/55-primesense-usb.rules


%post
if [ $1 == 1 ]; then
  niReg -r %{_libdir}/libXnDeviceSensorV2.so
  niReg -r %{_libdir}/libXnDeviceFile.so
fi


%preun
if [ $1 == 0 ]; then
  niReg -u %{_libdir}/libXnDeviceSensorV2.so
  niReg -u %{_libdir}/libXnDeviceFile.so
fi


%files
%doc LICENSE 
%dir %{_sysconfdir}/openni/primesense
%config(noreplace) %{_sysconfdir}/openni/primesense/*
%config(noreplace) %{_sysconfdir}/udev/rules.d/55-primesense-usb.rules
%{_libdir}/*.so
%{_bindir}/XnSensorServer

%changelog
* Wed Jan 31 2018 Igor Vlasenko <viy@altlinux.ru> 5.1.6.6-alt2_9
- to Sisyphus as opencv dependency

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.6.6-alt1_9
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.6.6-alt1_7
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 5.1.6.6-alt1_6
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 5.0.3.3-alt1_7
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 5.0.3.3-alt1_6
- initial fc import

