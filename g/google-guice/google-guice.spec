Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
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
%global tag     bd0d620

Name:           google-%{short_name}
Version:        3.1.2
Release:        alt1_6jpp7
Summary:        Lightweight dependency injection framework for Java 5 and above
Group:          Development/Java
License:        ASL 2.0
URL:            https://github.com/sonatype/sisu-%{short_name}
Source:         https://github.com/sonatype/sisu-%{short_name}/tarball/sisu-%{short_name}-%{version}#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  javapackages-tools >= 0.7.0
BuildRequires:  maven
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

Requires:       jpackage-utils
Requires:       aopalliance
Requires:       atinject
Requires:       cglib
Requires:       guava
Requires:       slf4j
Requires:       %{short_name}-parent = %{?epoch:%epoch:}%{version}-%{release}
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
Requires:       jpackage-utils

%description -n %{short_name}-parent
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides parent POM for Guice modules.

%if %{with extensions}

%package -n %{short_name}-assistedinject
Group: Development/Java
Summary:        AssistedInject extension module for Guice
Requires:       jpackage-utils
Requires:       %{short_name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n %{short_name}-assistedinject
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides AssistedInject module for Guice.

%package -n %{short_name}-extensions
Group: Development/Java
Summary:        Extensions for Guice
Requires:       jpackage-utils
Requires:       %{short_name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n %{short_name}-extensions
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides extensions POM for Guice.

%package -n %{short_name}-grapher
Group: Development/Java
Summary:        Grapher extension module for Guice
Requires:       jpackage-utils
Requires:       %{short_name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{short_name}-assistedinject = %{?epoch:%epoch:}%{version}-%{release}
Requires:       %{short_name}-multibindings = %{?epoch:%epoch:}%{version}-%{release}

%description -n %{short_name}-grapher
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Grapher module for Guice.

%package -n %{short_name}-jmx
Group: Development/Java
Summary:        JMX extension module for Guice
Requires:       jpackage-utils
Requires:       %{short_name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n %{short_name}-jmx
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides JMX module for Guice.

%package -n %{short_name}-jndi
Group: Development/Java
Summary:        JNDI extension module for Guice
Requires:       jpackage-utils
Requires:       %{short_name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n %{short_name}-jndi
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides JNDI module for Guice.

%package -n %{short_name}-multibindings
Group: Development/Java
Summary:        MultiBindings extension module for Guice
Requires:       jpackage-utils
Requires:       %{short_name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n %{short_name}-multibindings
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides MultiBindings module for Guice.

%package -n %{short_name}-persist
Group: Development/Java
Summary:        Persist extension module for Guice
Requires:       jpackage-utils
Requires:       hibernate-jpa-2.0-api
Requires:       tomcat-servlet-3.0-api
Requires:       %{short_name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n %{short_name}-persist
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Persist module for Guice.

%package -n %{short_name}-servlet
Group: Development/Java
Summary:        Servlet extension module for Guice
Requires:       jpackage-utils
Requires:       tomcat-servlet-3.0-api
Requires:       %{short_name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n %{short_name}-servlet
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Servlet module for Guice.

%package -n %{short_name}-spring
Group: Development/Java
Summary:        Spring extension module for Guice
Requires:       jpackage-utils
Requires:       springframework-beans
Requires:       %{short_name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n %{short_name}-spring
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Spring module for Guice.

%package -n %{short_name}-throwingproviders
Group: Development/Java
Summary:        ThrowingProviders extension module for Guice
Requires:       jpackage-utils
Requires:       %{short_name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n %{short_name}-throwingproviders
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides ThrowingProviders module for Guice.

%endif # with extensions

%package javadoc
Summary:        API documentation for Guice
Group:          Development/Java
Requires:       jpackage-utils
Provides:       %{short_name}-javadoc = %{version}-%{release}
BuildArch: noarch

%description javadoc
This package provides %{summary}.


%prep
%setup -q -n sonatype-sisu-%{short_name}-%{tag}
find -name '*.jar' -delete

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

# Don't try to build extension modules unless they are needed
%if %{without extensions}
%pom_disable_module extensions
%endif

%build
# Skip tests because of missing dependency (hsqldb-j5).
mvn-rpmbuild -e -Dmaven.test.skip=true verify javadoc:aggregate

%install
# directories
install -d -m 755 %{buildroot}%{_javadir}/%{short_name}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
# JARs
install -p -m 644 core/target/sisu-%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}/%{name}.jar
# POMs
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-parent.pom
install -p -m 644 core/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-%{name}.pom
# depmaps
%add_maven_depmap JPP.%{short_name}-%{short_name}-parent.pom -f parent
%add_maven_depmap JPP.%{short_name}-%{name}.pom %{short_name}/%{name}.jar -a com.google.inject:guice
# javadoc
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
# compat symlink
ln -sf %{short_name}/%{name}.jar %{buildroot}%{_javadir}

# Extensions
%if %{with extensions}
# JARs
install -p -m 644 extensions/assistedinject/target/%{short_name}-assistedinject-%{version}.jar %{buildroot}%{_javadir}/%{short_name}/%{short_name}-assistedinject.jar
install -p -m 644 extensions/grapher/target/%{short_name}-grapher-%{version}.jar %{buildroot}%{_javadir}/%{short_name}/%{short_name}-grapher.jar
install -p -m 644 extensions/jmx/target/%{short_name}-jmx-%{version}.jar %{buildroot}%{_javadir}/%{short_name}/%{short_name}-jmx.jar
install -p -m 644 extensions/jndi/target/%{short_name}-jndi-%{version}.jar %{buildroot}%{_javadir}/%{short_name}/%{short_name}-jndi.jar
install -p -m 644 extensions/multibindings/target/%{short_name}-multibindings-%{version}.jar %{buildroot}%{_javadir}/%{short_name}/%{short_name}-multibindings.jar
install -p -m 644 extensions/persist/target/%{short_name}-persist-%{version}.jar %{buildroot}%{_javadir}/%{short_name}/%{short_name}-persist.jar
install -p -m 644 extensions/servlet/target/%{short_name}-servlet-%{version}.jar %{buildroot}%{_javadir}/%{short_name}/%{short_name}-servlet.jar
install -p -m 644 extensions/spring/target/%{short_name}-spring-%{version}.jar %{buildroot}%{_javadir}/%{short_name}/%{short_name}-spring.jar
install -p -m 644 extensions/throwingproviders/target/%{short_name}-throwingproviders-%{version}.jar %{buildroot}%{_javadir}/%{short_name}/%{short_name}-throwingproviders.jar
# POMs
install -p -m 644 extensions/assistedinject/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-assistedinject.pom
install -p -m 644 extensions/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-extensions.pom
install -p -m 644 extensions/grapher/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-grapher.pom
install -p -m 644 extensions/jmx/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-jmx.pom
install -p -m 644 extensions/jndi/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-jndi.pom
install -p -m 644 extensions/multibindings/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-multibindings.pom
install -p -m 644 extensions/persist/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-persist.pom
install -p -m 644 extensions/servlet/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-servlet.pom
install -p -m 644 extensions/spring/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-spring.pom
install -p -m 644 extensions/throwingproviders/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{short_name}-%{short_name}-throwingproviders.pom
# depmaps
%add_maven_depmap JPP.%{short_name}-%{short_name}-assistedinject.pom %{short_name}/%{short_name}-assistedinject.jar -f assistedinject -a com.google.inject.extensions:guice-assistedinject
%add_maven_depmap JPP.%{short_name}-%{short_name}-extensions.pom -f extensions
%add_maven_depmap JPP.%{short_name}-%{short_name}-grapher.pom %{short_name}/%{short_name}-grapher.jar -f grapher -a com.google.inject.extensions:guice-grapher
%add_maven_depmap JPP.%{short_name}-%{short_name}-jmx.pom %{short_name}/%{short_name}-jmx.jar -f jmx -a com.google.inject.extensions:guice-jmx
%add_maven_depmap JPP.%{short_name}-%{short_name}-jndi.pom %{short_name}/%{short_name}-jndi.jar -f jndi -a com.google.inject.extensions:guice-jndi
%add_maven_depmap JPP.%{short_name}-%{short_name}-multibindings.pom %{short_name}/%{short_name}-multibindings.jar -f multibindings -a com.google.inject.extensions:guice-multibindings
%add_maven_depmap JPP.%{short_name}-%{short_name}-persist.pom %{short_name}/%{short_name}-persist.jar -f persist -a com.google.inject.extensions:guice-persist
%add_maven_depmap JPP.%{short_name}-%{short_name}-servlet.pom %{short_name}/%{short_name}-servlet.jar -f servlet -a com.google.inject.extensions:guice-servlet
%add_maven_depmap JPP.%{short_name}-%{short_name}-spring.pom %{short_name}/%{short_name}-spring.jar -f spring -a com.google.inject.extensions:guice-spring
%add_maven_depmap JPP.%{short_name}-%{short_name}-throwingproviders.pom %{short_name}/%{short_name}-throwingproviders.jar -f throwingproviders -a com.google.inject.extensions:guice-throwingproviders
%endif # with extensions

%files -f .mfiles
%doc README
%{_javadir}/%{name}.jar

%files -n %{short_name}-parent -f .mfiles-parent
%doc COPYING

%if %{with extensions}
%files -n %{short_name}-assistedinject -f .mfiles-assistedinject
%files -n %{short_name}-extensions -f .mfiles-extensions
%files -n %{short_name}-grapher -f .mfiles-grapher
%files -n %{short_name}-jmx -f .mfiles-jmx
%files -n %{short_name}-jndi -f .mfiles-jndi
%files -n %{short_name}-multibindings -f .mfiles-multibindings
%files -n %{short_name}-persist -f .mfiles-persist
%files -n %{short_name}-servlet -f .mfiles-servlet
%files -n %{short_name}-spring -f .mfiles-spring
%files -n %{short_name}-throwingproviders -f .mfiles-throwingproviders
%endif # with extensions

%files javadoc
%doc COPYING
%{_javadocdir}/%{name}


%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.2-alt1_6jpp7
- non-bootstrap build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

