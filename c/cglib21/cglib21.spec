# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define version 2.1.3
%define name cglib21
# Copyright (c) 2000-2010, JPackage Project
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

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'

%define _with_repolib 1

%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/cglib/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

# If you don't want to build the aspectwerkz hook,
# while aspectwerkz isn't available yet,
# give rpmbuild option '--without hook'

# A cglib without net.sf.cglib.transform.hook.* is useful to 
# build jmock which is an indirect dependency of cglib itself (through 
# aspectwerkz).

%define with_hook %{!?_without_hook:1}%{?_without_hook:0}
%define without_hook %{?_without_hook:1}%{!?_without_hook:0}
%define oname cglib

%define uscver 2.1_3

Summary:        Code Generation Library
Name:           cglib21
Version:        2.1.3
Release:        alt8_2jpp6
Epoch:          0
License:        Apache Software License 2
URL:            http://cglib.sourceforge.net/
Group:          Development/Java
Source0:        cglib-src-2.1_3.jar
Source1:        cglib-missing-words.txt
Source2:        cglib-component-info.xml
Source3:        http://repo2.maven.org/maven2/cglib/cglib/2.1_3/cglib-2.1_3.pom
Source4:        http://repo2.maven.org/maven2/cglib/cglib-nodep/2.1_3/cglib-nodep-2.1_3.pom
Patch0:         cglib-2.1.3-build_xml.patch
Patch1:         cglib-ExamplePreProcessor.patch
# FIXME
# Testcase "testFailOnMemoryLeak" fails with java-1.4.2-bea-1.4.2.08-2jpp
# producing a LinkageError. 
# Testcase "testRegisterCallbacks" also fails.
# java-1.4.2-sun-1.4.2.10-1jpp and # java-1.4.2-ibm-1.4.2.3-1jpp don't
Patch2:         cglib-2.1.3-TestEnhancer.patch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  jarjar
BuildRequires:  junit
BuildRequires:  asm >= 0:1.5.3
BuildRequires:  asm2
%if %{with_hook}
BuildRequires:  aspectwerkz >= 0:1.0
%endif
Requires:  asm >= 0:1.5.3
%if %{with_hook}
#Optional:  aspectwerkz >= 0:1.0
%endif
Provides:       %{name}-nohook = %{epoch}:%{version}-%{release}
BuildArch:      noarch
Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
cglib is a powerful, high performance and quality 
Code Generation Library, It is used to extend JAVA 
classes and implements interfaces at runtime.

NOTE: To use the Aspectwerks hook (net.sf.cglib.transform.hook.*), make sure
aspectwerks.jar is in the Classpath (from the 'aspectwerks' RPM)
NOTE: If you use the cglib.jar you may need to add asm.jar to your ClassPath
(from the 'asm' RPM).  The cglib-nodep.jar includes the ASM classes already. 

%if %{with_repolib}
%package        repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description    repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%package nohook
Summary:        Cglib without aspectwerkz hook
Group:          Development/Java
Requires:  asm >= 0:1.5.3

%description nohook
%{summary}.

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
cat <<EOT

    If you don't want to build the aspectwerkz hook,
    while aspectwerkz isn't available yet,
    give rpmbuild option '--without hook'

    A cglib without net.sf.cglib.transform.hook.* is useful to 
    build jmock which is an indirect dependency of cglib itself (through 
    aspectwerkz).

EOT

%setup -T -c -n %{name}
unzip -q %{SOURCE0}
# remove all binary libs
for f in $(find . -name "*.jar"); do mv $f $f.no; done
( cat << EO_JP
grant codeBase "file:/-"{
  permission java.security.AllPermission;
};
EO_JP
) > java.policy
# add missing test input file
cp %{SOURCE1} src/test/net/sf/cglib/util/words.txt

%if %{without_hook}
rm src/proxy/net/sf/cglib/transform/hook/*
rm src/test/net/sf/cglib/transform/hook/*
%endif

%patch0 -b .sav
#test
%if %{with_hook}
%patch1 -b .sav
%endif
%patch2 -b .sav

%build
build-jar-repository -s -p lib \
ant \
asm/asm-attrs \
asm/asm \
asm2/asm2 \
asm/asm-util \
jarjar \
junit \

%if %{with_hook}
build-jar-repository -s -p lib aspectwerkz-core
%endif

export CLASSPATH=
export OPT_JAR_LIST=:
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc test

%if %{with_hook}
mkdir _tmp
pushd _tmp
    jar xf ../dist/%{oname}-%{uscver}.jar
    rm -rf net/sf/cglib/transform/hook
    jar cmf META-INF/MANIFEST.MF ../dist/%{oname}-nohook-%{uscver}.jar net
popd
rm -rf _tmp
%else
cp dist/%{oname}-%{uscver}.jar dist/%{name}-nohook-%{uscver}.jar
%endif

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 dist/%{oname}-nohook-%{uscver}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-nohook-%{version}.jar
%if %{with_hook}
install -m 644 dist/%{oname}-%{uscver}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 dist/%{oname}-nodep-%{uscver}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-nodep-%{version}.jar
%endif
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap cglib cglib21 2.1_3 JPP %{name}
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-nodep.pom
%add_to_maven_depmap cglib cglib21-nodep 2.1_3 JPP %{name}-nodep

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rmdir docs/api
cp -pr docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

#demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp -pr src/proxy/samples $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

%if %{with_repolib}
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
# Deploy cglib-nodeps.jar as cglib.jar to conform to the existing usage in JBoss
%if %{with_hook}
cp -p $RPM_BUILD_ROOT%{_javadir}/cglib21-nodep.jar $RPM_BUILD_ROOT%{repodirlib}/cglib21.jar
%else
cp -p $RPM_BUILD_ROOT%{_javadir}/cglib21-nohook.jar $RPM_BUILD_ROOT%{repodirlib}/cglib21.jar
%endif
%endif

%if %{with_hook}
%files
%doc LICENSE
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-nodep-%{version}.jar
%{_javadir}/%{name}-nodep.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%endif

%files nohook
%doc LICENSE
%{_javadir}/%{name}-nohook-%{version}.jar
%{_javadir}/%{name}-nohook.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}-%{version}

%if %{with_repolib}
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt8_2jpp6
- new jpp release

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt7_4jpp5
- fixed cglib-nohook provides

* Wed Oct 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt6_4jpp5
- compatibility build

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

