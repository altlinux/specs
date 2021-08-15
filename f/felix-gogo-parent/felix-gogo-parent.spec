Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           felix-gogo-parent
Version:        6
Release:        alt1_2jpp11
Summary:        Parent pom for Apache Felix Gogo
License:        ASL 2.0
URL:            http://felix.apache.org/documentation/subprojects/apache-felix-gogo.html

Source0:        https://repo1.maven.org/maven2/org/apache/felix/gogo-parent/%{version}/gogo-parent-%{version}-source-release.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
Source44: import.info

%description
Apache Felix Gogo is a subproject of Apache Felix implementing a command
line shell for OSGi. It is used in many OSGi runtimes and servers.

%prep
%setup -q -n gogo-parent-%{version}

# Use compendium dep
%pom_xpath_remove "pom:dependency[pom:artifactId='org.osgi.namespace.service']"
%pom_xpath_remove "pom:dependency[pom:artifactId='org.osgi.service.event']"
%pom_xpath_remove "pom:dependency[pom:artifactId='org.osgi.service.log']"
%pom_xpath_remove "pom:dependency[pom:artifactId='org.apache.felix.framework']"
%pom_xpath_inject "pom:dependencies" "
<dependency>
<groupId>org.osgi</groupId>
<artifactId>osgi.cmpn</artifactId>
<version>6.0.0</version>
<scope>provided</scope>
</dependency>"

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE NOTICE

%changelog
* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 6-alt1_2jpp11
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 5-alt1_1jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 4-alt1_4jpp8
- fc update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 4-alt1_2jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 2-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt3_15jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt3_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt3_13jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Tue Aug 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1_3jpp7
- new version

