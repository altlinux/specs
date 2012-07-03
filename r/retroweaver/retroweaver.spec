# due to java-1.4.2-sun
ExclusiveArch: %ix86
#BuildRequires: java-devel = 1.4.2
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
BuildRequires: jpackage-utils 
BuildRequires: jaxen jakarta-oro
#rpm-build-java
# Copyright (c) 2000-2007, JPackage Project
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


Name:           retroweaver
Version:        2.0.2
Release:        alt5_1jpp5
Epoch:          0
Summary:        Retroweaver
License:        BSD
Url:            http://retroweaver.sourceforge.net/
Source0:        http://downloads.sourceforge.net/retroweaver/retroweaver-2.0.2.tar.bz2
Patch0:         %{name}-build.patch
Patch1: retroweaver-2.0.2-alt-no-svn.patch

Group:          Development/Java
BuildRequires: ant ant-junit
BuildRequires: junit
BuildRequires: emma
BuildRequires: pmd
BuildRequires: backport-util-concurrent
BuildRequires: objectweb-asm >= 0:3.1
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: java-1.4.2-sun-devel
#BuildRequires: jre-1.4.2-bea
#BuildRequires: jre-1.4.2-ibm
BuildRequires: java-1.5.0-sun-devel
#BuildRequires: jre-1.5.0-bea
#BuildRequires: jre-1.5.0-ibm
BuildRequires: java-1.6.0-sun-devel
BuildRequires: java-1.5.0-sun-devel
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Requires: backport-util-concurrent
Requires: objectweb-asm >= 0:3.1

%description
Retroweaver is a bytecode weaver that enables you to take 
advantage of the new Java 1.5 language features, while still
retaining total binary compatability with 1.4 virtual 
machines. Retroweaver operates by transforming Java class 
files compiled by a 1.5 compiler into version 1.4 class 
files which can then be run on any 1.4 virtual machine.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation

%description manual
%{summary}.

%prep
%setup -q
# remove all binary libs
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
ln -sf $(build-classpath objectweb-asm/asm-util) lib/asm-util-3.1.jar
ln -sf $(build-classpath objectweb-asm/asm-commons) lib/asm-commons-3.1.jar
ln -sf $(build-classpath objectweb-asm/asm) lib/asm-3.1.jar
ln -sf $(build-classpath backport-util-concurrent) lib/
ln -sf $(build-classpath junit) lib/
ln -sf $(build-classpath ant) lib/
ln -sf $(build-classpath jaxen) lib/
mkdir -p pmdhome/lib
ln -sf $(build-classpath pmd) pmdhome/lib
pushd pmdhome
ln -sf $(build-classpath objectweb-asm/asm-util) lib/asm-util-3.1.jar
ln -sf $(build-classpath objectweb-asm/asm-commons) lib/asm-commons-3.1.jar
ln -sf $(build-classpath objectweb-asm/asm) lib/asm-3.1.jar
ln -sf $(build-classpath backport-util-concurrent) lib/
ln -sf $(build-classpath junit) lib/
ln -sf $(build-classpath ant) lib/
ln -sf $(build-classpath jaxen) lib/
popd
%patch0 -b .sav0
%patch1 -p1 -b .sav1

%build
#export JAVA_HOME=%{_jvmdir}/java-1.5.0
export OPT_JAR_LIST="ant/ant-nodeps ant/ant-junit junit emma emma_ant"
export CLASSPATH=$(build-classpath jaxen oro)
ant \
    -Dversion=2.0.2 \
    -DbuildNumber=%release \
    -Djdk14.home=%{_jvmdir}/java-1.4.2-sun \
    -Djdk14.rmic=%{_jvmdir}/java-1.4.2-sun/bin/rmic \
    -Djre14.home=%{_jvmdir}/java-1.4.2-sun/jre \
    -Djre14.jvm=%{_jvmdir}/java-1.4.2-sun/jre/bin/java \
    -Djre14.runtime=%{_jvmdir}/java-1.4.2-sun/jre/lib/rt.jar \
    -Djre15.home=%{_jvmdir}/java-1.5.0-sun/jre \
    -Djre15.jvm=%{_jvmdir}/java-1.5.0-sun/jre/bin/java \
    -Djre16.home=%{_jvmdir}/java-1.6.0-sun/jre \
    -Djre16.jvm=%{_jvmdir}/java-1.6.0-sun/jre/bin/java \
    -Demma.lib=%{_javadir} \
    -Dpmd.home=$(pwd)/pmdhome \
    dist pmd docs
#    coverage pmd docs

echo skipped: \
    -Dibm14.home=%{_jvmdir}/java-1.4.2-ibm/jre \
    -Dibm14.jvm=%{_jvmdir}/java-1.4.2-ibm/jre/bin/java \
    -Dibm15.home=%{_jvmdir}/java-1.5.0-ibm/jre \
    -Dibm15.jvm=%{_jvmdir}/java-1.5.0-ibm/jre/bin/java \
    -Dbea14.home=%{_jvmdir}/java-1.4.2-bea/jre \
    -Dbea14.jvm=%{_jvmdir}/java-1.4.2-bea/jre/bin/java \
    -Dbea15.home=%{_jvmdir}/java-1.5.0-bea/jre \
    -Dbea15.jvm=%{_jvmdir}/java-1.5.0-bea/jre/bin/java \



%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/release/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap net.sourceforge.retroweaver %{name} %{version} JPP %{name}
install -m 644 target/release/%{name}-rt-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-rt-%{version}.jar
%add_to_maven_depmap net.sourceforge.retroweaver %{name}-rt %{version} JPP %{name}-rt
install -m 644 target/release/%{name}-all-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-all-%{version}.jar
install -m 644 target/release/%{name}-tests-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-tests-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir} 
for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 maven/%{name}.pom \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -pm 644 maven/%{name}-rt.pom \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-rt.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr docs $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#cp -pr target/coverage $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr target/pmd $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p ChangeLog.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

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

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt5_1jpp5
- fixed build

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt4_1jpp5
- support for new jpp-compat 0.17

* Thu Oct 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt3_1jpp5
- added ExclusiveArch

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt2_1jpp5
- fixed build w/java5

* Mon Jan 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.0.2-alt1_1jpp5.0
- first build

