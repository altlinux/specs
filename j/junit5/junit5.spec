%define version 5.14.4

# Component versions, taken from gradle.properties
%global platform_version 1.%(v=%{version}; echo ${v:2})
%global jupiter_version %{version}
%global vintage_version %{version}

Name:           junit5
Version:        5.14.4
Release:        alt1

Summary:        The programmer-friendly testing framework for Java and the JVM
License:        EPL-2.0
Group:          Development/Java
URL:            https://docs.junit.org/5.0.0/user-guide/
VCS:            https://github.com/junit-team/junit-framework

Source0:        %name-%version.tar

# Aggregator POM (used for packaging only)
Source100:      aggregator.pom
# Platform POMs
Source200:      junit-platform-commons-%platform_version.pom
Source201:      junit-platform-console-%platform_version.pom
Source202:      junit-platform-console-standalone-%platform_version.pom
Source203:      junit-platform-engine-%platform_version.pom
Source205:      junit-platform-launcher-%platform_version.pom
Source206:      junit-platform-runner-%platform_version.pom
Source207:      junit-platform-suite-api-%platform_version.pom
Source209:      junit-platform-testkit-%platform_version.pom
Source210:      junit-platform-suite-commons-%platform_version.pom
# Jupiter POMs
Source300:      junit-jupiter-%jupiter_version.pom
Source301:      junit-jupiter-api-%jupiter_version.pom
Source302:      junit-jupiter-engine-%jupiter_version.pom
Source303:      junit-jupiter-migrationsupport-%jupiter_version.pom
Source304:      junit-jupiter-params-%jupiter_version.pom
# Vintage POM
Source400:      junit-vintage-engine-%vintage_version.pom
# BOM POM
Source500:      junit-bom-%version.pom

Patch0:         0001-Add-JRE-class-generated-from-template.patch
Patch1:         0002-Drop-transitive-requirement-on-apiguardian.patch
Patch2:         0003-Add-missing-module-static-requires.patch
Patch3:         0004-Remove-legacy-XML-console-support.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-17-compat

BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(com.univocity:univocity-parsers)
BuildRequires:  mvn(info.picocli:picocli)

BuildArch: noarch

Obsoletes:      %name-guide < 5.10.2-alt2

%description
JUnit is a popular regression testing framework for Java platform.

%prep
%setup
%autopatch -p1

cp -p %SOURCE100 pom.xml
cp -p %SOURCE200 junit-platform-commons/pom.xml
cp -p %SOURCE201 junit-platform-console/pom.xml
cp -p %SOURCE202 junit-platform-console-standalone/pom.xml
cp -p %SOURCE203 junit-platform-engine/pom.xml
cp -p %SOURCE205 junit-platform-launcher/pom.xml
cp -p %SOURCE206 junit-platform-runner/pom.xml
cp -p %SOURCE207 junit-platform-suite-api/pom.xml
cp -p %SOURCE209 junit-platform-testkit/pom.xml
cp -p %SOURCE210 junit-platform-suite-commons/pom.xml
cp -p %SOURCE300 junit-jupiter/pom.xml
cp -p %SOURCE301 junit-jupiter-api/pom.xml
cp -p %SOURCE302 junit-jupiter-engine/pom.xml
cp -p %SOURCE303 junit-jupiter-migrationsupport/pom.xml
cp -p %SOURCE304 junit-jupiter-params/pom.xml
cp -p %SOURCE400 junit-vintage-engine/pom.xml
cp -p %SOURCE500 junit-bom/pom.xml

for pom in $(find -mindepth 2 -name pom.xml); do
	%pom_add_parent org.fedoraproject.xmvn.junit5:aggregator:any $pom
	bsn=org.${pom//-/.}
        %pom_xpath_inject pom:project "<properties><osgi.bsn>${bsn}</osgi.bsn></properties>" $pom
	%pom_xpath_set -f "pom:dependency[pom:artifactId='apiguardian-api']/pom:scope" provided $pom
	%pom_xpath_set -f "pom:dependency[pom:scope='runtime']/pom:scope" compile $pom
done

%pom_remove_parent junit-bom

%pom_add_dep org.junit.platform:junit-platform-commons:%platform_version junit-platform-console
%pom_add_dep org.junit.platform:junit-platform-launcher:%platform_version junit-platform-console
%pom_add_dep info.picocli:picocli junit-platform-console
%pom_add_dep com.univocity:univocity-parsers:2.5.4 junit-jupiter-params

%pom_disable_module junit-platform-console-standalone
%pom_remove_dep org.junit.platform:junit-platform-reporting junit-platform-console

cp -pr junit-platform-console/src/main/java9/* junit-platform-console/src/main/java/

%mvn_package :junit-bom
%mvn_package :aggregator __noinstall

%build
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%doc *.md

%changelog
* Thu Aug 27 2026 Evgeniy Serov <scala@altlinux.org> 5.14.4-alt1
- Updated to 5.14.4.

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

