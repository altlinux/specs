Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jboss-jms-2.0-api
%define version 1.0.0
%global namedreltag .Alpha1
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jms-2.0-api
Version:          1.0.0
Release:          alt1_0.5.Alpha1jpp8
Summary:          JBoss JMS API 2.0 Spec
License:          CDDL or GPLv2 with exceptions
Url:              http://www.jboss.org
Source0:          https://github.com/jboss/jboss-jms-api_spec/archive/jboss-jms-api_2.0_spec-%{namedversion}.tar.gz
Source1:          cddl.txt

BuildRequires:    jboss-parent
BuildRequires:    felix-osgi-foundation
BuildRequires:    felix-parent
BuildRequires:    maven-local

BuildArch:        noarch
Source44: import.info

%description
The Java Messaging Service 2.0 API classes

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jms-api_spec-jboss-jms-api_2.0_spec-%{namedversion}

cp %{SOURCE1} .

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE README cddl.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE README cddl.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.5.Alpha1jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_0.4.Alpha1jpp8
- new version

