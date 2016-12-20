Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global bundle org.apache.aries.util

Name:          aries-util
Version:       1.1.1
Release:       alt1_1jpp8
Summary:       Apache Aries Util
License:       ASL 2.0
URL:           http://aries.apache.org/
#Source0:       http://www.apache.org/dist/aries/%%{bundle}-parent-%%{version}-source-release.zip
Source0:       http://central.maven.org/maven2/org/apache/aries/%{bundle}-parent/%{version}/%{bundle}-parent-%{version}-source-release.zip
# org.osgi.service.framework.CompositeBundle was removed
# http://help.eclipse.org/mars/topic/org.eclipse.platform.doc.isv/porting/removals.html#compositeBundles
Patch0:        aries-util-1.1.0-remove-CompositeBundle.patch

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.eclipse:osgi)

BuildArch:     noarch
Source44: import.info

%description
This bundle contains the OSGi common util for Apache Aries.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{bundle}-parent-%{version}
# Do not remove test resources
find . -name  "*.jar" -print ! -type d -delete

%patch0 -p1

%pom_remove_parent
%pom_xpath_inject "pom:project" "<groupId>org.apache.aries</groupId>"
%pom_remove_parent util
%pom_remove_parent util-r42
%pom_xpath_inject "pom:project" "<groupId>org.apache.aries</groupId>" util
%pom_xpath_inject "pom:project" "<groupId>org.apache.aries</groupId>" util-r42

%pom_add_plugin org.apache.felix:maven-bundle-plugin util '
<extensions>true</extensions>
<configuration>
  <excludeDependencies>true</excludeDependencies>
  <instructions>
    <Bundle-Name>${project.name}</Bundle-Name>
    <Bundle-SymbolicName>${project.artifactId}</Bundle-SymbolicName>
    <Export-Package>${aries.osgi.export.pkg}</Export-Package>
    <Import-Package>${aries.osgi.import.pkg}</Import-Package>
    <Private-Package>${aries.osgi.private.pkg}</Private-Package>
    <Implementation-Title>Apache Aries</Implementation-Title>
    <Implementation-Version>${project.version}</Implementation-Version>
    <Bundle-Vendor>The Apache Software Foundation</Bundle-Vendor>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

%pom_add_plugin org.apache.felix:maven-bundle-plugin util-r42 '
<extensions>true</extensions>
<configuration>
  <excludeDependencies>true</excludeDependencies>
  <instructions>
    <Bundle-Name>${project.name}</Bundle-Name>
    <Bundle-SymbolicName>${project.artifactId}</Bundle-SymbolicName>
    <Implementation-Title>Apache Aries</Implementation-Title>
    <Implementation-Version>${project.version}</Implementation-Version>
    <Bundle-Vendor>The Apache Software Foundation</Bundle-Vendor>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

# Useless tasks
%pom_remove_plugin :maven-javadoc-plugin util
%pom_remove_plugin org.apache.aries.versioning:org.apache.aries.versioning.plugin util

# Use eclipse only
# cannot find symbol org.osgi.framework.Bundle#adapt(java.lang.Class<org.osgi.framework.wiring.BundleWiring>)
%pom_remove_dep org.osgi: util-r42
%pom_remove_dep org.osgi: util

%pom_xpath_remove "pom:dependency[pom:artifactId= 'osgi']/pom:scope" util-r42
%pom_xpath_remove "pom:dependency[pom:artifactId= 'osgi']/pom:scope" util
%pom_xpath_remove "pom:dependency[pom:artifactId= 'org.apache.aries.util-r42']/pom:scope" util

%build

# test disabled because of missing dependency:
# org.apache.aries.testsupport:org.apache.aries.testsupport.unit:1.0.0
%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_9jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_8jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_2jpp7
- new version

