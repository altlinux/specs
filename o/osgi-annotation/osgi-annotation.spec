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

Name:           osgi-annotation
Version:        8.0.0
Release:        alt1_3jpp11
Summary:        Annotations for use in compiling OSGi bundles
License:        ASL 2.0
URL:            https://www.osgi.org
BuildArch:      noarch

# Upstream project is behind an account registration system with no anonymous
# read access, so we download the source from maven central instead
Source0:        https://repo1.maven.org/maven2/org/osgi/osgi.annotation/%{version}/osgi.annotation-%{version}.jar
Source1:        https://repo1.maven.org/maven2/org/osgi/osgi.annotation/%{version}/osgi.annotation-%{version}.pom

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%endif
Source44: import.info

%description
Annotations for use in compiling OSGi bundles. This package is not normally
needed at run-time.

%package javadoc
Group: Development/Java
Summary: API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -c -q

mkdir -p src/main/java && mv OSGI-OPT/src/org src/main/java

rm -r org OSGI-OPT

cp -p %{SOURCE1} pom.xml

# Ensure OSGi metadata is generated
%pom_xpath_inject pom:project "
  <packaging>bundle</packaging>
  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <instructions>
            <Bundle-Name>\${project.artifactId}</Bundle-Name>
            <Bundle-SymbolicName>\${project.artifactId}</Bundle-SymbolicName>
          </instructions>
        </configuration>
      </plugin>
    </plugins>
  </build>"

# Known by two names in maven central, so add an alias for the older name
%mvn_alias org.osgi:osgi.annotation org.osgi:org.osgi.annotation

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE
%doc about.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 8.0.0-alt1_3jpp11
- new version

* Fri Jul 02 2021 Igor Vlasenko <viy@altlinux.org> 7.0.0-alt2_4jpp8
- added BR: unzip

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 7.0.0-alt1_4jpp8
- fc update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 7.0.0-alt1_2jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_7jpp8
- java update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_6jpp8
- new jpp release

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_3jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_2jpp8
- new version

