BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 15
# required for %%_jnidir macros
BuildRequires: rpm-build-java
BuildRequires: gcc-c++
%define version 2.2
%define name rxtx
#global upver	2.1
#global uprel	7r2
#global rel	0.8

%global upver	2.2
%global uprel	20100211
%global rel	0.6

#global jni	%{_jnidir}
%global jni	%{_libdir}/%{name}

Summary:	Parallel communication for the Java Development Toolkit
Name:		rxtx
Version:	%{upver}
Release:	alt1_0.6.20100211jpp6
License:	LGPLv2+
Group:		System/Libraries
URL:		http://rxtx.qbang.org/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  cvs -d:pserver:anonymous@qbang.org:/var/cvs/cvsroot co -r commapi-0-0-1 -D "2010-02-11" -d rxtx-%{uprel} rxtx-devel
#  tar cjvf rxtx-%{uprel}.tar.bz2 --exclude CVS --exclude .cvsignore rxtx-%{uprel}
Source:		%{name}-%{uprel}.tar.bz2
#Source:		http://rxtx.qbang.org/pub/rxtx/%{name}-%{upver}-%{uprel}.tgz
Patch1:		rxtx-2.2-loadlibrary.patch
Patch2:		rxtx-2.2-no-io.h.patch
Patch3:		rxtx-2.2-fhs_lock.patch
Patch4:		rxtx-2.2-lock.patch
#BuildRequires:	java-devel >= 1:1.6.0
BuildRequires:	jpackage-utils
BuildRequires:  libtool automake
BuildRequires:	ant >= 1.7.0
BuildRequires:	ant-junit >= 1.7.0
BuildRequires:	junit4
#Requires:	java >= 1:1.6.0
Requires:	jpackage-utils
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
%endif
# remove prebuild binaries
find . -name '*.jar' -exec rm {} \;
find . -name '*.hqx' -exec rm {} \;

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

%files
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
%{_javadir}/*
%{jni}

%changelog
* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_0.6.20100211jpp6
- update to new release by jppimport

* Sat Jul 09 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_0.4.20100211jpp6
- import by jppimport

