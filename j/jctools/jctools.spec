Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jctools
Version:       3.1.0
Release:       alt1_1jpp8
Summary:       Java Concurrency Tools for the JVM
License:       ASL 2.0
URL:           http://jctools.github.io/JCTools/
Source0:       https://github.com/JCTools/JCTools/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.javaparser:javaparser-core) >= 3.14.16
BuildRequires:  mvn(com.google.guava:guava-testlib)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-all)

BuildArch:     noarch

# Parent pom package obsoleted in F34
Obsoletes: %{name}-parent < 3.1.0-1
# Can't ship these modules any longer due to usage of Unsafe.defineClass
# not available in JDK 11, see https://github.com/JCTools/JCTools/issues/254
Obsoletes: %{name}-channels < 3.1.0-1
Obsoletes: %{name}-experimental < 3.1.0-1
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
Summary: Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n JCTools-%{version}

# Cleanup
find . -name '*.class' -print -delete
find . -name '*.jar' -print -delete

# Remove failure-prone tests (race condition?)
rm jctools-core/src/test/java/org/jctools/queues/MpqSanityTestMpscCompound.java
rm jctools-core/src/test/java/org/jctools/queues/atomic/AtomicMpqSanityTestMpscCompound.java
rm jctools-core/src/test/java/org/jctools/maps/NonBlockingHashMapTest.java

# Fix up version
%pom_xpath_set pom:project/pom:version %{version}
%pom_xpath_set -r pom:parent/pom:version %{version} %{name}-{build,core,channels,experimental}

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :coveralls-maven-plugin %{name}-core
%pom_remove_plugin :jacoco-maven-plugin %{name}-core
%pom_remove_plugin :maven-source-plugin %{name}-core
%pom_remove_plugin :maven-javadoc-plugin %{name}-core

# Unavailable deps
%pom_disable_module %{name}-benchmarks
%pom_disable_module %{name}-concurrency-test

# Can't build these modules due to use of Unsafe.defineClass which is not present
# in JDK 11, see https://github.com/JCTools/JCTools/issues/254
%pom_disable_module %{name}-channels
%pom_disable_module %{name}-experimental

# No need to package internal build tools
%mvn_package :jctools-parent __noinstall
%mvn_package :jctools-build __noinstall

%build
%mvn_build -s -f

%install
%mvn_install

%files -f .mfiles-%{name}-core
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
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

