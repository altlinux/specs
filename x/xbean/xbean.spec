Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven unzip
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
# Conditionals to help breaking eclipse <-> xbean dependency cycle
# when bootstrapping for new architectures
%if 0%{?fedora}
%bcond_without equinox
%bcond_without spring
%endif

Name:           xbean
Version:        3.13
BuildArch:      noarch

Release:        alt1_1jpp7
Summary:        Java plugin based web server

Group:          Development/Java
License:        ASL 2.0
URL:            http://geronimo.apache.org/xbean/

Source0:        http://repo2.maven.org/maven2/org/apache/%{name}/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        xbean.depmap

BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-logging
BuildRequires:  objectweb-asm
BuildRequires:  ant
BuildRequires:  qdox
BuildRequires:  slf4j
BuildRequires:  maven-local
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-idea-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-shade-plugin
%if %{with equinox}
BuildRequires:  eclipse-equinox-osgi
%else
BuildRequires:  felix-framework
%endif
%if %{with spring}
BuildRequires:  apache-commons-jexl
BuildRequires:  aries-blueprint
# test deps BuildRequires:  cglib
BuildRequires:  felix-osgi-compendium
BuildRequires:  felix-osgi-core
BuildRequires:  geronimo-annotation
BuildRequires:  pax-logging

BuildRequires:  maven-archiver
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-project
BuildRequires:  plexus-archiver
BuildRequires:  plexus-utils
BuildRequires:  springframework
BuildRequires:  springframework-beans
BuildRequires:  springframework-context
BuildRequires:  springframework-web
%endif

Requires:       apache-commons-logging
Requires:       objectweb-asm
Requires:       slf4j
%if %{with equinox}
Requires:       eclipse-equinox-osgi
%else
Requires:       felix-framework
%endif
Source44: import.info

%description
The goal of XBean project is to create a plugin based server
analogous to Eclipse being a plugin based IDE. XBean will be able to
discover, download and install server plugins from an Internet based
repository. In addition, we include support for multiple IoC systems,
support for running with no IoC system, JMX without JMX code,
lifecycle and class loader management, and a rock solid Spring
integration.

%if %{with spring}
# For now blueprint module fails to compile. Disable it.
%if 0
%package        blueprint
Group: Development/Java
Summary:        Schema-driven namespace handler for Apache Aries Blueprint
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       apache-commons-jexl
Requires:       aries-blueprint
Requires:       felix-osgi-compendium
Requires:       geronimo-annotation
Requires:       pax-logging

%description    blueprint
This package provides %{summary}.
%endif

%package        classloader
Group: Development/Java
Summary:        A flexibie multi-parent classloader
# maven-xbean-plugin
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       springframework-beans

%description    classloader
This package provides %{summary}.

%package        spring
Group: Development/Java
Summary:        Schema-driven namespace handler for spring contexts
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       springframework-beans
Requires:       springframework-context
Requires:       springframework-web

%description    spring
This package provides %{summary}.

%package        -n maven-%{name}-plugin
Group: Development/Java
Summary:        XBean plugin for Apache Maven
Requires:       %{name}-spring = %{?epoch:%epoch:}%{version}-%{release}
Requires:       maven
Requires:       maven-archiver
Requires:       maven-project
Requires:       plexus-archiver
Requires:       plexus-utils
Requires:       qdox
Requires:       springframework
Requires:       springframework-beans
Requires:       springframework-context
Requires:       springframework-web

%description    -n maven-%{name}-plugin
This package provides %{summary}.
%endif

%package        javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q
# build failing on this due to doxia-sitetools problems
rm src/site/site.xml

%pom_remove_parent
%pom_remove_dep mx4j:mx4j
%pom_remove_dep :xbean-asm-shaded xbean-reflect

# These aren't needed for now
%pom_disable_module xbean-asm-shaded
%pom_disable_module xbean-finder-shaded
%pom_disable_module xbean-telnet

# Prevent modules depending on springframework from building.
%if %{without spring}
   %pom_remove_dep org.springframework:
   #%%pom_disable_module xbean-blueprint
   %pom_disable_module xbean-classloader
   %pom_disable_module xbean-spring
   %pom_disable_module maven-xbean-plugin
%endif
# blueprint FTBFS, disable for now
%pom_disable_module xbean-blueprint


# Replace generic OSGi dependencies with either Equinox or Felix
%pom_remove_dep :org.osgi.core xbean-bundleutils
%pom_remove_dep org.eclipse:osgi xbean-bundleutils
%if %{with equinox}
  %pom_add_dep org.eclipse.osgi:org.eclipse.osgi xbean-bundleutils
%else
  rm -rf xbean-bundleutils/src/main/java/org/apache/xbean/osgi/bundle/util/equinox/
  %pom_add_dep org.apache.felix:org.apache.felix.framework xbean-bundleutils
%endif


