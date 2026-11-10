%define _unpackaged_files_terminate_build 1
%def_with check

Name: jlatexmath
Version: 1.0.7
Release: alt1
Epoch: 1

Summary: A Java API to render LaTeX
# See font-licenses.txt for the font inventory and LicenseRef definitions.
License: GPL-2.0-or-later WITH Classpath-exception-2.0 AND OFL-1.1-RFN AND Knuth-CTAN AND LicenseRef-DoubleStroke AND LicenseRef-BaKoMa AND ALT-Public-Domain
Group: Development/Java
Url: https://github.com/opencollab/jlatexmath/
VCS: https://github.com/opencollab/jlatexmath.git
BuildArch: noarch

Source: %name-%version.tar
Source1: Smoke.java
Source2: font-licenses.txt

Requires: fontconfig
Requires: jlatexmath-font-greek = %EVR
Requires: jlatexmath-font-cyrillic = %EVR

BuildRequires(pre): rpm-macros-java rpm-build-java
BuildRequires: /proc
BuildRequires: maven-local jpackage-17-compat
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-javadoc-plugin
BuildRequires: mvn(org.apache.xmlgraphics:fop)

%if_with check
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.openjdk.jmh:jmh-core)
BuildRequires: mvn(org.openjdk.jmh:jmh-generator-annprocess)
BuildRequires: fontconfig fonts-ttf-dejavu
BuildRequires: xvfb-run
%endif

%description
JLaTeXMath renders LaTeX mathematical expressions using Java graphics.

%package font-greek
Summary: Greek fonts for JLaTeXMath
License: GPL-2.0-or-later
Group: Development/Java

%description font-greek
Greek font resources for the JLaTeXMath formula renderer.

%package font-cyrillic
Summary: Cyrillic fonts for JLaTeXMath
License: GPL-2.0-or-later WITH Classpath-exception-2.0 AND Knuth-CTAN
Group: Development/Java

%description font-cyrillic
Cyrillic font resources for the JLaTeXMath formula renderer.

%package fop
Summary: Apache FOP integration for JLaTeXMath
License: GPL-2.0-or-later WITH Classpath-exception-2.0
Group: Development/Java

Requires: jlatexmath = %EVR

%description fop
Apache FOP integration for rendering LaTeX mathematical expressions.

%package javadoc
Summary: API documentation for JLaTeXMath
# OpenJDK's script.js is GPL-2.0-only with Classpath exception; jQuery is MIT.
License: GPL-2.0-or-later WITH Classpath-exception-2.0 AND GPL-2.0-only WITH Classpath-exception-2.0 AND MIT
Group: Development/Documentation

%description javadoc
API documentation for the JLaTeXMath library and Apache FOP integration.

%prep
%setup
%autopatch -p1
cp -p %SOURCE2 font-licenses.txt

# The upstream parent supplies release tooling, not library dependencies.
%pom_remove_parent
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :coveralls-maven-plugin
%pom_xpath_set pom:properties/pom:java.version 1.8

# Ship the library modules; examples and the deployment placeholder are not RPMs.
%pom_disable_module jlatexmath-example-giws
%pom_disable_module jlatexmath-example-export
%pom_disable_module jlatexmath-ignore

# Maven resolves declared test dependencies even when tests are skipped.
%if_without check
%pom_remove_dep junit:junit jlatexmath
%pom_remove_dep junit:junit jlatexmath-fop
%pom_remove_dep org.openjdk.jmh:jmh-core jlatexmath
%pom_remove_dep org.openjdk.jmh:jmh-generator-annprocess jlatexmath
%endif

%mvn_package :::javadoc: javadoc
%mvn_package :jlatexmath-parent jlatexmath
%mvn_package :jlatexmath jlatexmath
%mvn_package :jlatexmath-font-greek font-greek
%mvn_package :jlatexmath-font-cyrillic font-cyrillic
%mvn_package :jlatexmath-fop fop

# Preserve the conventional flat JAR paths for existing consumers.
%mvn_file :jlatexmath jlatexmath/jlatexmath jlatexmath
%mvn_file :jlatexmath-font-greek jlatexmath/jlatexmath-font-greek jlatexmath-font-greek
%mvn_file :jlatexmath-font-cyrillic jlatexmath/jlatexmath-font-cyrillic jlatexmath-font-cyrillic
%mvn_file :jlatexmath-fop jlatexmath/jlatexmath-fop jlatexmath-fop

%build
%mvn_build -- -Dmaven.test.skip=true -Dmaven.compiler.release=8 -Ddoclint=none

%install
%mvn_install

%check
# The includegraphics regression test creates an AWT Label.
xvfb-run -a xmvn --batch-mode --offline -Dmaven.compiler.release=8 test

classpath="%buildroot%_javadir/jlatexmath/*:/usr/share/java/*:/usr/share/java/batik/*:/usr/share/java/fop/*"
mkdir -p target/smoke
javac --release 8 -cp "$classpath" -d target/smoke %SOURCE1
java -Djava.awt.headless=true -cp "target/smoke:$classpath" Smoke

%files -f .mfiles-jlatexmath
%doc LICENSE COPYING font-licenses.txt
%doc jlatexmath/src/main/resources/org/scilab/forge/jlatexmath/fonts/licences

%files font-greek -f .mfiles-font-greek
%doc jlatexmath-font-greek/LICENSE jlatexmath-font-greek/COPYING

%files font-cyrillic -f .mfiles-font-cyrillic
%doc jlatexmath-font-cyrillic/LICENSE jlatexmath-font-cyrillic/COPYING
%doc jlatexmath/src/main/resources/org/scilab/forge/jlatexmath/fonts/licences/Knuth_License.txt

%files fop -f .mfiles-fop
%doc jlatexmath-fop/LICENSE jlatexmath-fop/COPYING

%files javadoc -f .mfiles-javadoc
%doc LICENSE COPYING

%changelog
* Tue Nov 10 2026 Ajrat Makhmutov <rauty@altlinux.org> 1:1.0.7-alt1
- First build for ALT.
