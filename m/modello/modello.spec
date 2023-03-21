Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
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

Name:           modello
Version:        2.0.0
Release:        alt1_2jpp11
Summary:        Modello Data Model toolkit
# The majority of files are under MIT license, but some of them are ASL 2.0.
# Some parts of the project are derived from the Exolab project,
# and are licensed under a 5-clause BSD license.
License:        MIT and ASL 2.0 and BSD
URL:            https://codehaus-plexus.github.io/modello

Source0:        https://repo1.maven.org/maven2/org/codehaus/%{name}/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         0001-Remove-dependency-on-Jsoup.patch

BuildArch:      noarch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-javac)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires:  mvn(org.sonatype.sisu:sisu-guice::no_aop:)
%endif

# Explicit javapackages-tools requires since modello script uses
# /usr/share/java-utils/java-functions
Requires:         javapackages-tools
Source44: import.info

%description
Modello is a Data Model toolkit in use by the Apache Maven Project.

Modello is a framework for code generation from a simple model.
Modello generates code from a simple model format based on a plugin
architecture, various types of code and descriptors can be generated
from the single model, including Java POJOs, XML
marshallers/unmarshallers, XSD and documentation.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
cp -p %{SOURCE1} LICENSE
# We don't generate site; don't pull extra dependencies.
%pom_remove_plugin :maven-site-plugin

%pom_remove_dep :jackson-bom
%pom_disable_module modello-plugin-jackson modello-plugins
%pom_disable_module modello-plugin-jsonschema modello-plugins
%pom_remove_dep :modello-plugin-jackson modello-maven-plugin
%pom_remove_dep :modello-plugin-jsonschema modello-maven-plugin

%pom_disable_module modello-plugin-snakeyaml modello-plugins
%pom_remove_dep :modello-plugin-snakeyaml modello-maven-plugin

%build
# skip tests because we have too old xmlunit in Fedora now (1.0.8)
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%jpackage_script org.codehaus.modello.ModelloCli "" "" modello:org.eclipse.sisu.plexus:org.eclipse.sisu.inject:google-guice-no_aop:atinject:plexus-containers/plexus-component-annotations:plexus/classworlds:plexus/utils:plexus/plexus-build-api:guava:plexus-compiler/plexus-compiler-api:plexus-compiler/plexus-compiler-javac %{name} true

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files -f .mfiles
%doc LICENSE
%{_bindir}/modello
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 0:2.0.0-alt1_2jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:1.11-alt1_6jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.11-alt1_3jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0:1.10.0-alt1_2jpp11
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_8jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9.1-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_3jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt1_2jpp8
- new version

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_2jpp7
- new version

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_0jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt5_3jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt4_3jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_3jpp7
- new version

* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt3_1jpp6
- fixed build with new plexus-containers

* Fri Apr 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_1jpp6
- fixed build with maven3

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp6
- new jpp release

* Thu Sep 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_0.2.a15.5jpp6
- reverted to a15

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_0.a17.1jpp5
- fixes for java6 support

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_0.a17.1jpp5
- rebuild with maven

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a17.1jpp5
- new version a17

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a15.1jpp5
- fixed build w/java5

* Fri Dec 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a15.1jpp1.7
- new version

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.a8.6jpp1.7
- build with maven2

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.a8.6jpp1.7
- converted from JPackage by jppimport script

