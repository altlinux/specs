%define _unpackaged_files_terminate_build 1

Name: felix-shell
Version: 1.4.3
Release: alt3

Summary: Apache Felix OSGi Shell Service
License: Apache-2.0
Group: Development/Java
URL: https://felix.apache.org/
VCS: https://svn.apache.org/repos/asf/felix/releases/org.apache.felix.shell-1.4.1/

ExcludeArch: %ix86

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: osgi-core
BuildRequires: osgi-compendium
BuildRequires: maven-plugin-bundle
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)

%description
Apache Felix Shell Service provides a classic command shell for OSGi
frameworks, including commands for managing bundles and services.
The package includes the OSGi bundle and its Maven metadata.

%package javadoc
Summary: API documentation for Apache Felix Shell
Group: Development/Documentation

%description javadoc
Java API documentation for Apache Felix Shell Service.

%prep
%setup

# Build the original upstream POM without its obsolete parent.
%pom_remove_parent
%pom_xpath_inject pom:project '<groupId>org.apache.felix</groupId>'

# Use OSGi APIs packaged in Sisyphus.
%pom_change_dep org.osgi:org.osgi.core org.osgi:org.osgi.core:8.0.0
%pom_change_dep org.osgi:org.osgi.compendium org.osgi:osgi.cmpn:7.0.0

%build
%mvn_build -f -- -Dmaven.compiler.release=8 -Dmaven.javadoc.source=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc
%_datadir/javadoc/%name/

%changelog
* Fri Oct 23 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.4.3-alt3
- fixed build

* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.org> 1.4.3-alt2_15jpp8
- fixed build

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_15jpp8
- update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_13jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_12jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_11jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_10jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_8jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_7jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_4jpp7
- new release

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.3-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt3_7jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt2_7jpp7
- new release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt2_3jpp6
- fixed build with maven3

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1_3jpp6
- new jpp release

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies
