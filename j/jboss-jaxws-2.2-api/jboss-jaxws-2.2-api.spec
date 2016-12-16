Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jaxws-2.2-api
%define version 2.0.3
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jaxws-2.2-api
Version:          2.0.3
Release:          alt1_1jpp8
Summary:          Java API for XML-Based Web Services 2.2
License:          CDDL or GPLv2 with exceptions
URL:              http://www.jboss.org/

# git clone git://github.com/jboss/jboss-jaxws-api_spec.git jboss-jaxws-api
# cd jboss-jaxws-api && git archive --format=tar --prefix=jboss-jaxws-2.2-api/ d6937fd2ebf76bfa8ea4706d6b50a172dbda9f9e | xz > jboss-jaxws-2.2-api-2.0.2.20120507gitd6937f.tar.xz
Source0:          https://github.com/jboss/jboss-jaxws-api_spec/archive/jboss-jaxws-api_2.2_spec-%{namedversion}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
Source44: import.info

%description
Java API for XML-Based Web Services 2.2 classes.

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jaxws-api_spec-jboss-jaxws-api_2.2_spec-%{namedversion}

# Unneeded plugin
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc src/main/resources/LICENSE.txt
%doc src/main/resources/NOTE.txt

%files javadoc -f .mfiles-javadoc
%doc src/main/resources/LICENSE.txt
%doc src/main/resources/NOTE.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.3-alt1_1jpp8
- new version

* Sun Feb 14 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_0.11.20120507gitd6937fjpp8
- updated gradle support

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_0.8.20120507gitd6937fjpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_0.5.20120507gitd6937fjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_0.4.20120507gitd6937fjpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt2_0.2.20120507gitd6937fjpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_0.2.20120507gitd6937fjpp7
- new release

