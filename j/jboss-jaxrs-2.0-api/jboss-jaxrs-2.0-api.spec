Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jaxrs-2.0-api
%define version 1.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global oname jboss-jaxrs-api_2.0_spec

Name:          jboss-jaxrs-2.0-api
Version:       1.0.0
Release:       alt1_3jpp8
Summary:       JAX-RS 2.0: The Java API for RESTful Web Services
# ASL 2.0 src/main/java/javax/ws/rs/core/GenericEntity.java
License:       (CDDL or GPLv2 with exceptions) and ASL 2.0
URL:           https://github.com/jboss/jboss-jaxrs-api_spec
Source0:       https://github.com/jboss/jboss-jaxrs-api_spec/archive/%{oname}-%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.jboss:jboss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
JSR 339: JAX-RS 2.0: The Java API for RESTful Web Services.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jboss-jaxrs-api_spec-%{oname}-%{namedversion}

# Unneeded plugin
%pom_remove_plugin :maven-source-plugin

%mvn_file :%{oname} %{name}

# remove after upgrading narayana
%mvn_alias ":jboss-jaxrs-api_2.0_spec" "org.jboss.resteasy:jaxrs-api"

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp8
- new version

