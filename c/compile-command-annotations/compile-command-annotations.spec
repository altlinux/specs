Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          compile-command-annotations
Version:       1.2.1
Release:       alt1_10jpp11
Summary:       Hotspot compile command annotations
License:       ASL 2.0
URL:           https://github.com/nicoulaj/compile-command-annotations
Source0:       https://github.com/nicoulaj/compile-command-annotations/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(commons-io:commons-io)
#BuildRequires: mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)
# For IT suite
#BuildRequires: mvn(org.codehaus.groovy:groovy)

BuildArch:     noarch
Source44: import.info

%description
Annotation based configuration file generator for the
Hotspot JVM JIT compiler.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}

# net.ju-n:net-ju-n-parent:32
%pom_remove_parent

# Prevent IT failures
#find ./src/it/tests -name "pom.xml" -exec sed -i "s/@project.build.sourceEncoding@/UTF-8/g" {} +
#find ./src/it/tests -name "pom.xml" -exec sed -i "s/@exec-maven-plugin.version@/1.4.0/g" {} +
#find ./src/it/tests -name "pom.xml" -exec sed -i "s/@maven-compiler-plugin.version@/3.3/g" {} +
# Fails on koji only
%pom_remove_plugin :maven-invoker-plugin

# TestNG support requires version 4.7 or above
%pom_change_dep :testng ::6.8.21

%mvn_file net.ju-n.compile-command-annotations:%{name} %{name}

%build

%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference COPYING

%files javadoc -f .mfiles-javadoc
%doc --no-dereference COPYING

%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 1.2.1-alt1_10jpp11
- new version

