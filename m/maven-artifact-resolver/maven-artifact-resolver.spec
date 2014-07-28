# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-artifact-resolver
Version:        1.0
Release:        alt1_7jpp7
# Epoch is added because the original package's version in maven-shared is 1.1-SNAPSHOT
Epoch:          1
Summary:        Maven Artifact Resolution API
Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/shared/%{name}
Source0:        http://central.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Replaced plexus-maven-plugin with plexus-component-metadata
Patch0:         %{name}-plexus.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  maven-artifact-manager
BuildRequires:  maven-project
BuildRequires:  maven-shared

Requires:       jpackage-utils
Requires:       maven-artifact-manager
Requires:       maven-project
Requires:       maven-shared

Obsoletes:      maven-shared-artifact-resolver < %{epoch}:%{version}-%{release}
Provides:       maven-shared-artifact-resolver = %{epoch}:%{version}-%{release}
Source44: import.info

%description
Provides a component for plugins to easily resolve project dependencies.


%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0 -p1

%pom_xpath_inject pom:project/pom:dependencies "
<dependency>
  <groupId>org.apache.maven</groupId>
  <artifactId>maven-compat</artifactId>
  <version>1.0</version>
</dependency>" pom.xml

# Incompatible method invocation
rm src/test/java/org/apache/maven/shared/artifact/resolver/DefaultProjectDependenciesResolverIT.java

%build
mvn-rpmbuild install javadoc:aggregate

%install
# JAR
install -dm 755 %{buildroot}%{_javadir}
install -pm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM
install -dm 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# JavaDoc
install -Ddm 755 %{buildroot}/%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%add_maven_depmap

%files
%doc DEPENDENCIES LICENSE NOTICE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%doc %{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_7jpp7
- new release

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_4jpp7
- update

