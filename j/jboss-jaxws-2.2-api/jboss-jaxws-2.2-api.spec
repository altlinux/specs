# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jaxws-2.2-api
%define version 2.0.2
%global namedreltag .20120507gitd6937f
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jaxws-2.2-api
Version:          2.0.2
Release:          alt2_0.8.20120507gitd6937fjpp8
Summary:          Java API for XML-Based Web Services 2.2
Group:            Development/Java
License:          CDDL or GPLv2 with exceptions
URL:              http://www.jboss.org/

# git clone git://github.com/jboss/jboss-jaxws-api_spec.git jboss-jaxws-api
# cd jboss-jaxws-api && git archive --format=tar --prefix=jboss-jaxws-2.2-api/ d6937fd2ebf76bfa8ea4706d6b50a172dbda9f9e | xz > jboss-jaxws-2.2-api-2.0.2.20120507gitd6937f.tar.xz

Source0:          %{name}-%{namedversion}.tar.xz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-source-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    jboss-specs-parent
Source44: import.info

%description
Java API for XML-Based Web Services 2.2 classes.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%doc src/main/resources/LICENSE.txt
%doc src/main/resources/NOTE.txt

%files javadoc -f .mfiles-javadoc
%doc src/main/resources/LICENSE.txt
%doc src/main/resources/NOTE.txt

%changelog
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

