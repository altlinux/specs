%define _unpackaged_files_terminate_build 1

Name: felix-configadmin
Version: 1.9.26
Release: alt1

Summary: Apache Felix OSGi Configuration Admin service
License: Apache-2.0
Group: Development/Java
Url: https://felix.apache.org/
VCS: https://github.com/apache/felix-dev.git

ExcludeArch: %ix86

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: javapackages-local
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: /proc

BuildRequires: felix-parent
BuildRequires: maven-plugin-bundle

BuildRequires: osgi-core
BuildRequires: osgi-compendium
BuildRequires: osgi-annotation
BuildRequires: mvn(org.osgi:org.osgi.core)
BuildRequires: mvn(org.osgi:osgi.cmpn)
BuildRequires: mvn(org.osgi:osgi.annotation)

BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)

%description
Apache Felix Configuration Admin implements the OSGi Configuration Admin
Service specification. This package provides its OSGi bundle and Maven metadata.

%package javadoc
Summary: API documentation for Apache Felix Configuration Admin
Group: Development/Documentation
BuildArch: noarch

%description javadoc
Java API documentation for Apache Felix Configuration Admin.

%prep
%setup
rm -f src/main/java/org/apache/felix/cm/impl/ConfigurationBase.java

%pom_remove_dep org.osgi:org.osgi.service.cm
%pom_remove_dep org.osgi:org.osgi.service.log
%pom_remove_dep org.osgi:org.osgi.service.coordinator
%pom_xpath_remove 'pom:project/pom:dependencies/pom:dependency[pom:scope="test"]'
%pom_add_dep org.osgi:osgi.cmpn:7.0.0:provided

%pom_xpath_remove 'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-bundle-plugin"]/pom:executions/pom:execution[pom:id="baseline"]'

%build
%mvn_build -f -- -Dmaven.test.skip=true -DskipTests \
    -Drat.skip=true -Dcheckstyle.skip=true -Dgpg.skip=true \
    -Dfelix.java.version=8 -Dmaven.compiler.release=8 \
    -Dmaven.compiler.source=8 -Dmaven.compiler.target=8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Thu Oct 22 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.9.26-alt1
- new version

* Sun Jul 14 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.14-alt2_5jpp8
- build with compedium6

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.14-alt1_5jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.14-alt1_4jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.8.14-alt1_3jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.14-alt1_2jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.14-alt1_1jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_15jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_14jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_3jpp7
- new release
