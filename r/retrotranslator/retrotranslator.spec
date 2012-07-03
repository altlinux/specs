Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: java-devel = 1.4.2
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-compat
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


Name:           retrotranslator
Version:        1.2.3
Release:        alt2_1jpp5
Epoch:          0
Summary:        Retrotranslator
License:        BSD
Url:            http://retrotranslator.sourceforge.net/
Source0:        http://downloads.sourceforge.net/retrotranslator/Retrotranslator-1.2.3-src.zip
Patch0:         retrotranslator-1.2.3-build.patch

Group:          Development/Java
BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: backport-util-concurrent >= 0:3.1
BuildRequires: junit
BuildRequires: mx4j
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires: backport-util-concurrent >= 0:3.1
Requires: mx4j

%description
Retrotranslator is a tool that makes Java applications 
compatible with various versions of the Java platform. It 
supports all Java 5 language features and a significant 
part of Java 5 API on J2SE 1.4. In other Java environments 
only the Java 5 language features that don't depend on the 
new API are supported. Retrotranslator is based on the ASM 
bytecode manipulation framework and the backport of 
concurrency utilities. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q  -n Retrotranslator-%{version}-src
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0

%build
ln -sf $(build-classpath backport-util-concurrent) lib
ln -sf $(build-classpath mx4j/mx4j) lib
# need a ver 48 junit for testing
mv lib/junit.jar.no lib/junit.jar
export OPT_JAR_LIST="ant/ant-junit"
export CLASSPATH=lib/junit.jar
ant \
   -Dbuild.sysclasspath=first \
   -Djava14_home=%{_jvmdir}/java-1.4.2 \
   -Djava15_home=%{_jvmdir}/java-1.5.0 \
   -Djava14_rt_jar=%{_jvmdir}/java-1.4.2/jre/lib/rt.jar \
   test javadoc


%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}

install -m 644 build/%{name}-runtime-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-runtime-%{version}.jar
%add_to_maven_depmap net.sf.retrotranslator %{name}-runtime %{version} JPP %{name}-runtime
install -m 644 build/%{name}-transformer-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-transformer-%{version}.jar
%add_to_maven_depmap net.sf.retrotranslator %{name}-transformer %{version} JPP %{name}-transformer

(cd $RPM_BUILD_ROOT%{_javadir} 
for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 conf/runtime/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-runtime.pom
install -m 644 conf/transformer/pom.xml \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-transformer.pom

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%{_javadir}/%{name}*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
%doc %{_docdir}/%{name}-%{version}/

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%changelog
* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt2_1jpp5
- selected java5 compiler explicitly

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt1_1jpp5
- jpp5 build

