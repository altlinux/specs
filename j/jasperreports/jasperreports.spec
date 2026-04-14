%define _unpackaged_files_terminate_build 1

Name: jasperreports
Version: 7.0.6
Release: alt1

Summary: Java reporting library (core module)
License: LGPL-3.0-or-later
Group: Development/Java
Url: https://github.com/Jaspersoft/jasperreports
Vcs: https://github.com/Jaspersoft/jasperreports.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: jpackage-17-compat
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: apache-commons-logging
BuildRequires: apache-commons-collections4
BuildRequires: jackson-core
BuildRequires: jackson-annotations
BuildRequires: jackson-databind
BuildRequires: jackson-dataformat-xml
BuildRequires: woodstox-core
BuildRequires: stax2-api
BuildRequires: batik
BuildRequires: batik-util
BuildRequires: xml-commons-apis
BuildRequires: apache-commons-beanutils
BuildRequires: apache-commons-lang3
BuildRequires: tascalate-javaflow
BuildRequires: icu4j
BuildRequires: metadata-extractor

%description
JasperReports is a Java reporting library. This package builds and ships
the core artifacts required for report compilation/fill/export pipelines.

%package project
Summary: Aggregator POM for JasperReports modules
Group: Development/Java

%description project
Aggregator POM artifact for JasperReports module dependency management.

%package parent
Summary: Parent POM for JasperReports modules
Group: Development/Java

%description parent
Parent POM shared by JasperReports reactor modules.

%package metadata
Summary: Metadata helper library for JasperReports
Group: Development/Java

%description metadata
Metadata helper classes and descriptors used by JasperReports modules.

%package annotation-processors
Summary: Annotation processors for JasperReports
Group: Development/Java

%description annotation-processors
Annotation processors used while compiling JasperReports modules.

%prep
%setup

# Build only core reactor and helper modules needed by core compilation.
%pom_disable_module core/pom-javaflow.xml
%pom_disable_module ext/fonts
%pom_disable_module ext/ant
%pom_disable_module ext/barbecue
%pom_disable_module ext/barcode4j
%pom_disable_module ext/castor
%pom_disable_module ext/charts
%pom_disable_module ext/chart-customizers
%pom_disable_module ext/chart-themes
%pom_disable_module ext/data-adapters
%pom_disable_module ext/data-adapters-http
%pom_disable_module ext/ejbql
%pom_disable_module ext/ejbql-j2ee
%pom_disable_module ext/excel-poi
%pom_disable_module ext/fastexcel
%pom_disable_module ext/functions
%pom_disable_module ext/groovy
%pom_disable_module ext/hibernate
%pom_disable_module ext/hibernate-j2ee
%pom_disable_module ext/javascript
%pom_disable_module ext/jaxen
%pom_disable_module ext/jdt
%pom_disable_module ext/json
%pom_disable_module ext/maven
%pom_disable_module ext/maven-bom
%pom_disable_module ext/olap
%pom_disable_module ext/pdf
%pom_disable_module ext/servlets
%pom_disable_module ext/servlets-j2ee
%pom_disable_module ext/spring
%pom_disable_module ext/xalan

# Drop network-oriented and non-essential plugins for distro builds.
%pom_remove_plugin -r -f org.codehaus.mojo:buildnumber-maven-plugin
%pom_remove_plugin -r -f org.codehaus.mojo:flatten-maven-plugin
%pom_remove_plugin -r -f org.owasp:dependency-check-maven
%pom_remove_plugin -r -f :maven-javadoc-plugin
%pom_remove_plugin -r -f :maven-source-plugin
%pom_remove_plugin -r -f :maven-site-plugin
%pom_remove_plugin -r -f :maven-deploy-plugin
%pom_remove_plugin -r -f :maven-install-plugin
%pom_remove_plugin -r -f :maven-release-plugin
%pom_remove_plugin -r -f :maven-enforcer-plugin
%pom_remove_plugin -r -f :maven-dependency-plugin
%pom_remove_plugin -r -f :maven-project-info-reports-plugin
%pom_remove_plugin -r -f net.tascalate.javaflow:net.tascalate.javaflow.tools.maven
%pom_remove_plugin -r -f com.google.code.maven-replacer-plugin:replacer

%pom_remove_plugin -f org.codehaus.mojo:buildnumber-maven-plugin pom-parent.xml
%pom_remove_plugin -f org.codehaus.mojo:flatten-maven-plugin pom-parent.xml
%pom_remove_plugin -f org.owasp:dependency-check-maven pom-parent.xml
%pom_remove_plugin -f org.apache.maven.plugins:maven-source-plugin pom-parent.xml
%pom_remove_plugin -f org.apache.maven.plugins:maven-site-plugin pom-parent.xml
%pom_remove_plugin -f org.apache.maven.plugins:maven-deploy-plugin pom-parent.xml
%pom_remove_plugin -f org.apache.maven.plugins:maven-install-plugin pom-parent.xml
%pom_remove_plugin -f org.apache.maven.plugins:maven-dependency-plugin pom-parent.xml
%pom_remove_plugin -f org.codehaus.mojo:clirr-maven-plugin pom-parent.xml
%pom_remove_plugin -f org.apache.maven.plugins:maven-javadoc-plugin core/pom-common.xml
%pom_remove_plugin -f org.apache.maven.plugins:maven-dependency-plugin core/pom-common.xml

# Parent package should not pull Maven plugin requirements from build metadata.
%pom_xpath_remove pom:build pom-parent.xml

# Rebind unavailable dependency to package present in sisyphus.
%pom_change_dep org.apache.commons:commons-beanutils2 org.apache.commons:commons-beanutils core/pom-common.xml
# Replace unresolved revision placeholders in all reactor POMs.
find . -type f -name 'pom*.xml' -print0 | \
  xargs -0 sed -i \
    -e 's/\${revision}/%version/g' \
    -e 's/\$revision/%version/g'

# Parent POM is outside reactor modules; register it explicitly.
%mvn_artifact --skip-dependencies pom-parent.xml

# Keep upstream imports untouched in git tree; rewrite only in build tree.
find core/src/main/java -type f -name '*.java' -print0 | \
  xargs -0 sed -i 's/org\.apache\.commons\.beanutils2/org.apache.commons.beanutils/g'

# Adapt JRDateLocaleConverter to beanutils 1.9.x API surface.
sed -i \
  -e 's/extends DateLocaleConverter<Date>/extends DateLocaleConverter/' \
  -e 's/super(null, null, null, false, false, false);/super(null, null, null, false);/' \
  -e 's/\<localizedPattern\>/locPattern/g' \
  core/src/main/java/net/sf/jasperreports/engine/util/JRDateLocaleConverter.java

# Install helper artifacts as dedicated subpackages.
%mvn_package :jasperreports-parent parent
%mvn_package :jasperreports-project project
%mvn_package :jasperreports-metadata metadata
%mvn_package :jasperreports-annotation-processors annotation-processors

%build
%mvn_build -s -f -j -- \
  -Ddependency-check.skip=true \
  -pl pom.xml,tools/metadata,tools/annotation-processors,core/pom.xml -am

%install
%mvn_install

%files -f .mfiles-jasperreports
%doc LICENSE README.md changes.txt

%files project -f .mfiles-project
%files parent -f .mfiles-parent
%files metadata -f .mfiles-metadata
%files annotation-processors -f .mfiles-annotation-processors

%changelog
* Mon Apr 13 2026 Ivan Khanas <xeno@altlinux.org> 7.0.6-alt1
- Initial core-focused package for ALT Linux.
