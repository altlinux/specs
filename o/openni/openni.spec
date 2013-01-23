# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: python-modules-xml python-devel
#define gitrev f8467404

Name:           openni
Version:        1.3.2.1
Release:        alt1_6
Summary:        Library for human-machine Natural Interaction

Group:          System/Libraries
License:        LGPLv3+ and BSD
URL:            http://www.openni.org
# No official releases, yet. To reproduce tarball (adapt version and gitrev):
# git clone git://github.com/OpenNI/OpenNI.git
# cd OpenNI.git
# rm -rf Platform/Win32 Platform/Android
# git archive --format tar --prefix=openni-1.3.2.1/ HEAD | gzip > ../openni-1.3.2.1.tar.gz
Source0:        openni-%{version}.tar.gz
Patch0:         openni-1.3.2.1-willow.patch
Patch1:         openni-1.3.2.1-fedora.patch
Patch2:         openni-1.3.2.1-disable-sse.patch
Patch3:         openni-1.3.2.1-silence-assert.patch
Patch4:         openni-1.3.2.1-fedora-java.patch
ExclusiveArch:  %{ix86} x86_64

BuildRequires:  libfreeglut-devel tinyxml-devel libjpeg-devel dos2unix libusb-devel
BuildRequires:  doxygen graphviz
Source44: import.info

%description
OpenNI (Open Natural Interaction) is a multi-language, cross-platform
framework that defines APIs for writing applications utilizing Natural
Interaction. OpenNI APIs are composed of a set of interfaces for writing NI
applications. The main purpose of OpenNI is to form a standard API that
enables communication with both:
 * Vision and audio sensors
 * Vision and audio perception middleware


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %%{name}-devel package contains libraries and header files for
developing applications that use %%{name}.


%package        java
Summary:        %{name} Java library
Group:          Development/C
Requires:       %{name} = %{version}-%{release}
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
Requires:       java
Requires:       jpackage-utils

%description    java
The %%{name}-java package contains a Java JNI library for
developing applications that use %%{name} in Java.


%package        doc
Summary:        API documentation for %{name}
Group:          Documentation
BuildArch:      noarch

%description    doc
The %%{name}-doc package contains the automatically generated API documentation
for OpenNI.


%package        examples
Summary:        Sample programs for %{name}
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}

%description    examples
The %%{name}-examples package contains example programs for OpenNI.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .willow
%patch1 -p1 -b .fedora
%patch2 -p1 -b .disable-sse
%patch3 -p1 -b .silence-assert
%patch4 -p1 -b .fedora-java

rm -rf Source/External
rm -rf Platform/Linux-x86/Build/Prerequisites/*
find Samples -name GL -prune -exec rm -rf {} \;
find Samples -name Libs -prune -exec rm -rf {} \;

for ext in c cpp; do
  find Samples -name "*.$ext" -exec \
    sed -i -e 's|#define SAMPLE_XML_PATH "../../../../Data/SamplesConfig.xml"|#define SAMPLE_XML_PATH "%{_sysconfdir}/%{name}/SamplesConfig.xml"|' {} \;
done

dos2unix README
dos2unix GPL.txt
dos2unix LGPL.txt

%build
cd Platform/Linux-x86/CreateRedist
# {?_smp_mflags} omitted, not supported by OpenNI Makefiles
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" DEBUG=1 \
./RedistMaker
#cat Output/BuildOpenNI.txt


%install
pushd Platform/Linux-x86/Redist
INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir} \
INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir} \
INSTALL_INC=$RPM_BUILD_ROOT%{_includedir}/ni \
INSTALL_VAR=$RPM_BUILD_ROOT%{_var}/lib/ni \
INSTALL_JAR=$RPM_BUILD_ROOT%{_libdir}/%{name} \
./install.sh -n

install -m 0755 Samples/Bin/Release/libSample-NiSampleModule.so $RPM_BUILD_ROOT%{_libdir}/libNiSampleModule.so
install -m 0755 Samples/Bin/Release/NiViewer $RPM_BUILD_ROOT%{_bindir}
install -m 0755 Samples/Bin/Release/Sample-NiAudioSample $RPM_BUILD_ROOT%{_bindir}/NiAudioSample
install -m 0755 Samples/Bin/Release/Sample-NiBackRecorder $RPM_BUILD_ROOT%{_bindir}/NiBackRecorder
install -m 0755 Samples/Bin/Release/Sample-NiConvertXToONI $RPM_BUILD_ROOT%{_bindir}/NiConvertXToONI
install -m 0755 Samples/Bin/Release/Sample-NiCRead $RPM_BUILD_ROOT%{_bindir}/NiCRead
install -m 0755 Samples/Bin/Release/Sample-NiRecordSynthetic $RPM_BUILD_ROOT%{_bindir}/NiRecordSynthetic
install -m 0755 Samples/Bin/Release/Sample-NiSimpleCreate $RPM_BUILD_ROOT%{_bindir}/NiSimpleCreate
install -m 0755 Samples/Bin/Release/Sample-NiSimpleRead $RPM_BUILD_ROOT%{_bindir}/NiSimpleRead
install -m 0755 Samples/Bin/Release/Sample-NiSimpleViewer $RPM_BUILD_ROOT%{_bindir}/NiSimpleViewer
install -m 0755 Samples/Bin/Release/Sample-NiUserTracker $RPM_BUILD_ROOT%{_bindir}/NiUserTracker

popd

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-doc
cp -a Source/DoxyGen/html/* $RPM_BUILD_ROOT%{_datadir}/%{name}-doc

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -p -m 0644 Data/SamplesConfig.xml $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_var}/lib/ni
echo "<Modules/>" > $RPM_BUILD_ROOT%{_var}/lib/ni/modules.xml


%post
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


%files
%doc LGPL.txt README
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_var}/lib/ni/modules.xml
%{_libdir}/*.so
%{_bindir}/ni*
%{_var}/lib/ni

%files devel
%doc Documentation/OpenNI_UserGuide.pdf
%{_includedir}/*
#{_libdir}/*.so

%files java
%{_libdir}/%{name}

%files examples
%config(noreplace) %{_sysconfdir}/%{name}/SamplesConfig.xml
%{_bindir}/Ni*
# not packaging any .desktop files for the sample applications. The
# applications will print relevant to the console and hence they are
# intended to be run on the console, not from the menu

%files doc
%{_datadir}/%{name}-doc


%changelog
* Wed Jan 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.2.1-alt1_6
- update to new release by fcimport

* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.2.1-alt1_5
- initial fc import

