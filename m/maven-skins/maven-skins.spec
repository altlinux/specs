BuildRequires: /proc
BuildRequires: jpackage-compat
%global app_version 1.0-SNAPSHOT
%global def_version 1.1-SNAPSHOT
%global cla_version 1.1-SNAPSHOT
%global sty_version 1.2-SNAPSHOT

Name:           maven-skins
Version:        5
Release:        alt2_6jpp7
Summary:        Maven Skins

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/skins/
# svn export http://svn.apache.org/repos/asf/maven/skins/tags/maven-skins-5
# tar caf maven-skins-5-tar.xz maven-skins-5/
Source0:        %{name}-%{version}.tar.xz
BuildArch: noarch

BuildRequires:  maven
BuildRequires:  maven-install-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-site-plugin
Requires:       jpackage-utils
Source44: import.info

%description
Skins for the maven site generator. 

%prep
%setup -q 

sed -i -e "s|5-SNAPSHOT|5|g" maven-application-skin/pom.xml
sed -i -e "s|5-SNAPSHOT|5|g" maven-default-skin/pom.xml
sed -i -e "s|5-SNAPSHOT|5|g" maven-classic-skin/pom.xml
sed -i -e "s|5-SNAPSHOT|5|g" maven-stylus-skin/pom.xml
rm -fr src/site/site.xml

%build
mvn-rpmbuild install

%install

# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -m 644 maven-application-skin/target/maven-application-skin-%{app_version}.jar   %{buildroot}%{_javadir}/%{name}/maven-application-skin.jar
install -m 644 maven-default-skin/target/maven-default-skin-%{def_version}.jar   %{buildroot}%{_javadir}/%{name}/maven-default-skin.jar
install -m 644 maven-classic-skin/target/maven-classic-skin-%{cla_version}.jar   %{buildroot}%{_javadir}/%{name}/maven-classic-skin.jar
install -m 644 maven-stylus-skin/target/maven-stylus-skin-%{sty_version}.jar   %{buildroot}%{_javadir}/%{name}/maven-stylus-skin.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom
install -pm 644 maven-application-skin/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-maven-application-skin.pom
%add_maven_depmap JPP.%{name}-maven-application-skin.pom %{name}/maven-application-skin.jar
install -pm 644 maven-default-skin/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-maven-default-skin.pom
%add_maven_depmap JPP.%{name}-maven-default-skin.pom %{name}/maven-default-skin.jar
install -pm 644 maven-classic-skin/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-maven-classic-skin.pom
%add_maven_depmap JPP.%{name}-maven-classic-skin.pom %{name}/maven-classic-skin.jar
install -pm 644 maven-stylus-skin/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-maven-stylus-skin.pom
%add_maven_depmap JPP.%{name}-maven-stylus-skin.pom %{name}/maven-stylus-skin.jar

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 5-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 5-alt1_6jpp7
- new version

