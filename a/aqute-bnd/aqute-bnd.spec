# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
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

Name:           aqute-bnd
Version:        0.0.363
Release:        alt2_8jpp7
Summary:        BND Tool
License:        ASL 2.0
Group:          Development/Java
URL:            http://www.aQute.biz/Code/Bnd

# NOTE : sources for 0.0.363 are no longer available
# The following links would work for 0.0.370-0.0.401 version range, but
# we need to stay by 0.0.363 to minimize problems during the 1.43.0 introduction
Source0:        http://www.aqute.biz/repo/biz/aQute/bnd/%{version}/bnd-%{version}.jar
Source1:        http://www.aqute.biz/repo/biz/aQute/bnd/%{version}/bnd-%{version}.pom
Source2:        aqute-service.tar.gz

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  ant
Source44: import.info


%description
The bnd tool helps you create and diagnose OSGi R4 bundles.
The key functions are:
- Show the manifest and JAR contents of a bundle
- Wrap a JAR so that it becomes a bundle
- Create a Bundle from a specification and a class path
- Verify the validity of the manifest entries
The tool is capable of acting as:
- Command line tool
- File format
- Directives
- Use of macros

%package javadoc
Requires:       jpackage-utils
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c

mkdir -p target/site/apidocs/
mkdir -p target/classes/
mkdir -p src/main/
mv OSGI-OPT/src src/main/java
pushd src/main/java
tar xfs %{SOURCE2}
popd
sed -i "s|import aQute.lib.filter.*;||g" src/main/java/aQute/bnd/make/ComponentDef.java
sed -i "s|import aQute.lib.filter.*;||g" src/main/java/aQute/bnd/make/ServiceComponent.java

# get rid of eclipse plugins which are not usable anyway and complicate
# things
rm -rf src/main/java/aQute/bnd/annotation/Test.java \
       src/main/java/aQute/bnd/{classpath,jareditor,junit,launch,plugin} \
       aQute/bnd/classpath/messages.properties

# remove bundled stuff
for f in $(find aQute/ -type f -name "*.class"); do
    rm -f $f
done

# Convert CR+LF to LF
sed -i "s|\r||g" LICENSE

%build
export LANG=en_US.utf8
export OPT_JAR_LIST=:
export CLASSPATH=$(build-classpath ant)

%{javac} -d target/classes -target 1.5 -source 1.5 $(find src/main/java -type f -name "*.java")
%{javadoc} -d target/site/apidocs -sourcepath src/main/java aQute.lib.header aQute.lib.osgi aQute.lib.qtokens aQute.lib.filter
cp -p LICENSE maven-dependencies.txt plugin.xml pom.xml target/classes
for f in $(find aQute/ -type f -not -name "*.class"); do
    cp -p $f target/classes/$f
done
pushd target/classes
%{jar} cmf ../../META-INF/MANIFEST.MF ../%{name}-%{version}.jar *
popd

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -Dm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt2_8jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt1_7jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.363-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

