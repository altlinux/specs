Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/cglib/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           cglib
Version:        2.2
Release:	alt2_4jpp6
Epoch:          0
Summary:        Code Generation Library
License:        ASL 2.0
URL:            http://cglib.sourceforge.net/
Group:          Development/Java
Source0:        http://downloads.sourceforge.net/sourceforge/cglib/cglib-src-2.2.jar
Source1:        cglib-missing-words.txt
Source2:        http://repo2.maven.org/maven2/cglib/cglib/2.2/cglib-2.2.pom
Source3:        cglib-component-info.xml
Source4:        http://repo2.maven.org/maven2/cglib/cglib-nodep/2.2/cglib-nodep-2.2.pom
Patch0:         cglib-2.2-TestEnhancer.patch
Obsoletes:      %{name}-nohook < %{epoch}:%{version}-%{release}
Provides:       %{name}-nohook = %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: objectweb-asm >= 0:3.1
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6
BuildRequires: ant-junit >= 0:1.6
BuildRequires: jarjar
BuildRequires: junit
BuildRequires: objectweb-asm >= 0:3.1
BuildArch:      noarch
Source44: import.info

%description
cglib is a powerful, high performance and quality 
Code Generation Library, It is used to extend JAVA 
classes and implements interfaces at runtime.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation

%description demo
%{summary}.

%prep
%setup -q -c -n %{name}
%patch0 -p1
%{_bindir}/find -name "*.jar" | %{_bindir}/xargs -t %{__rm}

pushd lib
%{__ln_s} $(build-classpath ant) ant.jar
%{__ln_s} $(build-classpath objectweb-asm/asm) asm-3.1.jar
%{__ln_s} $(build-classpath objectweb-asm/asm-commons) asm-commons-3.1.jar
%{__ln_s} $(build-classpath objectweb-asm/asm-util) asm-util-3.1.jar
%{__ln_s} $(build-classpath jarjar) jarjar.jar
%{__ln_s} $(build-classpath junit) junit.jar
popd

( cat << EO_JP
grant codeBase "file:/-"{
  permission java.security.AllPermission;
};
EO_JP
) > java.policy

%{__cp} -p %{SOURCE1} src/test/net/sf/cglib/util/words.txt

%build
export CLASSPATH=$(build-classpath objectweb-asm/asm objectweb-asm/asm-commons objectweb-asm/asm-util jarjar junit)
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dtest.failonerror=false jar javadoc test

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
%{__cp} -p dist/%{name}-nodep-%{version}.jar %{buildroot}%{_javadir}/%{name}-nodep-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do %{__ln_s} ${jar} `/bin/echo $jar | %{__sed} "s|-%{version}||g"`; done)

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%{__cp} -p %{SOURCE4} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}-nodep.pom
%add_to_maven_depmap cglib cglib %{version} JPP %{name}
%add_to_maven_depmap cglib cglib-nodep %{version} JPP %{name}-nodep
%add_to_maven_depmap net.sf.cglib cglib %{version} JPP %{name}
%add_to_maven_depmap net.sf.cglib cglib-nodep %{version} JPP %{name}-nodep

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
# FIXME: (dwalluck): breaks -bi --short-circuit
%{__rm} -rf docs/api
%{__cp} -pr docs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# demo
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}-%{version}
%{__cp} -pr src/proxy/samples %{buildroot}%{_datadir}/%{name}-%{version}

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__install} -p -m 644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE1} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{SOURCE2} %{buildroot}%{repodirsrc}
%{__install} -p -m 644 %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{buildroot}%{_javadir}/%{name}.jar %{buildroot}%{repodirlib}/cglib.jar
%endif

%files
%doc LICENSE
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-nodep-%{version}.jar
%{_javadir}/%{name}-nodep.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_datadir}/maven2/poms/JPP-%{name}-nodep.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}-%{version}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_4jpp6
- added net.sf.cglib group id

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_4jpp6
- added pom

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_4jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_3jpp5
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_2jpp1.7
- converted from JPackage by jppimport script

* Wed May 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt4_2jpp1.7
- fixed provides to avoid unmets on cglib

* Fri May 25 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt3_2jpp1.7
- imported with jppimport script; note: bootstrapped version

* Thu May 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_2jpp1.7
- fixed cglib provides

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_2jpp1.7
- imported with jppimport script; note: bootstrapped version

