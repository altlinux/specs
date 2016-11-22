Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name log4j-jboss-logmanager
%define version 1.1.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             log4j-jboss-logmanager
Version:          1.1.0
Release:          alt1_3jpp8
Summary:          JBoss Log4j Emulation
License:          ASL 2.0
Url:              https://github.com/jboss-logging/log4j-jboss-logmanager
Source0:          https://github.com/jboss-logging/log4j-jboss-logmanager/archive/%{namedversion}.tar.gz
Source1:          LICENSE

BuildRequires:    jboss-parent
BuildRequires:    jboss-modules
BuildRequires:    jboss-logmanager
BuildRequires:    jboss-logging
BuildRequires:    junit
BuildRequires:    maven-local

%if 0%{?fedora} >= 21
BuildRequires:    log4j12
%else
BuildRequires:    log4j
%endif

BuildArch:        noarch
Source44: import.info

%description
This package contains the JBoss Log4J Emulation.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n log4j-jboss-logmanager-%{namedversion}

cp %{SOURCE1} .

%pom_remove_plugin :maven-shade-plugin
%pom_xpath_set "pom:dependencies/pom:dependency[pom:artifactId = 'log4j']/pom:version" "12"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_3jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_2jpp8
- unbootsrap build

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

