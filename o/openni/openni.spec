Group: System/Libraries
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global commit 1e9524ffd759841789dadb4ca19fb5d4ac5820e7
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


Name:           openni
Version:        1.5.7.10
Release:        alt2_30
Summary:        Library for human-machine Natural Interaction

License:        ASL 2.0 and BSD
URL:            http://www.openni.org
# To reproduce tarball (adapt version and shortcommit):
# wget https://github.com/OpenNI/OpenNI/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
# tar xvf openni-%{version}-%{shortcommit}.tar.gz
# cd OpenNI-%{commit}
# rm -rf Platform/Win32 Platform/Android Platform/ARC
# cd ..
# tar czf openni-%{version}-%{shortcommit}-fedora.tar.gz OpenNI-%{commit}
Source0:        openni-%{version}-%{shortcommit}-fedora.tar.gz
Source1:        libopenni.pc
Patch0:         openni-1.5.7.10-willow.patch
Patch1:         openni-1.5.7.10-fedora.patch
Patch2:         openni-1.5.2.23-disable-sse.patch
Patch3:         openni-1.3.2.1-silence-assert.patch
Patch4:         openni-1.3.2.1-fedora-java.patch
Patch5:         openni-1.5.2.23-disable-softfloat.patch
Patch6:         openni-1.5.2.23-armsamples.patch
Patch7:         openni-1.5.7.10-rename-equivalent-for-gcc6.patch
Patch8:         openni-freeglut.patch
# Fix compilation with -ansi or -std options
# https://github.com/OpenNI/OpenNI/commit/ca99f6181234c682bba42a6ba988cc10cee894d7
Patch9:         openni-ansi.patch

Patch10:        python3.patch

ExclusiveArch:  %{ix86} x86_64 %{arm}

BuildRequires:  gcc-c++
BuildRequires:  libfreeglut-devel, tinyxml-devel, libjpeg-devel, dos2unix, libusb-devel
BuildRequires:  python3, doxygen graphviz libgraphviz
Source44: import.info
Patch33: openni-1.5.7.10-alt-armh.patch

%description
OpenNI (Open Natural Interaction) is a multi-language, cross-platform
framework that defines APIs for writing applications utilizing Natural
Interaction. OpenNI APIs are composed of a set of interfaces for writing NI
applications. The main purpose of OpenNI is to form a standard API that
enables communication with both:
 * Vision and audio sensors
 * Vision and audio perception middleware


%package        devel
Group: Development/Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        java
Group: Development/Other
Summary:        %{name} Java library
Requires:       %{name} = %{version}-%{release}
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
Requires:       java-headless
Requires:       jpackage-utils

%description    java
The %{name}-java package contains a Java JNI library for
developing applications that use %{name} in Java.


%package        doc
Group: Documentation
Summary:        API documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the automatically generated API documentation
for OpenNI.


%package        examples
Group: Development/Tools
Summary:        Sample programs for %{name}
Requires:       %{name} = %{version}-%{release}

%description    examples
The %{name}-examples package contains example programs for OpenNI.

