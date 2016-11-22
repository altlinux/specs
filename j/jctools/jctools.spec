Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jctools
%define version 1.1
%global namedreltag -alpha
%global namedversion %{version}%{?namedreltag}

Name:          jctools
Version:       1.1
Release:       alt1_0.3.alphajpp8
Summary:       Java Concurrency Tools for the JVM
License:       ASL 2.0
URL:           http://jctools.github.io/JCTools/
Source0:       https://github.com/JCTools/JCTools/archive/v%{namedversion}.tar.gz

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

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n JCTools-%{namedversion}
# Cleanup
find . -name '*.class' -print -delete
find . -name '*.jar' -print -delete

# Prevent build failure
%pom_remove_plugin :maven-enforcer-plugin

# Unavailable deps
%pom_disable_module jctools-benchmarks

# Add OSGi support
%pom_xpath_set "pom:project/pom:packaging" bundle jctools-core
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 jctools-core '
<extensions>true</extensions>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.3.alphajpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.2.alphajpp8
- new version

