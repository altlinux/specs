BuildRequires: /proc
BuildRequires: jpackage-compat
%global project felix
%global bundle org.apache.felix.gogo.command
%global groupId org.apache.felix
%global artifactId %{bundle}

Name:           %{project}-gogo-command
Version:        0.12.0
Release:        alt2_4jpp7
Summary:        Apache Felix Gogo Command

Group:          Development/Java
License:        ASL 2.0
URL:            http://felix.apache.org
Source0:        http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

Patch0:         felix-gogo-command-pom.xml.patch
Patch1:         java7compatibility.patch

BuildArch:      noarch

# This is to ensure we get OpenJDK and not GCJ
BuildRequires:  maven
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  jpackage-utils

BuildRequires:  felix-osgi-core
BuildRequires:  felix-framework
BuildRequires:  felix-osgi-compendium
BuildRequires:  felix-gogo-runtime
BuildRequires:  felix-gogo-parent
BuildRequires:  mvn(org.apache.felix:org.apache.felix.bundlerepository)


Requires:       felix-framework
Requires:       felix-osgi-compendium
Requires:       felix-gogo-runtime
Requires:       mvn(org.apache.felix:org.apache.felix.bundlerepository)
Source44: import.info

%description
Provides basic shell commands for Gogo.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%global POM %{_mavenpomdir}/JPP.%{project}-%{bundle}.pom

%prep
%setup -q -n %{bundle}-%{version} 
%patch0 -p1
%patch1 -p1

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{project}
install -m 644 target/%{bundle}-%{version}.jar \
        %{buildroot}%{_javadir}/%{project}/%{bundle}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{project}-%{bundle}.pom

%add_maven_depmap JPP.%{project}-%{bundle}.pom %{project}/%{bundle}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
%__cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.12.0-alt1_4jpp7
- new release

