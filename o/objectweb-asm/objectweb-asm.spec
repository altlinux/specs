Epoch: 0
Group: Development/Java
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without junit5
%bcond_without osgi

Name:           objectweb-asm
Version:        7.0
Release:        alt1_2jpp8
Summary:        Java bytecode manipulation and analysis framework
License:        BSD
URL:            http://asm.ow2.org/
BuildArch:      noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        parent.pom
Source2:        http://repo1.maven.org/maven2/org/ow2/asm/asm/%{version}/asm-%{version}.pom
Source3:        http://repo1.maven.org/maven2/org/ow2/asm/asm-analysis/%{version}/asm-analysis-%{version}.pom
Source4:        http://repo1.maven.org/maven2/org/ow2/asm/asm-commons/%{version}/asm-commons-%{version}.pom
Source5:        http://repo1.maven.org/maven2/org/ow2/asm/asm-test/%{version}/asm-test-%{version}.pom
Source6:        http://repo1.maven.org/maven2/org/ow2/asm/asm-tree/%{version}/asm-tree-%{version}.pom
Source7:        http://repo1.maven.org/maven2/org/ow2/asm/asm-util/%{version}/asm-util-%{version}.pom
# We still want to create an "all" uberjar, so this is a custom pom to generate it
# TODO: Fix other packages to no longer depend on "asm-all" so we can drop this
Source8:        asm-all.pom
# The source contains binary jars that cannot be verified for licensing and could be proprietary
Source9:       generate-tarball.sh

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.ow2:ow2:pom:)
%if %{with junit5}
BuildRequires:  mvn(org.codehaus.janino:janino)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit-platform)
%endif

%if %{with osgi}
# asm-all needs to be in pluginpath for BND.  If this self-dependency
# becomes a problem then ASM core will have to be build from source
# with javac before main maven build, just like bnd-module-plugin
BuildRequires:  objectweb-asm >= 6
%endif

# Explicit javapackages-tools requires since asm-processor script uses
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Source44: import.info

%description
ASM is an all purpose Java bytecode manipulation and analysis
framework.  It can be used to modify existing classes or dynamically
generate classes, directly in binary form.  Provided common
transformations and analysis algorithms allow to easily assemble
custom complex transformations and code analysis tools.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q

# A custom parent pom to aggregate the build
cp -p %{SOURCE1} pom.xml

%if %{without junit5}
%pom_disable_module asm-test
%endif

# Insert poms into modules
for pom in asm asm-analysis asm-commons asm-test asm-tree asm-util; do
  cp -p $RPM_SOURCE_DIR/${pom}-%{version}.pom $pom/pom.xml
  # Fix junit5 configuration
%if %{with junit5}
  %pom_add_dep org.junit.jupiter:junit-jupiter-engine:5.1.0:test $pom
  %pom_add_plugin org.apache.maven.plugins:maven-surefire-plugin:2.22.0 $pom
%endif
%if %{with osgi}
  if [ "$pom" != "asm-test" ] ; then
    # Make into OSGi bundles
    bsn="org.objectweb.${pom//-/.}"
    %pom_xpath_inject pom:project "<packaging>bundle</packaging>" $pom
    %pom_add_plugin org.apache.felix:maven-bundle-plugin:3.5.0 $pom \
"   <extensions>true</extensions>
    <configuration>
      <instructions>
        <Bundle-SymbolicName>$bsn</Bundle-SymbolicName>
        <Bundle-RequiredExecutionEnvironment>JavaSE-1.8</Bundle-RequiredExecutionEnvironment>
        <_removeheaders>Bnd-LastModified,Build-By,Created-By,Include-Resource,Require-Capability,Tool</_removeheaders>
        <_pluginpath>$(pwd)/tools/bnd-module-plugin/bnd-module-plugin.jar, $(find-jar objectweb-asm/asm-all)</_pluginpath>
        <_plugin>org.objectweb.asm.tools.ModuleInfoBndPlugin;</_plugin>
      </instructions>
    </configuration>"
  fi
%endif
done

# Disable tests that use unlicensed class files
sed -i -e '/testReadAndWriteWithComputeMaxsAndLargeSubroutines/i@org.junit.jupiter.api.Disabled("missing class file")' \
  asm/src/test/java/org/objectweb/asm/ClassWriterTest.java
sed -i -e '/testMergeWithJsrReachableFromTwoDifferentPaths/i@org.junit.jupiter.api.Disabled("missing class file")' \
  asm-analysis/src/test/java/org/objectweb/asm/tree/analysis/BasicInterpreterTest.java
sed -i -e '/testSortLocalVariablesAndInstantiate()/i@org.junit.jupiter.api.Disabled("missing class file")' \
  asm-commons/src/test/java/org/objectweb/asm/commons/LocalVariablesSorterTest.java

# Insert asm-all pom
mkdir -p asm-all
sed 's/@VERSION@/%{version}/g' %{SOURCE8} > asm-all/pom.xml

# Remove invalid self-dependency
%pom_remove_dep org.ow2.asm:asm-test asm-test

# Compat aliases
%mvn_alias :asm-all org.ow2.asm:asm-debug-all

# No need to ship the custom parent pom
%mvn_package :asm-aggregator __noinstall
# Don't ship the test framework to avoid runtime dep on junit
%mvn_package :asm-test __noinstall

%build
# Must compile bnd plugin first, which is used to generate Java 9 module-info.class files
pushd tools/bnd-module-plugin
javac -sourcepath ../../asm/src/main/java/ -cp $(build-classpath aqute-bnd) $(find -name *.java)
jar cf bnd-module-plugin.jar -C src/main/java org
popd

%if %{with junit5}
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8
%else
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8
%endif

%install
%mvn_install

%jpackage_script org.objectweb.asm.xml.Processor "" "" %{name}/asm:%{name}/asm-attrs:%{name}/asm-util %{name}-processor true

%files -f .mfiles
%doc --no-dereference LICENSE.txt
%{_bindir}/%{name}-processor

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 0:7.0-alt1_2jpp8
- new version

* Thu Jun 20 2019 Igor Vlasenko <viy@altlinux.ru> 0:6.2.1-alt1_1jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0:6.1.1-alt1_1jpp8
- new version

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:6.0-alt1_1jpp8
- java update

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:5.1-alt1_8jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:5.1-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.1-alt1_4jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.4-alt1_2jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.3-alt1_2jpp8
- java 8 mass update

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_7jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_4jpp7
- update

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_4jpp6
- updated OSGi manifest to match version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt4_4jpp6
- added pom groupid asm

* Sun Oct 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt3_4jpp6
- fixed poms

* Fri Sep 16 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt2_4jpp6
- removed asm2 pom provides

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt1_4jpp6
- new version

* Sat Feb 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_2jpp6
- added osgi manifest

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_2jpp6
- new version

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt2_5jpp5
- added OSGi manifest

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_3jpp5
- converted from JPackage by jppimport script

* Mon Jan 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

