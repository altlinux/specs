# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /osgi(org.apache.ant*/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:      jacoco
Version:   0.7.8
Release:   alt1_5jpp8
Summary:   Java Code Coverage for Eclipse 
Group:     System/Libraries
License:   EPL
URL:       http://www.eclemma.org/jacoco/
Source0:   https://github.com/jacoco/jacoco/archive/v%{version}.tar.gz
Source1:   EnchancedManifest.mf

BuildArch:        noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-tools-javadoc)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.jacoco:org.jacoco.build:pom:)
BuildRequires:  mvn(org.ow2.asm:asm-debug-all)
BuildRequires:  dos2unix
Source44: import.info


%description
JaCoCo is a free code coverage library for Java, 
which has been created by the EclEmma team based on the lessons learned 
from using and integration existing libraries over the last five years. 


%package    javadoc
Group: System/Libraries
Summary:    Java-docs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%package    maven-plugin
Group: System/Libraries
Summary:    A Jacoco plugin for maven

%description maven-plugin
A Jacoco plugin for maven.

%prep
%setup -q 

# Make it work with ASM 6.0
# TODO: forward upstream
sed -i '/org.objectweb.asm/s/version="[^"]*"/bundle-version="[5.1.0,7.0.0)"/' $(find -name \*.MF)

%pom_disable_module ../org.jacoco.examples org.jacoco.build
%pom_disable_module ../org.jacoco.doc org.jacoco.build
%pom_disable_module ../org.jacoco.tests org.jacoco.build
%pom_disable_module ../jacoco org.jacoco.build

%mvn_package ":jacoco-maven-plugin:{jar,pom}:{}:" maven-plugin
%mvn_package ":{org.}*:{jar,pom}:runtime:"

sed -i -e "s|nb-configuration.xml|nb-configuration.xml,build.xml, pom.xml|g" org.jacoco.build/pom.xml

# Remove problematic plugin, which old patch tried to correct, completely
%pom_remove_plugin org.codehaus.groovy.maven:gmaven-plugin ./org.jacoco.build/pom.xml

# Remove enforcer plugin that causes build failure of 'Jacoco :: Maven Plugin'
%pom_remove_plugin -f -r org.apache.maven.plugins:maven-enforcer-plugin

# Add execution config for maven.antrun.plugin
%pom_xpath_inject pom:plugin[pom:artifactId=\'maven-antrun-plugin\']/pom:executions '<execution>
             <id>parse-version</id>
             <phase>validate</phase>
             <goals>
               <goal>run</goal>
             </goals>
             <configuration>
                <target>
                     <property name="jacoco.runtime.package.name" value="org.jacoco.agent.rt.internal_${randomNumber}" />
               </target>
               <exportAntProperties>true</exportAntProperties>
             </configuration>
           </execution>' org.jacoco.build/pom.xml


%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

# workaround missing premain in agent.rt RH1151442. Not sure where to fix this in build.
# TODO, fix in build itself
# 'all' have already premain, 'sources' don't need.
a=`find org.jacoco.agent.rt/target/ | grep jar | grep -v -e sources -e all`
for x in $a ; do
jar -umf %{SOURCE1}  $x
done;

%install
%mvn_install

# ant config
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo %{name} %{name}/org.jacoco.ant objectweb-asm/asm-debug-all > %{buildroot}%{_sysconfdir}/ant.d/%{name}

%files -f .mfiles
%dir %{_javadir}/%{name}
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%doc org.jacoco.doc/docroot/*
%doc org.jacoco.doc/about.html

%files maven-plugin -f .mfiles-maven-plugin

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.8-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.8-alt1_4jpp8
- fc27 update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.8-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.7-alt1_2jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.6-alt1_1jpp8
- new version

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.5-alt1_2jpp8
- java 8 mass update

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

