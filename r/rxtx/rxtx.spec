# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name rxtx
%define version 2.2
#global upver	2.1
#global uprel	7r2
#global rel	0.8

%global upver	2.2
%global uprel	20100211
%global rel	0.14

#global jni	%{_jnidir}
%global jni	%{_libdir}/%{name}

Summary:	Parallel communication for the Java Development Toolkit
Name:		rxtx
Version:	%{upver}
Release:	alt3_0.14.20100211.3jpp8
License:	LGPLv2+
Group:		System/Libraries
URL:		http://rxtx.qbang.org/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  cvs -d:pserver:anonymous@qbang.org:/var/cvs/cvsroot co -r commapi-0-0-1 -D "2010-02-11" -d rxtx-%{uprel} rxtx-devel
#  tar cjvf rxtx-%{uprel}.tar.bz2 --exclude CVS --exclude .cvsignore rxtx-%{uprel}
Source:		%{name}-%{uprel}.tar.bz2
#Source:		http://rxtx.qbang.org/pub/rxtx/%{name}-%{upver}-%{uprel}.tgz
Source1:	README.fedora
Patch1:		rxtx-2.2-loadlibrary.patch
Patch2:		rxtx-2.2-no-io.h.patch
Patch3:		rxtx-2.2-fhs_lock.patch
Patch4:		rxtx-2.2-lock.patch
Patch5:		rxtx-2.2-Add-Arduino-driver-ttyACM-rxtxcomm-as-device.patch
Patch6:		rxtx-2.2-java-version-fix.patch
Patch7:         rxtx-2.2-convert-strcpy-to-strncpy.patch

#BuildRequires:	java-devel >= 1:1.6.0
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:	libtool-common automake-common
BuildRequires:	ant >= 1.7.0
BuildRequires:	ant-junit >= 1.7.0
BuildRequires:	junit
BuildRequires:	maven-local
#Requires:	java >= 1:1.6.0
Requires: javapackages-tools rpm-build-java
ExcludeArch:	ppc ppc64 s390 s390x
Source44: import.info

%description
rxtx is an full implementation of java commapi which aims to support RS232
IEEE 1284, RS485, I2C and RawIO.

%prep
#setup -q -n rxtx-%{upver}-%{uprel}
%setup -q -n rxtx-%{uprel}
sed -e 's|@JNIPATH@|%{jni}|' %{PATCH1} | patch -s -b --suffix .p1 -p1
%patch2 -p1
%patch3 -p1
%if 0%{?fedora} > 13 || 0%{?rhel} > 6
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%endif
# remove prebuild binaries
find . -name '*.jar' -exec rm {} \;
find . -name '*.hqx' -exec rm {} \;
cp -a %{SOURCE1} .

%build
export JAVA_HOME=%{java_home}
%configure
# parallel make fails with make %%{?_smp_mflags}
make
iconv -f ISO_8859-1 -t UTF-8 ChangeLog >ChangeLog.utf-8
mv ChangeLog.utf-8 ChangeLog

%install
mkdir -p %{buildroot}%{_javadir} %{buildroot}%{jni}
make RXTX_PATH=%{buildroot}%{jni} JHOME=%{buildroot}%{_javadir} install
#echo "Driver=gnu.io.RXTXCommDriver" > %{buildroot}%{_javadir}/gnu.io.rxtx.properties
find %{buildroot} -name '*.la' -exec rm {} \;

%mvn_artifact org.rxtx:rxtx:%{version} RXTXcomm.jar
%mvn_file org.rxtx:rxtx:%{version} RXTXcomm
%mvn_install
rm -f  %{buildroot}%{_datadir}/java/RXTXcomm.jar
ln -s %{_jnidir}/RXTXcomm.jar %{buildroot}%{_datadir}/java/RXTXcomm.jar

%files
%doc AUTHORS COPYING ChangeLog INSTALL README TODO README.fedora
%{_javadir}/*
%{_jnidir}/*
%{jni}
%attr(644, root, root) %{_datadir}/maven-metadata/%{name}.xml

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_0.14.20100211.3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_0.14.20100211.1jpp8
- %%_jnidir set to /usr/lib/java

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_0.14.20100211.1jpp8
- java8 mass update

* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_0.7.20100211.2jpp7
- update to new release by jppimport

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_0.7.20100211.1jpp7
- update to new release by jppimport

* Sun Dec 02 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_0.6.20100211.2jpp7
- use /var/lock/serial

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_0.6.20100211jpp6
- update to new release by jppimport

* Sat Jul 09 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_0.4.20100211jpp6
- import by jppimport

