%define _unpackaged_files_terminate_build 1

Name: checker-framework
Version: 4.4.0
Release: alt1
%global framework_version %version

Summary: A powerful framework for extending the Java type system
License: GPL-2.0 WITH Classpath-exception-2.0 AND MIT
Group: Development/Java
URL: http://checkerframework.org
VCS: https://github.com/typetools/checker-framework.git
BuildArch: noarch

Source0: %name-%version.tar
Source1: checker-compat-qual-2.5.6-sources.jar
Source2: checker-compat-qual-2.5.6.pom
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: rpm-build-java-osgi
BuildRequires: java-21-openjdk-devel
BuildRequires: xgradle
BuildRequires: shadow-gradle-plugin
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: plumelib-reflection-util
BuildRequires: mvn(org.plumelib:javac-parse)
BuildRequires: plumelib-hashmap-util
BuildRequires: plumelib-plume-util
BuildRequires: mvn(junit:junit)
BuildRequires: graphviz

%description
Checker Framework enhances Java's type system to make it more powerful and
useful. This lets software developers detect and prevent errors in their
Java programs. The Checker Framework includes compiler plug-ins ("checkers")
that find bugs or verify their absence. It also permits you to write your
own compiler plug-ins.

%package -n checker-qual
License: MIT
Summary: Type qualifier annotations for Checker Framework
Group: Development/Java
BuildArch: noarch

%description -n checker-qual
A set of type qualifier annotations such as @NonNull and @Interned
that programmers add to Java source code for checking with the
Checker Framework. These annotations define additional constraints
on types that are then enforced at compile time by one of the
Framework's checkers.

This package should be installed if you are developing code that
will be checked using the Checker Framework.

%package -n checker-javacutil
Summary: Utility classes for Checker Framework javac integration
Group: Development/Java
BuildArch: noarch

%description -n checker-javacutil
Utility classes that help the Checker Framework interact with javac.
This package contains shared utilities used by various Checker Framework components.

%package -n checker-dataflow
Summary: Dataflow analysis framework for Checker Framework
Group: Development/Java
BuildArch: noarch

%description -n checker-dataflow
A dataflow framework used by the Checker Framework for static analysis.
This package provides the core dataflow analysis capabilities used by
Checker Framework checkers.

%package -n checker-dataflow-shaded
Summary: Shaded dataflow framework for Checker Framework
Group: Development/Java
BuildArch: noarch

%description -n checker-dataflow-shaded
Shaded version of the dataflow framework to avoid dependency conflicts.
This package contains a relocated version of the dataflow framework for
use in environments where dependency isolation is required.

%package -n checker-dataflow-nullaway
Summary: Dataflow framework for Nullaway integration
Group: Development/Java
BuildArch: noarch

%description -n checker-dataflow-nullaway
Dataflow framework configured for use with Nullaway static analysis tool.
This package provides the dataflow analysis components specifically
adapted for Nullaway.

%package -n checker-dataflow-errorprone
Summary: Dataflow framework for Error Prone integration
Group: Development/Java
BuildArch: noarch

%description -n checker-dataflow-errorprone
Dataflow framework configured for use with Error Prone static analysis tool.
This package provides the dataflow analysis components specifically
adapted for Error Prone.

%package -n checker-util
License: MIT
Summary: Utility classes for Checker Framework
Group: Development/Java
BuildArch: noarch

%description -n checker-util
General utility classes used throughout the Checker Framework.
This package provides common utilities and helper functions for
Checker Framework components.

%package -n checker-compat-qual
Version: 2.5.6
Release: alt4
License: MIT
Summary: Legacy nullness compatibility annotations for Checker Framework
Group: Development/Java

%description -n checker-compat-qual
Original legacy declaration and type-use nullness annotations. These use a
distinct Java namespace and coexist with current Checker Framework qualifiers.

%prep
%setup
%autopatch -p1
# This buildSrc contains only the unused upstream Spotless formatting plugin.
mv buildSrc buildSrc.formatting
mkdir compat-src
(cd compat-src && jar xf %SOURCE1)

%build
%gradle_publish -PreleaseVersion=%framework_version \
    -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk

mkdir compat-classes
find compat-src -name '*.java' -print | sort > compat-sources.list
javac --release 8 -encoding UTF-8 -d compat-classes @compat-sources.list
jar --create --file checker-compat-qual.jar -C compat-classes .
%mvn_artifact %SOURCE2 checker-compat-qual.jar

%install
%gradle_register

%mvn_package org.checkerframework:checker-qual checker-qual
%mvn_package org.checkerframework:javacutil checker-javacutil
%mvn_package org.checkerframework:dataflow checker-dataflow
%mvn_package org.checkerframework:dataflow-shaded checker-dataflow-shaded
%mvn_package org.checkerframework:dataflow-nullaway checker-dataflow-nullaway
%mvn_package org.checkerframework:dataflow-errorprone checker-dataflow-errorprone
%mvn_package org.checkerframework:checker-util checker-util
%mvn_package org.checkerframework:checker-compat-qual checker-compat-qual

%gradle_install

%check
%gradle_check -PreleaseVersion=%framework_version \
    -Dorg.gradle.java.home=%_jvmdir/java-21-openjdk

%files -n checker-qual -f .mfiles-checker-qual
%doc checker-qual/LICENSE.txt

%files -n checker-javacutil -f .mfiles-checker-javacutil
%doc LICENSE.txt

%files -n checker-dataflow -f .mfiles-checker-dataflow

%files -n checker-dataflow-shaded -f .mfiles-checker-dataflow-shaded

%files -n checker-dataflow-nullaway -f .mfiles-checker-dataflow-nullaway

%files -n checker-dataflow-errorprone -f .mfiles-checker-dataflow-errorprone

%files -n checker-util -f .mfiles-checker-util
%doc checker-util/LICENSE.txt

%files -n checker-compat-qual -f .mfiles-checker-compat-qual

%changelog
* Wed Nov 11 2026 Ivan Khanas <xeno@altlinux.org> 4.4.0-alt1
- New version.

* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 3.52.0-alt3
- Add legacy compatibility annotations and split Maven metadata by package.

* Mon Nov 24 2025 Ivan Khanas <xeno@altlinux.org> 3.52.0-alt2
- Add checker-dataflow subpackage.
- Add checker-dataflow-errorprone subpackage.
- Add checker-dataflow-nullaway subpackage.
- Add checker-dataflow-shaded subpackage.
- Add checker-javacutil subpackage.
- Add checker-util subpackage.

* Tue Nov 18 2025 Ivan Khanas <xeno@altlinux.org> 3.52.0-alt1
- First build for ALT.
