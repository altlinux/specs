Name:    google-guice
Version: 5.1.0
Release: alt2
Epoch:   0

Summary: Lightweight dependency injection framework for Java 5 and above
License: Apache-2.0
Group:   Development/Java
URL:     https://github.com/google/guice

BuildArch: noarch

# ./create-tarball.sh %%version
Source0: %name-%version.tar.xz
Source1: create-tarball.sh
Source2: google-guice-guice.xml

BuildRequires(pre): /proc rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: mvn(aopalliance:aopalliance)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(javax.inject:javax.inject)
BuildRequires: mvn(javax.servlet:servlet-api)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.apache:apache-jar-resource-bundle) = 1.4

AutoReq: yes,noosgi

# Needed for bootstrap maven
#Provides: mvn(com.google.inject:guice::no_aop:)
#Provides: mvn(org.sonatype.sisu:sisu-guice::no_aop:)

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

%package -n guice-parent
Group: Development/Java
Summary: Guice parent POM

%description -n guice-parent
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides parent POM for Guice modules.

%package -n guice-assistedinject
Group: Development/Java
Summary: AssistedInject extension module for Guice

%description -n guice-assistedinject
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides AssistedInject module for Guice.

%package -n guice-extensions
Group: Development/Java
Summary: Extensions for Guice

%description -n guice-extensions
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides extensions POM for Guice.

%package -n guice-grapher
Group: Development/Java
Summary: Grapher extension module for Guice

%description -n guice-grapher
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Grapher module for Guice.

%package -n guice-jmx
Group: Development/Java
Summary: JMX extension module for Guice

%description -n guice-jmx
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides JMX module for Guice.

%package -n guice-jndi
Group: Development/Java
Summary: JNDI extension module for Guice

%description -n guice-jndi
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides JNDI module for Guice.

%package -n guice-servlet
Group: Development/Java
Summary: Servlet extension module for Guice

%description -n guice-servlet
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Servlet module for Guice.

%package -n guice-throwingproviders
Group: Development/Java
Summary: ThrowingProviders extension module for Guice

%description -n guice-throwingproviders
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides ThrowingProviders module for Guice.

%package -n guice-bom
Group: Development/Java
Summary: Bill of Materials for Guice

%description -n guice-bom
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides Bill of Materials module for Guice.

%{?javadoc_package}

%prep
%setup

%java_remove_annotations core/src/ \
  -p ^com.google.common.annotations. \
  -p ^com.google.errorprone.annotations.

# We don't have struts2 in Fedora yet.
%pom_disable_module struts2 extensions
# Android-specific extension
%pom_disable_module dagger-adapter extensions
 
# Remove additional build profiles, which we don't use anyways
# and which are only pulling additional dependencies.
%pom_xpath_remove "pom:profile[pom:id='guice.with.jarjar']" core
 
# Fix OSGi metadata due to not using jarjar
%pom_xpath_set "pom:instructions/pom:Import-Package" \
  "!com.google.inject.*,*" core
 
# Animal sniffer is only causing problems. Disable it for now.
%pom_remove_plugin :animal-sniffer-maven-plugin core
%pom_remove_plugin :animal-sniffer-maven-plugin extensions
 
%pom_remove_plugin :maven-gpg-plugin
 
# We don't have the custom doclet used by upstream. Remove
# maven-javadoc-plugin to generate javadocs with default style.
%pom_remove_plugin -r :maven-javadoc-plugin
 
# remove test dependency to make sure we don't produce requires
# see #1007498
%pom_remove_dep :guava-testlib extensions
%pom_xpath_remove "pom:dependency[pom:classifier='tests']" extensions
 
%pom_remove_parent
%pom_disable_module persist extensions
%pom_disable_module spring extensions
%pom_disable_module testlib extensions

%build
%mvn_file  ":guice-{*}"  guice/guice-@1
%mvn_file  ":guice" guice/%{name} %{name}
%mvn_build -f -s

%install
%mvn_install
install -Dpm0644 %SOURCE2 %buildroot%_datadir/maven-metadata/google-guice-guice.xml

ln -s %_javadir/guice/google-guice.jar \
  %buildroot%_javadir/guice/guice.jar

%files -n %{?module_prefix}%{name} -f .mfiles-guice
%_javadir/guice/guice.jar
%files -n guice-parent -f .mfiles-guice-parent
%files -n guice-assistedinject -f .mfiles-guice-assistedinject
%files -n guice-extensions -f .mfiles-extensions-parent
%files -n guice-grapher -f .mfiles-guice-grapher
%files -n guice-jmx -f .mfiles-guice-jmx
%files -n guice-jndi -f .mfiles-guice-jndi
%files -n guice-servlet -f .mfiles-guice-servlet
%files -n guice-throwingproviders -f .mfiles-guice-throwingproviders
%files -n guice-bom -f .mfiles-guice-bom

%changelog
* Fri Aug 15 2025 Ivan Khanas <xeno@altlinux.org> 0:5.1.0-alt2
- Create a symlink with the correct artifact name.

* Mon Aug 04 2025 Andrey Cherepanov <cas@altlinux.org> 0:5.1.0-alt1
- New version.

* Mon May 30 2022 Igor Vlasenko <viy@altlinux.org> 0:4.2.3-alt1_6jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:4.2.3-alt1_3jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0:4.2.2-alt1_1jpp8
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:4.1-alt1_14jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:4.1-alt1_12jpp8
- fc29 update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:4.1-alt1_11jpp8
- java fc28+ update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:4.1-alt1_10jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:4.1-alt1_8jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:4.1-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.0-alt1_5jpp8
- new fc release

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

