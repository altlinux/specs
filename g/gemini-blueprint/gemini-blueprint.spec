# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name gemini-blueprint
%define version 1.0.2
%global namedreltag .RELEASE
%global namedversion %{version}%{?namedreltag}
Name:          gemini-blueprint
Version:       1.0.2
Release:       alt1_2jpp7
Summary:       Reference Implementation of the OSGi Blueprint Service
Group:         Development/Java
# BSD file - test-support/src/main/java/org/eclipse/gemini/blueprint/test/internal/util/DependencyVisitor.java,
License:       ASL 2.0 and BSD and EPL
URL:           http://www.eclipse.org/gemini/
# https://github.com/glyn/Gemini-Blueprint
# git clone git://github.com/eclipse/gemini.blueprint gemini-blueprint-1.0.2.RELEASE
# (cd gemini-blueprint-1.0.2.RELEASE/ && git archive --format=tar --prefix=gemini-blueprint-1.0.2.RELEASE/ 1.0.2.RELEASE | xz > ../gemini-blueprint-1.0.2.RELEASE-src-git.tar.xz)
Source0:       %{name}-%{namedversion}-src-git.tar.xz
# add maven-{bundle,jar}-plugin configuration
Patch0:        %{name}-%{namedversion}-add-osgi-manifests.patch
BuildRequires: jpackage-utils

BuildRequires: aopalliance
BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: log4j
BuildRequires: slf4j
BuildRequires: springframework
BuildRequires: springframework-aop
BuildRequires: springframework-beans
BuildRequires: springframework-context
BuildRequires: springframework-context-support

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

# test deps
BuildRequires: easymock
BuildRequires: junit
BuildRequires: multithreadedtc
# BuildRequires: springframework-test

Requires:      aopalliance
Requires:      felix-osgi-compendium
Requires:      felix-osgi-core
Requires:      log4j
Requires:      slf4j
Requires:      springframework
Requires:      springframework-aop
Requires:      springframework-beans
Requires:      springframework-context
Requires:      springframework-context-support

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
Eclipse Gemini Blueprint project makes it
easy to build Java applications that run
in an OSGi framework. 
By using Gemini Blueprint, applications
benefit from using a better separation of
modules, the ability to dynamically add,
remove, and update modules in a running system,
the ability to deploy multiple versions of a
module simultaneously (and have clients
automatically bind to the appropriate one),
and a dynamic service model.

NOTE: Eclipse Gemini Blueprint can be considered the
successor of Spring DM (OSGi) 2.x (http://www.springsource.org/osgi).

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-bundle-plugin']/pom:configuration/pom:instructions" "<Bundle-Activator>org.eclipse.gemini.blueprint.extender.internal.boot.ChainActivator</Bundle-Activator>" extender


find . -name "*.class" -delete
find . -name "*.jar" -type f -delete

%pom_remove_plugin com.springsource.bundlor:com.springsource.bundlor.maven
%pom_remove_plugin :maven-clover2-plugin
%pom_remove_plugin :maven-antrun-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :jdepend-maven-plugin

# remove org.springframework.build.aws.maven
%pom_xpath_remove pom:extensions
# remove clover knopflerfish profiles (todo remove also eclipse/equinox and org.apache.felix profiles)
%pom_xpath_remove pom:profiles

sed -i "s|<groupId>org.aopalliance|<groupId>aopalliance|" pom.xml {core,extender}/pom.xml
sed -i "s|<artifactId>com.springsource.org.aopalliance|<artifactId>aopalliance|" pom.xml {core,extender}/pom.xml

sed -i "s|<groupId>org.junit</groupId>|<groupId>junit</groupId>|" pom.xml
sed -i "s|<artifactId>com.springsource.org.junit</artifactId>|<artifactId>junit</artifactId>|" pom.xml

# test deps
%pom_remove_dep log4j:log4j
# build deps
sed -i "s|<groupId>org.apache.log4j</groupId>|<groupId>log4j</groupId>|" pom.xml
sed -i "s|<artifactId>com.springsource.org.apache.log4j</artifactId>|<artifactId>log4j</artifactId>|" pom.xml

sed -i "s|<groupId>multithreadedtc</groupId>|<groupId>edu.umd.cs.mtc</groupId>|" core/pom.xml

%pom_remove_dep org.springframework:spring-test
%pom_remove_dep org.springframework:spring-test core

# require org.springframework:org.springframework.test*
rm -r core/src/test/java/org/eclipse/gemini/blueprint/internal/util/BeanFactoryUtilsTest.java \
  core/src/test/java/org/eclipse/gemini/blueprint/DictionaryEditorTest.java

# TODO require:
# org.springframework spring-test
# org.knopflerfish framework
# org.apache.felix org.apache.felix.main
# org.eclipse.osgi org.eclipse.osgi
%pom_disable_module test-support
%pom_remove_dep org.eclipse.gemini.blueprint:gemini-blueprint-test

# Fix CRLF
sed 's/\r//' -i changelog.txt license-apache.txt readme-building.txt readme.txt

%build
# some test fails for unavailable build deps*
mvn-rpmbuild -Dproject.build.sourceEncoding=UTF-8 -Dmaven.test.failure.ignore=true install javadoc:aggregate

%install

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml  %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom

mkdir -p %{buildroot}%{_javadir}/%{name}
# TODO test-support
for m in core extender mock io; do
    install -m 644 ${m}/target/%{name}-${m}-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/%{name}-${m}.jar
    install -pm 644 ${m}/pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
%add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}-*.jar
%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%{_mavenpomdir}/JPP.%{name}-%{name}-*.pom
%{_mavendepmapfragdir}/%{name}
%doc about.html changelog.txt epl-v10.html license-apache.txt notice.html readme-building.txt readme.txt

%files javadoc
%{_javadocdir}/%{name}
%doc epl-v10.html license-apache.txt notice.html

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_2jpp7
- new release

