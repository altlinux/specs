Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-interceptors-1.2-api
%define version 1.0.0
%global namedreltag .Alpha3
%global namedversion %{version}%{?namedreltag}
%global oname jboss-interceptors-api_1.2_spec
Name:          jboss-interceptors-1.2-api
Version:       1.0.0
Release:       alt1_0.3.Alpha3jpp7
Summary:       Java EE Interceptors 1.2 API
License:       CDDL or GPLv2 with exceptions
URL:           https://github.com/jboss/jboss-interceptors-api_spec
Source0:       https://github.com/jboss/jboss-interceptors-api_spec/archive/%{namedversion}.tar.gz

BuildRequires: jboss-parent

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-source-plugin

BuildArch:     noarch
Source44: import.info

%description
The Java EE  Interceptors 1.2 API classes from JSR 318.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jboss-interceptors-api_spec-%{namedversion}

%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-bundle-plugin']" \
 "<version>any</version>"

# Fix incorrect-fsf-address
sed -i "s,59,51,;s,Temple Place,Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%build

%mvn_file :%{oname} %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.3.Alpha3jpp7
- new release

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.1.Alpha3jpp7
- new version