%prep
%setup -q -n OpenNI-%{commit}
%patch0 -p1 -b .willow
%patch1 -p1 -b .fedora
%patch2 -p1 -b .disable-sse
%patch3 -p1 -b .silence-assert
%patch4 -p1 -b .fedora-java
%patch5 -p1 -b .disable-softfloat
%patch6 -p1 -b .armsamples
%patch7 -p1 -b .rename-equivalent-for-gcc6
%patch8 -p0 -b .freeglut
%patch9 -p1 -b .ansi
dos2unix Platform/Linux/CreateRedist/Redist_OpenNi.py
%patch10 -p1 -b python3
rm -rf Source/External
rm -rf Platform/Linux/Build/Prerequisites/*
find Samples -name GL -prune -exec rm -rf {} \;
find Samples -name Libs -prune -exec rm -rf {} \;

for ext in c cpp; do
  find Samples -name "*.$ext" -exec \
    sed -i -e 's|#define SAMPLE_XML_PATH "../../../../Data/SamplesConfig.xml"|#define SAMPLE_XML_PATH "%{_sysconfdir}/%{name}/SamplesConfig.xml"|' {} \;
done

sed -i 's|python|python3|' Platform/Linux/CreateRedist/RedistMaker
sed -i 's|if (os.path.exists("/usr/bin/gmcs"))|if (0)|' Platform/Linux/CreateRedist/Redist_OpenNi.py

dos2unix README
dos2unix LICENSE
%patch33 -p1

%build
cd Platform/Linux/CreateRedist
# {?_smp_mflags} omitted, not supported by OpenNI Makefiles
chmod +x RedistMaker RedistMaker.Arm

CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" DEBUG=1 \
%ifarch %arm
./RedistMaker.Arm || cat Output/BuildOpenNI.txt
%else
./RedistMaker
%endif
cat Output/BuildOpenNI.txt


%install
pushd Platform/Linux/Redist/OpenNI-Bin-Dev-Linux-%{niarch}-v%{version}
INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir} \
INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir} \
INSTALL_INC=$RPM_BUILD_ROOT%{_includedir}/ni \
INSTALL_VAR=$RPM_BUILD_ROOT%{_var}/lib/ni \
INSTALL_JAR=$RPM_BUILD_ROOT%{_libdir}/%{name} \
./install.sh -n

install -m 0755 Samples/Bin/%{niarch}-Release/libSample-NiSampleModule.so $RPM_BUILD_ROOT%{_libdir}/libNiSampleModule.so
install -m 0755 Samples/Bin/%{niarch}-Release/NiViewer $RPM_BUILD_ROOT%{_bindir}
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiAudioSample $RPM_BUILD_ROOT%{_bindir}/NiAudioSample
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiBackRecorder $RPM_BUILD_ROOT%{_bindir}/NiBackRecorder
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiConvertXToONI $RPM_BUILD_ROOT%{_bindir}/NiConvertXToONI
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiCRead $RPM_BUILD_ROOT%{_bindir}/NiCRead
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiRecordSynthetic $RPM_BUILD_ROOT%{_bindir}/NiRecordSynthetic
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiSimpleCreate $RPM_BUILD_ROOT%{_bindir}/NiSimpleCreate
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiSimpleRead $RPM_BUILD_ROOT%{_bindir}/NiSimpleRead
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiSimpleViewer $RPM_BUILD_ROOT%{_bindir}/NiSimpleViewer
install -m 0755 Samples/Bin/%{niarch}-Release/Sample-NiUserTracker $RPM_BUILD_ROOT%{_bindir}/NiUserTracker

popd

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -p -m 0644 Data/SamplesConfig.xml $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_var}/lib/ni
touch $RPM_BUILD_ROOT%{_var}/lib/ni/modules.xml

mkdir -p %{buildroot}%{_libdir}/pkgconfig
sed -e 's![@]prefix[@]!%{_prefix}!g' \
    -e 's![@]exec_prefix[@]!%{_exec_prefix}!g' \
    -e 's![@]libdir[@]!%{_libdir}!g' \
    -e 's![@]includedir[@]!%{_includedir}!g' \
    -e 's![@]version[@]!%{version}!g' \
    %{SOURCE1} > %{buildroot}%{_libdir}/pkgconfig/libopenni.pc
for rpm404_ghost in %{_var}/lib/ni/modules.xml
do
    mkdir -p %buildroot`dirname "$rpm404_ghost"`
    touch %buildroot"$rpm404_ghost"
done

# hack for error (#100): non-identical noarch packages
find Source/DoxyGen/html -name '*.dot' -delete


%post
%{?ldconfig}
if [ $1 == 1 ]; then
  niReg -r %{_libdir}/libnimMockNodes.so
  niReg -r %{_libdir}/libnimCodecs.so
  niReg -r %{_libdir}/libnimRecorder.so
fi


%preun
if [ $1 == 0 ]; then
  niReg -u %{_libdir}/libnimMockNodes.so
  niReg -u %{_libdir}/libnimCodecs.so
  niReg -u %{_libdir}/libnimRecorder.so
fi


: 

%files
%doc LICENSE README NOTICE CHANGES
%dir %{_sysconfdir}/%{name}
%dir %{_var}/lib/ni
%ghost %{_var}/lib/ni/modules.xml
%{_libdir}/*.so
%{_bindir}/ni*

%files devel
%doc Documentation/OpenNI_UserGuide.pdf
%{_includedir}/*
%{_libdir}/pkgconfig/libopenni.pc

%files java
%{_libdir}/%{name}

%files examples
%config(noreplace) %{_sysconfdir}/%{name}/SamplesConfig.xml
%{_bindir}/Ni*
# not packaging any .desktop files for the sample applications. The
# applications will print relevant to the console and hence they are
# intended to be run on the console, not from the menu

%files doc
%doc Source/DoxyGen/html


%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 1.5.7.10-alt2_30
- update to new release by fcimport (restored build on %{ix86})

* Sat Feb 27 2021 Igor Vlasenko <viy@altlinux.org> 1.5.7.10-alt2_23
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 1.5.7.10-alt2_21
- update to new release by fcimport

* Sun Dec 08 2019 Igor Vlasenko <viy@altlinux.ru> 1.5.7.10-alt2_17
- fixed build

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.5.7.10-alt2_13
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.5.7.10-alt2_11
- update to new release by fcimport

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.7.10-alt2_6
- Fixed build with gcc-6

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.5.7.10-alt1_6
- update to new release by fcimport

* Tue Jan 13 2015 Igor Vlasenko <viy@altlinux.ru> 1.5.7.10-alt1_4
- update to new release by fcimport

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.2.1-alt1_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.2.1-alt1_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.2.1-alt1_7
- update to new release by fcimport

* Wed Jan 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.2.1-alt1_6
- update to new release by fcimport

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.2.1-alt1_5
- initial fc import

