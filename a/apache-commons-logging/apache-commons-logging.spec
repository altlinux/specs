Epoch: 0
Group: Development/Java
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

Name:           apache-commons-logging
Version:        1.2
Release:        alt1_27jpp11
Summary:        Apache Commons Logging
License:        ASL 2.0
URL:            http://commons.apache.org/logging
BuildArch:      noarch

Source0:        http://www.apache.org/dist/commons/logging/source/commons-logging-%{version}-src.tar.gz
Source2:        http://mirrors.ibiblio.org/pub/mirrors/maven2/commons-logging/commons-logging-api/1.1/commons-logging-api-1.1.pom

Patch0:         0001-Generate-different-Bundle-SymbolicName-for-different.patch
Patch1:         0002-Port-to-maven-jar-plugin-3.0.0.patch

BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif
Source44: import.info

%description
The commons-logging package provides a simple, component oriented
interface (org.apache.commons.logging.Log) together with wrappers for
logging systems. The user can choose at runtime which system they want
to use. In addition, a small number of basic implementations are
provided to allow users to use the package standalone.
commons-logging was heavily influenced by Avalon's Logkit and Log4J. The
commons-logging abstraction is meant to minimize the differences between
the two, and to allow a developer to not tie himself to a particular
logging implementation.

%{?javadoc_package}

%prep
%setup -q -n commons-logging-%{version}-src
%patch0 -p1
%patch1 -p1


%pom_remove_dep -r :avalon-framework
%pom_remove_dep -r :logkit
%pom_remove_dep -r :log4j
rm src/main/java/org/apache/commons/logging/impl/AvalonLogger.java
rm src/main/java/org/apache/commons/logging/impl/Log4JLogger.java
rm src/main/java/org/apache/commons/logging/impl/LogKitLogger.java
rm -r src/test/java/org/apache/commons/logging/{avalon,log4j,logkit}
rm src/test/java/org/apache/commons/logging/pathable/{Parent,Child}FirstTestCase.java


# Avoid hard-coded versions in OSGi metadata
%pom_xpath_set "pom:properties/pom:commons.osgi.import" '*;resolution:=optional'

%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-scm-publish-plugin

sed -i 's/\r//' RELEASE-NOTES.txt LICENSE.txt NOTICE.txt

# for compatibility reasons
%mvn_file ":commons-logging{*}" "commons-logging@1" "%{name}@1"
%mvn_alias ":commons-logging{*}" "org.apache.commons:commons-logging@1" "apache:commons-logging@1"

# Remove log4j12 tests
rm -rf src/test/java/org/apache/commons/logging/log4j/log4j12

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.compiler.source=1.6 -Dmaven.compiler.target=1.6 -Dcommons.osgi.symbolicName=org.apache.commons.logging

# The build produces more artifacts from one pom
%mvn_artifact %{SOURCE2} target/commons-logging-%{version}-api.jar
%mvn_artifact commons-logging:commons-logging-adapters:%{version} target/commons-logging-%{version}-adapters.jar

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt
%doc PROPOSAL.html RELEASE-NOTES.txt

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 0:1.2-alt1_27jpp11
- update

* Fri Jun 11 2021 Igor Vlasenko <viy@altlinux.org> 0:1.2-alt1_25jpp11
- new version

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0:1.2-alt1_23jpp11
- fixed build

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0:1.2-alt1_20jpp11
- update

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_17jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_14jpp8
- fc29 update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_13jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_11jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_5jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_2jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt8_20jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt7_20jpp7
- fixed build

* Tue Jul 15 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt6_20jpp7
- fixed build

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt5_20jpp7
- added jakarta cpmpat symlinks

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt4_20jpp7
- no not package repolib in main commons-logging

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt3_20jpp7
- new release

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt3_6jpp6
- fixed build

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_6jpp6
- synced osgi manifest

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_6jpp6
- new version

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_2jpp6
- new version

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_8jpp5
- updated OSGi manifest

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_7jpp5
- rebuild with osgi provides

* Mon May 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp1.7
- updated to new jpackage release

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_3jpp1.7
- added eclipse manifest

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_3jpp1.7
- updated to new jpackage release

* Fri Nov 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_2jpp1.7
- updated to new jpackage release

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt4
- added JPackage compatibility stuff

* Sun Aug 29 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt3
- Disabled check by default due to a circular build dependency

* Thu Jul 15 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt2
- Disabled avalon by default

* Thu Jun 17 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt1
- New upstream release
- Patch0 obsoleted

* Thu Feb 26 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.3-alt1
- Adapted for Sisyphus from the JPackage project
