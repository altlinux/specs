Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define fedora 21
%if 0%{?fedora}
%bcond_without extensions
%endif

%global short_name guice

Name:           google-%{short_name}
Version:        3.1.3
Release:        alt1_1jpp7
Summary:        Lightweight dependency injection framework for Java 5 and above
Group:          Development/Java
License:        ASL 2.0
URL:            https://github.com/sonatype/sisu-%{short_name}
# ./create-tarball.sh %{version}
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  javapackages-tools >= 0.7.0
BuildRequires:  maven-local
BuildRequires:  maven-remote-resources-plugin
BuildRequires: apache-resource-bundles apache-jar-resource-bundle
BuildRequires:  aopalliance
BuildRequires:  atinject
BuildRequires:  cglib
BuildRequires:  guava
BuildRequires:  slf4j

%if %{with extensions}
BuildRequires:  hibernate-jpa-2.0-api
BuildRequires:  springframework-beans
BuildRequires:  tomcat-servlet-3.0-api
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

%package -n %{short_name}-throwingproviders
Group: Development/Java
Summary:        ThrowingProviders extension module for Guice

%description -n %{short_name}-throwingproviders
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides ThrowingProviders module for Guice.

%endif # with extensions

%package javadoc
Summary:        API documentation for Guice
Group:          Development/Java
Provides:       %{short_name}-javadoc = %{version}-%{release}
BuildArch: noarch

%description javadoc
This package provides %{summary}.


%prep
%setup -q -n %{name}-%{version}

# We don't have struts2 in Fedora yet.
%pom_disable_module struts2 extensions

# Remove additional build profiles, which we don't use anyways
# and which are only pulling additional dependencies.
%pom_xpath_remove pom:project/pom:profiles core

# Animal sniffer is only causing problems. Disable it for now.
%pom_remove_plugin :animal-sniffer-maven-plugin core
%pom_remove_plugin :animal-sniffer-maven-plugin extensions

# We don't have the custom doclet used by upstream. Remove
# maven-javadoc-plugin to generate javadocs with default style.
%pom_remove_plugin :maven-javadoc-plugin

%pom_remove_dep javax.persistence:persistence-api extensions/persist
%pom_add_dep org.hibernate.javax.persistence:hibernate-jpa-2.0-api extensions/persist

# Don't try to build extension modules unless they are needed
%if %{without extensions}
%pom_disable_module extensions
%endif


%build
%if %{with extensions}
%mvn_alias ":guice-{assistedinject,grapher,jmx,jndi,multibindings,persist,\
servlet,spring,throwingproviders}" "com.google.inject.extensions:guice-@1"
%endif # with extensions

%mvn_file  ":guice-{*}"  %{short_name}/guice-@1
%mvn_file  ":sisu-guice" %{short_name}/%{name} %{name}
%mvn_alias ":sisu-guice" "com.google.inject:guice"
# Skip tests because of missing dependency (hsqldb-j5).
%mvn_build -f -s

%install
%mvn_install

%files -f .mfiles-sisu-guice

%files -n %{short_name}-parent -f .mfiles-guice-parent
%doc COPYING

%if %{with extensions}
%files -n %{short_name}-assistedinject -f .mfiles-guice-assistedinject
%files -n %{short_name}-extensions -f .mfiles-guice-extensions
%files -n %{short_name}-grapher -f .mfiles-guice-grapher
%files -n %{short_name}-jmx -f .mfiles-guice-jmx
%files -n %{short_name}-jndi -f .mfiles-guice-jndi
%files -n %{short_name}-multibindings -f .mfiles-guice-multibindings
%files -n %{short_name}-persist -f .mfiles-guice-persist
%files -n %{short_name}-servlet -f .mfiles-guice-servlet
%files -n %{short_name}-spring -f .mfiles-guice-spring
%files -n %{short_name}-throwingproviders -f .mfiles-guice-throwingproviders
%endif # with extensions

%files javadoc -f .mfiles-javadoc
%doc COPYING


%changelog
* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.3-alt1_1jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.2-alt2_6jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.2-alt1_6jpp7
- non-bootstrap build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

