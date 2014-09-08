Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name native2ascii-maven-plugin
%define version 1.0
%global namedreltag -beta-1
%global namedversion %{version}%{?namedreltag}
Name:          native2ascii-maven-plugin
Version:       1.0
Release:       alt3_0.7.beta1jpp7
Summary:       Native2Ascii Maven Plugin
License:       MIT
URL:           http://mojo.codehaus.org/%{name}/
Source0:       http://repo2.maven.org/maven2/org/codehaus/mojo/%{name}/%{namedversion}/%{name}-%{namedversion}-source-release.zip

BuildRequires: mvn(org.codehaus.mojo:mojo-parent)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-project)

BuildRequires: junit

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-plugin-plugin
BuildRequires: maven-surefire-provider-junit4

# requires by javadoc-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-invoker)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components)

BuildArch:     noarch
Source44: import.info

%description
Converts files with characters in any
supported character encoding to
one with ASCII and/or Unicode escapes.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%pom_remove_plugin org.apache.maven.plugins:maven-invoker-plugin

%build

%mvn_file :%{name} %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.7.beta1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.5.beta1jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.2.beta1jpp7
- fixed build

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.2.beta1jpp7
- fixed build

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.2.beta1jpp7
- new version

