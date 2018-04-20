Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           osgi-compendium
Version:        6.0.0
Release:        alt1_5jpp8
Summary:        Interfaces and Classes for use in compiling OSGi bundles
License:        ASL 2.0
URL:            http://www.osgi.org
BuildArch:      noarch

Source0:        https://osgi.org/download/r6/osgi.cmpn-%{version}.jar

BuildRequires:  maven-local
BuildRequires:  mvn(javax.persistence:persistence-api)
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.osgi:osgi.annotation)
BuildRequires:  mvn(org.osgi:osgi.core)
Source44: import.info


%description
OSGi Compendium, Interfaces and Classes for use in compiling bundles.


%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.


%prep
%setup -q -c

rm -r org
find -name '*.class' -delete

mkdir -p src/main/{java,resources}
mv OSGI-OPT/src/org src/main/java/
mv xmlns src/main/resources

# J2ME stuff
rm -r src/main/java/org/osgi/service/io

mv META-INF/maven/org.osgi/osgi.cmpn/pom.xml .

%pom_xpath_inject pom:project '
<packaging>bundle</packaging>
<properties>
  <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
</properties>
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <extensions>true</extensions>
      <configuration>
        <instructions>
          <Bundle-Name>${project.artifactId}</Bundle-Name>
          <Bundle-SymbolicName>${project.artifactId}</Bundle-SymbolicName>
        </instructions>
      </configuration>
    </plugin>
  </plugins>
</build>'

%pom_add_dep org.osgi:osgi.annotation::provided
%pom_add_dep org.osgi:osgi.core::provided
%pom_add_dep javax.servlet:javax.servlet-api::provided
%pom_add_dep javax.persistence:persistence-api::provided

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE
%doc about.html

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE


%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_5jpp8
- java update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_4jpp8
- new jpp release

