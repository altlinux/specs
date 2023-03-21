Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           google-gson
Version:        2.9.1
Release:        alt1_1jpp11
Summary:        Java lib for conversion of Java objects into JSON representation
License:        ASL 2.0
URL:            https://github.com/google/gson
Source0:        https://github.com/google/gson/archive/gson-parent-%{version}.tar.gz

# Internal packages are naughtily used by other packages in Fedora
Patch1: 0002-Also-export-internal-packages-in-OSGi-metadata.patch
# Remove dependency on unavailable templating-maven-plugin
# Reverts upstream commit https://github.com/google/gson/commit/d84e26d
Patch3: 0004-This-commit-added-a-dependency-on-templating-maven-p.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  bnd-maven-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
Source44: import.info

%description
Gson is a Java library that can be used to convert a Java object into its
JSON representation. It can also be used to convert a JSON string into an
equivalent Java object. Gson can work with arbitrary Java objects including
pre-existing objects that you do not have source-code of.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n gson-gson-parent-%{version}
#rm ./gradle/wrapper/gradle-wrapper.jar
%patch1 -p1
%patch3 -p1

# The test EnumWithObfuscatedTest requires the plugins copy-rename-maven-plugin, proguard-maven-plugin and maven-resources-plugin to work correctly because it tests Gson interaction with a class obfuscated by ProGuard.
# https://github.com/google/gson/issues/2045
rm ./gson/src/test/java/com/google/gson/functional/EnumWithObfuscatedTest.java

# to check later
rm ./gson/src/test/java/com/google/gson/internal/bind/DefaultDateTypeAdapterTest.java
# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin :copy-rename-maven-plugin gson
%pom_remove_plugin :proguard-maven-plugin gson

%pom_remove_plugin  :moditect-maven-plugin gson

# Remove dependency on unavailable templating-maven-plugin
%pom_remove_plugin  org.codehaus.mojo:templating-maven-plugin gson
rm gson/src/test/java/com/google/gson/internal/GsonBuildConfigTest.java
rm gson/src/test/java/com/google/gson/functional/GsonVersionDiagnosticsTest.java

# to fix error: package javax.annotation is not visible import javax.annotation.PostConstruct;
rm extras/src/main/java/com/google/gson/typeadapters/PostConstructAdapterFactory.java
rm extras/src/test/java/com/google/gson/typeadapters/PostConstructAdapterFactoryTest.java

#depends on com.google.caliper
%pom_disable_module metrics

#depends on com.google.protobuf:protobuf-java:jar:4.0.0-rc-2 and com.google.truth:truth:jar:1.1.3
%pom_disable_module proto

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE
%doc README.md CHANGELOG.md UserGuide.md

%files javadoc  -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 2.9.1-alt1_1jpp11
- new version

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 2.9.0-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 2.8.6-alt1_7jpp11
- update

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 2.8.6-alt1_3jpp11
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.8.2-alt1_3jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 2.8.2-alt1_2jpp8
- fc29 update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 2.8.2-alt1_1jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_6jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1_3jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_3jpp7
- new version

