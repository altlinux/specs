# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires:  maven2-plugin-deploy
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-shade-plugin
Version:        2.0
Release:        alt2_1jpp7
Summary:        This plugin provides the capability to package the artifact in an uber-jar

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/%{name}
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: maven-local
BuildRequires: maven-wagon
BuildRequires: plexus-container-default
BuildRequires: plexus-containers-component-metadata
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-testing-harness
BuildRequires: jdependency >= 0.6
BuildRequires: xmlunit
Requires: ant
Requires: maven
Requires: jpackage-utils
Requires: jdependency >= 0.6

Obsoletes: maven2-plugin-shade <= 0:2.0.8
Provides: maven2-plugin-shade = 1:%{version}-%{release}
Source44: import.info

%description
This plugin provides the capability to package the artifact in an
uber-jar, including its dependencies and to shade - i.e. rename - the
packages of some of the dependencies.


%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q

rm src/test/jars/plexus-utils-1.4.1.jar
ln -s $(build-classpath plexus/utils) src/test/jars/plexus-utils-1.4.1.jar

%build
# A class from aopalliance is not found. Simply adding BR does not solve it
mvn-rpmbuild install javadoc:aggregate -Dmaven.test.skip

%install
# jars
install -Dpm 644 target/%{name}-%{version}.jar   %{buildroot}%{_javadir}/%{name}.jar

# poms
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
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
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2_1jpp7
- rebuild with maven-local

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_1jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_2jpp7
- new version

* Thu Apr 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2jpp
- reverted to bootstrap pack due to regression

* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_2jpp7
- complete build

* Tue Mar 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

