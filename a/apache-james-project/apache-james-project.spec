# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global server_ver      2.2.0
%global short_name      apache-james

Name:             %{short_name}-project
Version:          1.6
Release:          alt2_3jpp7
Summary:          Main project POM files and resources
License:          ASL 2.0
Group:            Development/Java
URL:              http://james.apache.org/
Source0:          http://repo1.maven.org/maven2/org/apache/james/james-parent/%{version}/james-parent-%{version}-source-release.zip
BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    apache-commons-parent

Requires:         maven
Requires:         jpackage-utils
Requires(post):   jpackage-utils
Requires(postun): jpackage-utils
Source44: import.info

%description
Main project POM files and resources for Apache James project


%prep
%setup -q -n james-parent-%{version}

%build
# to build james skin for site plugin
mvn-rpmbuild install

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}/%{short_name}
install -p -m 644 maven-skin/target/maven-skin-%{version}.jar %{buildroot}%{_javadir}/%{short_name}/maven-skin.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 maven-skin/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-maven-skin.pom
%add_to_maven_depmap org.apache.james maven-skin %{version} JPP/%{short_name} maven-skin

install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-parent.pom
%add_to_maven_depmap org.apache.james james-parent %{version} JPP/%{short_name} parent

install -pm 644 project/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-project.pom
%add_to_maven_depmap org.apache.james james-project %{version} JPP/%{short_name} project

install -pm 644 project/server/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-server-root.pom
%add_to_maven_depmap org.apache.james james-server-root %{version} JPP/%{short_name} server-root

pom_ver=`echo %{server_ver} | tr . -`
install -pm 644 project/server/%{server_ver}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-server-site.pom
%add_to_maven_depmap org.apache.james james-server-site-$pom_ver %{version} JPP/%{short_name} server-site

%files
%doc LICENSE NOTICE
%{_javadir}/%{short_name}/*.jar
%{_mavenpomdir}/JPP.%{short_name}-maven-skin.pom
%{_mavenpomdir}/JPP.%{short_name}-parent.pom
%{_mavenpomdir}/JPP.%{short_name}-project.pom
%{_mavenpomdir}/JPP.%{short_name}-server-root.pom
%{_mavenpomdir}/JPP.%{short_name}-server-site.pom
%{_mavendepmapfragdir}/*


%changelog
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.6-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_3jpp7
- new release

