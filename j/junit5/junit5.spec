%define version 5.10.2

# Component versions, taken from gradle.properties
%global platform_version 1.%(v=%{version}; echo ${v:2})
%global jupiter_version %{version}
%global vintage_version %{version}

Name: junit5
Version: 5.10.2
Release: alt2
Summary: Java regression testing framework
License: EPL-2.0
Group: Development/Java
URL: https://junit.org/junit5/
BuildArch: noarch

Source0: r%{version}.tar.gz

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
Source209:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-testkit/%{platform_version}/junit-platform-testkit-%{platform_version}.pom
Source210:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-suite-commons/%{platform_version}/junit-platform-suite-commons-%{platform_version}.pom
# Jupiter POMs
Source300:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter/%{jupiter_version}/junit-jupiter-%{jupiter_version}.pom
Source301:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-api/%{jupiter_version}/junit-jupiter-api-%{jupiter_version}.pom
Source302:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-engine/%{jupiter_version}/junit-jupiter-engine-%{jupiter_version}.pom
Source303:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-migrationsupport/%{jupiter_version}/junit-jupiter-migrationsupport-%{jupiter_version}.pom
Source304:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-params/%{jupiter_version}/junit-jupiter-params-%{jupiter_version}.pom
# Vintage POM
Source400:      https://repo1.maven.org/maven2/org/junit/vintage/junit-vintage-engine/%{vintage_version}/junit-vintage-engine-%{vintage_version}.pom
# BOM POM
Source500:      https://repo1.maven.org/maven2/org/junit/junit-bom/%{version}/junit-bom-%{version}.pom

BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-17-compat
BuildRequires: asciidoc asciidoc-a2x
BuildRequires: maven-local
BuildRequires: mvn(com.univocity:univocity-parsers)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apiguardian:apiguardian-api)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.opentest4j:opentest4j)
BuildRequires: maven-shade-plugin
BuildRequires: maven-antrun-plugin

%description
JUnit is a popular regression testing framework for Java platform.

%package guide
Group: Development/Java
Summary: Documentation for %{name}

%description guide
JUnit 5 User Guide.

%prep
%setup -n %{name}-r%{version}

cp -p %{SOURCE100} pom.xml
cp -p %{SOURCE200} junit-platform-commons/pom.xml
cp -p %{SOURCE201} junit-platform-console/pom.xml
cp -p %{SOURCE202} junit-platform-console-standalone/pom.xml
cp -p %{SOURCE203} junit-platform-engine/pom.xml
cp -p %{SOURCE205} junit-platform-launcher/pom.xml
cp -p %{SOURCE206} junit-platform-runner/pom.xml
cp -p %{SOURCE207} junit-platform-suite-api/pom.xml
cp -p %{SOURCE209} junit-platform-testkit/pom.xml
cp -p %{SOURCE210} junit-platform-suite-commons/pom.xml
cp -p %{SOURCE300} junit-jupiter/pom.xml
cp -p %{SOURCE301} junit-jupiter-api/pom.xml
cp -p %{SOURCE302} junit-jupiter-engine/pom.xml
cp -p %{SOURCE303} junit-jupiter-migrationsupport/pom.xml
cp -p %{SOURCE304} junit-jupiter-params/pom.xml
cp -p %{SOURCE400} junit-vintage-engine/pom.xml
cp -p %{SOURCE500} junit-bom/pom.xml

rm -f ./platform-tests/src/test/resources/listeners/uidtracking/maven/pom.xml
for pom in $(find -mindepth 2 -name pom.xml); do
    # Set parent to aggregator
	%pom_add_parent org.fedoraproject.xmvn.junit5:aggregator:any $pom
    #pom_xpath_inject pom:project "<parent><groupId>org.fedoraproject.xmvn.junit5</groupId><artifactId>aggregator</artifactId><version>1.0.0</version></parent>" $pom
    # OSGi BSN
    #bsn=$(sed 's|/pom.xml$||;s|.*/|org.|;s|-|.|g' <<<"$pom")
	bsn=org.${pom//-/.}
    %pom_xpath_inject pom:project "<properties><osgi.bsn>${bsn}</osgi.bsn></properties>" $pom
    # Incorrect scope - API guardian is just annotation, needed only during compilation
	%pom_xpath_set -f "pom:dependency[pom:artifactId='apiguardian-api']/pom:scope" provided $pom
	%pom_xpath_set -f "pom:dependency[pom:scope='runtime']/pom:scope" compile $pom
done

%pom_remove_parent junit-bom

# Add deps which are shaded by upstream and therefore not present in POMs.
%pom_add_dep net.sf.jopt-simple:jopt-simple:5.0.4 junit-platform-console

# Add apiguardian to compile classpath for compiling junit-jupiter module.
%pom_add_dep org.apiguardian:apiguardian-api:compile junit-jupiter

# Fix module-info.java for junit-jupiter-params to include univocity.parsers dependency
rm junit-jupiter-params/src/module/org.junit.jupiter.params/module-info.java

# Disable the console modules
%pom_disable_module junit-platform-console
%pom_disable_module junit-platform-console-standalone

%mvn_package :aggregator __noinstall

#rm junit-platform-testkit/src/module/org.junit.platform.testkit/module-info.java

%build
%mvn_build -f -j
ln -s ../../javadoc/junit5 documentation/src/docs/api

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.md LICENSE-notice.md

%files guide
%doc --no-dereference documentation/src/docs/*

%changelog
* Mon Nov 17 2025 Ivan Khanas <xeno@altlinux.org> 5.10.2-alt2
- Add JPMS support for all modules except platform-testkit and params.

* Sat Jul 26 2025 Andrey Cherepanov <cas@altlinux.org> 5.10.2-alt1
- New version.

* Tue May 06 2025 Anton Meleshnikov <alton@altlinux.org> 5.8.2-alt1
- New version 5.8.2 (thanks fedora for the spec).

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

