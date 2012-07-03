# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-deploy-plugin
Version:        2.7
Release:        alt1_2jpp7
Summary:        Maven Deploy Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-deploy-plugin/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Dependency on maven-compat was missing in pom.xml resulting in missing classes
Patch0:         %{name}-maven-compat-dep.patch

BuildArch: noarch

# Basic stuff
BuildRequires: jpackage-utils

# Maven and its dependencies
BuildRequires: maven
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-doxia
BuildRequires: maven-doxia-tools
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-archiver
# The following maven packages haven't updated yet
BuildRequires: maven-idea-plugin
BuildRequires: maven-changes-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-invoker-plugin

Requires: maven
Requires: jpackage-utils

Provides:       maven2-plugin-deploy = 0:%{version}-%{release}
Obsoletes:      maven2-plugin-deploy <= 0:2.0.8
Source44: import.info

%description
Uploads the project artifacts to the internal remote repository.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1

%build
# A test class doesn't compile
mvn-rpmbuild -Dmaven.test.skip install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

%add_to_maven_depmap org.apache.maven.plugins maven-deploy-plugin %{version} JPP maven-deploy-plugin

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc DEPENDENCIES LICENSE NOTICE 
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt1_2jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 2.7-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

