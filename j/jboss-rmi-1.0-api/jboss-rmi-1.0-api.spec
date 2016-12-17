Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-rmi-1.0-api
%define version 1.0.4
%define namedreltag .Final
%define namedversion %{version}%{?namedreltag}

Name:          jboss-rmi-1.0-api
Version:       1.0.4
Release:       alt3_15jpp8
Summary:       Java Remote Method Invocation 1.0 API
License:       GPLv2 with exceptions
URL:           http://www.jboss.org

# git clone https://github.com/jboss/jboss-rmi-api_spec
# cd jboss-rmi-api_spec/ && git archive --format=tar --prefix=jboss-rmi-1.0-api-1.0.4.Final/ jboss-rmi-api_1.0_spec-1.0.4.Final | xz > jboss-rmi-1.0-api-1.0.4.Final.tar.xz
Source0:       %{name}-%{namedversion}.tar.xz

# Fix the address of the FSF in the license file:
Patch0:        %{name}-fix-fsf-address.patch

BuildRequires: maven-local
BuildRequires: mvn(jacorb:jacorb) >= 2.3.1
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
Java Remote Method Invocation 1.0 API classes.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc	
This package contains the API documentation for %{name}.

%prep

# Unpack the sources:
%setup -q -n %{name}-%{namedversion}

# Apply the patches:
%patch0 -p1

# Force as Requires dep
%pom_xpath_remove "pom:dependency[pom:groupId = 'jacorb']/pom:scope"

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc src/main/resources/LICENSE

%files javadoc -f .mfiles-javadoc
%doc src/main/resources/LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_15jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_14jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_13jpp8
- java8 mass update

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_7jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_5jpp7
- new fc release

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3jpp7
- new version

