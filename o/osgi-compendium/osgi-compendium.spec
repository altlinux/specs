Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Optionally build with a reduced dependency set
%bcond_with jp_minimal

Name:           osgi-compendium
Version:        7.0.0
Release:        alt1_2jpp8
Summary:        Interfaces and Classes for use in compiling OSGi bundles
License:        ASL 2.0
URL:            http://www.osgi.org
BuildArch:      noarch

Source0:        https://osgi.org/download/r7/osgi.cmpn-%{version}.jar

BuildRequires:  maven-local
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
%if %{without jp_minimal}
BuildRequires:  mvn(javax.persistence:persistence-api)
BuildRequires:  mvn(javax.ws.rs:javax.ws.rs-api) >= 2.1.5
%endif
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

# Delete pre-built binaries
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
%if %{without jp_minimal}
%pom_add_dep javax.persistence:persistence-api::provided
%pom_add_dep javax.ws.rs:javax.ws.rs-api::provided
%else
# Don't compile in Jax RS and JPA support when jp_minimal is activated
rm -r src/main/java/org/osgi/service/jaxrs
rm -r src/main/java/org/osgi/service/jpa
rm -r src/main/java/org/osgi/service/transaction/control/jpa
%endif

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE
%doc about.html

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE


%changelog
* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 7.0.0-alt1_2jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_5jpp8
- java update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_4jpp8
- new jpp release

