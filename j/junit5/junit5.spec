Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 5.7.1
%bcond_with bootstrap

# Component versions, taken from gradle.properties
%global platform_version 1.%(v=%{version}; echo ${v:2})
%global jupiter_version %{version}
%global vintage_version %{version}

Name:           junit5
Version:        5.7.1
Release:        alt1_3jpp11
Summary:        Java regression testing framework
License:        EPL-2.0
URL:            https://junit.org/junit5/
BuildArch:      noarch

Source0:        https://github.com/junit-team/junit5/archive/r%{version}/junit5-%{version}.tar.gz

# Aggregator POM (used for packaging only)
Source100:      aggregator.pom
# Platform POMs
Source200:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-commons/%{platform_version}/junit-platform-commons-%{platform_version}.pom
Source201:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console/%{platform_version}/junit-platform-console-%{platform_version}.pom
Source202:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/%{platform_version}/junit-platform-console-standalone-%{platform_version}.pom
Source203:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-engine/%{platform_version}/junit-platform-engine-%{platform_version}.pom
Source205:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-launcher/%{platform_version}/junit-platform-launcher-%{platform_version}.pom
Source206:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-runner/%{platform_version}/junit-platform-runner-%{platform_version}.pom
Source207:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-suite-api/%{platform_version}/junit-platform-suite-api-%{platform_version}.pom
Source208:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-reporting/%{platform_version}/junit-platform-reporting-%{platform_version}.pom
Source209:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-testkit/%{platform_version}/junit-platform-testkit-%{platform_version}.pom
# Jupiter POMs
Source300:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter/%{jupiter_version}/junit-jupiter-%{jupiter_version}.pom
Source301:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-api/%{jupiter_version}/junit-jupiter-api-%{jupiter_version}.pom
Source302:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-engine/%{jupiter_version}/junit-jupiter-engine-%{jupiter_version}.pom
Source303:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-migrationsupport/%{jupiter_version}/junit-jupiter-migrationsupport-%{jupiter_version}.pom
Source304:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-params/%{jupiter_version}/junit-jupiter-params-%{jupiter_version}.pom
Source305:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter/%{jupiter_version}/junit-jupiter-%{jupiter_version}.pom
# Vintage POM
Source400:      https://repo1.maven.org/maven2/org/junit/vintage/junit-vintage-engine/%{vintage_version}/junit-vintage-engine-%{vintage_version}.pom
# BOM POM
Source500:      https://repo1.maven.org/maven2/org/junit/junit-bom/%{version}/junit-bom-%{version}.pom

BuildRequires:  asciidoc asciidoc-a2x
BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(com.univocity:univocity-parsers)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.opentest4j:opentest4j)
%endif
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

cp -p %{SOURCE100} pom.xml
cp -p %{SOURCE200} junit-platform-commons/pom.xml
cp -p %{SOURCE201} junit-platform-console/pom.xml
cp -p %{SOURCE202} junit-platform-console-standalone/pom.xml
cp -p %{SOURCE203} junit-platform-engine/pom.xml
cp -p %{SOURCE205} junit-platform-launcher/pom.xml
cp -p %{SOURCE206} junit-platform-runner/pom.xml
cp -p %{SOURCE207} junit-platform-suite-api/pom.xml
cp -p %{SOURCE208} junit-platform-reporting/pom.xml
cp -p %{SOURCE209} junit-platform-testkit/pom.xml
cp -p %{SOURCE300} junit-jupiter/pom.xml
cp -p %{SOURCE301} junit-jupiter-api/pom.xml
cp -p %{SOURCE302} junit-jupiter-engine/pom.xml
cp -p %{SOURCE303} junit-jupiter-migrationsupport/pom.xml
cp -p %{SOURCE304} junit-jupiter-params/pom.xml
cp -p %{SOURCE305} junit-jupiter/pom.xml
cp -p %{SOURCE400} junit-vintage-engine/pom.xml
cp -p %{SOURCE500} junit-bom/pom.xml

for pom in $(find -mindepth 2 -name pom.xml); do
    # Set parent to aggregator
    %pom_xpath_inject pom:project "<parent><groupId>org.fedoraproject.xmvn.junit5</groupId><artifactId>aggregator</artifactId><version>1.0.0</version></parent>" $pom
    # OSGi BSN
    bsn=$(sed 's|/pom.xml$||;s|.*/|org.|;s|-|.|g' <<<"$pom")
    %pom_xpath_inject pom:project "<properties><osgi.bsn>${bsn}</osgi.bsn></properties>" $pom
    # Incorrect scope - API guardian is just annotation, needed only during compilation
    %pom_xpath_set -f "pom:dependency[pom:artifactId='apiguardian-api']/pom:scope" provided $pom
done

%pom_remove_parent junit-bom

# Add deps which are shaded by upstream and therefore not present in POMs.
%pom_add_dep net.sf.jopt-simple:jopt-simple:5.0.4 junit-platform-console
%pom_add_dep com.univocity:univocity-parsers:2.5.4 junit-jupiter-params

# Disable the console modules
%pom_disable_module junit-platform-console
%pom_disable_module junit-platform-console-standalone

%mvn_package :aggregator __noinstall

%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

# Build docs.  Ignore exit asciidoc -- it fails for some reason, but
# still produces readable docs.
asciidoc documentation/src/docs/asciidoc/index.adoc || :
ln -s ../../javadoc/junit5 documentation/src/docs/api

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.md LICENSE-notice.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.md LICENSE-notice.md

%files guide
%doc --no-dereference documentation/src/docs/*

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 5.7.1-alt1_3jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 5.7.1-alt1_1jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 5.6.2-alt1_4jpp11
- new version

* Sat May 29 2021 Igor Vlasenko <viy@altlinux.org> 5.5.2-alt2_2jpp11
- fixed build

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 5.5.2-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 5.4.2-alt1_2jpp8
- new version

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 5.4.0-alt1_1jpp8
- new version

* Tue Jun 18 2019 Igor Vlasenko <viy@altlinux.ru> 5.3.1-alt1_1jpp8
- new version

* Sat Jun 02 2018 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_3jpp8
- new version

