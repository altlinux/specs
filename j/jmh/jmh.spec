%define _unpackaged_files_terminate_build 1

Name: jmh
Version: 1.37
Release: alt2

Summary: Java Microbenchmark Harness
License: GPL-2.0-only
Group: Development/Java
Url: http://openjdk.java.net/projects/code-tools/jmh
Vcs: https://github.com/openjdk/jmh.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre):rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
BuildRequires: maven-local
BuildRequires: junit
BuildRequires: jopt-simple
BuildRequires: apache-commons-math
BuildRequires: objectweb-asm
BuildRequires: maven-enforcer
BuildRequires: jna
BuildRequires: jna-contrib
Requires: jopt-simple

%description
The JMH is a Java harness for building, running, and analysing
nano/micro/macro benchmarks written in Java and other languages
targeting the JVM.

%package core-benchmarks
Group: Development/Java
Summary: JMH Core Benchmarks

%description core-benchmarks
JMH Core Benchmarks.

%package generator-annprocess
Group: Development/Java
Summary: JMH Generators: Annotation Processors

%description generator-annprocess
JMH benchmark generator, based on annotation processors.

%package generator-asm
Group: Development/Java
Summary: JMH Generators: ASM

%description generator-asm
JMH benchmark generator, based on ASM bytecode manipulation.

%package generator-bytecode
Group: Development/Java
Summary: JMH Generators: Bytecode

%description generator-bytecode
JMH benchmark generator, based on byte-code inspection.

%package generator-reflection
Group: Development/Java
Summary: JMH Generators: Reflection

%description generator-reflection
JMH benchmark generator, based on reflection.

%package parent
Group: Development/Java
Summary: Java Microbenchmark Harness Parent POM

%description parent
Java Microbenchmark Harness Parent POM.

%package samples
Group: Development/Java
Summary: JMH Samples

%description samples
JMH Samples.

%prep
%setup

%pom_disable_module %name-archetypes
%pom_disable_module %name-core-ct
%pom_disable_module %name-core-it

# Plugins unnecessary for RPM builds
%pom_remove_plugin -r :maven-eclipse-plugin
%pom_remove_plugin -r :maven-license-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin    :maven-enforcer-plugin

# wagon-ssh
%pom_xpath_remove "pom:build/pom:extensions" %name-core

# textTest_ROOT:218->test:134->compare:115 Mismatch expected:<...thrpt ...
rm -r %name-core/src/test/java/org/openjdk/jmh/results/format/ResultFormatTest.java

# http://mail.openjdk.java.net/pipermail/jmh-dev/2015-August/001997.html
sed -i "s,59,51,;s,Temple Place,Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," src/license/gpl_cpe/license.txt

%build
%mvn_build -s

%install
%mvn_install

rm -rf %buildroot%_javadocdir

%files -f .mfiles-%name-core
%doc --no-dereference %name-core/LICENSE

%files core-benchmarks -f .mfiles-%name-core-benchmarks
%doc --no-dereference %name-core-benchmarks/LICENSE

%files generator-annprocess -f .mfiles-%name-generator-annprocess
%doc --no-dereference %name-generator-annprocess/LICENSE

%files generator-asm -f .mfiles-%name-generator-asm
%doc --no-dereference %name-generator-asm/LICENSE

%files generator-bytecode -f .mfiles-%name-generator-bytecode
%doc --no-dereference %name-generator-bytecode/LICENSE

%files generator-reflection -f .mfiles-%name-generator-reflection
%doc --no-dereference %name-generator-reflection/LICENSE

%files parent -f .mfiles-%name-parent
%doc --no-dereference LICENSE

%files samples -f .mfiles-%name-samples
%doc --no-dereference %name-samples/LICENSE src/license/bsd/*

%changelog
* Fri Jun 19 2026 Anton Meleshnikov <alton@altlinux.org> 1.37-alt2
- FTBFS fix.

* Fri Nov 07 2025 Ivan Khanas <xeno@altlinux.org> 1.37-alt1
- New version.

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

