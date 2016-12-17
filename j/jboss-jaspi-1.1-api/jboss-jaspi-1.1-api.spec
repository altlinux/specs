Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jaspi-1.1-api
%define version 1.0.0
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jaspi-1.1-api
Version:          1.0.0
Release:          alt1_1jpp8
Summary:          JBoss Java Authentication SPI for Containers 1.1 API
License:          CDDL or GPLv2 with exceptions
URL:              https://github.com/jboss/jboss-jaspi-api_spec
Source0:          https://github.com/jboss/jboss-jaspi-api_spec/archive/jboss-jaspi-api_1.1_spec-%{namedversion}.tar.gz

BuildRequires:    maven-local
BuildRequires:    mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)

BuildArch:	  noarch
Source44: import.info

%description
The Java Authentication SPI for Containers 1.1 API classes

%package javadoc
Group: Development/Java
Summary:	Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jaspi-api_spec-jboss-jaspi-api_1.1_spec-%{namedversion}

# Unneeded plugin
%pom_remove_plugin :maven-source-plugin

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc README
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_1jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.4.Beta1jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.3.Beta1jpp8
- java 8 mass update

