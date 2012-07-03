BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-idea-plugin
Version:        2.2
Release:        alt1_7jpp7
Summary:        Maven IDEA Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/%{name}
# svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-idea-plugin-2.2
# tar caf maven-idea-plugin-2.2.tar.xz maven-idea-plugin-2.2
Source0:        %{name}-%{version}.tar.xz
Patch0:         add_compat.patch

BuildArch: noarch

BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: maven
BuildRequires: maven-wagon
BuildRequires: plexus-container-default
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-testing-harness
BuildRequires: dom4j
Requires: ant
Requires: maven
Requires: jpackage-utils

Obsoletes: maven2-plugin-idea <= 0:2.0.8
Provides: maven2-plugin-idea = 1:%{version}-%{release}
Source44: import.info

%description
The IDEA Plugin is used to generate files (ipr, iml, and iws) for a
project so you can work on it using the IDE, IntelliJ IDEA.


%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.


%prep
%setup -q 
%patch0

%build
# we skip test because even with binary mvn release these fail for
# various reasons.
mvn-rpmbuild -e \
        -Dmaven.test.failure.ignore=true \
        install javadoc:javadoc

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Mar 26 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_7jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

