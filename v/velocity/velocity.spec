Epoch: 1
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

Name:           velocity
Version:        1.7
Release:        alt3_36jpp11
Summary:        Java-based template engine
License:        ASL 2.0
URL:            http://velocity.apache.org/
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        http://repo1.maven.org/maven2/org/apache/%{name}/%{name}/%{version}/%{name}-%{version}.pom
# Remove bundled binaries which cannot be easily verified for licensing
Source2:        generate-tarball.sh

Patch1:         0001-Port-to-apache-commons-lang3.patch
Patch2:         0002-Force-use-of-JDK-log-chute.patch
Patch3:         0003-CVE-2020-13936.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache:apache:pom:)
%endif
Source44: import.info

%description
Velocity is a Java-based template engine. It permits anyone to use the
simple yet powerful template language to reference objects defined in
Java code.
When Velocity is used for web development, Web designers can work in
parallel with Java programmers to develop web sites according to the
Model-View-Controller (MVC) model, meaning that web page designers can
focus solely on creating a site that looks good, and programmers can
focus solely on writing top-notch code. Velocity separates Java code
from the web pages, making the web site more maintainable over the long
run and providing a viable alternative to Java Server Pages (JSPs) or
PHP.
Velocity's capabilities reach well beyond the realm of web sites; for
example, it can generate SQL and PostScript and XML (see Anakia for more
information on XML transformations) from templates. It can be used
either as a standalone utility for generating source code and reports,
or as an integrated component of other systems. Velocity also provides
template services for the Turbine web application framework.
Velocity+Turbine provides a template service that will allow web
applications to be developed according to a true MVC model.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q
cp %{SOURCE1} ./pom.xml
%patch1 -p1
%patch2 -p1
%patch3 -p1

find . -name '*.jar' ! -name 'test*.jar' -print -delete
find . -name '*.class' ! -name 'Foo.class' -print -delete

# Disable unneeded features
rm -r src/java/org/apache/velocity/{anakia,texen,servlet,convert}
rm src/java/org/apache/velocity/runtime/log/{Avalon,Log4J}Log{Chute,System}.java
rm src/java/org/apache/velocity/runtime/log/{CommonsLog,Servlet}LogChute.java
rm src/java/org/apache/velocity/runtime/log/SimpleLog4JLogSystem.java
rm src/java/org/apache/velocity/runtime/log/VelocityFormatter.java
rm src/java/org/apache/velocity/app/event/implement/Escape{Html,JavaScript,Sql,Xml,}Reference.java

%pom_remove_dep :oro
%pom_remove_dep :jdom
%pom_remove_dep :commons-logging
%pom_remove_dep :log4j
%pom_remove_dep :servlet-api
%pom_remove_dep :logkit
%pom_remove_dep :ant
%pom_remove_dep :werken-xpath

%mvn_alias : %{name}:%{name}

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc README.txt
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1:1.7-alt3_36jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:1.7-alt3_34jpp11
- fc34 update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1:1.7-alt3_32jpp11
- update

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_27jpp8
- fc update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_25jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_22jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_21jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_20jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_19jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt3_18jpp8
- unbootstrap build

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_7jpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_6jpp7
- fc update

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_5jpp7
- new version

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt3_1jpp6
- fixed build

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt2_1jpp6
- added velocity:velocity jppmap

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt1_1jpp6
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt2_4jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_4jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_3jpp5
- converted from JPackage by jppimport script

* Tue Jan 22 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_2jpp1.7
- pom fixes

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_1jpp1.7
- updated to new jpackage release

* Thu Nov 01 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt1_6jpp1.7
- import from jpackage;set epoch 1; overrides unstable version

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.3
- rebuild with excalibur-avalon-logkit

* Fri Dec 02 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt0.2
- nightly build 20051125053934 

* Sat May 07 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt0.1
- 1.5-dev
- svn snapshot 20050507

* Fri May 06 2005 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt1
- Initial build for ALT Linux Sisyphus

