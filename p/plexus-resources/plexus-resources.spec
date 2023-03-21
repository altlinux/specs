Epoch: 0
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

Name:           plexus-resources
Version:        1.2.0
Release:        alt1_2jpp11
Summary:        Plexus Resource Manager
License:        MIT
URL:            https://github.com/codehaus-plexus/plexus-resources
BuildArch:      noarch

Source0:        https://github.com/codehaus-plexus/plexus-resources/archive/plexus-resources-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%endif
Source44: import.info
Source45: plexus-resources-1.0-components.xml

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
API documentation for %{name}.

%prep
%setup -q -n plexus-resources-plexus-resources-%{version}

mkdir -p target/classes/META-INF/plexus
cp -p %{SOURCE45} target/classes/META-INF/plexus/components.xml


%build
%mvn_file  : plexus/resources
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:1.2.0-alt1_2jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:1.1.0-alt1_7jpp11
- update

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0:1.1.0-alt1_4jpp11
- fixed build

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0:1.1.0-alt1_2jpp11
- new version

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.26.a7jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.25.a7jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.23.a7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.22.a7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.21.a7jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.20.a7jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt7_0.19.a7jpp8
- new version

* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt6jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.14.a7jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.13.a7jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.9.a7jpp7
- rebuild with maven-local

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.9.a7jpp7
- new fc release

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.8.a7jpp7
- fixed plexus component generation

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.8.a7jpp7
- fc version

* Sun Feb 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.1.a4.4jpp6
- new version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.1.a4.4jpp6
- rebuild w/new maven2; disabled tests

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a4.2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a4.1jpp5
- converted from JPackage by jppimport script

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a3.1jpp1.7
- converted from JPackage by jppimport script

