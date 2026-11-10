%define _unpackaged_files_terminate_build 1

Name: felix-osgi-obr
Version: 1.0.2
Epoch: 1
Release: alt3

Summary: OSGi Bundle Repository (OBR) Service API
License: Apache-2.0
Group: Development/Java
URL: https://felix.apache.org/
VCS: https://svn.apache.org/repos/asf/felix/releases/org.osgi.service.obr-1.0.2

ExcludeArch: %ix86

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-java
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: osgi-core
BuildRequires: maven-plugin-bundle
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)

%description
Legacy OSGi Bundle Repository Service API used by Apache Felix OBR.
Provides the org.osgi.service.obr interfaces as an OSGi bundle and
publishes the original Apache Felix Maven coordinates.

%package javadoc
Summary: API documentation for OSGi OBR Service API
Group: Development/Documentation

%description javadoc
Java API documentation for the OSGi Bundle Repository Service API.

%prep
%setup

# The obsolete org.apache.felix:felix:1.0.2 parent is not needed.
# groupId was inherited from that parent, so declare it explicitly.
%pom_remove_parent
%pom_xpath_inject pom:project '<groupId>org.apache.felix</groupId>'

# Use the system OSGi Core API without embedding it into the bundle.
%pom_change_dep org.apache.felix:org.osgi.core org.osgi:org.osgi.core:8.0.0:provided

# Use the system Maven Bundle Plugin, preserving upstream instructions.
%pom_xpath_remove 'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-bundle-plugin"]/pom:version'
%pom_xpath_set 'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-bundle-plugin"]/pom:configuration/pom:instructions/pom:Bundle-SymbolicName' '${project.artifactId}'
%pom_xpath_set 'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-bundle-plugin"]/pom:configuration/pom:instructions/pom:Export-Package' '${project.artifactId}'

%build
%mvn_build -f -- -Dmaven.compiler.release=8 -Dmaven.javadoc.source=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc
%_datadir/javadoc/%name/

%changelog
* Mon Oct 26 2026 Timofei Fedotov <sovtouch@altlinux.org> 1:1.0.2-alt3
- Back to Sisyphus.

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_24jpp8
- update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_22jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_21jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_20jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_19jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_18jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_17jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_16jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_15jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_9jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt2_6jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_6jpp7
- new release

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt1_5jpp7
- fc package
