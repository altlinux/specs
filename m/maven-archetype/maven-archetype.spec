Name:           maven-archetype
Version:        3.3.0
Release:        alt1

Summary:        Apache Maven Archetype (Plugin)
Group:          Development/Java
License:        Apache-2.0
URL:            https://maven.apache.org/archetype/
VCS:            https://github.com/apache/maven-archetype

Source0:        %name-%version.tar

Patch0:         0001-avoid-reliance-on-groovy.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.jdom:jdom2)
BuildRequires:  mvn(org.apache.maven.shared:maven-invoker)
BuildRequires:  apache-commons-collections
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
BuildRequires:  mvn(org.xmlunit:xmlunit-matchers)
BuildRequires:  mvn(com.ibm.icu:icu4j)
BuildRequires:  mvn(org.apache.maven.shared:maven-script-interpreter)

BuildArch:      noarch

%description
Archetype is a Maven project templating toolkit. An archetype is
defined as an original pattern or model from which all other things of
the same kind are made. The names fits as we are trying to provide a
system that provides a consistent means of generating Maven
projects. Archetype will help authors create Maven project templates
for users, and provides users with the means to generate parameterized
versions of those project templates.

Using archetypes provides a great way to enable developers quickly in
a way consistent with best practices employed by your project or
organization. Within the Maven project we use archetypes to try and
get our users up and running as quickly as possible by providing a
sample project that demonstrates many of the features of Maven while
introducing new users to the best practices employed by Maven. In a
matter of seconds a new user can have a working Maven project to use
as a jumping board for investigating more of the features in Maven. We
have also tried to make the Archetype mechanism additive and by that
we mean allowing portions of a project to be captured in an archetype
so that pieces or aspects of a project can be added to existing
projects. A good example of this is the Maven site archetype. If, for
example, you have used the quick start archetype to generate a working
project you can then quickly create a site for that project by using
the site archetype within that existing project. You can do anything
like this with archetypes.

You may want to standardize J2EE development within your organization
so you may want to provide archetypes for EJBs, or WARs, or for your
web services. Once these archetypes are created and deployed in your
organization's repository they are available for use by all developers
within your organization.

%javadoc_package

%package catalog
Group:          Development/Java
Summary:        Maven Archetype Catalog model

%description catalog
%summary.

%package common
Group:          Development/Java
Summary:        Maven Archetype common classes

%description common
%summary.

%package descriptor
Group:          Development/Java
Summary:        Maven Archetype Descriptor model

%description descriptor
%summary.

%package packaging
Group:          Development/Java
Summary:        Maven Archetype packaging configuration for archetypes

%description packaging
%summary.

%prep
%setup
%autopatch -p1

%pom_remove_dep :groovy archetype-common
%pom_remove_dep org.apache.ivy:ivy archetype-common

%pom_remove_plugin :apache-rat-plugin

%pom_disable_module maven-archetype-plugin

%mvn_package :archetype-models maven-archetype

%build
# tests are disabled cause there are some problems with them
%mvn_build -f -s

%install
%mvn_install

%files -f .mfiles-maven-archetype
%doc NOTICE.txt README.md

%files catalog -f .mfiles-archetype-catalog

%files common -f .mfiles-archetype-common
%doc NOTICE.txt README.md

%files descriptor -f .mfiles-archetype-descriptor

%files packaging -f .mfiles-archetype-packaging

%changelog
* Mon Apr 06 2026 Evgeniy Serov <scala@altlinux.org> 3.3.0-alt1
- Updated to 3.3.0.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:3.2.0-alt1_4jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:3.2.0-alt1_1jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0:3.1.2-alt1_3jpp11
- fixed build

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_10jpp8
- fc update & java 8 build

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_3jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt1_2jpp8
- new version

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_3jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_1jpp7
- new release

* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt5_7jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt4_7jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt3_7jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_7jpp7
- fixed build

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_7jpp7
- new version

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

