%define _with_native 1
BuildRequires: /proc
BuildRequires: jpackage-1.4-compat
# Copyright (c) 2000-2005, JPackage Project
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

%define native      %{?_with_native:1}%{!?_with_native:0}

%define base_name   daemon
%define short_name  commons-%{base_name}

Name:           jsvc
Version:        1.0.1
Release:        alt4_6jpp1.7
Epoch:          1
Summary:        Jakarta Commons Daemon Package
License:        Apache Software License 2.0
Group:          Development/Java
URL:            http://jakarta.apache.org/commons/daemon/
Source0:        http://www.apache.org/dist/jakarta/commons/daemon/source/daemon-1.0.1.tar.gz
Patch:          jakarta-commons-daemon-crosslink.patch

%if %{native}
##BuildRequires: java-devel
%else
%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires: ant
%endif
BuildRequires: jpackage-utils >= 0:1.6
Provides:       %{short_name}
Obsoletes:      %{short_name}

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

Patch1: jakarta-commons-daemon-1.0.1-libs.patch
%description
The scope of this package is to define an API in line with the current
Java(tm) Platform APIs to support an alternative invocation mechanism
which could be used instead of the above mentioned public static void
main(String[]) method.  This specification cover the behavior and life
cycle of what we define as Java(tm) daemons, or, in other words, non
interactive Java(tm) applications.

%package        -n jakarta-%{short_name}-jsvc
Summary:        Java daemon launcher
Group:          Development/Java
Provides:       jsvc = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description    -n jakarta-%{short_name}-jsvc
%{summary}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
Javadoc for %{name}.


%prep
%setup -q -n %{base_name}-%{version}
%patch0 -p0
chmod 644 src/samples/*


%patch1 -p1
%build
%if %{native}
cd src/native/unix
%configure --with-java=%{java_home}
make %{?_smp_mflags}
%else
ant -Dant.lib=%{_javadir} -Dj2se.javadoc=%{_javadocdir}/java dist
%endif


%install
%if %{native}
install -Dpm 755 src/native/unix/jsvc $RPM_BUILD_ROOT%{_sbindir}/jsvc
%else
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 dist/%{short_name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|jakarta-||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
%endif

%if ! %{native}
%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ $1 -eq 0 ]; then
  %{__rm} -f %{_javadocdir}/%{name}
fi

%if ! %{native}
%post
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%postun
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif
%endif

%if %{native}
%files -n jakarta-%{short_name}-jsvc
%doc LICENSE*
%{_sbindir}/jsvc
%else

%files
%doc LICENSE* PROPOSAL.html RELEASE-NOTES.txt STATUS.html src/samples
%doc src/docs/*
%{_javadir}/*

%if %{gcj_support}
%{_libdir}/gcj/%{name}
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%endif

%changelog
* Fri May 18 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt4_6jpp1.7
- jsvc is again split into separate package

* Fri May 11 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt3_6jpp1.7
- built with jsvc

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt2_6jpp1.7
- converted from JPackage by jppimport script

* Fri Apr 07 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.1-alt2
- Fix the JDK path for x86_64

* Thu Mar 30 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.1-alt1
- Updated to 1.0.1
- Patch1: fix up link order to satisfy ld --as-needed

* Sat Dec 18 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt3
- Reverted the 1.0-alt2 package by Vladimir Lettiev
- Adapted to rpm-build-java
- Set default JVM location to /usr/lib/j2se [Patch0]

* Fri Aug 06 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0-alt1
- 1.0 release
- Splintered off the jsvc package that has runtime dependencies
- More spec cleanup

* Fri Nov 28 2003 Alexey Borovskoy <alb@altlinux.ru> 1.0alpha-alt1
- First build for ALTLinux
- Spec cleanup

* Sat Oct 11 2003 Ville Skyttä <ville.skytta at iki.fi> - 1:1.0-0.alpha.1jpp
- Update to 1.0 alpha, bump epoch.
- Non-versioned, crosslinked javadocs.
- Build native jsvc with "--with native".

* Thu Feb 27 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.0-5jpp
- fix ASF license

* Thu Feb 27 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.0-4jpp
- fix missing packager tag
- get latest nightly (20030227)
- fix ant lib location for javadoc
- added common-launcher jar

* Fri Jul 12 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.0-3jpp
- clean up spec

* Mon Jun 10 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.0-2jpp
- use sed instead of bash 2.x extension in link area to make spec compatible
  with distro using bash 1.1x

* Fri Jun 07 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.0-1jpp 
- 1.0 (cvs 20020606)
- added short names in %{_javadir}, as does jakarta developpers
- first jPackage release
