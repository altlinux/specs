Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 5.0.1
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             hibernate-commons-annotations
Version:          5.0.1
Release:          alt1_4jpp8
Summary:          Hibernate Annotations

# For details see:
# - https://github.com/hibernate/hibernate-commons-annotations/commit/4a902b4f97f923f9044a4127357b44fe5dc39cdc
# - https://github.com/hibernate/hibernate-commons-annotations/commit/a11c44cd65dadcedaf8981379b94a2c4e31428d1
License:          LGPLv2
# Incorrect Free Software Foundation address https://hibernate.atlassian.net/browse/HCANN-78
URL:              http://www.hibernate.org/

Source0:          https://github.com/hibernate/hibernate-commons-annotations/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
Source1:          https://repository.jboss.org/nexus/service/local/repositories/central/content/org/hibernate/common/%{name}/%{namedversion}/%{name}-%{namedversion}.pom

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.bsc.maven:maven-processor-plugin)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
Source44: import.info


%description
Following the DRY (Don't Repeat Yourself) principle, 
Hibernate Validator let's you express your domain 
constraints once (and only once) and ensure their 
compliance at various level of your system 
automatically.

Common reflection code used in support of annotation processing.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n hibernate-commons-annotations-%{namedversion}
# Cleanup
find . -name '*.class' -print -delete
find . -name '*.jar' -print -delete

cp %{SOURCE1} pom.xml

# Set encodig
%pom_xpath_inject pom:project "
<properties>
 <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
 <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
</properties>"

# Generate logging source
%pom_add_plugin org.bsc.maven:maven-processor-plugin:2.2.4 . "
<configuration>
    <defaultOutputDirectory>\${project.build.directory}/generated-sources/logging</defaultOutputDirectory>
    <processors>
        <processor>org.jboss.logging.processor.apt.LoggingToolsProcessor</processor>
    </processors>
</configuration>
<executions>
    <execution>
        <id>process</id>
        <phase>generate-sources</phase>
        <goals>
            <goal>process</goal>
        </goals>
    </execution>
</executions>
<dependencies>
    <dependency>
        <groupId>org.jboss.logging</groupId>
        <artifactId>jboss-logging-processor</artifactId>
        <version>2.0.1.Final</version>
    </dependency>
</dependencies>"

# Inject and configure MANIFEST items
%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin:2.6 . "
<configuration>
  <archive>
    <manifestFile>\${project.build.outputDirectory}/META-INF/MANIFEST.MF</manifestFile>
    <manifestEntries>
      <Implementation-Url>http://hibernate.org</Implementation-Url>
      <Implementation-Vendor>Hibernate.org</Implementation-Vendor>
      <Implementation-Vendor-Id>org.hibernate</Implementation-Vendor-Id>
      <Implementation-Version>\${project.version}</Implementation-Version>
      <Main-Class>org.hibernate.annotations.common.Version</Main-Class>
    </manifestEntries>
  </archive>
</configuration>"

# Add OSGi support
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.5.4 . "
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>\${project.groupId}.\${project.artifactId}</Bundle-SymbolicName>
    <Bundle-Name>\${project.artifactId}</Bundle-Name>
    <Bundle-Vendor>Hibernate.org</Bundle-Vendor>
    <Bundle-Version>\${project.version}</Bundle-Version>
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
</executions>"
# Add missing deps
%pom_add_dep org.jboss.logging:jboss-logging-annotations:2.0.1.Final:compile
%pom_add_dep junit:junit:4.12:test

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc changelog.txt readme.txt
%doc --no-dereference lgpl.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference lgpl.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.1-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.4-alt1_2jpp8
- java 8 mass update

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt1_2jpp7
- new version

