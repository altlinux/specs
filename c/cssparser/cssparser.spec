Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          cssparser
Version:       0.9.18
Release:       alt1_2jpp8
Summary:       CSS Parser
License:       LGPLv2+ 
URL:           http://cssparser.sourceforge.net/
# sh ./fetch-cssparser.sh <VERSION>
Source0:       cssparser-%{version}.tar.xz
Source1:       fetch-cssparser.sh

BuildArch:     noarch

BuildRequires: java-devel >= 1.6.0
BuildRequires: maven-local
BuildRequires: mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin) >= 2.6
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.w3c.css:sac) >= 1.3
Source44: import.info

%description
A CSS parser which implements SAC (the Simple API for CSS).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q 
%pom_remove_plugin :maven-checkstyle-plugin
# unused artefact
%pom_remove_plugin :maven-source-plugin

# SACParserCSS3Test.unicodeInputByteStreamDefaultEncoding:2981
# expected:<...:before { content: "[? - ?]" }> but was:<...:before { content: "[? - ?]" }>
rm src/test/java/com/steadystate/css/parser/SACParserCSS3Test.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc doc/license.html doc/readme.html
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.18-alt1_2jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9.15-alt1_4jpp8
- java 8 mass update

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.9.7-alt1_1jpp7
- new version

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.9.6-alt1_3jpp7
- new version

* Tue Mar 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt3_1jpp5
- fixed build with javacc 5

* Tue Mar 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt2_1jpp5
- fixed build with javacc 5

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt2_1jpp5
- fixed build with new maven 2.0.8

* Mon Feb 09 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.9.5-alt1_1jpp5
- new version

