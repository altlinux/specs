Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           pmd
Epoch:          0
Version:        5.4.1
Release:        alt1_2jpp8
Summary:        Scans Java source code and looks for potential problems
License:        BSD and ASL 2.0 and LGPLv3+
URL:            http://pmd.sourceforge.net/
BuildArch:      noarch

Source0:        http://downloads.sourceforge.net/project/pmd/pmd/%{version}/pmd-src-%{version}.zip

# fix api incompatibilities with newer saxon
# not sent upstream
Patch1:         saxon.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(jaxen:jaxen)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.javacc:javacc)
BuildRequires:  mvn(net.sf.saxon:saxon)
BuildRequires:  mvn(net.sourceforge.pmd:pmd-build)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-testutil)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-markdown)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires:  mvn(org.mozilla:rhino)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info

%description
PMD scans Java source code and looks for potential problems like:
* Possible bugs: empty try/catch/finally/switch statements
+ Dead code: unused local variables, parameters and private methods
+ Suboptimal code: wasteful String/StringBuffer usage
+ Overcomplicated expressions: unnecessary if statements, for loops
  that could be while loops
+ Duplicate code: copied/pasted code means copied/pasted bugs

PMD has plugins for JDeveloper, Eclipse, JEdit, JBuilder, BlueJ,
CodeGuide, NetBeans/Sun Java Studio Enterprise/Creator, IntelliJ IDEA,
TextPad, Maven, Ant, Gel, JCreator, and Emacs.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-src-%{version}
%patch1 -p1

# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.class" -exec rm -f {} \;

%mvn_alias : pmd:pmd

%pom_xpath_remove pom:build/pom:extensions

%pom_xpath_set pom:parent/pom:version %{version} */pom.xml

sed -i 's/net.sourceforge.saxon/net.sf.saxon/' `find -name pom.xml`

%pom_xpath_set -r '//pom:property[@name="javacc.jar"]/@value' `xmvn-resolve net.java.dev.javacc:javacc`

%build
# tests require com.github.tomakehurst:wiremock
%mvn_build -f -- -P!jdk9-disabled

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.4.1-alt1_2jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.4.1-alt1_1jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt5_15jpp7
- new release

* Thu Jul 24 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt5_14jpp7
- merged junit-junit4

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt4_14jpp7
- fixed build with new junit

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt3_14jpp7
- fc update

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt3_2jpp6
- dropped velocity14

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt2_2jpp6
- fixed build with java 7

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt1_2jpp6
- new jpp release

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.2.5-alt1_1jpp5
- new jpp release

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.2.4-alt1_2jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.9-alt1_2jpp5
- converted from JPackage by jppimport script

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.6-alt1_1jpp1.7
- converted from JPackage by jppimport script

