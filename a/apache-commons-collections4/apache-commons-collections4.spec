%define _unpackaged_files_terminate_build 1

Name: apache-commons-collections4
Version: 4.6.0
Release: alt1

Summary: Extensions to the Java Collections Framework
License: Apache-2.0
Group: Development/Java
URL: https://commons.apache.org/proper/commons-collections/
VCS: https://github.com/apache/commons-collections.git

Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.junit-pioneer:junit-pioneer)
BuildRequires: mvn(org.mockito:mockito-junit-jupiter)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: mvn(org.openjdk.jmh:jmh-core)

%description
Apache Commons Collections provides new interfaces, implementations and
utilities that extend and augment the Java Collections Framework.

%package javadoc
Summary: API documentation for %{name}
Group: Development/Java

%description javadoc
API documentation for Apache Commons Collections.

%prep
%setup -q
%pom_xpath_set pom:parent/pom:version 107
%pom_add_plugin org.codehaus.mojo:build-helper-maven-plugin:3.6.1
%mvn_file org.apache.commons:commons-collections4 commons-collections4
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-scm-publish-plugin
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :japicmp-maven-plugin
%pom_remove_plugin :exec-maven-plugin

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-commons-collections4
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 4.6.0-alt1
- New version.

* Sun Jun 12 2022 Igor Vlasenko <viy@altlinux.org> 4.4-alt1_6jpp11
- java11 build

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 4.4-alt1_1jpp8
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_5jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_3jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_2jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_1jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_7jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_6jpp8
- new version

