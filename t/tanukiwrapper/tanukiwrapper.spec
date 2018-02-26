BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2008, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%define gcj_support 0


Name:           tanukiwrapper
Version:        3.2.3
Release:        alt1_5jpp6
Summary:        Java Service Wrapper
Epoch:          0
License:        BSD
URL:            http://wrapper.tanukisoftware.org/
Source0:        http://download.sourceforge.net/wrapper/wrapper_3.2.3_src.tar.gz
Patch1:         %{name}-build.patch
Patch2:         %{name}-crosslink.patch
Patch3:         %{name}-makefile-linux-x86-32.patch
#Add Makefiles so package builds for all FC architectures.
Patch4:         %{name}-Makefile-s390-s390x-ppc.patch
# The following patch is only needed for GCJ.
Patch5:         %{name}-nosun-jvm-64.patch
Group:          Development/Java
BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: glibc-devel
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-nodeps >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: %{__perl}
BuildRequires: java-javadoc
Requires: jpackage-utils >= 0:1.7.4
Obsoletes:      %{name}-demo < 0:3.1.2-2jpp

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Source44: import.info
Patch33: tanukiwrapper-3.2.3-alt-Makefile.patch

%description
The Java Service Wrapper is an application which has 
evolved out of a desire to solve a number of problems 
common to many Java applications: 
- Run as a Windows Service or Unix Daemon
- Application Reliability
- Standard, Out of the Box Scripting
- On Demand Restarts
- Flexible Configuration
- Ease Application installations
- Logging

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires(post): %{__rm}
Requires(postun): %{__rm}
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n wrapper_%{version}_src
%patch1
%patch2
%patch33 -p1
#%patch3
%patch4
# The following patch is only needed for GCJ.
%if %{gcj_support}
%patch5
%endif
find . -name "*.jar" -exec %__rm -f {} \;
%__perl -p -i -e 's/\r//' doc/AUTHORS
%__perl -p -i -e 's|-O3|%optflags|' src/c/Makefile*
%__perl -p -e \
  's|=\.\./lib/wrapper\.jar$|=%{_javadir}/%{name}.jar| ;
   s|=\.\./lib$|=%{_libdir}|' \
  src/conf/wrapper.conf.in > wrapper.conf.sample
%__perl -p -e \
  's|"\./wrapper"|"%{_sbindir}/%{name}"| ;
   s|"\.\./conf/wrapper\.conf"|"/path/to/wrapper.conf"|' \
  src/bin/sh.script.in > script.sh.sample
#%patch33 -p1

%build
export CLASSPATH=$(build-classpath ant junit)
#export JAVA_HOME=%{_jvmdir}/java-1.6.0
%ifarch x86_64 ia64 ppc64 sparc64 s390x
bits=64
%else
bits=32
%endif
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=first -Djdk.api=%{_javadocdir}/java -Dbits=$bits \
  main jdoc

%install
%__rm -rf %{buildroot}

# jar
%__mkdir_p %{buildroot}%{_javadir}
%__install -p -m 0644 lib/wrapper.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s}f ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# jni
%__install -d -m 755 %{buildroot}%{_libdir}
%__install -p -m 755 lib/libwrapper.so %{buildroot}%{_libdir}

# commands
%__install -d -m 755 %{buildroot}%{_sbindir}
%__install -p -m 755 bin/wrapper %{buildroot}%{_sbindir}/%{name}

# javadoc
%__install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -a jdoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
%__rm -f %{_javadocdir}/%{name}
%{__ln_s}f %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  %__rm -f %{_javadocdir}/%{name}
fi

%files
%doc doc/license.txt *.sample
%{_sbindir}/%{name}
%{_libdir}/libwrapper.so
%{_javadir}/%{name}*.jar

%if %{gcj_support}
%{_libdir}/gcj/%{name}/tanukiwrapper-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%doc doc/*

%changelog
* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.3-alt1_5jpp6
- new jpp release

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2.3-alt1_3jpp5
- rebuild with default profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.2.3-alt1_2jpp5
- converted from JPackage by jppimport script

* Mon Oct 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.2.3-alt1_1jpp1.7
- converted from JPackage by jppimport script

