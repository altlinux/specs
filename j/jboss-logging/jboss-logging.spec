%define _unpackaged_files_terminate_build 1

Name: jboss-logging
Version: 3.6.3
Release: alt1

Summary: The JBoss Logging Framework
License: Apache-2.0
Group: Development/Java
Url: http://community.jboss.org
Vcs: https://github.com/jboss-logging/jboss-logging.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: jpackage-17-compat
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: jboss-parent
BuildRequires: slf4j
BuildRequires: dmlloyd-module-info
BuildRequires: log4j
BuildRequires: logback-classic
BuildRequires: jboss-logmanager

%description
This package contains the JBoss Logging Framework.

%prep
%setup

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :formatter-maven-plugin
%pom_remove_plugin :impsort-maven-plugin
# Log4j in sisyphus is Log4j 2.x with 1.x compat bridge, not real Log4j 1.x.
# Log4jProviderTestCase and Log4jClassPathTestCase rely on Log4j 1.x-specific
# behavior (AppenderSkeleton event levels, NDC stacking, provider auto-detection)
# that the bridge does not replicate correctly.
%pom_xpath_inject \
  "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:executions/pom:execution[pom:id='default']/pom:configuration/pom:excludes" \
  "<exclude>**/Log4jProviderTestCase.java</exclude>"
%pom_xpath_remove \
  "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:executions/pom:execution[pom:id='log4j-cp-test']"

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%changelog
* Fri Mar 27 2026 Ivan Khanas <xeno@altlinux.org> 3.6.3-alt1
- New version.

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 3.4.1-alt1_9jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 3.4.1-alt1_6jpp11
- fc34 update

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 3.4.1-alt1_2jpp11
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_5jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_3jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.3.0-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt1_6jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.4-alt1_4jpp8
- java 8 mass update

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.2-alt1_1jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt3_4jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt1_4jpp7
- new version

