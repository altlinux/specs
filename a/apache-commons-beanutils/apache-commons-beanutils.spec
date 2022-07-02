Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
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

Name:           apache-commons-beanutils
Version:        1.9.4
Release:        alt1_10jpp11
Summary:        Java utility methods for accessing and modifying the properties of arbitrary JavaBeans
License:        ASL 2.0
URL:            http://commons.apache.org/beanutils
BuildArch:      noarch
Source0:        http://archive.apache.org/dist/commons/beanutils/source/commons-beanutils-%{version}-src.tar.gz

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
%endif
Source44: import.info

%description
The scope of this package is to create a package of Java utility methods
for accessing and modifying the properties of arbitrary JavaBeans.  No
dependencies outside of the JDK are required, so the use of this package
is very lightweight.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n commons-beanutils-%{version}-src
sed -i 's/\r//' *.txt

%pom_remove_plugin :maven-assembly-plugin

%mvn_alias :{*} :@1-core :@1-bean-collections
%mvn_alias :{*} org.apache.commons:@1 org.apache.commons:@1-core org.apache.commons:@1-bean-collections
%mvn_file : %{name} %{name}-core %{name}-bean-collections
%mvn_file : commons-beanutils commons-beanutils-core commons-beanutils-bean-collections

%build
# Some tests fail in Koji
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.compiler.source=1.7 -Dmaven.compiler.target=1.7 -Dcommons.osgi.symbolicName=org.apache.commons.beanutils

%install
%mvn_install

%files -f .mfiles
%doc RELEASE-NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 0:1.9.4-alt1_10jpp11
- update

* Mon Jul 05 2021 Igor Vlasenko <viy@altlinux.org> 0:1.9.4-alt1_6jpp11
- quick fix (closes: #40375)

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0:1.9.4-alt1_2jpp11
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt1_5jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9.3-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.2-alt5_5jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.2-alt5_4jpp8
- java 8 mass update

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.9.2-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_9jpp7
- new release

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_7jpp7
- fc update

* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt3_4jpp6
- fixed build

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt2_4jpp6
- fixed repolib

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_4jpp6
- new version

