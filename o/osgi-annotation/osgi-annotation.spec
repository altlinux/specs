Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:    osgi-annotation
Version: 6.0.0
Release: alt1_3jpp8
Summary: Annotations for use in compiling OSGi bundles

License: ASL 2.0
URL:     http://www.osgi.org/
# Upstream project is behind an account registration system with no anonymous
# read access, so we download the source from maven central instead
Source0: http://repo1.maven.org/maven2/org/osgi/osgi.annotation/%{version}/osgi.annotation-%{version}-sources.jar
Source1: http://repo1.maven.org/maven2/org/osgi/osgi.annotation/%{version}/osgi.annotation-%{version}.pom

BuildArch:     noarch

BuildRequires: maven-local
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

mkdir -p src/main/resources && mv about.html src/main/resources
mkdir -p src/main/java && mv org src/main/java
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
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE
%dir %{_javadir}/osgi-annotation
%dir %{_mavenpomdir}/osgi-annotation

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_3jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1_2jpp8
- new version

