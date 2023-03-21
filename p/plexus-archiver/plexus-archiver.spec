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

Name:           plexus-archiver
Version:        4.2.7
Release:        alt1_2jpp11
Summary:        Plexus Archiver Component
License:        ASL 2.0
URL:            https://codehaus-plexus.github.io/plexus-archiver
BuildArch:      noarch

Source0:        https://github.com/codehaus-plexus/plexus-archiver/archive/plexus-archiver-%{version}.tar.gz

Patch0:         0001-Remove-support-for-snappy.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-io)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.tukaani:xz)
%endif
Source44: import.info

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%mvn_file :%{name} plexus/archiver

%patch0 -p1
%pom_remove_dep org.iq80.snappy:snappy
rm -rf src/main/java/org/codehaus/plexus/archiver/snappy
rm -f src/main/java/org/codehaus/plexus/archiver/tar/SnappyTarFile.java
rm -f src/main/java/org/codehaus/plexus/archiver/tar/PlexusIoTarSnappyFileResourceCollection.java
rm src/test/java/org/codehaus/plexus/archiver/snappy/SnappyArchiverTest.java
rm src/test/java/org/codehaus/plexus/archiver/tar/TarSnappyUnArchiverTest.java

# Tests use old plexus-containers-default
sed -i '/getLoggerManager/d' src/test/java/org/codehaus/plexus/archiver/DuplicateFilesTest.java

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:4.2.7-alt1_2jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:4.2.4-alt1_3jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:4.2.4-alt1_1jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0:4.2.2-alt1_3jpp11
- new version

* Tue May 11 2021 Igor Vlasenko <viy@altlinux.org> 0:4.2.1-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:4.1.0-alt1_1jpp8
- new version

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0:3.6.0-alt1_3jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.6.0-alt1_1jpp8
- java update

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt1_5jpp8
- unbootstrap build

* Thu May 24 2018 Igor Vlasenko <viy@altlinux.ru> 0:3.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0:3.4-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt1_0.3.gitdc873a4jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt1_0.2.gitdc873a4jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4.2-alt1_3jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt1_2jpp7
- new version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_1jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

