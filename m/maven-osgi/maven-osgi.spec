Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-osgi
Version:        0.2.0
Release:        alt1_0jpp7
# Maven-shared defines maven-osgi version as 0.3.0
Epoch:          1
Summary:        Library for Maven-OSGi integration
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-osgi
# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-osgi-0.2.0 maven-osgi-0.2.0
# tar caf maven-osgi-0.2.0.tar.xz maven-osgi-0.2.0/
Source0:        %{name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-plugin-testing-harness
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-shared
Requires:       aqute-bndlib
Requires:       jpackage-utils
Requires:       maven-project
Requires:       maven-shared

#Obsoletes:      maven-shared-osgi < %{epoch}:%{version}-%{release}
Provides:       maven-shared-osgi = %{epoch}:%{version}-%{release}
Source44: import.info

%description
Library for Maven-OSGi integration.

This is a replacement package for maven-shared-osgi

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.


%prep
%setup -q

# Replace plexus-maven-plugin with plexus-component-metadata
find -name 'pom.xml' -exec sed \
    -i 's/<artifactId>plexus-maven-plugin<\/artifactId>/<artifactId>plexus-component-metadata<\/artifactId>/' '{}' ';'
find -name 'pom.xml' -exec sed \
    -i 's/<goal>descriptor<\/goal>/<goal>generate-metadata<\/goal>/' '{}' ';'

cp %{SOURCE1} LICENSE.txt

# There are binary jars in test resources
find -iname '*.jar' -exec rm '{}' ';'

%build
# Binary jars were removed, thus some tests fail
mvn-rpmbuild install javadoc:aggregate -Dmaven.test.failure.ignore

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
%doc LICENSE.txt
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE.txt
%doc %{_javadocdir}/%{name}


%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.2.0-alt1_0jpp7
- new release

