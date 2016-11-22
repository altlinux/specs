Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-sasl
%define version 1.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-sasl
Version:          1.0.0
Release:          alt2_13jpp8
Summary:          SASL Provider for J2SE
License:          LGPLv2+
URL:              https://github.com/jboss-remoting/jboss-sasl

# git clone git://github.com/jboss-remoting/jboss-sasl.git
# cd jboss-sasl/ && git archive --format=tar --prefix=jboss-sasl-1.0.0.Final/ 1.0.0.Final | xz > jboss-sasl-1.0.0.Final.tar.xz
Source0:          %{name}-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)
BuildRequires:    mvn(org.jboss.logging:jboss-logging-processor)
BuildRequires:    mvn(org.jboss.maven.plugins:maven-injection-plugin)
Source44: import.info

%description
This package contains SASL Provider for J2SE

%package javadoc
Group: Development/Java
Summary:          Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_13jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_12jpp8
- java8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp7
- new version

