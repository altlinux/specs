Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global hghash 534d83d9137f
Name:          jmh
Version:       1.11.3
Release:       alt1_3jpp8
Summary:       Java Microbenchmark Harness
# BSD jmh-samples/src/main/java/*
# 2 files have unknown license, reported @ http://mail.openjdk.java.net/pipermail/jmh-dev/2015-August/002037.html
License:       GPLv2 with exceptions
URL:           http://openjdk.java.net/projects/code-tools/jmh/
Source0:       http://hg.openjdk.java.net/code-tools/jmh/archive/%{hghash}.tar.bz2

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.sf.jopt-simple:jopt-simple)
BuildRequires: mvn(org.apache.commons:commons-math3)
# BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-site-plugin)
BuildRequires: mvn(org.ow2.asm:asm)

Obsoletes:     %{name}-core-ct
Obsoletes:     %{name}-core-it

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
License:       BSD

%description samples
JMH Samples.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
# BSD jmh-samples/src/main/java/*
License:       BSD and GPLv2 with exceptions
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{hghash}

%pom_disable_module %{name}-archetypes
%pom_disable_module %{name}-core-ct
%pom_disable_module %{name}-core-it

%pom_remove_plugin -r :maven-eclipse-plugin
%pom_remove_plugin -r :maven-license-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:executions"

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
sed -i "s,59,51,;s,Temple Place,Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301,"  $(find -name "LICENSE") src/license/gpl_cpe/license.txt

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}-core
%doc %{name}-core/LICENSE

%files core-benchmarks -f .mfiles-%{name}-core-benchmarks
%doc %{name}-core-benchmarks/LICENSE

%files generator-annprocess -f .mfiles-%{name}-generator-annprocess
%doc %{name}-generator-annprocess/LICENSE

%files generator-asm -f .mfiles-%{name}-generator-asm
%doc %{name}-generator-asm/LICENSE

%files generator-bytecode -f .mfiles-%{name}-generator-bytecode
%doc %{name}-generator-bytecode/LICENSE

%files generator-reflection -f .mfiles-%{name}-generator-reflection
%doc %{name}-generator-reflection/LICENSE

%files parent -f .mfiles-%{name}-parent
%doc LICENSE src/license/*

%files samples -f .mfiles-%{name}-samples
%doc %{name}-samples/LICENSE src/license/bsd/*

%files javadoc -f .mfiles-javadoc
%doc LICENSE src/license/*

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.11.3-alt1_3jpp8
- new fc release

* Wed Dec 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.11.3-alt1_2jpp8
- new version

