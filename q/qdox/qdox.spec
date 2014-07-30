# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
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

Summary:        Extract class/interface/method definitions from sources
Name:           qdox
Version:        1.12.1
Release:        alt1_5jpp7
Epoch:          1
License:        ASL 2.0
URL:            http://qdox.codehaus.org/
Group:          Development/Java
Source0:        http://repo2.maven.org/maven2/com/thoughtworks/qdox/qdox/%{version}/%{name}-%{version}-project.tar.bz2
Source1:        qdox-MANIFEST.MF

BuildRequires:  jpackage-utils >= 0:1.7.4
BuildRequires:  ant >= 0:1.6
BuildRequires:  ant-junit >= 0:1.6
BuildRequires:  junit >= 0:3.8.1
BuildRequires:  byaccj
BuildRequires:  jflex
BuildRequires:  maven-local
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-changes-plugin
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-plugin-cobertura
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-deploy-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-release-plugin
BuildRequires:  zip


BuildArch:      noarch
Obsoletes:      qdox-manual <= 0:1.9.2
Source44: import.info
Obsoletes: qdox16-poms < 1.1


%description
QDox is a high speed, small footprint parser
for extracting class/interface/method definitions
from source files complete with JavaDoc @tags.
It is designed to be used by active code
generators or documentation tools.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API docs for %{name}.


%prep
%setup -q 
find -name *.jar -delete
rm -rf bootstrap

# Ant changed groupId
%pom_remove_dep ant:ant
%pom_add_dep org.apache.ant:ant

# We don't need these plugins
%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin :maven-jflex-plugin
%pom_remove_plugin :maven-resources-plugin
%pom_remove_plugin :xsite-maven-plugin
%pom_xpath_remove pom:build/pom:extensions

%build
# Generate scanner (upstream does this with maven-jflex-plugin)
jflex \
      -d src/java \
      --skel src/grammar/skeleton.inner \
      src/grammar/lexer.flex

# Generate parser (upstream does this with maven-antrun-plugin)
dir=src/java/com/thoughtworks/qdox/parser/impl
mkdir -p $dir
(cd ./$dir
byaccj \
       -v \
       -Jnorun \
       -Jnoconstruct \
       -Jclass=Parser \
       -Jsemantic=Value \
       -Jpackage=com.thoughtworks.qdox.parser.impl \
       ../../../../../../grammar/parser.y)

# Build artifact
mvn-rpmbuild \
        -Dmaven.test.skip=true \
        install \
        javadoc:aggregate

# Inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE1} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u target/%{name}-%{version}.jar META-INF/MANIFEST.MF

%install
# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap -a qdox:qdox

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE.txt README.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE.txt
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.12.1-alt1_5jpp7
- new release

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.12.1-alt1_2jpp7
- fc update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.12-alt3_2jpp6
- fixed build

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.12-alt2_2jpp6
- fixed build with java 7

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.12-alt1_2jpp6
- new version

* Tue Oct 26 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt2_5jpp6
- rebuild with target=5

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt1_5jpp6
- new version

* Fri Feb 13 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.6.1-alt1_5jpp5
- reverted to version 1.6.1

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_1jpp5
- fixed build with jpackage 5

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_1jpp1.7
- rebuilt with maven1

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_4jpp1.7
- converted from JPackage by jppimport script

