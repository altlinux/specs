Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jandex
%define version 2.0.2
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jandex
Version:          2.0.2
Release:          alt1_1jpp8
Summary:          Java Annotation Indexer
License:          ASL 2.0
URL:              https://github.com/wildfly/jandex
Source0:          https://github.com/wildfly/jandex/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(jdepend:jdepend)
BuildRequires:    mvn(org.apache.ant:ant)
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.apiviz:apiviz)
Source44: import.info


%description
This package contains Java Annotation Indexer

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# org.jboss.jandex:typeannotation-test:1.0
%pom_remove_dep :typeannotation-test
rm src/test/java/org/jboss/jandex/test/TypeAnnotationTestCase.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_5jpp7
- new version

