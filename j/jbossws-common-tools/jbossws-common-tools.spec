# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jbossws-common-tools
%define version 1.2.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jbossws-common-tools
Version:          1.2.0
Release:          alt1_6jpp8
Summary:          JBossWS Common Tools
Group:            Development/Other
License:          LGPLv2+ and ASL 2.0
URL:              http://www.jboss.org/jbossws

# svn export http://anonsvn.jboss.org/repos/jbossws/common-tools/tags/jbossws-common-tools-1.2.0.Final/ jbossws-common-tools-1.2.0.Final
# tar cafJ jbossws-common-tools-1.2.0.Final.tar.xz jbossws-common-tools-1.2.0.Final
Source0:          jbossws-common-tools-%{namedversion}.tar.xz
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt

BuildArch:        noarch

BuildRequires:    ant
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    gnu-getopt
BuildRequires:    jbossws-spi
BuildRequires:    jbossws-api
BuildRequires:    jbossws-parent
BuildRequires:    junit
BuildRequires:    plexus-pom
BuildRequires:    plexus-components-pom

%if 0%{?fedora} >= 21
BuildRequires:    log4j12
%else
BuildRequires:    log4j
%endif
Source44: import.info

%description
JBoss Web Services - Common Tools

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jbossws-common-tools-%{namedversion}

cp %{SOURCE1} .

%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'log4j']/pom:version" "12"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_6jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_5jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_7jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_5jpp7
- update

