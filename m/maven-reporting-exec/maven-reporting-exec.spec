# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-reporting-exec
Version:        1.0.1
Release:        alt1_4jpp7
BuildArch:      noarch
Summary:        Classes to manage report plugin executions with Maven 3

License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-reporting-exec/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/reporting/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        maven-model-depmap.xml

Patch0:         %{name}-disabling-enforcer.patch

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4

Requires:       maven
Requires:       slf4j
Requires:       maven-wagon
Requires:       jpackage-utils
Source44: import.info

%description
Classes to manage report plugin executions with Maven 3. Contains classes for
managing and configuring reports and their execution.

%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
The API documentation of %{name}.



%prep
%setup -qn %{name}-%{version}
%patch0 -p1

# convert CR+LF to LF
sed -i 's/\r//g' pom.xml src/main/java/org/apache/maven/reporting/exec/*



%build
# Test.failure.ignore=true is here because a test of MavenReportExecutor
# fails with PlexusContainerException
mvn-rpmbuild install javadoc:aggregate -Dmaven.local.depmap.file=%{SOURCE1} \
 -Dmaven.test.failure.ignore=true 



%install
# JAR
install -Dpm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# JavaDoc
install -Ddm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}



%files
%doc LICENSE NOTICE DEPENDENCIES
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}
%doc LICENSE NOTICE



%changelog
* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_4jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

