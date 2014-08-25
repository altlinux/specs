Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven-local unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-shared-jar
Version:        1.1
Release:        alt1_2jpp7
# Maven-shared defines maven-shared-jar version as 1.1
Epoch:          1
Summary:        Maven JAR Utilities
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-shared-jar
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  plexus-containers-container-default
BuildRequires:  maven-surefire-provider-junit
Requires:       apache-commons-collections
Requires:       bcel
Requires:       jpackage-utils
Requires:       maven
Requires:       plexus-digest

Obsoletes:      maven-shared-jar < %{epoch}:%{version}-%{release} 
Provides:       maven-shared-jar = %{epoch}:%{version}-%{release}
Source44: import.info

%description
Utilities that help identify the contents of a JAR, including Java class
analysis and Maven metadata analysis.

This is a replacement package for maven-shared-jar

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.


%prep
%setup -q

%pom_add_dep org.codehaus.plexus:plexus-container-default

find -type f -iname '*.jar' -delete

# Replace plexus-maven-plugin with plexus-component-metadata
find -name 'pom.xml' -exec sed \
    -i 's/<artifactId>plexus-maven-plugin<\/artifactId>/<artifactId>plexus-component-metadata<\/artifactId>/' '{}' ';'
find -name 'pom.xml' -exec sed \
    -i 's/<goal>descriptor<\/goal>/<goal>generate-metadata<\/goal>/' '{}' ';'

%build
# Tests require the jars that were removed
mvn-rpmbuild package javadoc:aggregate -Dmaven.test.skip

%install
# JAR
install -Ddm 755 %{buildroot}/%{_javadir}
install -Dpm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM
install -Ddm 755 %{buildroot}/%{_mavenpomdir}
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# JavaDoc
install -Ddm 755 %{buildroot}/%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE NOTICE
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE NOTICE
%doc %{_javadocdir}/%{name}


%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_2jpp7
- update

* Sun Aug 24 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

