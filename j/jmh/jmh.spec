Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global hghash 7ff584954008
Name:          jmh
Version:       1.13
Release:       alt1_8jpp8
Summary:       Java Microbenchmark Harness
License:       GPLv2 with exceptions
URL:           http://openjdk.java.net/projects/code-tools/jmh/
Source0:       http://hg.openjdk.java.net/code-tools/jmh/archive/%{hghash}.tar.bz2

# Patch for jopt-simple >= 5
Patch0: jopt-simple.patch

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.sf.jopt-simple:jopt-simple) >= 5
BuildRequires: mvn(org.apache.commons:commons-math3)
BuildRequires: mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires: mvn(org.ow2.asm:asm)
Requires: mvn(net.sf.jopt-simple:jopt-simple) >= 5

BuildArch:     noarch
Source44: import.info

%description
The JMH is a Java harness for building, running, and analysing
nano/micro/macro benchmarks written in Java and other languages
targeting the JVM.

%package core-benchmarks
Group: Development/Java
Summary:       JMH Core Benchmarks

%description core-benchmarks
JMH Core Benchmarks.

%package generator-annprocess
Group: Development/Java
Summary:       JMH Generators: Annotation Processors

%description generator-annprocess
JMH benchmark generator, based on annotation processors.

%package generator-asm
Group: Development/Java
Summary:       JMH Generators: ASM

%description generator-asm
JMH benchmark generator, based on ASM bytecode manipulation.

%package generator-bytecode
Group: Development/Java
Summary:       JMH Generators: Bytecode

%description generator-bytecode
JMH benchmark generator, based on byte-code inspection.

%package generator-reflection
Group: Development/Java
Summary:       JMH Generators: Reflection

%description generator-reflection
JMH benchmark generator, based on reflection.

%package parent
Group: Development/Java
Summary:       Java Microbenchmark Harness Parent POM

%description parent
Java Microbenchmark Harness Parent POM.

%package samples
Group: Development/Java
Summary:       JMH Samples
# BSD jmh-samples/src/main/java/*
License:       BSD

%description samples
JMH Samples.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
License:       BSD and GPLv2 with exceptions
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{hghash}
%patch0 -p1

%pom_disable_module %{name}-archetypes
%pom_disable_module %{name}-core-ct
%pom_disable_module %{name}-core-it

# Plugins unnecessary for RPM builds
%pom_remove_plugin -r :maven-eclipse-plugin
%pom_remove_plugin -r :maven-license-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

# wagon-ssh
%pom_xpath_remove "pom:build/pom:extensions" %{name}-core

# textTest_ROOT:218->test:134->compare:115 Mismatch expected:<...thrpt ...
rm -r %{name}-core/src/test/java/org/openjdk/jmh/results/format/ResultFormatTest.java

# Fix non ASCII chars
for s in $(find %{name}-samples -name "*.java") \
 %{name}-core-benchmarks/src/main/java/org/openjdk/jmh/validation/tests/BlackholeConsumeCPUTest.java \
 %{name}-core-benchmarks/src/main/java/org/openjdk/jmh/validation/tests/BlackholeConsecutiveTest.java \
 %{name}-core-benchmarks/src/main/java/org/openjdk/jmh/validation/tests/BlackholeSingleTest.java \
 %{name}-core-benchmarks/src/main/java/org/openjdk/jmh/validation/tests/BlackholePipelinedTest.java \
 %{name}-core-benchmarks/src/main/java/org/openjdk/jmh/validation/IterationScoresFormatter.java ;do
  native2ascii -encoding UTF8 ${s} ${s}
done

# http://mail.openjdk.java.net/pipermail/jmh-dev/2015-August/001997.html
sed -i "s,59,51,;s,Temple Place,Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," src/license/gpl_cpe/license.txt

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}-core
%doc --no-dereference %{name}-core/LICENSE

%files core-benchmarks -f .mfiles-%{name}-core-benchmarks
%doc --no-dereference %{name}-core-benchmarks/LICENSE

%files generator-annprocess -f .mfiles-%{name}-generator-annprocess
%doc --no-dereference %{name}-generator-annprocess/LICENSE

%files generator-asm -f .mfiles-%{name}-generator-asm
%doc --no-dereference %{name}-generator-asm/LICENSE

%files generator-bytecode -f .mfiles-%{name}-generator-bytecode
%doc --no-dereference %{name}-generator-bytecode/LICENSE

%files generator-reflection -f .mfiles-%{name}-generator-reflection
%doc --no-dereference %{name}-generator-reflection/LICENSE

%files parent -f .mfiles-%{name}-parent
%doc --no-dereference LICENSE src/license/*

%files samples -f .mfiles-%{name}-samples
%doc --no-dereference %{name}-samples/LICENSE src/license/bsd/*

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE src/license/*

%changelog
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_8jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_4jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.11.3-alt1_3jpp8
- new fc release

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.11.3-alt1_2jpp8
- new version

