# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/unzip
# END SourceDeps(oneline)
Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           osgi-core
Version:        8.0.0
Release:        alt1_3jpp11
Summary:        OSGi Core API

License:        ASL 2.0
URL:            https://www.osgi.org

Source0:        https://docs.osgi.org/download/r8/osgi.core-%{version}.jar

BuildArch:      noarch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.osgi:osgi.annotation)
%endif
Source44: import.info

%description
OSGi Core, Interfaces and Classes for use in compiling bundles.

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

mv META-INF/maven/org.osgi/osgi.core/pom.xml .

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

%mvn_alias : org.osgi:org.osgi.core

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8

%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE
%doc about.html

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 8.0.0-alt1_3jpp11
- new version

* Fri Jul 02 2021 Igor Vlasenko <viy@altlinux.org> 7.0.0-alt2_3jpp8
- added BR: unzip

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 7.0.0-alt1_3jpp8
- fc update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 7.0.0-alt1_1jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_6jpp8
- java update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_5jpp8
- new jpp release

