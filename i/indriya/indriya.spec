%define _unpackaged_files_terminate_build 1

Name: indriya
Version: 2.2.4
Release: alt1

Summary: Units of Measurement reference implementation
License: BSD-3-Clause
Group: Development/Java
URL: https://github.com/unitsofmeasurement/indriya
VCS: https://github.com/unitsofmeasurement/indriya.git
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-system.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(tech.uom:uom-parent:pom:)
BuildRequires: mvn(jakarta.inject:jakarta.inject-api)
BuildRequires: mvn(javax.measure:unit-api)
BuildRequires: mvn(tech.uom.lib:uom-lib-common)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: mvn(org.apiguardian:apiguardian-api)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.hamcrest:hamcrest-library)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)

%description
Indriya implements JSR 385 Units of Measurement, including quantities,
units, conversions, formatting and measurement services.

%prep
%setup
%autopatch -p1
%pom_xpath_inject pom:project "<version>%version</version>"
%pom_set_parent tech.uom:uom-parent:2.2.5
# Preserve the genuine parent build model, not XMvn's reduced system model.
install -D -m 644 %_mavenpomdir/uom-parent/uom-parent.pom .parent/pom.xml
%pom_xpath_inject pom:parent "<relativePath>.parent/pom.xml</relativePath>"
%pom_remove_plugin com.mycila:license-maven-plugin
# One installed JDK emits each original release-specific source set.
%pom_remove_plugin org.apache.maven.plugins:maven-toolchains-plugin
%pom_xpath_remove "//pom:jdkToolchain"
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
# The library has no OSGi API references; retain the bundle manifest plugin.
%pom_remove_dep org.osgi:org.osgi.core
%pom_remove_dep org.osgi:org.osgi.compendium
%pom_remove_dep org.osgi:org.osgi.annotation
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
# The unused JUnit4 runner bridge blocks Surefire's Jupiter provider.
%pom_remove_dep org.junit.platform:junit-platform-runner
# Preserve original JUnit4 assertion/helper imports without the runner bridge.
%pom_add_dep junit:junit:4.13.2:test
# Keep the active profile strict and use the declared build JDK normally.
%pom_xpath_set "//pom:testFailureIgnore" false
%pom_xpath_remove "//pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration/pom:jvm"
# JaCoCo can populate this property; system XMvn may skip coverage tooling.
%pom_xpath_inject pom:properties "<argLine></argLine>"
%pom_xpath_set "/pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration/pom:argLine" "@{argLine} --enable-preview -Xms64m -Xmx1g"
%pom_xpath_set "//pom:profile[pom:id='test-toolchains-bypass']//pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration/pom:argLine" "@{argLine} --enable-preview -Xmx1g"
%pom_add_dep_mgmt jakarta.inject:jakarta.inject-api:2.0.1

%build
%mvn_build -j -- -DfailIfNoTests=true

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 2.2.4-alt1
- Initial build for ALT.
