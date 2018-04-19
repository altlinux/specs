Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           zinc
Version:        0.3.1
Release:        alt1_5jpp8
Summary:        Incremental scala compiler
License:        ASL 2.0
URL:            https://github.com/typesafehub/zinc
BuildArch:      noarch

Source0:        https://github.com/typesafehub/zinc/archive/v%{version}.tar.gz
Source1:        http://repo1.maven.org/maven2/com/typesafe/zinc/zinc/%{version}/zinc-%{version}.pom
# ASL mandates that the licence file be included in redistributed source
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt

# Patch fixes compilation failure, which is probably caused by
# incompatible Scala version
Patch0:         0001-Fix-file-filtering.patch

BuildRequires:  javapackages-local
BuildRequires:  mvn(org.scala-lang:scala-library)
BuildRequires:  mvn(org.scala-sbt:incremental-compiler)
BuildRequires:  mvn(com.martiansoftware:nailgun-server)
Source44: import.info

%description
Zinc is a stand-alone version of sbt's incremental compiler.

%prep
%setup -q
rm -rf src/scriptit dist nailgun project

%patch0 -p1

cp %{SOURCE1} pom.xml
cp %{SOURCE2} LICENSE.txt

%pom_xpath_remove "pom:dependency[pom:classifier='sources']"
%pom_change_dep :incremental-compiler org.scala-sbt:

%build
scalac -cp $(build-classpath sbt nailgun) src/main/scala/com/typesafe/zinc/*
jar cf zinc.jar com
%mvn_artifact pom.xml zinc.jar

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_4jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_3jpp8
- new jpp release

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_2jpp8
- new version

