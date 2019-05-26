Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.1.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             log4j-jboss-logmanager
Version:          1.1.2
Release:          alt1_7jpp8
Summary:          JBoss Log4j Emulation
License:          ASL 2.0
Url:              https://github.com/jboss-logging/log4j-jboss-logmanager
Source0:          https://github.com/jboss-logging/log4j-jboss-logmanager/archive/%{namedversion}.tar.gz

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(log4j:log4j:12)
BuildRequires:    mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires:    mvn(org.jboss.modules:jboss-modules)

Provides:         bundled(log4j12) = 1.2.17-15

BuildArch:        noarch
Source44: import.info

%description
This package contains the JBoss Log4J Emulation.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n log4j-jboss-logmanager-%{namedversion}

cp -p src/main/resources/META-INF/LICENSE .
cp -p src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

sed -i 's/createSourcesJar>true/createSourcesJar>false/' pom.xml

%pom_change_dep :log4j ::12

%build

# Tests run: 36, Failures: 0, Errors: 0, Skipped: 7
# Test suite disable cause:
# The forked VM terminated without properly saying goodbye. VM crash or System.exit called?
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_7jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_2jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_3jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_2jpp8
- unbootsrap build

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

