BuildRequires: /proc
BuildRequires: jpackage-compat
# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%global project felix
%global bundle org.osgi.compendium
%global groupId org.apache.felix
%global artifactId %{bundle}

Name:    %{project}-osgi-compendium
Version: 1.4.0
Release: alt2_3jpp6
Summary: Felix OSGi R4 Compendium Bundle

Group:   Development/Java
License: ASL 2.0
URL:     http://felix.apache.org
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz
Source1: %{name}.demap

# Remove <parent>
Patch0: %{bundle}-%{version}~pom.xml.patch

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven2
BuildRequires:    maven2-plugin-compiler
BuildRequires:    maven2-plugin-install
BuildRequires:    maven2-plugin-jar
BuildRequires:    maven2-plugin-javadoc
BuildRequires:    maven2-plugin-release
BuildRequires:    maven2-plugin-resources
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-plugin-bundle
BuildRequires: felix-osgi-core
BuildRequires: tomcat6-servlet-2.5-api
BuildRequires: felix-osgi-foundation

Requires: felix-osgi-core
Requires: felix-osgi-foundation
#Requires: tomcat6-servlet-2.5-api

Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info

%description
OSGi Service Platform Release 4 Compendium Interfaces and Classes.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%global POM %{_mavenpomdir}/JPP.%{project}-%{name}.pom

%prep
%setup -q -n %{bundle}-%{version}
%patch0 -p1 -b .sav

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
%__mkdir_p $MAVEN_REPO_LOCAL
mvn-jpp -e \
        -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
        -Dmaven2.jpp.depmap.file="%{SOURCE1}" \
        install javadoc:javadoc

%install
%__rm -rf %{buildroot}

# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{project}
install -m 644 target/%{bundle}-%{version}.jar \
        %{buildroot}%{_javadir}/%{project}/%{bundle}-%{version}.jar

# versionless symlinks to jars
(cd %{buildroot}%{_javadir}/%{project} && for jar in *-%{version}*.jar; \
    do %__ln_s -f $jar `echo $jar| sed "s|-%{version}||g"`; done)

%add_to_maven_depmap %{groupId} %{artifactId} %{version} JPP/%{project} %{bundle}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{POM}

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%__rm -rf target/site/api*

%files
%doc LICENSE
%{_javadir}/%{project}/*
%{POM}
%config(noreplace) %{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Mon Sep 05 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_3jpp6
- dropped tomcat6-servlet-2.5-api dep to fix apache-commons-chain

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_3jpp6
- new jpp release

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

