Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global     addver M0
%global     toolchain_id org.eclipse.jetty.toolchain

Name:       jetty-schemas
Version:    3.1
Release:    alt1_7jpp8
Summary:    XML Schemas for Jetty
License:    CDDL or GPLv2 with exceptions
URL:        http://www.eclipse.org/jetty/
BuildArch:  noarch

Source0:    http://git.eclipse.org/c/jetty/%{toolchain_id}.git/snapshot/%{toolchain_id}-%{name}-%{version}.%{addver}.tar.bz2
Source1:    https://glassfish.dev.java.net/public/CDDL+GPL_1_1.html

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-toolchain:pom:)
Source44: import.info

%description
%{summary}.

%prep
%setup -q -n %{toolchain_id}-%{name}-%{version}.%{addver}
cp %SOURCE1 .

# Disable default-jar execution of maven-jar-plugin, which avoids
# problems with version 3.0.0 of the plugin.
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" "
      <execution>
        <id>default-jar</id>
        <phase>skip</phase>
      </execution>" jetty-schemas

%build
pushd %{name}
%mvn_build

%install
pushd %{name}
%mvn_install

%files -f %{name}/.mfiles
%dir %{_javadir}/%{name}
%doc CDDL+GPL_1_1.html

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_7jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_5jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_4jpp8
- java 8 mass update

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

