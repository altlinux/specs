Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Component versions, taken from gradle.properties
%global platform_version 1.0.0
%global jupiter_version 5.0.0
%global vintage_version 4.12.0

# Build with or without Gradle plugin.
# NOTE: We are always building junit5 using Maven.
# Turned off by default as it's not compatible with current gradle
%bcond_with gradle

Name:           junit5
Version:        5.0.0
Release:        alt1_3jpp8
Summary:        Java regression testing framework
# junit-platform-surefire-provider is under ASL 2.0, all other modules use EPL (see LICENSE.md)
License:        EPL and ASL 2.0
URL:            http://junit.org/junit5/
BuildArch:      noarch

Source0:        https://github.com/junit-team/junit5/archive/r%{version}.tar.gz

# Aggregator POM (used for packaging only)
Source100:      aggregator.pom
# Platform POMs
Source200:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-commons/%{platform_version}/junit-platform-commons-%{platform_version}.pom
Source201:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console/%{platform_version}/junit-platform-console-%{platform_version}.pom
Source202:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/%{platform_version}/junit-platform-console-standalone-%{platform_version}.pom
Source203:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-engine/%{platform_version}/junit-platform-engine-%{platform_version}.pom
Source204:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-gradle-plugin/%{platform_version}/junit-platform-gradle-plugin-%{platform_version}.pom
Source205:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-launcher/%{platform_version}/junit-platform-launcher-%{platform_version}.pom
Source206:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-runner/%{platform_version}/junit-platform-runner-%{platform_version}.pom
Source207:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-suite-api/%{platform_version}/junit-platform-suite-api-%{platform_version}.pom
Source208:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-surefire-provider/%{platform_version}/junit-platform-surefire-provider-%{platform_version}.pom
# Jupiter POMs
Source301:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-api/%{jupiter_version}/junit-jupiter-api-%{jupiter_version}.pom
Source302:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-engine/%{jupiter_version}/junit-jupiter-engine-%{jupiter_version}.pom
Source303:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-migrationsupport/%{jupiter_version}/junit-jupiter-migrationsupport-%{jupiter_version}.pom
Source304:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-params/%{jupiter_version}/junit-jupiter-params-%{jupiter_version}.pom
# Vintage POM
Source400:      https://repo1.maven.org/maven2/org/junit/vintage/junit-vintage-engine/%{vintage_version}/junit-vintage-engine-%{vintage_version}.pom

BuildRequires:  maven-local
BuildRequires:  mvn(com.univocity:univocity-parsers)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sf.jopt-simple:jopt-simple)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.surefire:common-java5)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-api)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.opentest4j:opentest4j)

%if %{with gradle}
BuildRequires:  mvn(org.codehaus.gmavenplus:gmavenplus-plugin)
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
BuildRequires:  mvn(org.gradle:gradle-base-services)
BuildRequires:  mvn(org.gradle:gradle-base-services-groovy)
BuildRequires:  mvn(org.gradle:gradle-core)
BuildRequires:  mvn(org.gradle:gradle-language-jvm)
BuildRequires:  mvn(org.gradle:gradle-model-core)
BuildRequires:  mvn(org.gradle:gradle-platform-base)
BuildRequires:  mvn(org.gradle:gradle-platform-jvm)
BuildRequires:  mvn(org.gradle:gradle-plugins)
BuildRequires:  mvn(org.gradle:gradle-reporting)
BuildRequires:  mvn(org.gradle:gradle-testing-base)
BuildRequires:  mvn(org.gradle:gradle-testing-jvm)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%endif

BuildRequires:  asciidoc asciidoc-a2x
Source44: import.info

%description
JUnit is a popular regression testing framework for Java platform.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Junit5 API documentation.

%package guide
Group: Development/Java
Summary:        Documentation for %{name}
Requires:       %{name}-javadoc = %{version}-%{release}

%description guide
JUnit 5 User Guide.

%prep
%setup -q -n %{name}-r%{version}
find -name \*.jar -delete

cp -p junit-jupiter-api/LICENSE.md LICENSE-Eclipse.md
cp -p junit-platform-surefire-provider/LICENSE.md LICENSE-Apache.md

