Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global srcname JCTools

Name:           jctools
Version:        3.3.0
Release:        alt1_1jpp8
Summary:        Java Concurrency Tools for the JVM
License:        ASL 2.0

URL:            https://github.com/JCTools/JCTools
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.javaparser:javaparser-core) >= 3.14.16
BuildRequires:  mvn(com.google.guava:guava-testlib)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-all)

# unused parent package was removed for fedora 33+
Obsoletes:      %{name}-parent < 3.1.0-1

# unused channels and experimental modules disabled with 3.1.0 for fedora 33+
# Unsafe.defineClass is not available in JDK 11:
# https://github.com/JCTools/JCTools/issues/254
Obsoletes:      %{name}-channels < 3.1.0-1
Obsoletes:      %{name}-experimental < 3.1.0-1
Source44: import.info

%description
This project aims to offer some concurrent data structures
currently missing from the JDK:

A. SPSC/MPSC/SPMC/MPMC Bounded lock free queues
A. SPSC/MPSC Unbounded lock free queues
A. Alternative interfaces for queues
A. Offheap concurrent ring buffer for ITC/IPC purposes
A. Single Writer Map/Set implementations
A. Low contention stats counters
A. Executor


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q -n %{srcname}-%{version}

# drop some failure-prone tests (race conditions?)
rm jctools-core/src/test/java/org/jctools/queues/MpqSanityTestMpscCompound.java
rm jctools-core/src/test/java/org/jctools/queues/atomic/AtomicMpqSanityTestMpscCompound.java
rm jctools-core/src/test/java/org/jctools/maps/NonBlockingHashMapTest.java

# set correct version in all pom.xml files
%pom_xpath_set pom:project/pom:version %{version}
%pom_xpath_set pom:parent/pom:version %{version} jctools-{build,core,channels,experimental}

# remove plugins unnecessary for RPM builds
%pom_remove_plugin :coveralls-maven-plugin jctools-core
%pom_remove_plugin :jacoco-maven-plugin jctools-core
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-source-plugin jctools-core
%pom_remove_plugin :maven-javadoc-plugin jctools-core

# remove tests with additional kotlin dependencies
%pom_remove_dep org.jetbrains.kotlinx:lincheck jctools-core
rm -r jctools-core/src/test/java/org/jctools/maps/linearizability_test/

# disable unused modules with unavailable dependencies
%pom_disable_module jctools-benchmarks
%pom_disable_module jctools-concurrency-test

# incompatible with Java 11 and unused in fedora:
# https://github.com/JCTools/JCTools/issues/254
%pom_disable_module jctools-channels
%pom_disable_module jctools-experimental

# do not install internal build tools
%mvn_package :jctools-build __noinstall

# do not install unused parent POM
%mvn_package :jctools-parent __noinstall


%build
%mvn_build -s -f


%install
%mvn_install


%files -f .mfiles-jctools-core
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE


%changelog
* Mon Aug 16 2021 Igor Vlasenko <viy@altlinux.org> 3.3.0-alt1_1jpp8
- new version

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 3.2.0-alt1_1jpp8
- fc update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 3.1.0-alt1_1jpp8
- new version

* Sun Oct 11 2020 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1_6jpp8
- new version

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1_1jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_3jpp8
- java update

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_2jpp8
- new version

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.3.alphajpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.2.alphajpp8
- new version

