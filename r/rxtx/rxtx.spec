Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name rxtx
%global upver	2.2
%global uprel	20100211

%global jni	%{_libdir}/%{name}

Summary:	Parallel communication for the Java Development Toolkit
Name:		rxtx
Version:	%{upver}
Release:	alt3_0.20.20100211jpp8
License:	LGPLv2+
URL:		http://rxtx.qbang.org/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  cvs -d:pserver:anonymous@qbang.org:/var/cvs/cvsroot co -r commapi-0-0-1 -D "2010-02-11" -d rxtx-%%{uprel} rxtx-devel
#  tar cjvf rxtx-%%{uprel}.tar.bz2 --exclude CVS --exclude .cvsignore rxtx-%%{uprel}
Source0:	%{name}-%{uprel}.tar.bz2
Source1:	README.distro
Source2:	rxtx-osgi.bnd
Patch1:		rxtx-2.2-loadlibrary.patch
Patch2:		rxtx-sys_io_h_check.patch
Patch3:		rxtx-2.2-fhs_lock.patch
Patch4:		rxtx-2.2-lock.patch
Patch5:		rxtx-2.2-Add-Arduino-driver-ttyACM-rxtxcomm-as-device.patch
Patch6:		rxtx-2.2-java-version-fix.patch
Patch7:		rxtx-2.2-convert-strcpy-to-strncpy.patch

BuildRequires:	libtool automake
BuildRequires:	ant
BuildRequires:	ant-junit
BuildRequires:	junit
BuildRequires:	aqute-bnd
BuildRequires:	javapackages-local
Source44: import.info
Patch33: rxtx-20100211-alt-hack.patch

%description
rxtx is an full implementation of java commapi which aims to support RS232
IEEE 1284, RS485, I2C and RawIO.

%prep
%setup -q -n rxtx-%{uprel}
sed -e 's|@JNIPATH@|%{jni}|' %{PATCH1} | patch -s -b --suffix .p1 -p1
%patch2 -p1
%patch3 -p1
%if 0%{?fedora} || 0%{?rhel} > 6
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%endif
# remove prebuild binaries
find . -name '*.jar' -exec rm {} \;
find . -name '*.hqx' -exec rm {} \;
cp -a %{SOURCE1} .

# Don't need to install jar file, mvn_install will do it
sed -i -e '/JHOME/d' Makefile.in
%patch33 -p1

%build
export JAVA_HOME=%{java_home}
%configure
# parallel make fails with make %%{?_smp_mflags}
make
iconv -f ISO_8859-1 -t UTF-8 ChangeLog >ChangeLog.utf-8
mv ChangeLog.utf-8 ChangeLog

# Inject OSGi metadata
bnd wrap -p %{SOURCE2} -v %{version} -o RXTXcomm-bnd.jar RXTXcomm.jar
mv RXTXcomm-bnd.jar RXTXcomm.jar

%install
mkdir -p %{buildroot}%{jni}
make RXTX_PATH=%{buildroot}%{jni} install
find %{buildroot} -name '*.la' -exec rm {} \;

%mvn_artifact org.rxtx:rxtx:%{version} RXTXcomm.jar
%mvn_file org.rxtx:rxtx:%{version} RXTXcomm
%mvn_install

%files -f .mfiles
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog README TODO README.distro
%{jni}

%changelog
* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_0.20.20100211jpp8
- java update

* Mon Nov 06 2017 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_0.19.20100211jpp8
- fixed bad_elf_symbols inl/inw (Patch33)

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

