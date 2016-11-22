Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
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
Name:          janino
Version:       2.7.8
Release:       alt1_5jpp8
Summary:       An embedded Java compiler
License:       BSD
URL:           http://unkrig.de/w/Janino
Source0:       http://janino.net/download/%{name}-%{version}.zip
Source1:       http://repo1.maven.org/maven2/org/codehaus/%{name}/%{name}-parent/%{version}/%{name}-parent-%{version}.pom
Source2:       http://repo1.maven.org/maven2/org/codehaus/%{name}/commons-compiler/%{version}/commons-compiler-%{version}.pom
Source3:       http://repo1.maven.org/maven2/org/codehaus/%{name}/commons-compiler-jdk/%{version}/commons-compiler-jdk-%{version}.pom
Source4:       http://repo1.maven.org/maven2/org/codehaus/%{name}/%{name}/%{version}/%{name}-%{version}.pom
# removes the de.unkrig.commons.nullanalysis annotations
# http://unkrig.de/w/Unkrig.de
# https://svn.code.sf.net/p/loggifier/code/tags/loggifier_0.9.9.v20140430-1829/de.unkrig.commons.nullanalysis/
Patch0:        %{name}-2.7.8-remove-nullanalysis-annotations.patch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.codehaus:codehaus-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
Janino is a super-small, super-fast Java compiler. Not only can it compile
a set of source files to a set of class files like the JAVAC tool, but also
can it compile a Java expression, block, class body or source file in
memory, load the byte-code and execute it directly in the same JVM. Janino
is not intended to be a development tool, but an embedded compiler for
run-time compilation purposes, e.g. expression evaluators or "server pages"
engines like JSP.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

find . -name "*.jar" -delete
find . -name "*.class" -delete

for m in commons-compiler \
  commons-compiler-jdk \
  %{name};do
  mkdir -p ${m}/src
  (
    cd ${m}/src/
    unzip -qq  ../../${m}-src.zip
    if [ -f org.codehaus.commons.compiler.properties ]; then
      mkdir -p main/resources
      mv org.codehaus.commons.compiler.properties main/resources
    fi
  )
done

%patch0 -p1

install -m 644 %{SOURCE1} pom.xml
install -m 644 %{SOURCE2} commons-compiler/pom.xml
install -m 644 %{SOURCE3} commons-compiler-jdk/pom.xml
install -m 644 %{SOURCE4} %{name}/pom.xml

%pom_change_dep -r :ant-nodeps :ant

# RHBZ#842604
%pom_xpath_set "pom:plugin[pom:artifactId = 'maven-compiler-plugin']/pom:configuration/pom:source" 1.6
%pom_xpath_set "pom:plugin[pom:artifactId = 'maven-compiler-plugin']/pom:configuration/pom:target" 1.6

perl -pi -e 's/\r$//g' new_bsd_license.txt README.txt

# Cannot run program "svn"
%pom_remove_plugin :buildnumber-maven-plugin

%pom_remove_plugin :maven-clean-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt
%doc new_bsd_license.txt

%files javadoc -f .mfiles-javadoc
%doc new_bsd_license.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.7.8-alt1_5jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.7.8-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.1-alt2_18jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.1-alt2_16jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.1-alt2_14jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.1-alt1_14jpp7
- fc release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.5.11-alt1_2jpp5
- new jpackage release

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.5.11-alt1_1jpp1.7
- converted from JPackage by jppimport script

