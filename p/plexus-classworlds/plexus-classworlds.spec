Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: maven-local
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
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

Name:           plexus-classworlds
Version:        2.6.0
Release:        alt1_12jpp11
Summary:        Plexus Classworlds Classloader Framework
License:        ASL 2.0 and Plexus
URL:            https://github.com/codehaus-plexus/plexus-classworlds
BuildArch:      noarch

Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
%endif
Source44: import.info

%description
Classworlds is a framework for container developers
who require complex manipulation of Java's ClassLoaders.
Java's native ClassLoader mechanisms and classes can cause
much headache and confusion for certain types of
application developers. Projects which involve dynamic
loading of components or otherwise represent a 'container'
can benefit from the classloading control provided by
classworlds.

%{?javadoc_package}

%prep
%setup -q -n %{name}-%{name}-%{version}
%mvn_file : %{name} plexus/classworlds
%mvn_alias : classworlds:classworlds

%pom_add_dep junit:junit:4.13.1:test

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-dependency-plugin

# These tests depend on artifacts that are not packaged
sed -i /testConfigure_Valid/s/./@org.junit.Ignore/ $(find -name ConfiguratorTest.java)
sed -i /testConfigure_Optionally_Existent/s/./@org.junit.Ignore/ $(find -name ConfiguratorTest.java)

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt LICENSE-2.0.txt

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:2.6.0-alt1_12jpp11
- update

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 0:2.6.0-alt1_8jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt1_2jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.5.2-alt2_11jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.5.2-alt2_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.5.2-alt2_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.5.2-alt2_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.5.2-alt2_5jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.5.2-alt2_4jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.5.2-alt2_3jpp8
- added osgi provides

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.5.2-alt1_3jpp8
- new version

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.5.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4.2-alt1_4jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_7jpp7
- new release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_3jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