cp -p %{SOURCE100} pom.xml
cp -p %{SOURCE200} junit-platform-commons/pom.xml
cp -p %{SOURCE201} junit-platform-console/pom.xml
cp -p %{SOURCE202} junit-platform-console-standalone/pom.xml
cp -p %{SOURCE203} junit-platform-engine/pom.xml
cp -p %{SOURCE204} junit-platform-gradle-plugin/pom.xml
cp -p %{SOURCE205} junit-platform-launcher/pom.xml
cp -p %{SOURCE206} junit-platform-runner/pom.xml
cp -p %{SOURCE207} junit-platform-suite-api/pom.xml
cp -p %{SOURCE208} junit-platform-surefire-provider/pom.xml
cp -p %{SOURCE301} junit-jupiter-api/pom.xml
cp -p %{SOURCE302} junit-jupiter-engine/pom.xml
cp -p %{SOURCE303} junit-jupiter-migrationsupport/pom.xml
cp -p %{SOURCE304} junit-jupiter-params/pom.xml
cp -p %{SOURCE400} junit-vintage-engine/pom.xml

for pom in $(find -mindepth 2 -name pom.xml); do
    # Set parent to aggregator
    %pom_xpath_inject pom:project "<parent><groupId>org.fedoraproject.xmvn.junit5</groupId><artifactId>aggregator</artifactId><version>1.0.0</version></parent>" $pom
    # OSGi BSN
    bsn=$(sed 's|/pom.xml$||;s|.*/|org.|;s|-|.|g' <<<"$pom")
    %pom_xpath_inject pom:project "<properties><osgi.bsn>${bsn}</osgi.bsn></properties>" $pom
    # Incorrect scope - API guardian is just annotation, needed only during compilation
    %pom_xpath_set -r "pom:dependency[pom:artifactId='apiguardian-api']/pom:scope" provided $pom
done

# Add deps which are shaded by upstream and therefore not present in POMs.
%pom_add_dep net.sf.jopt-simple:jopt-simple:5.0.4 junit-platform-console
%pom_add_dep com.univocity:univocity-parsers:2.5.4 junit-jupiter-params

# Incorrect scope - whoever needs Surefire provider will have to depend on Surefire.
%pom_xpath_set "pom:dependency[pom:groupId='org.apache.maven.surefire']/pom:scope" provided junit-platform-surefire-provider

# Incorrect scope - Junit4 is needed for compilation too, not only runtime.
%pom_xpath_set "pom:dependency[pom:artifactId='junit']/pom:scope" compile junit-vintage-engine

%if %{with gradle}

# Gradle plugin is written in Groovy, so compile it with GMavenPlus.
%pom_xpath_inject pom:project "<build><plugins><plugin><groupId>org.codehaus.gmavenplus</groupId><artifactId>gmavenplus-plugin</artifactId><version>1.6</version><executions><execution><goals><goal>compile</goal></goals></execution></executions></plugin></plugins></build>" junit-platform-gradle-plugin

# Gradle deps are only for compilation, and therefore not included in POM.
%pom_add_dep org.codehaus.groovy:groovy-all::provided junit-platform-gradle-plugin
%pom_add_dep org.gradle:gradle-base-services-groovy::provided junit-platform-gradle-plugin
%pom_add_dep org.gradle:gradle-base-services::provided junit-platform-gradle-plugin
%pom_add_dep org.gradle:gradle-core::provided junit-platform-gradle-plugin
%pom_add_dep org.gradle:gradle-language-jvm::provided junit-platform-gradle-plugin
%pom_add_dep org.gradle:gradle-model-core::provided junit-platform-gradle-plugin
%pom_add_dep org.gradle:gradle-platform-base::provided junit-platform-gradle-plugin
%pom_add_dep org.gradle:gradle-platform-jvm::provided junit-platform-gradle-plugin
%pom_add_dep org.gradle:gradle-plugins::provided junit-platform-gradle-plugin
%pom_add_dep org.gradle:gradle-reporting::provided junit-platform-gradle-plugin
%pom_add_dep org.gradle:gradle-testing-base::provided junit-platform-gradle-plugin
%pom_add_dep org.gradle:gradle-testing-jvm::provided junit-platform-gradle-plugin
%pom_add_dep org.slf4j:slf4j-api::provided junit-platform-gradle-plugin

%else
%pom_disable_module junit-platform-gradle-plugin
%endif

%mvn_package :aggregator __noinstall

%build
%mvn_build -f

# Build docs.  Ignore exit asciidoc -- it fails for some reason, but
# still produces readable docs.
asciidoc documentation/src/docs/asciidoc/index.adoc || :
ln -s ../../javadoc/junit5 documentation/src/docs/api

%install
%mvn_install

%jpackage_script org/junit/platform/console/ConsoleLauncher "" "" junit5:junit:opentest4j:jopt-simple %{name} true

%files -f .mfiles
%{_bindir}/%{name}
%doc --no-dereference LICENSE.md LICENSE-Eclipse.md LICENSE-Apache.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.md LICENSE-Eclipse.md LICENSE-Apache.md

%files guide
%doc --no-dereference documentation/src/docs/*

%changelog
* Sat Jun 02 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_3jpp8
- new version

