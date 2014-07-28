# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
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
Release:       alt3_0.5.beta1jpp7
Summary:       Native2Ascii Maven Plugin
Group:         Development/Java
License:       MIT
URL:           http://mojo.codehaus.org/%{name}/
Source0:       http://repo2.maven.org/maven2/org/codehaus/mojo/%{name}/%{namedversion}/%{name}-%{namedversion}-source-release.zip
BuildRequires: jpackage-utils
BuildRequires: mojo-parent

BuildRequires: junit
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-invoker-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

BuildRequires: maven-project

# requires by javadoc-plugin
BuildRequires: mvn(org.apache.maven.shared:maven-invoker)
BuildRequires: mvn(org.apache.maven.shared:maven-shared-components)

Requires:      maven
Requires:      maven-project
Requires:      mojo-parent

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Converts files with characters in any
supported character encoding to
one with ASCII and/or Unicode escapes.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%pom_remove_plugin org.apache.maven.plugins:maven-invoker-plugin

%build

mvn-rpmbuild install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{namedversion}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.5.beta1jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3_0.2.beta1jpp7
- fixed build

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_0.2.beta1jpp7
- fixed build

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_0.2.beta1jpp7
- new version

