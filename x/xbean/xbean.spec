BuildRequires: maven-plugin-plugin
Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 18
Name:           xbean
Version:        3.11.1
BuildArch:      noarch

Release:        alt4_3jpp7
Summary:        Java plugin based web server

Group:          Development/Java
License:        ASL 2.0
URL:            http://geronimo.apache.org/xbean/

# unfortunately no source/binary releases are being made lately, just
# tags in repos and binary releases in maven repositories
# svn export http://svn.apache.org/repos/asf/geronimo/xbean/tags/xbean-3.8
# tar caf xbean-3.8.tar.xz xbean-3.8
Source0:        xbean-%{version}.tar.xz
Source1:        xbean.depmap

BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-logging
BuildRequires:  objectweb-asm
BuildRequires:  ant
BuildRequires:  qdox
BuildRequires:  slf4j
BuildRequires:  maven
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
%if !0%{?rhel:1}
BuildRequires:  eclipse-rcp
BuildRequires:  maven-archiver
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-project
BuildRequires:  plexus-archiver
BuildRequires:  plexus-utils
BuildRequires:  springframework
BuildRequires:  springframework-beans
BuildRequires:  springframework-context
BuildRequires:  springframework-web
%else
BuildRequires:  felix-framework
%endif

Requires:       jpackage-utils
Requires:       apache-commons-logging
Requires:       objectweb-asm
Requires:       slf4j
Requires:       eclipse-rcp
Source44: import.info

%description
The goal of XBean project is to create a plugin based server
analogous to Eclipse being a plugin based IDE. XBean will be able to
discover, download and install server plugins from an Internet based
repository. In addition, we include support for multiple IoC systems,
support for running with no IoC system, JMX without JMX code,
lifecycle and class loader management, and a rock solid Spring
integration.

%if !0%{?rhel:1}
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
Requires:       jpackage-utils
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
%pom_disable_module xbean-blueprint
%pom_disable_module xbean-classloader
%pom_disable_module xbean-finder-shaded
%pom_disable_module xbean-telnet

# Prevent modules depending on springframework from building.
if [ %{?rhel} ]; then
   %pom_remove_dep org.springframework:
   %pom_disable_module xbean-spring
   %pom_disable_module maven-xbean-plugin
fi

%pom_add_plugin :maven-compiler-plugin . "
    <configuration>
      <source>1.5</source>
      <target>1.5</target>
    </configuration>"

# Force use of Equinox
%pom_remove_dep :org.osgi.core xbean-bundleutils
%pom_remove_dep org.eclipse:osgi xbean-bundleutils
%pom_xpath_inject "pom:project/pom:dependencies" "
    <dependency>
      <groupId>org.eclipse.osgi</groupId>
      <artifactId>org.eclipse.osgi</artifactId>
      <version>any</version>
    </dependency>" xbean-bundleutils


# Fix dependency on xbean-asm-shaded to original objectweb-asm
sed -i 's/org.apache.xbean.asm/org.objectweb.asm/' \
    xbean-reflect/src/main/java/org/apache/xbean/recipe/XbeanAsmParameterNameLoader.java

# Fix ant groupId
find -name pom.xml -exec sed -i "s|<groupId>ant</groupId>|<groupId>org.apache.ant</groupId>|" {} \;

# Do not build equinox specific part for rhel.
if [ %{?rhel} ]; then
   rm -rf xbean-bundleutils/src/main/java/org/apache/xbean/osgi/bundle/util/equinox/
   sed -i "s|<groupId>org.eclipse|<groupId>org.apache.felix|g" xbean-bundleutils/pom.xml
   sed -i "s|<artifactId>osgi|<artifactId>org.apache.felix.framework|g" xbean-bundleutils/pom.xml
fi


%build
mvn-rpmbuild -e \
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

if [ %{?fedora} ]; then
   # xbean-spring
   install -m 644 %{name}-spring/target/%{name}-spring-%{version}.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}/%{name}-spring.jar
   install -pm 644 %{name}-spring/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-%{name}-spring.pom
   %add_maven_depmap JPP.%{name}-%{name}-spring.pom %{name}/%{name}-spring.jar -f spring
   # maven-xbean-plugin
   install -m 644 maven-%{name}-plugin/target/maven-%{name}-plugin-%{version}.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}/maven-%{name}-plugin.jar
   install -pm 644 maven-%{name}-plugin/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-maven-%{name}-plugin.pom
   %add_maven_depmap JPP.%{name}-maven-%{name}-plugin.pom %{name}/maven-%{name}-plugin.jar -f maven-plugin
fi

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

%if !0%{?rhel:1}
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

