%define _unpackaged_files_terminate_build 1

Name: google-guice7
Version: 7.0.0
Release: alt1

Summary: Lightweight dependency injection framework for Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/google/guice
VCS: https://github.com/google/guice.git

BuildArch: noarch

Source0: %name-%version.tar.xz

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.felix:org.apache.felix.framework)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: mvn(com.google.errorprone:error_prone_annotations)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(org.apache:apache-jar-resource-bundle)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(jakarta.inject:jakarta.inject-api)
BuildRequires: mvn(jakarta.inject:jakarta.inject-tck)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(aopalliance:aopalliance)
BuildRequires: jakarta-servlet
BuildRequires: mvn(org.mockito:mockito-core)

AutoReq: yes,noosgi

%description
Put simply, Guice alleviates the need for factories and the use of new
in your Java code. Think of Guice's @Inject as the new new. You will
still need to write factories in some cases, but your code will not
depend directly on them. Your code will be easier to change, unit test
and reuse in other contexts.

Guice embraces Java's type safe nature, especially when it comes to
features introduced in Java 5 such as generics and annotations. You
might think of Guice as filling in missing features for core
Java. Ideally, the language itself would provide most of the same
features, but until such a language comes along, we have Guice.

Guice helps you design better APIs, and the Guice API itself sets a
good example. Guice is not a kitchen sink. We justify each feature
with at least three use cases. When in doubt, we leave it out. We
build general functionality which enables you to extend Guice rather
than adding every feature to the core framework.

%package -n guice7-assistedinject
Group: Development/Java
Summary: AssistedInject extension module for Guice

%description -n guice7-assistedinject
Guice is a lightweight dependency injection framework for Java. This package
provides the AssistedInject module for Guice.

%package -n guice7-grapher
Group: Development/Java
Summary: Grapher extension module for Guice

%description -n guice7-grapher
Guice is a lightweight dependency injection framework for Java. This package
provides the Grapher module for Guice.

%package -n guice7-jmx
Group: Development/Java
Summary: JMX extension module for Guice

%description -n guice7-jmx
Guice is a lightweight dependency injection framework for Java. This package
provides the JMX module for Guice.

%package -n guice7-jndi
Group: Development/Java
Summary: JNDI extension module for Guice

%description -n guice7-jndi
Guice is a lightweight dependency injection framework for Java. This package
provides the JNDI module for Guice.

%package -n guice7-servlet
Group: Development/Java
Summary: Servlet extension module for Guice

%description -n guice7-servlet
Guice is a lightweight dependency injection framework for Java. This package
provides the Servlet module for Guice.

%package -n guice7-throwingproviders
Group: Development/Java
Summary: ThrowingProviders extension module for Guice

%description -n guice7-throwingproviders
Guice is a lightweight dependency injection framework for Java. This package
provides the ThrowingProviders module for Guice.

%package -n guice7-testlib
Group: Development/Java
Summary: Test utilities for Guice extensions

%description -n guice7-testlib
This package provides test utilities for Guice extensions.

%javadoc_package

%prep
%setup

%pom_remove_parent

%pom_disable_module dagger-adapter extensions
%pom_disable_module persist extensions
%pom_disable_module spring extensions

%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_xpath_remove "pom:profile[pom:id='guice.with.jarjar']" core
%pom_xpath_set "pom:instructions/pom:Import-Package" \
  "!com.google.inject.*,*" core

%pom_add_dep com.google.code.findbugs:jsr305 core

%mvn_alias :guice :::classes:

%build
%mvn_compat_version "com.google.inject:*" 7.0.0
%mvn_compat_version "com.google.inject.extensions:*" 7.0.0
%mvn_file ":guice-{*}" guice7/guice7-@1
%mvn_file ":guice" guice7/%{name}
%mvn_file ":extensions-parent" guice7/guice7-extensions-parent
%mvn_package :guice-parent guice
%mvn_package :extensions-parent guice
%mvn_package :guice-bom guice
%mvn_build -s

%install
%mvn_install

%files -n %{?module_prefix}%{name} -f .mfiles-guice
%doc COPYING
%files -n guice7-assistedinject -f .mfiles-guice-assistedinject
%files -n guice7-grapher -f .mfiles-guice-grapher
%files -n guice7-jmx -f .mfiles-guice-jmx
%files -n guice7-jndi -f .mfiles-guice-jndi
%files -n guice7-servlet -f .mfiles-guice-servlet
%files -n guice7-throwingproviders -f .mfiles-guice-throwingproviders
%files -n guice7-testlib -f .mfiles-guice-testlib

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 7.0.0-alt1
- Initial build for ALT.
