Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       modeler
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          2.0.1
Release:          alt1_11jpp7
Summary:          Model MBeans utility classes
Group:            Development/Java
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
# POM file based on the one from an unreleased upstream snapstream
Source1:          pom.xml
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    ant
BuildRequires:    apache-commons-beanutils
BuildRequires:    apache-commons-digester
BuildRequires:    apache-commons-logging
BuildRequires:    maven-local

Requires:         jpackage-utils
Requires:         apache-commons-beanutils
Requires:         apache-commons-digester
Requires:         apache-commons-logging
Source44: import.info

%description
Commons Modeler makes the process of setting up JMX (Java Management 
Extensions) MBeans easier by configuring the required meta data using an XML 
descriptor. In addition, Modeler provides a factory mechanism to create the 
actual Model MBean instances.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' RELEASE-NOTES.txt
sed -i 's/\r//' NOTICE.txt

# Copy pom file into place
cp -p %{SOURCE1} .

# Remove redundant dep on mx4j
%pom_remove_dep mx4j:mx4j-jmx

# Fix ant dependency
%pom_remove_dep ant:ant
%pom_add_dep org.apache.ant:ant:1.8

%build
mvn-rpmbuild install javadoc:aggregate -Dproject.build.sourceEncoding=UTF-8

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
(cd %{buildroot}%{_javadir} && for jar in *; do ln -sf ${jar} `echo $jar| sed  "s|apache-||g"`; done)

# pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap -a "org.apache.commons:%{short_name}" JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt1_11jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1:2.0.1-alt1_9jpp7
- fc update

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_0.r832084.4jpp6
- set target 5

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_0.r832084.4jpp6
- new version

