# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%global project felix
%global bundle org.apache.felix.main
%global groupId org.apache.felix

Name:    %{project}-main
Version: 4.2.0
Release: alt1_1jpp7
Summary: Apache Felix Main

Group:   Development/Java
License: ASL 2.0
URL:     http://felix.apache.org
Source0: http://www.apache.org/dist/%{project}/%{bundle}-%{version}-source-release.tar.gz

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: felix-bundlerepository
BuildRequires: felix-gogo-command
BuildRequires: felix-gogo-runtime
BuildRequires: felix-gogo-shell
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: felix-framework >= 4.2.0
BuildRequires: maven-local
BuildRequires: maven-dependency-plugin
BuildRequires: maven-surefire-provider-junit4

Requires: felix-bundlerepository
Requires: felix-gogo-command
Requires: felix-gogo-runtime
Requires: felix-gogo-shell
Requires: felix-osgi-compendium
Requires: felix-osgi-core
Requires: felix-framework >= 4.2.0
Requires: jpackage-utils
Source44: import.info
Obsoletes: felix < 2

%description
Apache Felix Main Classes.

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
%{_javadir}/%{project}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_1jpp7
- new version

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt3_8jpp7
- new release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt3_6jpp6
- fixed build with maven3

* Sun Jan 15 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt2_6jpp6
- obsolete felix1

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_6jpp6
- new jpp release

