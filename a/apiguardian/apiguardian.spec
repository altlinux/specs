Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           apiguardian
Version:        1.0.0
Release:        alt1_3jpp8
Summary:        API Guardian Java annotation
License:        ASL 2.0
URL:            https://github.com/apiguardian-team/apiguardian
BuildArch:      noarch

Source0:        https://github.com/apiguardian-team/apiguardian/archive/r%{version}.tar.gz

Source100:      https://repo1.maven.org/maven2/org/apiguardian/apiguardian-api/%{version}/apiguardian-api-%{version}.pom

BuildRequires:  maven-local
Source44: import.info

%description
API Guardian indicates the status of an API element and therefore its
level of stability as well.  It is used to annotate public types,
methods, constructors, and fields within a framework or application in
order to publish their API status and level of stability and to
indicate how they are intended to be used by consumers of the API.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n apiguardian-r%{version}
find -name \*.jar -delete
cp -p %{SOURCE100} pom.xml

# Inject OSGi manifest required by Eclipse
%pom_xpath_inject pom:project "
  <build>
    <pluginManagement>
      <plugins>
        <plugin>
          <artifactId>maven-jar-plugin</artifactId>
          <configuration>
            <archive>
              <manifestEntries>
                <Automatic-Module-Name>org.apiguardian.api</Automatic-Module-Name>
                <Implementation-Title>apiguardian-api</Implementation-Title>
                <Implementation-Vendor>apiguardian.org</Implementation-Vendor>
                <Implementation-Version>%{version}</Implementation-Version>
                <Specification-Title>apiguardian-api</Specification-Title>
                <Specification-Vendor>apiguardian.org</Specification-Vendor>
                <Specification-Version>%{version}</Specification-Version>
                <!-- OSGi metadata required by Eclipse -->
                <Bundle-ManifestVersion>2</Bundle-ManifestVersion>
                <Bundle-SymbolicName>org.apiguardian</Bundle-SymbolicName>
                <Bundle-Version>%{version}</Bundle-Version>
                <Export-Package>org.apiguardian.api;version=\"%{version}\"</Export-Package>
              </manifestEntries>
            </archive>
          </configuration>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>"


%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp8
- fc29 update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp8
- new version

