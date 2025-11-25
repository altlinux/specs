%define _unpackaged_files_terminate_build 1

Name: checker-framework
Version: 3.52.0
Release: alt2

Summary: A powerful framework for extending the Java type system
License: GPL-2.0 WITH Classpath-exception-2.0
Group: Development/Java
Url: http://checkerframework.org
Vcs: https://github.com/typetools/checker-framework.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-%version-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-17-compat
BuildRequires: xgradle
BuildRequires: shadow-gradle-plugin
BuildRequires: classgraph
BuildRequires: plumelib-reflection-util
BuildRequires: plumelib-hashmap-util
BuildRequires: plumelib-options
BuildRequires: plumelib-plume-util
BuildRequires: junit5

%description
Checker Frameworkenhances Java's type system to make it more powerful and
useful. This lets software developers detect and prevent errors in their
Java programs. The Checker Framework includes compiler plug-ins ("checkers")
that find bugs or verify their absence. It also permits you to write your
own compiler plug-ins.

%package -n checker-qual
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
Requires: checker-qual = %EVR

%description -n checker-javacutil
Utility classes that help the Checker Framework interact with javac.
This package contains shared utilities used by various Checker Framework components.

%package -n checker-dataflow
Summary: Dataflow analysis framework for Checker Framework
Group: Development/Java
BuildArch: noarch
Requires: checker-qual = %EVR
Requires: checker-javacutil = %EVR

%description -n checker-dataflow
A dataflow framework used by the Checker Framework for static analysis.
This package provides the core dataflow analysis capabilities used by
Checker Framework checkers.

%package -n checker-dataflow-shaded
Summary: Shaded dataflow framework for Checker Framework
Group: Development/Java
BuildArch: noarch
Requires: checker-qual = %EVR

%description -n checker-dataflow-shaded
Shaded version of the dataflow framework to avoid dependency conflicts.
This package contains a relocated version of the dataflow framework for
use in environments where dependency isolation is required.

%package -n checker-dataflow-nullaway
Summary: Dataflow framework for Nullaway integration
Group: Development/Java
BuildArch: noarch
Requires: checker-qual = %EVR

%description -n checker-dataflow-nullaway
Dataflow framework configured for use with Nullaway static analysis tool.
This package provides the dataflow analysis components specifically
adapted for Nullaway.

%package -n checker-dataflow-errorprone
Summary: Dataflow framework for Error Prone integration
Group: Development/Java
BuildArch: noarch
Requires: checker-qual = %EVR

%description -n checker-dataflow-errorprone
Dataflow framework configured for use with Error Prone static analysis tool.
This package provides the dataflow analysis components specifically
adapted for Error Prone.

%package -n checker-util
Summary: Utility classes for Checker Framework
Group: Development/Java
BuildArch: noarch
Requires: checker-qual = %EVR

%description -n checker-util
General utility classes used throughout the Checker Framework.
This package provides common utilities and helper functions for
Checker Framework components.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register

%gradle_install

%files -n checker-qual
%_mavenmetadatadir/checker-framework.xml
%_javadir/checker-framework/checker-qual.jar
%_mavenpomdir/checker-framework/checker-qual.pom

%files -n checker-javacutil
%_javadir/checker-framework/javacutil.jar
%_mavenpomdir/checker-framework/javacutil.pom

%files -n checker-dataflow
%_javadir/checker-framework/dataflow.jar
%_mavenpomdir/checker-framework/dataflow.pom

%files -n checker-dataflow-shaded
%_javadir/checker-framework/dataflow-shaded.jar
%_mavenpomdir/checker-framework/dataflow-shaded.pom

%files -n checker-dataflow-nullaway
%_javadir/checker-framework/dataflow-nullaway.jar
%_mavenpomdir/checker-framework/dataflow-nullaway.pom

%files -n checker-dataflow-errorprone
%_javadir/checker-framework/dataflow-errorprone.jar
%_mavenpomdir/checker-framework/dataflow-errorprone.pom

%files -n checker-util
%_javadir/checker-framework/checker-util.jar
%_mavenpomdir/checker-framework/checker-util.pom

%changelog
* Mon Nov 24 2025 Ivan Khanas <xeno@altlinux.org> 3.52.0-alt2
- Add checker-dataflow subpackage.
- Add checker-dataflow-errorprone subpackage.
- Add checker-dataflow-nullaway subpackage.
- Add checker-dataflow-shaded subpackage.
- Add checker-javacutil subpackage.
- Add checker-util subpackage.

* Tue Nov 18 2025 Ivan Khanas <xeno@altlinux.org> 3.52.0-alt1
- First build for ALT.
