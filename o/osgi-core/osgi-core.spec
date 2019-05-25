Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           osgi-core
Version:        7.0.0
Release:        alt1_1jpp8
Summary:        OSGi Core API
License:        ASL 2.0
URL:            https://www.osgi.org
BuildArch:      noarch

Source0:        https://osgi.org/download/r7/osgi.core-%{version}.jar

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.osgi:osgi.annotation)
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
* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 7.0.0-alt1_1jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_6jpp8
- java update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_5jpp8
- new jpp release

