Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           cal10n
Version:        0.8.1
Release:        alt1_2jpp8
Summary:        Compiler assisted localization library (CAL10N)
License:        MIT
URL:            http://cal10n.qos.ch
Source0:        https://github.com/qos-ch/%{name}/archive/v_%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
Source44: import.info

%description
Compiler Assisted Localization, abbreviated as CAL10N (pronounced as "calion")
is a java library for writing localized (internationalized) messages.
Features:
    * java compiler verifies message keys used in source code
    * tooling to detect errors in message keys
    * native2ascii tool made superfluous, as you can directly encode bundles
      in the most convenient charset, per locale.
    * good performance (300 nanoseconds per key look-up)
    * automatic reloading of resource bundles upon change


%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%package -n maven-%{name}-plugin
Group: Development/Java
Summary:        CAL10N maven plugin

%description -n maven-%{name}-plugin
Maven plugin verifying that the codes defined in
an enum type match those in the corresponding resource bundles. 

%prep
%setup -q -n %{name}-v_%{version}

find . -name \*.jar -delete

%pom_xpath_remove pom:extensions
%pom_add_dep org.apache.maven:maven-artifact maven-%{name}-plugin
%pom_disable_module %{name}-site
%pom_disable_module maven-%{name}-plugin-smoke
%mvn_package :*-{plugin} @1

# Disable default-jar execution of maven-jar-plugin, which is causing
# problems with version 3.0.0 of the plugin.
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" "
    <execution>
      <id>default-jar</id>
      <phase>skip</phase>
    </execution>" cal10n-api

%build
%mvn_build -- -Dproject.build.sourceEncoding=ISO-8859-1

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE.txt

%files -n maven-%{name}-plugin -f .mfiles-plugin

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.8.1-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.7.7-alt1_7jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.7.7-alt1_6jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7.7-alt1_3jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7.7-alt1_1jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7.4-alt4_9jpp7
- fixed build

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:0.7.4-alt3_9jpp7
- fc update

* Wed Aug 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7.4-alt3_5jpp6
- applied repocop patches

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7.4-alt2_5jpp6
- fixed build with java 7

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.7.4-alt1_5jpp6
- fixed build

