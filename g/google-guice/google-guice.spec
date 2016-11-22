Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 24
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%if 0%{?fedora}
%bcond_without extensions
%endif

%global short_name guice

Name:           google-%{short_name}
Version:        4.0
Release:        alt1_4jpp8
Summary:        Lightweight dependency injection framework for Java 5 and above
License:        ASL 2.0
URL:            https://github.com/google/%{short_name}
BuildArch:      noarch

# ./create-tarball.sh %%{version}
Source0:        %{name}-%{version}.tar.xz
Source1:        create-tarball.sh

Patch0:         0001-Revert-Some-work-on-issue-910-ensure-that-anonymous-.patch

# Rejected upstream: https://github.com/google/guice/issues/492
Patch100:       https://raw.githubusercontent.com/sonatype/sisu-guice/master/PATCHES/GUICE_492_slf4j_logger_injection.patch
# Forwarded upstream: https://github.com/google/guice/issues/618
Patch101:       https://raw.githubusercontent.com/sonatype/sisu-guice/master/PATCHES/GUICE_618_extensible_filter_pipeline.patch

BuildRequires:  maven-local >= 3.2.4
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  munge-maven-plugin
BuildRequires:  maven-gpg-plugin
BuildRequires:  apache-resource-bundles
BuildRequires:  aopalliance
BuildRequires:  atinject
BuildRequires:  cglib
BuildRequires:  guava
BuildRequires:  slf4j

%if %{with extensions}
BuildRequires:  hibernate-jpa-2.0-api
BuildRequires:  springframework-beans
%endif

# Test dependencies:
%if 0
BuildRequires:  maven-surefire-provider-testng
BuildRequires:  aqute-bnd
BuildRequires:  atinject-tck
BuildRequires:  easymock2
BuildRequires:  felix-framework
BuildRequires:  hibernate3-entitymanager
BuildRequires:  mvn(org.hsqldb:hsqldb-j5)
BuildRequires:  testng
%endif

Provides:       %{short_name} = %{version}-%{release}
Source44: import.info

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

%package -n %{short_name}-parent
Group: Development/Java
Summary:        Guice parent POM

%description -n %{short_name}-parent
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides parent POM for Guice modules.

%if %{with extensions}

%package -n %{short_name}-assistedinject
Group: Development/Java
Summary:        AssistedInject extension module for Guice

%description -n %{short_name}-assistedinject
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides AssistedInject module for Guice.

%package -n %{short_name}-extensions
Group: Development/Java
Summary:        Extensions for Guice

%description -n %{short_name}-extensions
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides extensions POM for Guice.

%package -n %{short_name}-grapher
Group: Development/Java
Summary:        Grapher extension module for Guice

%description -n %{short_name}-grapher
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Grapher module for Guice.

%package -n %{short_name}-jmx
Group: Development/Java
Summary:        JMX extension module for Guice

%description -n %{short_name}-jmx
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides JMX module for Guice.

%package -n %{short_name}-jndi
Group: Development/Java
Summary:        JNDI extension module for Guice

%description -n %{short_name}-jndi
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides JNDI module for Guice.

%package -n %{short_name}-multibindings
Group: Development/Java
Summary:        MultiBindings extension module for Guice

%description -n %{short_name}-multibindings
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides MultiBindings module for Guice.

%package -n %{short_name}-persist
Group: Development/Java
Summary:        Persist extension module for Guice

%description -n %{short_name}-persist
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Persist module for Guice.

%package -n %{short_name}-servlet
Group: Development/Java
Summary:        Servlet extension module for Guice

%description -n %{short_name}-servlet
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Servlet module for Guice.

%package -n %{short_name}-spring
Group: Development/Java
Summary:        Spring extension module for Guice

%description -n %{short_name}-spring
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Spring module for Guice.

%package -n %{short_name}-testlib
Group: Development/Java
Summary:        TestLib extension module for Guice

%description -n %{short_name}-testlib
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides TestLib module for Guice.

%package -n %{short_name}-throwingproviders
Group: Development/Java
Summary:        ThrowingProviders extension module for Guice

%description -n %{short_name}-throwingproviders
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides ThrowingProviders module for Guice.

%package -n %{short_name}-bom
Group: Development/Java
Summary:        Bill of Materials for Guice

%endif # with extensions

%description -n %{short_name}-bom
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Bill of Materials module for Guice.

%package javadoc
Group: Development/Java
Summary:        API documentation for Guice
Provides:       %{short_name}-javadoc = %{version}-%{release}
BuildArch: noarch

%description javadoc
This package provides %{summary}.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch100 -p1
%patch101 -p1

# We don't have struts2 in Fedora yet.
%pom_disable_module struts2 extensions
# Android-specific extension
%pom_disable_module dagger-adapter extensions

# Remove additional build profiles, which we don't use anyways
# and which are only pulling additional dependencies.
%pom_xpath_remove "pom:profile[pom:id='guice.with.jarjar']" core

# Animal sniffer is only causing problems. Disable it for now.
%pom_remove_plugin :animal-sniffer-maven-plugin core
%pom_remove_plugin :animal-sniffer-maven-plugin extensions

# We don't have the custom doclet used by upstream. Remove
# maven-javadoc-plugin to generate javadocs with default style.
%pom_remove_plugin :maven-javadoc-plugin

# remove test dependency to make sure we don't produce requires
# see #1007498
%pom_remove_dep :guava-testlib extensions
%pom_xpath_remove "pom:dependency[pom:classifier[text()='tests']]" extensions

%pom_remove_parent
%pom_set_parent com.google.inject:guice-parent:%{version} jdk8-tests

# Don't try to build extension modules unless they are needed
%if %{without extensions}
%pom_disable_module extensions
%endif

%mvn_package :jdk8-tests __noinstall

%build
%if %{with extensions}
%mvn_alias "com.google.inject.extensions:" "org.sonatype.sisu.inject:"
%endif # with extensions

%mvn_package :::no_aop: guice

%mvn_file  ":guice-{*}"  %{short_name}/guice-@1
%mvn_file  ":guice" %{short_name}/%{name} %{name}
%mvn_alias ":guice" "org.sonatype.sisu:sisu-guice"
# Skip tests because of missing dependency guice-testlib
%mvn_build -f -s

%install
%mvn_install

%files -f .mfiles-guice
%dir %{_javadir}/%{short_name}

%files -n %{short_name}-parent -f .mfiles-guice-parent
%doc COPYING

%if %{with extensions}
%files -n %{short_name}-assistedinject -f .mfiles-guice-assistedinject
%files -n %{short_name}-extensions -f .mfiles-extensions-parent
%files -n %{short_name}-grapher -f .mfiles-guice-grapher
%files -n %{short_name}-jmx -f .mfiles-guice-jmx
%files -n %{short_name}-jndi -f .mfiles-guice-jndi
%files -n %{short_name}-multibindings -f .mfiles-guice-multibindings
%files -n %{short_name}-persist -f .mfiles-guice-persist
%files -n %{short_name}-servlet -f .mfiles-guice-servlet
%files -n %{short_name}-spring -f .mfiles-guice-spring
%files -n %{short_name}-testlib -f .mfiles-guice-testlib
%files -n %{short_name}-throwingproviders -f .mfiles-guice-throwingproviders
%endif # with extensions

%files -n %{short_name}-bom -f .mfiles-guice-bom

%files javadoc -f .mfiles-javadoc
%doc COPYING


%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.0-alt1_4jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.0-alt1_3jpp8
- added osgi provides

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.0-alt1_2jpp8
- java8 mass update

* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.3-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.2-alt2_6jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.2-alt1_6jpp7
- non-bootstrap build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

