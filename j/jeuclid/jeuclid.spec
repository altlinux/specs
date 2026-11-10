%define _unpackaged_files_terminate_build 1
%def_with check

Name: jeuclid
Version: 3.1.14
Release: alt1
Epoch: 2

Summary: A complete MathML rendering solution
License: Apache-2.0 AND MIT AND ISO-permission AND W3C AND W3C-19980720 AND Unicode-3.0
Group: Development/Java
Url: https://github.com/rototor/jeuclid/
VCS: https://github.com/rototor/jeuclid.git
BuildArch: noarch

Source: %name-%version.tar
Source1: Smoke.java
Source2: Unicode-LICENSE.txt
Patch: %name-%version-alt.patch

Requires: fontconfig fonts-ttf-dejavu

BuildRequires(pre): rpm-macros-java rpm-build-java
BuildRequires: /proc
BuildRequires: maven-local jpackage-17-compat
BuildRequires: maven-plugin-bundle maven-javadoc-plugin
BuildRequires: ant batik xmlgraphics-commons apache-commons-logging jsr-305
BuildRequires: mvn(org.apache.xmlgraphics:fop)

%if_with check
BuildRequires: mvn(junit:junit)
BuildRequires: fontconfig fonts-ttf-dejavu xvfb-run
%endif

%description
JEuclid provides MathML rendering and document handling for Java.

%package fop
Summary: Apache FOP integration for JEuclid
License: Apache-2.0
Group: Development/Java

Requires: jeuclid = %EVR

%description fop
Apache FOP integration for rendering MathML expressions with JEuclid.

%package javadoc
Summary: API documentation for JEuclid
License: Apache-2.0 AND GPL-2.0-only WITH Classpath-exception-2.0 AND MIT
Group: Development/Documentation

%description javadoc
API documentation for the JEuclid library and Apache FOP integration.

%prep
%setup
%autopatch -p1
cp -p %SOURCE2 Unicode-LICENSE.txt

# The build-tools extension contains site/checkstyle assets only.
%pom_xpath_remove pom:build/pom:extensions
# The WAR is a test browser/site, not the core JUnit regression tests.
%pom_disable_module jeuclid-testsuite

# Signing, staging, site publication and source JARs are release tasks.
%pom_remove_plugin -r -f :maven-gpg-plugin
%pom_remove_plugin -r -f :nexus-staging-maven-plugin
%pom_remove_plugin -r -f :maven-site-plugin
%pom_remove_plugin -r -f :maven-source-plugin

# This optional optimization serializes dictionaries; runtime can read XML.
%pom_remove_plugin :gmaven-plugin jeuclid-core

%pom_xpath_set -r "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" 1.8
%pom_xpath_set -r "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" 1.8
# Do not retrieve external API indexes during an offline documentation build.
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:configuration/pom:links"
# The legacy parallel mode has no thread count; run the regression tests serially.
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration/pom:parallel"
# Enable the AWT regression tests under Xvfb in the check section.
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration/pom:systemProperties/pom:property[pom:name='java.awt.headless']/pom:value" false

# FreeHEP is optional and unavailable in the builder's repository.
# Keep Batik SVG and ImageIO export; the PDF test checks backend availability.
rm jeuclid-core/src/main/java/net/sourceforge/jeuclid/converter/FreeHep*.java
sed -i '/FreeHepDetector/d' jeuclid-core/src/main/resources/META-INF/services/net.sourceforge.jeuclid.converter.ConverterDetector
%pom_remove_dep org.freehep:freehep-graphicsio-emf jeuclid-core
%pom_remove_dep org.freehep:freehep-graphicsio-pdf jeuclid-core
%pom_remove_dep org.freehep:freehep-graphicsio-ps jeuclid-core
%pom_remove_dep org.freehep:freehep-graphicsio-svg jeuclid-core
%pom_remove_dep org.freehep:freehep-graphicsio-swf jeuclid-core

%if_without check
%pom_remove_dep junit:junit
%endif

%mvn_package :::javadoc: javadoc
%mvn_package :jeuclid-parent jeuclid
%mvn_package :jeuclid-core jeuclid
%mvn_package :jeuclid-fop fop
# Upstream moved the original coordinates to de.rototor.jeuclid.
%mvn_alias :jeuclid-parent net.sourceforge.jeuclid:jeuclid-parent
%mvn_alias :jeuclid-core net.sourceforge.jeuclid:jeuclid-core
%mvn_alias :jeuclid-fop net.sourceforge.jeuclid:jeuclid-fop
%mvn_file :jeuclid-core jeuclid/jeuclid-core jeuclid jeuclid-core
%mvn_file :jeuclid-fop jeuclid/jeuclid-fop

%build
%mvn_build -- -Dmaven.test.skip=true -Dmaven.compiler.release=8 -Ddoclint=none

%install
%mvn_install

%check
xvfb-run -a xmvn --batch-mode --offline -Dmaven.compiler.release=8 test

classpath="%buildroot%_javadir/jeuclid/*:%_datadir/java/*:%_datadir/java/batik/*:%_datadir/java/fop/*:%_datadir/java/jsr-305/*:%_datadir/ant/lib/*"
mkdir -p target/smoke
javac --release 8 -cp "$classpath" -d target/smoke %SOURCE1
java -Djava.awt.headless=true -cp "target/smoke:$classpath" Smoke

%files -f .mfiles-jeuclid
%doc LICENSE.txt NOTICE README.md Unicode-LICENSE.txt

%files fop -f .mfiles-fop
%doc LICENSE.txt NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE

%changelog
* Tue Nov 10 2026 Ajrat Makhmutov <rauty@altlinux.org> 2:3.1.14-alt1
- First build for ALT.