# Fix dependency on xbean-asm-shaded to original objectweb-asm
sed -i 's/org.apache.xbean.asm/org.objectweb.asm/' \
    xbean-reflect/src/main/java/org/apache/xbean/recipe/XbeanAsmParameterNameLoader.java

# disable copy of internal aries-blueprint
sed -i "s|<Private-Package>|<!--Private-Package>|" xbean-blueprint/pom.xml
sed -i "s|</Private-Package>|</Private-Package-->|" xbean-blueprint/pom.xml

# Fix ant groupId
find -name pom.xml -exec sed -i "s|<groupId>ant</groupId>|<groupId>org.apache.ant</groupId>|" {} \;
# Fix cglib artifactId
find -name pom.xml -exec sed -i "s|<artifactId>cglib-nodep</artifactId>|<artifactId>cglib</artifactId>|" {} \;

%build
mvn-rpmbuild -e \
        -Dmaven.compiler.source=1.5 \
        -Dmaven.compiler.target=1.5 \
        -Dmaven.local.depmap.file="%{SOURCE1}" \
        -Dmaven.test.skip=true \
        install javadoc:aggregate


%install
install -dm 755 $RPM_BUILD_ROOT/%{_javadir}/%{name}
install -dm 755 $RPM_BUILD_ROOT/%{_mavenpomdir}
install -dm 755 $RPM_BUILD_ROOT/%{_mavendepmapfragdir}
install -dm 755 $RPM_BUILD_ROOT/%{_javadocdir}/%{name}

# parent pom
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-main.pom
%add_maven_depmap JPP.%{name}-main.pom

for sub in bundleutils classpath finder naming reflect; do
    install -m 644 %{name}-${sub}/target/%{name}-${sub}-%{version}.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}/%{name}-${sub}.jar
    install -pm 644 %{name}-${sub}/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-%{name}-${sub}.pom
    %add_maven_depmap JPP.%{name}-%{name}-${sub}.pom %{name}/%{name}-${sub}.jar
done

%if %{with spring}
   for m in classloader spring; do  # blueprint should be there too
       install -m 644 %{name}-${m}/target/%{name}-${m}-%{version}.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}/%{name}-${m}.jar;
       install -pm 644 %{name}-${m}/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
       %add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar -f ${m}
   done
   # maven-xbean-plugin
   install -m 644 maven-%{name}-plugin/target/maven-%{name}-plugin-%{version}.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}/maven-%{name}-plugin.jar
   install -pm 644 maven-%{name}-plugin/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-maven-%{name}-plugin.pom
   %add_maven_depmap JPP.%{name}-maven-%{name}-plugin.pom %{name}/maven-%{name}-plugin.jar -f maven-plugin
%endif

# javadocs
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc LICENSE NOTICE
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-bundleutils.jar
%{_javadir}/%{name}/%{name}-classpath.jar
%{_javadir}/%{name}/%{name}-finder.jar
%{_javadir}/%{name}/%{name}-naming.jar
%{_javadir}/%{name}/%{name}-reflect.jar
%{_mavenpomdir}/JPP.%{name}-main.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-bundleutils.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-classpath.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-finder.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-naming.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-reflect.pom
%{_mavendepmapfragdir}/%{name}

%if %{with spring}
%if 0
%files blueprint
%doc LICENSE NOTICE %{name}-blueprint/target/restaurant.xsd*
%{_javadir}/%{name}/%{name}-blueprint.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-blueprint.pom
%{_mavendepmapfragdir}/%{name}-blueprint
%endif

%files classloader
%doc LICENSE NOTICE
%{_javadir}/%{name}/%{name}-classloader.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-classloader.pom
%{_mavendepmapfragdir}/%{name}-classloader

%files spring
%doc LICENSE NOTICE
%{_javadir}/%{name}/%{name}-spring.jar
%{_mavenpomdir}/JPP.%{name}-%{name}-spring.pom
%{_mavendepmapfragdir}/%{name}-spring

%files -n maven-%{name}-plugin
%doc LICENSE NOTICE
%{_javadir}/%{name}/maven-%{name}-plugin.jar
%{_mavenpomdir}/JPP.%{name}-maven-%{name}-plugin.pom
%{_mavendepmapfragdir}/%{name}-maven-plugin
%endif

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.13-alt1_1jpp7
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.12-alt1_4jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt4_3jpp7
- fixed build

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt3_3jpp7
- restored rcp dep

* Sun Mar 31 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt2_3jpp7
- bootstrapping eclipse - dropped eclipse-rcp dep

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt1_3jpp7
- new version

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.8-alt1_2jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.7-alt3_7jpp7
- fixed build

* Tue May 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.7-alt2_7jpp7
- added maven-xbean-plugin

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.7-alt1_7jpp7
- new version

* Tue Jan 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.4.3-alt1_2jpp6
- new version

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt1_1jpp5
- first build

