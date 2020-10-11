Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           maven-shade-plugin
Version:        3.2.1
Release:        alt1_1jpp8
Summary:        This plugin provides the capability to package the artifact in an uber-jar
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/%{name}
BuildArch:      noarch

Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-transfer)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.jdom:jdom2)
BuildRequires:  mvn(org.mockito:mockito-all)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.vafer:jdependency)
BuildRequires:  mvn(xmlunit:xmlunit)
Source44: import.info

%description
This plugin provides the capability to package the artifact in an
uber-jar, including its dependencies and to shade - i.e. rename - the
packages of some of the dependencies.


%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q

rm src/test/jars/plexus-utils-1.4.1.jar
ln -s $(build-classpath plexus/utils) src/test/jars/plexus-utils-1.4.1.jar

%pom_remove_dep 'com.google.guava:guava:'
%pom_add_dep 'com.google.guava:guava'

sed -i 's/import org\.apache\.maven\.shared\.transfer\.artifact\.\(.*\)/import org.apache.maven.shared.artifact.\1/' src/main/java/org/apache/maven/plugins/shade/mojo/ShadeMojo.java
sed -i 's/import org\.apache\.maven\.shared\.transfer\.artifact\.\(.*\)/import org.apache.maven.shared.artifact.\1/' src/test/java/org/apache/maven/plugins/shade/mojo/ShadeMojoTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_1jpp8
- new version

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.1-alt1_3jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_3jpp8
- java fc28+ update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_1jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_3jpp8
- fc27 update

* Mon Oct 30 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.3-alt1_1jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.2-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_2jpp8
- unbootsrap build

* Wed Jan 27 2016 Igor Vlasenko <viy@altlinux.ru> 2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_1jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_4jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_1jpp7
- rebuild with maven-local

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_1jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_2jpp7
- new version

* Thu Apr 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2jpp
- reverted to bootstrap pack due to regression

* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_2jpp7
- complete build

* Tue Mar 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

