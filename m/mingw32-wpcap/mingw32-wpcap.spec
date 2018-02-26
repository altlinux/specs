BuildRequires: rpm-build-mingw32
# one of the sources is a zip file
BuildRequires: unzip
BuildRequires: gcc-c++
%define version 4.1.final2
%define name mingw32-wpcap
%global versionmajor 4
%global versionminor 1
%global versionsuffix 2

%global wpcapexamples %{_docdir}/%{name}/examples
%global wpcapdoc %{_docdir}/%{name}

Name:           mingw32-wpcap
Version:        %{versionmajor}.%{versionminor}.final%{versionsuffix}
Release:        alt1_2
Summary:        MinGW user-level packet capture

Group:          System/Libraries
License:        BSD with advertising
URL:            http://www.winpcap.org/
Source0:        http://www.winpcap.org/install/bin/WpcapSrc_%{versionmajor}_%{versionminor}_%{versionsuffix}.zip
Source1:        wpcap.pc
Patch0:         wpcap.patch
BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 52
BuildRequires:  mingw32-gcc
BuildRequires:  doxygen
BuildRequires:  unzip
BuildRequires:  dos2unix
BuildRequires:  bison
BuildRequires:  flex
Requires:       mingw32-filesystem >= 50
Source44: import.info

%description
MinGW Windows pcap library.

%package examples
Summary:        Example source code for MinGW pcap
Group:          System/Libraries
Requires:       %{name} = %{version}

%description examples
This package contains examples on the usage of the Windows pcap
library.

%package docs
Summary:        MinGW pcap documentation
Group:          System/Libraries
Requires:       %{name} = %{version}

%description docs
This package contains the Windows pcap library documentation.


%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}



%prep
%setup -q -n winpcap

%patch0 -p0 -b .build

find . -type f -print0 |xargs -0 dos2unix
pushd wpcap/libpcap/Win32/Include/
mv ip6_misc.h IP6_misc.h
popd

%build
pushd packetNtx/Dll/Project
make -f GNUmakefile CC=i586-pc-mingw32-gcc YACC=bison %{?_smp_mflags} 
popd
pushd wpcap/PRJ
make -f GNUmakefile CC=i586-pc-mingw32-gcc YACC=bison %{?_smp_mflags} 
popd
pushd dox/prj
doxygen winpcap_noc.dox
popd


%install
install -d $RPM_BUILD_ROOT/%{_mingw32_bindir}
install -d $RPM_BUILD_ROOT/%{_mingw32_libdir}/pkgconfig
install -m0644 %{SOURCE1} $RPM_BUILD_ROOT/%{_mingw32_libdir}/pkgconfig
install -m0644 packetNtx/Dll/Project/libpacket.a $RPM_BUILD_ROOT/%{_mingw32_libdir}/libpacket.dll.a
install -m0644 packetNtx/Dll/Project/Packet.dll $RPM_BUILD_ROOT/%{_mingw32_bindir}/packet.dll
install -m0644 wpcap/lib/libwpcap.a $RPM_BUILD_ROOT/%{_mingw32_libdir}/libwpcap.dll.a
install -m0644 wpcap/PRJ/wpcap.dll $RPM_BUILD_ROOT/%{_mingw32_bindir}
install -m0644 packetNtx/Dll/Packet.def $RPM_BUILD_ROOT/%{_mingw32_libdir}/packet.def
install -m0644 wpcap/PRJ/WPCAP.DEF $RPM_BUILD_ROOT/%{_mingw32_libdir}/wpcap.def
install -d $RPM_BUILD_ROOT/%{_mingw32_includedir}/wpcap/pcap
install -m0644 wpcap/libpcap/pcap/*.h $RPM_BUILD_ROOT/%{_mingw32_includedir}/wpcap/pcap
install -m0644 wpcap/libpcap/pcap.h $RPM_BUILD_ROOT/%{_mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/pcap-int.h $RPM_BUILD_ROOT/%{_mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/pcap-bpf.h $RPM_BUILD_ROOT/%{_mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/pcap-namedb.h $RPM_BUILD_ROOT/%{_mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/remote-ext.h $RPM_BUILD_ROOT/%{_mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/pcap-stdinc.h $RPM_BUILD_ROOT/%{_mingw32_includedir}/wpcap/
install -m0644 wpcap/Win32-Extensions/Win32-Extensions.h $RPM_BUILD_ROOT/%{_mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/Win32/Include/bittypes.h $RPM_BUILD_ROOT/%{_mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/Win32/Include/IP6_misc.h $RPM_BUILD_ROOT/%{_mingw32_includedir}/wpcap/
install -m0644 wpcap/libpcap/Win32/Include/Gnuc.h $RPM_BUILD_ROOT/%{_mingw32_includedir}/wpcap/
install -m0644 Common/Packet32.h $RPM_BUILD_ROOT/%{_mingw32_includedir}/wpcap/
install -d $RPM_BUILD_ROOT/%{wpcapdoc}/html
install -m0644 dox/WinPcap_docs.html $RPM_BUILD_ROOT/%{wpcapdoc}/
install -m0644 dox/prj/docs/* $RPM_BUILD_ROOT/%{wpcapdoc}/html
install -m0644 dox/pics/*.gif $RPM_BUILD_ROOT/%{wpcapdoc}/html
install -m0644 dox/*.gif $RPM_BUILD_ROOT/%{wpcapdoc}/html
install -d $RPM_BUILD_ROOT/%{wpcapexamples}
install -d $RPM_BUILD_ROOT/%{wpcapexamples}
cp -r Examples $RPM_BUILD_ROOT/%{wpcapexamples}/remote
cp -r Examples-pcap $RPM_BUILD_ROOT/%{wpcapexamples}/pcap
rm -rf $RPM_BUILD_ROOT/%{wpcapexamples}/remote/NetMeter
rm -rf $RPM_BUILD_ROOT/%{wpcapexamples}/remote/kdump
rm -rf $RPM_BUILD_ROOT/%{wpcapexamples}/pcap/winpcap_stress
rm -rf $RPM_BUILD_ROOT/%{wpcapexamples}/pcap/stats


%files
%doc wpcap/libpcap/LICENSE
%{_mingw32_libdir}/pkgconfig/wpcap.pc
%{_mingw32_bindir}/packet.dll
%{_mingw32_bindir}/wpcap.dll
%{_mingw32_libdir}/libpacket.dll.a
%{_mingw32_libdir}/libwpcap.dll.a
%{_mingw32_libdir}/packet.def
%{_mingw32_libdir}/wpcap.def
%{_mingw32_includedir}/wpcap

%files docs
%{wpcapdoc}/WinPcap_docs.html
%{wpcapdoc}/html

%files examples
%{wpcapexamples}

%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 4.1.final2-alt1_2
- initial release by fcimport

