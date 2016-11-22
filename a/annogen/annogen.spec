Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          annogen 
Version:       0.1.0
Release:       alt1_14jpp8
Summary:       Java framework for JSR-175 annotations 
License:       ASL 2.0
URL:           https://github.com/codehaus/annogen
# git clone https://github.com/codehaus/annogen/ annogen-0.1.0
# rm -rf annogen-0.1.0/annogen/ide-projects rm -rf annogen-0.1.0/annogen/trunk
# mv annogen-0.1.0/annogen/tags/release-0_1_0 annogen-0.1.0
# rm -rf annogen-0.1.0/annogen
# mv annogen-0.1.0/release-0_1_0/* annogen-0.1.0
# rm -rf annogen-0.1.0/release-0_1_0
# find annogen-0.1.0/ -name '*.jar' -delete
# tar cJf annogen-0.1.0-CLEAN.tar.xz annogen-0.1.0
Source0:       %{name}-%{version}-CLEAN.tar.xz
Source1:       http://repo1.maven.org/maven2/annogen/annogen/0.1.0/annogen-0.1.0.pom
Patch0:        annogen-doc-build.patch
BuildArch:     noarch
BuildRequires: ant
BuildRequires: dos2unix
BuildRequires: javapackages-local
BuildRequires: qdox
Requires:      qdox
Source44: import.info

%description
Annogen is a framework which helps you work with JSR175 Annotations. 
In a nutshell, Annogen generates a proxy layer in front of your 
Annotations.

%package javadoc
Group: Development/Java
Summary:      API documentation for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1

sed -i.tools_jar "s|/usr/lib/jvm/java-1.7.0-openjdk-1.7.0.1.x86_64|%{_jvmdir}/java|" build-docs.xml

sed -i.version "s|0.1.1|%{version}|" build.properties

find examples -type f | xargs dos2unix
find license -type f | xargs dos2unix
find docs -name '*.html' -o -name '*.css' | xargs dos2unix

sed -i.qdox2 "s|import com.thoughtworks.qdox.model.AbstractJavaEntity;|import com.thoughtworks.qdox.model.impl.AbstractJavaEntity;|" \
 annogen/adapters/qdox/src/org/codehaus/annogen/override/QDoxElementIdPool.java \
 annogen/adapters/qdox/src/org/codehaus/annogen/view/QDoxAnnoViewer.java

for x in *.xml; do 
  sed -i -e "s/source='1.4'/source='1.6'/; s/target='1.4'/target='1.6'/;" $x;
done

%build

export CLASSPATH=$( build-classpath qdox)
ant jars
ant docs

%install
%mvn_file %{name}:%{name} %{name}
%mvn_artifact %{SOURCE1} build/distribution/%{name}-%{version}.jar
%mvn_install -J build/docs

%files -f .mfiles
%doc examples/
%doc license/LICENSE.txt license/NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc license/LICENSE.txt license/NOTICE.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.1.0-alt1_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.1.0-alt1_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.1.0-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.1.0-alt1_5jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.1.0-alt1_3jpp7
- fc update

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt3_8jpp6
- fixed build with java 7 (fixed patch1)

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt2_8jpp6
- converted from JPackage by jppimport script

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt2_8jpp5
- selected java5 compiler explicitly

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt1_8jpp5
- new jpackage release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt1_3jpp5
- converted from JPackage by jppimport script

* Mon Dec 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.1.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

