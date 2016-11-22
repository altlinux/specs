Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global spec_ver 1.0
%global spec_name geronimo-validation_%{spec_ver}_spec

Name:           geronimo-validation
Version:        1.1
Release:        alt2_15jpp8
Summary:        Geronimo implementation of JSR 303
License:        ASL 2.0
# should be http://geronimo.apache.org/
URL:            http://apache.org/
# svn export https://svn.apache.org/repos/asf/geronimo/specs/tags/geronimo-validation_1.0_spec-1.1/
# tar caf geronimo-validation_1.0_spec-1.1.tar.xz geronimo-validation_1.0_spec-1.1
Source0:        %{spec_name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  geronimo-parent-poms
BuildRequires:  geronimo-osgi-support
Source44: import.info

%description
This is the Geronimo implementation of JSR-303, the Bean
Validation API specification.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{spec_name}-%{version}
%pom_xpath_set "pom:project/pom:parent/pom:groupId" org.apache.geronimo.specs
%pom_xpath_set "pom:project/pom:parent/pom:artifactId" specs
%pom_xpath_set "pom:project/pom:parent/pom:version" 1.4
%pom_xpath_inject "pom:project/pom:parent" "<relativePath>../pom.xml</relativePath>"
%pom_xpath_set "pom:project/pom:packaging" jar

%mvn_file : %{name}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_13jpp8
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5jpp7
- new version

