BuildRequires: maven-dependency-plugin modello
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-verifier-plugin
Version:        1.0
Release:        alt1_5jpp7
Summary:        Maven Verifier Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-verifier-plugin/
#svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-verifier-plugin-1.0/
#tar -zcf maven-verifier-plugin-1.0.tar.gz maven-verifier-plugin-1.0/
Source0:        %{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven
BuildRequires: maven-plugin-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: junit
BuildRequires: plexus-utils
BuildRequires: maven-surefire-provider-junit

Requires: maven
Requires: jpackage-utils
Requires: junit
Requires: plexus-utils

Requires(post):       jpackage-utils
Requires(postun):     jpackage-utils

Obsoletes: maven2-plugin-verifier <= 0:2.0.8
Provides: maven2-plugin-verifier = 1:%{version}-%{release}
Source44: import.info

%description
Assists in integration testing by means of evaluating 
success/error conditions read from a configuration file.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q 

%build
mvn-rpmbuild install javadoc:javadoc

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar  %{buildroot}%{_javadir}/%{name}.jar

%add_to_maven_depmap org.apache.maven.plugins maven-verifier-plugin %{version} JPP maven-verifier-plugin

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5jpp7
- new version

