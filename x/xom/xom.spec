Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: dom4j
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
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

# To build with dom4j issue rpmbuild --with dom4j xom.spec

%define with_dom4j %{?_with_dom4j:1}%{!?_with_dom4j:0}
%define without_dom4j %{!?_with_dom4j:1}%{?_with_dom4j:0}

Summary:        XML Object Model
Name:           xom
Version:        1.2.10
Release:        alt1_9jpp8
Epoch:          1
License:        LGPLv2
URL:            http://www.xom.nu
Source0:        http://www.cafeconleche.org/XOM/%{name}-%{version}-src.tar.gz

# Don't download jaxen, set javac target/source to 1.5
Patch0:         %{name}-build.patch

BuildRequires:  ant >= 0:1.6
BuildRequires:  javapackages-local
BuildRequires:  maven-local
BuildRequires:  jarjar
BuildRequires:  jaxen
BuildRequires:  junit
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
%if %{with_dom4j}
BuildRequires:  dom4j
%endif
BuildRequires:  xml-commons-apis
BuildRequires:  tagsoup
# Use JAXP implementation in JDK
BuildRequires:  java-devel
BuildRequires:  xml-commons-resolver
BuildRequires:  servlet

Requires:  jaxen
Requires:  xalan-j2
Requires:  xerces-j2
Requires:  xml-commons-apis

BuildArch: noarch
Source44: import.info


%description
XOM is a new XML object model. It is an open source (LGPL),
tree-based API for processing XML with Java that strives
for correctness, simplicity, and performance, in that order.
XOM is designed to be easy to learn and easy to use. It
works very straight-forwardly, and has a very shallow
learning curve. Assuming you're already familiar with XML,
you should be able to get up and running with XOM very quickly.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%package demo
Group: Development/Java
Summary:        Samples for %{name}
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description demo
This package provides %{summary}.

%prep
%setup -q -n XOM

find \( -name '*.jar' -or -name '*.class' \) -delete

%patch0 -p1

# fix non ASCII chars
for s in src/nu/xom/tests/BuilderTest.java\
 src/nu/xom/tests/SerializerTest.java;do
  native2ascii -encoding UTF8 ${s} ${s}
done

# Fix encoding
sed -i 's/\r//g' LICENSE.txt
sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301,"  $(find -name "*.java") \
 LICENSE.txt lgpl.txt

%build
mkdir -p lib
pushd lib
ln -sf $(build-classpath junit) junit.jar
ln -sf $(build-classpath xerces-j2) dtd-xercesImpl.jar
ln -sf $(build-classpath xalan-j2) xalan.jar
ln -sf $(build-classpath xml-commons-apis) xmlParserAPIs.jar
ln -sf $(build-classpath jaxen) jaxen.jar

# jarjar has more than one jars
while IFS=':' read -ra JARJAR_JARS; do 
    for j in "${JARJAR_JARS[@]}";do 
        ln -sf $j $(basename $j .jar)-1.0.jar
    done
done <<<$(build-classpath jarjar)
popd
mkdir -p lib2
pushd lib2
ln -sf $(build-classpath tagsoup) tagsoup-1.2.jar
ln -sf $(build-classpath xml-commons-resolver) resolver.jar

%if %{with_dom4j}
ln -sf $(build-classpath dom4j) dom4j.jar
%endif

ln -sf $(build-classpath servlet) servlet.jar
popd

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -v compile15 jar samples betterdoc maven2

pushd build/apidocs
for f in `find -name \*.css -o -name \*.html`; do
  sed -i 's/\r//g' $f
done
popd

mv build/maven2/project.xml build/maven2/pom.xml
%pom_add_dep jaxen:jaxen build/maven2/pom.xml
%mvn_artifact build/maven2/pom.xml build/%{name}-%{version}.jar
%mvn_alias xom:xom com.io7m.xom:xom

%install
%mvn_install
# For compatibility
# jars
ln -s xom/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
#install -d -m 755 %{buildroot}%{_javadir}
#install -m 644 build/%{name}-%{version}.jar \
#  %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 644 build/xom-samples.jar %{buildroot}%{_datadir}/%{name}

# POM
install -d -m 755 %{buildroot}%{_mavenpomdir}
ln -s xom/xom.pom %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
#install -m 644 build/maven2/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
#%add_maven_1depmap JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%doc README.txt
%doc LICENSE.txt
%doc Todo.txt
%doc lgpl.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt
%doc lgpl.txt

%files demo
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/xom-samples.jar

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.2.10-alt1_9jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.2.10-alt1_8jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2.10-alt1_6jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.2.10-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_12jpp7
- new release

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_9jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.6-alt1_2jpp6
- new jpp relase

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_1jpp5
- new version

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.b2.4jpp5
- jpp5 build

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_6jpp1.7
- updated to new jpackage release

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_5jpp1.7
fixes jvm 5.0 poisoning

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5jpp1.7
- full-fledged build

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_5jpp1.7
- imported with jppimport script; note: bootstrapped version

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_4jpp1.7
- imported with jppimport script; note: bootstrapped version

