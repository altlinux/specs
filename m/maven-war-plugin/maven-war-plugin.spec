# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
# END SourceDeps(oneline)
Requires: xpp3-minimal
BuildRequires: xpp3-minimal
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-war-plugin
Version:        2.3
Release:        alt1_5jpp7
Summary:        Maven WAR Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-war-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch: noarch

# Basic stuff
BuildRequires: jpackage-utils
# Maven and its dependencies
BuildRequires: maven-local
BuildRequires: maven-plugin-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-shared-filtering
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-idea-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-changes-plugin
# Others
BuildRequires: xstream

Requires: maven
Requires: xstream
Requires: jpackage-utils

Provides:       maven2-plugin-war = 0:%{version}-%{release}
Obsoletes:      maven2-plugin-war <= 0:2.0.8
Source44: import.info

%description
Builds a Web Application Archive (WAR) file from the project output and its 
dependencies.

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
mvn-rpmbuild -Dmaven.test.skip=true \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

%add_to_maven_depmap org.apache.maven.plugins maven-war-plugin %{version} JPP maven-war-plugin

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE NOTICE

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.3-alt1_5jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_2jpp7
- new release

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2_5jpp7
- fixed build with xpp3

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_5jpp7
- new version

