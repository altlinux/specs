Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name properties-maven-plugin
%define version 1.0
%global namedreltag -alpha-2
%global namedversion %{version}%{?namedreltag}
Name:          properties-maven-plugin
Version:       1.0
Release:       alt3_0.11.alpha2jpp8
Summary:       Properties Maven Plugin
License:       ASL 2.0
URL:           http://www.mojohaus.org/properties-maven-plugin/
# Source code available @ https://github.com/mojohaus/properties-maven-plugin
# svn export http://svn.codehaus.org/mojo/tags/properties-maven-plugin-1.0-alpha-2/
# tar czf properties-maven-plugin-1.0-alpha-2-src-svn.tar.gz properties-maven-plugin-1.0-alpha-2
Source0:       %{name}-%{namedversion}-src-svn.tar.gz
# reported @ https://github.com/mojohaus/properties-maven-plugin/issues/2
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch:     noarch
Source44: import.info

%description
The Properties Maven Plugin is here to make life a little easier when dealing
with properties. It provides goals to read and write properties from files.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# use maven 3.x apis
sed -i "s|maven-project|maven-core|" pom.xml

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%mvn_file :%{name} %{name}

%build

# no test to run
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.11.alpha2jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.10.alpha2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.6.alpha2jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.4.alpha2jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.2.alpha2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.2.alpha2jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.2.alpha2jpp7
- new version

