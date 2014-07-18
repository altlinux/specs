BuildRequires: maven-plugin-plugin
Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: maven-jaxb2-plugin
Version: 0.8.1
Release: alt3_7jpp7
Summary: Provides the capability to generate java sources from schemas
Group: Development/Java
License: BSD and ASL 2.0
URL: http://java.net/projects/maven-jaxb2-plugin/pages/Home

# svn export https://svn.java.net/svn/maven-jaxb2-plugin~svn/tags/0.8.1/ maven-jaxb2-plugin-0.8.1
# tar -zcvf maven-jaxb2-plugin-0.8.1.tar.gz maven-jaxb2-plugin-0.8.1
Source0: %{name}-%{version}.tar.gz

# Don't try to use an internal bundled resolver, as this is not available in
# Fedora:
Patch0: %{name}-dont-use-internal-resolver.patch

# Build only version 2.2:
Patch1: %{name}-build-2.2-only.patch

# Adapt for Maven 3:
Patch2: %{name}-adapt-for-maven-3.patch

# Add dependency on codemodel:
Patch3: %{name}-add-codemodel-dependency.patch

# Remove the enconding option as the version of the XJC compiler that we build
# in Fedora doesn't have it:
Patch4: %{name}-remove-enconding-option.patch

BuildArch: noarch

BuildRequires: maven
BuildRequires: jpackage-utils
BuildRequires: xml-commons-resolver
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-anno-plugin
BuildRequires: glassfish-jaxb
BuildRequires: codemodel

Requires: codemodel
Requires: glassfish-jaxb
Requires: maven
Requires: jpackage-utils
Requires: xml-commons-resolver
Requires: maven-anno-plugin
Source44: import.info


%description
This Maven 2 plugin wraps the JAXB 2.x XJC compiler and provides the capability
to generate Java sources from XML Schemas.


%package javadoc
Summary: API documentation for %{name}
Group: Development/Java
Requires: jpackage-utils
BuildArch: noarch


%description javadoc
The API documentation of %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1


%build
mvn-rpmbuild install javadoc:aggregate 


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -Dpm 644 plugin-2.2/target/maven-jaxb22-plugin-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
install -Dpm 644 plugin-core/target/maven-jaxb2-plugin-core-%{version}.jar %{buildroot}%{_javadir}/%{name}-core.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-project.pom
install -Dpm 644 plugin-2.2/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
install -Dpm 644 plugin-core/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-core.pom

# Dependencies map:
%add_maven_depmap JPP-%{name}-project.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
%add_maven_depmap JPP-%{name}-core.pom %{name}-core.jar

# Javadoc files:
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/.


%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*


%files javadoc
%doc %{_javadocdir}/%{name}


%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt3_7jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt1_7jpp7
- new version

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.6.1-alt1_1jpp5
- new version

