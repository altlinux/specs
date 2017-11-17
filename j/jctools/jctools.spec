Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.0.2
%global namedreltag %nil
%global namedversion %{version}%{?namedreltag}

Name:          jctools
Version:       2.0.2
Release:       alt1_2jpp8
Summary:       Java Concurrency Tools for the JVM
License:       ASL 2.0
URL:           http://jctools.github.io/JCTools/
Source0:       https://github.com/JCTools/JCTools/archive/v%{namedversion}/%{name}-%{namedversion}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.hamcrest:hamcrest-all)
BuildRequires: mvn(org.ow2.asm:asm-all)

BuildArch:     noarch
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

%package experimental
Group: Development/Java
Summary:       JCTools Experimental implementations

%description experimental
Experimental implementations for the
Java Concurrency Tools Library.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%package parent
Group: Development/Java
Summary:       JCTools Parent POM

%description parent
JCTools Parent POM.

%prep
%setup -q -n JCTools-%{namedversion}
# Cleanup
find . -name '*.class' -print -delete
find . -name '*.jar' -print -delete

%pom_xpath_set pom:project/pom:version %{namedversion}
%pom_xpath_set -r pom:parent/pom:version %{namedversion} %{name}-core %{name}-experimental

# Prevent build failure
%pom_remove_plugin :maven-enforcer-plugin

# Unavailable deps
%pom_disable_module %{name}-benchmarks
%pom_disable_module %{name}-concurrency-test

# This dep is unused and unneeded
%pom_remove_dep "com.google.guava:guava-testlib" jctools-experimental

# Not available
%pom_remove_plugin :cobertura-maven-plugin %{name}-core

# Useless tasks
%pom_remove_plugin :maven-source-plugin %{name}-core
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin']/pom:executions" %{name}-core

# Add OSGi support
for mod in core experimental; do
 %pom_xpath_set "pom:project/pom:packaging" bundle %{name}-${mod}
 %pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 %{name}-${mod} '
 <extensions>true</extensions>
 <executions>
   <execution>
     <id>bundle-manifest</id>
     <phase>process-classes</phase>
     <goals>
       <goal>manifest</goal>
     </goals>
   </execution>
 </executions>
 <configuration>
  <excludeDependencies>true</excludeDependencies>
 </configuration>'
done

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}-core
%doc README.md
%doc LICENSE

%files experimental -f .mfiles-%{name}-experimental

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%files parent -f .mfiles-%{name}-parent
%doc LICENSE

%changelog
* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.2-alt1_2jpp8
- new version

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.3.alphajpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.2.alphajpp8
- new version

