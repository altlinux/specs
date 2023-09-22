Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# This package is a component of sbt, but needs sbt to build.  Use this to
# bootstrap when sbt is not available.
%bcond_with sbt

# Scal build version
%global scala_version 2.13

Name:           scalacheck
Version:        1.15.4
Release:        alt1_3jpp11
Summary:        Property-based testing for Scala

License:        BSD
URL:            http://www.scalacheck.org/
Source0:        https://github.com/typelevel/scalacheck/archive/%{version}/%{name}-%{version}.tar.gz

%if %{without sbt}
# We don't generate a POM from the ant build
Source1:       https://repo1.maven.org/maven2/org/scalacheck/%{name}_%{scala_version}/%{version}/%{name}_%{scala_version}-%{version}.pom
Source2:       %{name}.mf
Source3:       Generate.java
%endif

ExcludeArch:    %ix86 armh

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.scala-sbt:test-interface)
%if %{without sbt}
BuildRequires:  mvn(org.scala-lang:scala-compiler)
%else
BuildRequires:  sbt
%endif
Source44: import.info

%description
ScalaCheck is a library written in Scala and used for automated
property-based testing of Scala or Java programs. ScalaCheck was
originally inspired by the Haskell library QuickCheck, but has also
ventured into its own.

ScalaCheck has no external dependencies other than the Scala runtime,
and works great with sbt, the Scala build tool. It is also fully
integrated in the test frameworks ScalaTest and specs2. You can of
course also use ScalaCheck completely standalone, with its built-in
test runner.

%prep
%setup -q


%if %{with sbt}
cp -r /usr/share/java/sbt/ivy-local .
mkdir boot
%endif

%mvn_file org.%{name}:%{name}_%{scala_version} %{name}

%build
%if %{without sbt}
# Generate files
GENDIR=$PWD/src/main/scala/org/scalacheck
cd project
cp -p %{SOURCE3} .
CLASSPATH=.:$(build-classpath scala/scala-library)
scalac -g:vars codegen.scala
javac  -target 1.8 -source 1.8 -cp $CLASSPATH Generate.java
java -cp $CLASSPATH Generate $GENDIR
cd -

# Build the jar
mkdir target
files="project/codegen.scala $(find src/main/scala -name \*.scala)"
files="$files $(find src/main/scala-2.13+ -name \*.scala)"
files="$files $(find jvm/src/main -name \*.scala)"
scalac -g:vars -release 11 -classpath $(build-classpath test-interface) \
  -d target $files
cd target
sed 's/@VERSION@/%{version}/g' %{SOURCE2} > %{name}.mf
jar -c -m %{name}.mf -f %{name}.jar org
cd -
%mvn_artifact %{SOURCE1} target/%{name}.jar
%else
export SBT_BOOT_DIR=$PWD/boot
export SBT_IVY_DIR=$PWD/ivy-local
sbt package deliverLocal publishM2Configuration
%mvn_artifact target/scala-%{scala_version}/%{name}_%{scala_version}-%{version}.pom target/scala-%{scala_version}/%{name}_%{scala_version}-%{version}.jar
%endif

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.markdown README.markdown doc/UserGuide.md
%doc --no-dereference LICENSE

%changelog
* Fri Sep 22 2023 Andrey Cherepanov <cas@altlinux.org> 1.15.4-alt1_3jpp11
- NMU: Do not build for armh

* Sat Aug 14 2021 Igor Vlasenko <viy@altlinux.org> 1.15.4-alt1_2jpp11
- new version

* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 1.15.3-alt1_1jpp11
- new version

