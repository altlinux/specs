%define _unpackaged_files_terminate_build 1

Name: unit-api
Version: 2.2
Release: alt1

Summary: Units of Measurement Java API
License: BSD-3-Clause
Group: Development/Java
URL: https://github.com/unitsofmeasurement/unit-api
VCS: https://github.com/unitsofmeasurement/unit-api.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: mvn(tech.uom:uom-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(jakarta.inject:jakarta.inject-api)

%description
Units of Measurement defines quantities, units, prefixes and converters
with a service-provider interface for unit systems and quantity factories.

%prep
%setup
%pom_xpath_inject pom:project "<version>%version</version>"
%pom_set_parent tech.uom:uom-parent:2.2.5
# Preserve the genuine parent build model, not XMvn's reduced system model.
install -D -m 644 %_mavenpomdir/uom-parent/uom-parent.pom .parent/pom.xml
%pom_xpath_inject pom:parent "<relativePath>.parent/pom.xml</relativePath>"
%pom_remove_plugin com.mycila:license-maven-plugin
%pom_remove_plugin net.revelc.code:formatter-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%changelog
* Fri Nov 06 2026 Ivan Khanas <xeno@altlinux.org> 2.2-alt1
- Initial build for ALT.
