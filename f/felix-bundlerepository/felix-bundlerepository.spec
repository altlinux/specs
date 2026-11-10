%define _unpackaged_files_terminate_build 1

Name: felix-bundlerepository
Version: 2.0.10
Release: alt3

Summary: Apache Felix OSGi Bundle Repository service
License: Apache-2.0 AND MIT
Group: Development/Java
Url: https://felix.apache.org/
VCS: https://github.com/apache/felix-dev.git

ExcludeArch: %ix86

Source0: %name-%version.tar
Patch0: felix-bundlerepository-osgi-repository-1.1-compat.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-plugin-bundle
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)

%define felix_utils_mvn_ver 1.10.2
%define felix_gogo_mvn_ver 1.1.6
%define woodstox_mvn_ver 7.1.1

BuildRequires: felix-utils
BuildRequires: felix-osgi-obr
BuildRequires: felix-shell
BuildRequires: felix-gogo-runtime
BuildRequires: kxml2
BuildRequires: osgi-core
BuildRequires: osgi-compendium
BuildRequires: woodstox-core
BuildRequires: xmlpull

%description
Apache Felix Bundle Repository implements OSGi Repository and legacy OBR
services for discovery and installation of OSGi bundles.

The package provides the OSGi bundle and Maven metadata.

%prep
%setup
%autopatch -p1

test -f pom.xml
test -d src/main/java
test -f LICENSE
test -f NOTICE

%pom_add_dep xmlpull:xmlpull:1.2.0

%pom_remove_parent
%pom_xpath_inject pom:project '<groupId>org.apache.felix</groupId>'

%pom_xpath_inject \
    'pom:project/pom:dependencies/pom:dependency[pom:groupId="org.easymock" and pom:artifactId="easymock"]' \
    '<scope>test</scope>'

%pom_xpath_inject 'pom:project/pom:dependencies' '
  <dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.13.2</version>
    <scope>test</scope>
  </dependency>'

%pom_change_dep :org.apache.felix.utils org.apache.felix:org.apache.felix.utils:%felix_utils_mvn_ver
%pom_change_dep :org.osgi.service.obr org.apache.felix:org.osgi.service.obr:1.0.2
%pom_change_dep :org.apache.felix.shell org.apache.felix:org.apache.felix.shell:1.4.1
%pom_change_dep :org.apache.felix.gogo.runtime org.apache.felix:org.apache.felix.gogo.runtime:%felix_gogo_mvn_ver
%pom_change_dep :kxml2 net.sf.kxml:kxml2:2.5.0
%pom_change_dep :org.osgi.compendium org.osgi:osgi.cmpn:7.0.0
%pom_change_dep :org.osgi.core org.osgi:org.osgi.core:8.0.0
%pom_change_dep :woodstox-core-asl com.fasterxml.woodstox:woodstox-core:%woodstox_mvn_ver

%pom_xpath_remove 'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-bundle-plugin"]/pom:version'
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-source-plugin
%pom_xpath_set 'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration/pom:source' 8
%pom_xpath_set 'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration/pom:target' 8
%pom_xpath_inject 'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]' '<version>3.14.0</version>'

%build
export JAVA_HOME=%_jvmdir/java-21-openjdk
export PATH="$JAVA_HOME/bin:$PATH"

%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE LICENSE.kxml2 DEPENDENCIES

%changelog
* Mon Oct 26 2026 Timofei Fedotov <sovtouch@altlinux.org> 2.0.10-alt3
- Back to sisyphus.

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 2.0.10-alt2_11jpp11
- fixed build

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.0.10-alt1_11jpp11
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_7jpp8
- update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_5jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_4jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.10-alt1_2jpp8
- new version

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.8-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt4_20jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt4_19jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt4_18jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt2_15jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt1_7jpp7
- new release
