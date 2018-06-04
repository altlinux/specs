Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global gittag ASM_6_1_1

Name:           objectweb-asm
Version:        6.1.1
Release:        alt1_1jpp8
Summary:        Java bytecode manipulation and analysis framework
License:        BSD
URL:            http://asm.ow2.org/
BuildArch:      noarch

Source0:        https://gitlab.ow2.org/asm/asm/repository/%{gittag}/archive.tar.gz
Source1:        parent.pom
Source2:        http://repo1.maven.org/maven2/org/ow2/asm/asm/%{version}/asm-%{version}.pom
Source3:        http://repo1.maven.org/maven2/org/ow2/asm/asm-analysis/%{version}/asm-analysis-%{version}.pom
Source4:        http://repo1.maven.org/maven2/org/ow2/asm/asm-commons/%{version}/asm-commons-%{version}.pom
Source5:        http://repo1.maven.org/maven2/org/ow2/asm/asm-test/%{version}/asm-test-%{version}.pom
Source6:        http://repo1.maven.org/maven2/org/ow2/asm/asm-tree/%{version}/asm-tree-%{version}.pom
Source7:        http://repo1.maven.org/maven2/org/ow2/asm/asm-util/%{version}/asm-util-%{version}.pom
Source8:        http://repo1.maven.org/maven2/org/ow2/asm/asm-xml/%{version}/asm-xml-%{version}.pom
# We still want to create an "all" uberjar, so this is a custom pom to generate it
# TODO: Fix other packages to no longer depend on "asm-all" so we can drop this
Source9:        asm-all-%{version}.pom

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.codehaus.janino:janino)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires:  mvn(org.junit.platform:junit-platform-surefire-provider)
BuildRequires:  mvn(org.ow2:ow2:pom:)
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
%setup -q -n asm-%{gittag}-11b3cabce9b90706cf91a47dd15215c667f8055b

find -name *.jar -delete
rm -rf gradle/

# A custom parent pom to aggregate the build
cp -p %{SOURCE1} pom.xml

# Insert poms into modules
for pom in asm asm-analysis asm-commons asm-test asm-tree asm-util asm-xml; do
  cp -p $RPM_SOURCE_DIR/${pom}-%{version}.pom $pom/pom.xml
  # Fix junit5 configuration
  %pom_add_dep org.junit.jupiter:junit-jupiter-engine:5.1.0:test $pom
  %pom_add_plugin org.apache.maven.plugins:maven-surefire-plugin:2.21.0 $pom \
"            <dependencies>
                <dependency>
                    <groupId>org.junit.platform</groupId>
                    <artifactId>junit-platform-surefire-provider</artifactId>
                    <version>1.2.0-RC1</version>
                </dependency>
            </dependencies>"
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
        <_pluginpath>$(pwd)/tools/bnd-module-plugin/bnd-module-plugin.jar</_pluginpath>
        <_plugin>org.objectweb.asm.tools.ModuleInfoBndPlugin;</_plugin>
      </instructions>
    </configuration>"
  fi
done

# Insert asm-all pom
mkdir -p asm-all
cp -p %{SOURCE9} asm-all/pom.xml

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

%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%jpackage_script org.objectweb.asm.xml.Processor "" "" %{name}/asm:%{name}/asm-attrs:%{name}/asm-util:%{name}/asm-xml %{name}-processor true

%files -f .mfiles
%doc --no-dereference LICENSE.txt
%{_bindir}/%{name}-processor

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
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

