# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name properties-maven-plugin
%define version 1.0
%global namedreltag -alpha-2
%global namedversion %{version}%{?namedreltag}
Name:          properties-maven-plugin
Version:       1.0
Release:       alt3_0.4.alpha2jpp7
Summary:       Properties Maven Plugin
Group:         Development/Java
License:       ASL 2.0
URL:           http://mojo.codehaus.org/properties-maven-plugin/
# svn export http://svn.codehaus.org/mojo/tags/properties-maven-plugin-1.0-alpha-2/
# tar czf properties-maven-plugin-1.0-alpha-2-src-svn.tar.gz properties-maven-plugin-1.0-alpha-2
Source0:       %{name}-%{namedversion}-src-svn.tar.gz

BuildRequires: jpackage-utils
BuildRequires: mojo-parent

BuildRequires: maven-local
BuildRequires: plexus-utils

# test deps (no test to run)
BuildRequires: junit

BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin

Requires:      maven
Requires:      plexus-utils

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
The Properties Maven Plugin is here to make life a little easier when dealing
with properties. It provides goals to read and write properties from files.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# use maven 3.x apis
sed -i "s|maven-project|maven-core|" pom.xml

%build

mvn-rpmbuild install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{namedversion}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.4.alpha2jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.2.alpha2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.2.alpha2jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.2.alpha2jpp7
- new version

