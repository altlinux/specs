Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           plexus-languages
Version:        1.1.1
Release:        alt1_2jpp11
Summary:        Plexus Languages
License:        ASL 2.0
URL:            https://github.com/codehaus-plexus/plexus-languages
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
# Sources contain bundled jars that we cannot verify for licensing
Source2:        generate-tarball.sh

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
%endif
Source44: import.info

%description
Plexus Languages is a set of Plexus components that maintain shared
language features.

%{?javadoc_package}

%prep
%setup -q -n plexus-languages-plexus-languages-%{version}

cp %{SOURCE1} .

%pom_remove_plugin :maven-enforcer-plugin

# Remove module build specific to Java 9
%pom_xpath_remove 'pom:profiles' plexus-java

%build
# many tests rely on bundled test jars/classes
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE-2.0.txt

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1.1.1-alt1_2jpp11
- new version

* Thu May 26 2022 Igor Vlasenko <viy@altlinux.org> 1.0.6-alt1_6jpp11
- fc update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.0.6-alt1_1jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 1.0.5-alt1_6jpp11
- new version

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 1.0.3-alt1_2jpp11
- new version

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_5jpp8
- fc update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_4jpp8
- new version

* Tue Jun 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt2_4jpp8
- fixed build with new objectweb-asm

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_4jpp8
- fc 28 update

