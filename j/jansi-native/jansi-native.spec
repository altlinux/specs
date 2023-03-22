Epoch: 0
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-generic-compat
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global bits %{__isa_bits}
%global debug_package %{nil}

# jansi-native-1.8 tag is missing from git
# https://github.com/fusesource/jansi-native/commit/5015ad0
%global commit 5015ad023a55785dbe6ad19cc786c0533387feff

Name:           jansi-native
Version:        1.8
Release:        alt1_12jpp11
Summary:        Jansi Native implements the JNI Libraries used by the Jansi project
License:        ASL 2.0
URL:            http://jansi.fusesource.org/
Source0:        https://github.com/fusesource/jansi-native/archive/%{commit}/jansi-native-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.fusesource:fusesource-pom:pom:)
BuildRequires:  mvn(org.fusesource.hawtjni:maven-hawtjni-plugin) >= 1.9
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-runtime) >= 1.9
# jansi-native provides JNI libraries for use by the JAVA Jansi project,
# so it is only necessary on java_arches
Source44: import.info

%description
Jansi is a small java library that allows you to use ANSI escape sequences
in your Java console applications. It implements ANSI support on platforms
which don't support it like Windows and provides graceful degradation for
when output is being sent to output devices which cannot support ANSI sequences.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch:        noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jansi-native-%{commit}

%mvn_alias :jansi-linux%{bits} :jansi-linux
%mvn_file :jansi-linux%{bits} %{name}/jansi-linux%{bits} %{name}/jansi-linux

# use more modern source and target settings
%pom_xpath_set //pom:source 1.8
%pom_xpath_set //pom:target 1.8

# fix javadoc generation for java 11
%pom_remove_plugin :maven-javadoc-plugin
%pom_xpath_inject pom:pluginManagement/pom:plugins "<plugin>
<artifactId>maven-javadoc-plugin</artifactId>
<configuration>
<source>1.8</source>
<detectJavaApiLink>false</detectJavaApiLink>
</configuration>
</plugin>"

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dplatform=linux%{bits}

%install
%mvn_install

%files -f .mfiles
%doc readme.md changelog.md
%doc --no-dereference license.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference license.txt

%changelog
* Wed Mar 22 2023 Igor Vlasenko <viy@altlinux.org> 0:1.8-alt1_12jpp11
- update

* Sat Jun 11 2022 Igor Vlasenko <viy@altlinux.org> 0:1.8-alt1_9jpp11
- added jni provides for maven migration

* Fri Jun 10 2022 Igor Vlasenko <viy@altlinux.org> 0:1.8-alt1_7jpp11
- update

* Fri May 28 2021 Igor Vlasenko <viy@altlinux.org> 0:1.8-alt1_5jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0:1.8-alt1_2jpp11
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_8jpp8
- new version

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_5jpp8
- regenerated to fix __isa_bits definition

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_3jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_11jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_10jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_9jpp8
- %%_jnidir set to /usr/lib/java

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_9jpp8
- java 8 mass update

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_5jpp7
- new release

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp7
- new version

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp7
- new version

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_1jpp6
- fixed build

* Fri Feb 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp6
- new version

