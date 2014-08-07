BuildRequires: maven-plugin-plugin
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:		maven-toolchains-plugin
Version:	1.0
Release:	alt4_4jpp7
Summary:	Maven plugin for sharing configuration across projects

Group:		Development/Java
License:	ASL 2.0
URL:		http://maven.apache.org/plugins/maven-toolchains-plugin/
Source0:	http://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
# Dep on plexus-container-default is needed, otherwise a wrong implementation of
# PlexusConfiguration class is taken from sisu-inject-plexus.jar
Patch0:		%{name}-plexus.patch

BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	jpackage-utils
BuildRequires:	plexus-container-default
BuildRequires:	maven-surefire-provider-junit4

Requires:	maven
Requires:	jpackage-utils
Source44: import.info

%description
The Toolchains Plugins allows to share configuration across plugins. For
example to make sure the plugins like compiler, surefire, javadoc, webstart
etc. all use the same JDK for execution. Similarly to maven-enforcer-plugin, it
allows to control environmental constraints in the build.

%package javadoc
Summary:	API documentation for %{name}
Group:		Development/Java
Requires:	jpackage-utils
BuildArch: noarch

%description javadoc
The API documentation of %{name}.


%prep
%setup -q
%patch0 -p1

rm -rf bin

%build
mvn-rpmbuild install javadoc:aggregate 

%install
# JAR
install -Dpm 644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# POM
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# JavaDoc
install -Ddm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}


%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt4_4jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_4jpp7
- new version

