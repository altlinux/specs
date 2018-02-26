Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
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


Name:           jdepend
Version:        2.9.1
Release:	alt3_3jpp6
Epoch:          0
Summary:        Java Design Quality Metrics
License:        BSD
Group:          Development/Java
URL:            http://www.clarkware.com/software/JDepend.html
Source0:        http://www.clarkware.com/software/jdepend-2.9.1.zip
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/jdepend/jdepend/2.9.1/jdepend-2.9.1.pom
Patch0:         jdepend-2.9.1-test.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: jpackage-utils
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
JDepend traverses a set of Java class and source file directories and
generates design quality metrics for each Java package. JDepend allows
you to automatically measure the quality of a design in terms of its
extensibility, reusability, and maintainability to effectively manage
and control package dependencies.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demos for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q
%patch0 -b .sav0
%{_bindir}/find -type f -name "*.jar" |  %{_bindir}/xargs -t %{__rm}
%{_bindir}/find -type f -name "*.zip" |  %{_bindir}/xargs -t %{__rm}
%{_bindir}/find -type d |  %{_bindir}/xargs -t %{__chmod} 0755

%build
export CLASSPATH=
export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 package compile-sample

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} ${jar/-%{version}/}; done)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap jdepend jdepend %{version} JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__cp} -pr build/docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# demo
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__cp} -pr sample %{buildroot}%{_datadir}/%{name}
%{__cp} -pr build/epayment %{buildroot}%{_datadir}/%{name}/sample

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc CHANGES LICENSE README contrib/jdepend2dot*
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_3jpp6
- added pom

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_1jpp5
- new jpackage release

* Mon Apr 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_1jpp1.7
- rebuild with new packages

* Wed Apr 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt2_1jpp1.7
- converted from JPackage by jppimport script

* Wed Apr 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Mon Sep 20 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.8.2-alt1
- Updated to upstream release 2.8.2
- Disabled debug compiler option by default

* Mon Jun 07 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.7-alt1
- New upstream release

* Fri Oct 10 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.6-alt1
- Ported to Sisyphus from JPackage
