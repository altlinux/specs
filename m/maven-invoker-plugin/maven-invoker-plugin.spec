# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-invoker-plugin
Version:        1.8
Release:        alt1_5jpp7
Summary:        Maven Invoker Plugin

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-invoker-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         pom-xml.patch

BuildArch: noarch

# Basic stuff
BuildRequires: jpackage-utils
# Maven and its dependencies
BuildRequires: maven-local
BuildRequires: maven-resources-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-script-interpreter
BuildRequires: maven-invoker
BuildRequires: mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires: mvn(org.apache.maven.doxia:doxia-site-renderer)

# Others
BuildRequires: groovy

Requires: maven
Requires: groovy
Requires: jpackage-utils
Requires: maven-invoker
Requires: maven-shared-reporting-api
Requires: maven-shared-reporting-impl
Requires: maven-script-interpreter
Requires: mvn(org.apache.maven.doxia:doxia-sink-api)
Requires: mvn(org.apache.maven.doxia:doxia-site-renderer)

Provides:       maven2-plugin-invoker = 1:%{version}-%{release}
Obsoletes:      maven2-plugin-invoker <= 0:2.0.8
Source44: import.info

%description
The Maven Invoker Plugin is used to run a set of Maven projects. The plugin 
can determine whether each project execution is successful, and optionally 
can verify the output generated from a given project execution.
  

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q 
%patch0

%build
mvn-rpmbuild \
        -Dmaven.test.failure.ignore=true \
        install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%doc LICENSE NOTICE
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_5jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt3_1jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2_1jpp7
- fixed build

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_1jpp7
- new release

* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_5jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

