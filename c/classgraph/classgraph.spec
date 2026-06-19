%define _unpackaged_files_terminate_build 1

Name: classgraph
Version: 4.8.184
Release: alt2

Summary: An uber-fast parallelized Java classpath scanner and module scanner
License: MIT
Group: Development/Java
Url: https://github.com/classgraph/classgraph
Vcs: https://github.com/classgraph/classgraph.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre):rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: narcissus
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-antrun-plugin
BuildRequires: maven-source-plugin
BuildRequires: jmh-generator-annprocess
BuildRequires: jmh
BuildRequires: cdi-api

%description
ClassGraph is an uber-fast parallelized classpath scanner and module scanner
for Java, Scala, Kotlin and other JVM languages.

%{?javadoc_package}

%prep
%setup

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin

%pom_remove_dep org.ops4j.pax.url:pax-url-aether
%pom_remove_dep org.slf4j:slf4j-jdk14
%pom_remove_dep org.hibernate.javax.persistence:hibernate-jpa-2.1-api
%pom_remove_dep com.google.jimfs:jimfs
%pom_remove_dep jakarta.validation:jakarta.validation-api
%pom_remove_dep org.eclipse.jdt:org.eclipse.jdt.annotation 

%build
# Skip tests, most of test deps are not available in Sisyphus.
%mvn_build -- -Dmaven.test.skip=true

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE-ClassGraph.txt

%changelog
* Fri Jun 19 2026 Anton Meleshnikov <alton@altlinux.org> 4.8.184-alt2
- FTBFS fix.

* Fri Nov 21 2025 Ivan Khanas <xeno@altlinux.org> 4.8.184-alt1
- First build for ALT.
