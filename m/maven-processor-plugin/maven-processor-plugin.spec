Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          maven-processor-plugin
Version:       2.2.4
Release:       alt1_6jpp8
Summary:       Maven Processor Plugin
License:       LGPLv3+
Url:           https://github.com/bsorrentino/maven-annotation-plugin
Source0:       https://github.com/bsorrentino/maven-annotation-plugin/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
# main deps
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
# test deps
BuildRequires: mvn(junit:junit)

BuildArch:     noarch
Source44: import.info

%description
A maven plugin to process annotation for jdk6 at compile time

This plugin helps to use from maven the new annotation processing
provided by JDK6 integrated in java compiler

This plugin could be considered the 'alter ego' of maven apt plugin.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n maven-annotation-plugin-%{name}-%{version}
%pom_xpath_remove pom:project/pom:profiles
%pom_xpath_remove pom:build/pom:extensions

cp -p src/main/resources/COPYING.LESSER .

%mvn_file :%{name} %{name}/%{name} %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc COPYING.LESSER

%files javadoc -f .mfiles-javadoc
%doc COPYING.LESSER

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1_6jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1_5jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_4jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_1jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_3jpp7
- new version

