# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%global project felix
%global bundle org.apache.felix.framework
%global groupId org.apache.felix

Name:           %{project}-framework
Version:        4.2.1
Release:        alt1_1jpp7
Summary:        Apache Felix Framework

Group:          Development/Java
License:        ASL 2.0
URL:            http://felix.apache.org
Source0:        http://www.apache.org/dist/%{project}/%{bundle}-%{version}-source-release.tar.gz

BuildArch:      noarch

BuildRequires: jpackage-utils
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: maven-local
BuildRequires: maven-surefire-provider-junit4
BuildRequires: apache-rat-plugin

Requires: felix-osgi-compendium
Requires: felix-osgi-core
Requires: jpackage-utils
Source44: import.info

%description
Apache Felix Framework Interfaces and Classes.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}/%{project}
install -m 644 target/%{bundle}-%{version}.jar \
        %{buildroot}%{_javadir}/%{project}/%{bundle}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{project}-%{bundle}.pom

%add_maven_depmap JPP.%{project}-%{bundle}.pom %{project}/%{bundle}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE NOTICE
%{_mavenpomdir}/JPP.%{project}-%{bundle}.pom 
%{_mavendepmapfragdir}/%{name} 
%{_javadir}/%{project}/*

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1_1jpp7
- new version

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt1_4jpp7
- new version

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt1_3jpp7
- new release

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_3jpp6
- new jpp release

