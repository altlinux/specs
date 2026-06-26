%define _unpackaged_files_terminate_build 1

Name: spotbugs
Version: 4.9.8
Release: alt2

Summary: SpotBugs is the spiritual successor of FindBugs
License: Apache-2.0
Group: Development/Java
Url: https://spotbugs.github.io
Vcs: https://github.com/spotbugs/spotbugs.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Remove-all-external-gradle-plugins-alt-patch.patch
Patch1: 0002-Apache-bcel-6.8.2-compat-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-11-compat
BuildRequires: google-gson
BuildRequires: objectweb-asm
BuildRequires: jsr-305
BuildRequires: slf4j
BuildRequires: apache-commons-bcel
BuildRequires: apache-commons-lang3
BuildRequires: apache-commons-text
BuildRequires: apache-commons-cli
BuildRequires: jcip-annotations
BuildRequires: dom4j
BuildRequires: jakarta-annotations
BuildRequires: ant-lib
BuildRequires: hamcrest
BuildRequires: junit5
BuildRequires: apiguardian
Requires: spotbugs-annotations

%description
SpotBugs is a static analysis tool for Java programs. It examines compiled Java
bytecode to identify potential bugs, security vulnerabilities, and bad
practices. SpotBugs extends the original FindBugs project with modernized
infrastructure, new bug detectors, and active community maintenance.

It supports integration with popular build systems such as Maven, Gradle, and
Ant, and can be used standalone or as part of CI/CD pipelines.  SpotBugs helps
developers maintain cleaner, safer, and more reliable Java codebases through
automatic code inspection.

%package annotations
Summary: SpotBugs annotations for static analysis
Group: Development/Java
BuildArch: noarch

%description annotations
SpotBugs annotations package.  Contains compile-time annotations used by the
SpotBugs engine to improve accuracy of static analysis and reduce false
positives. These annotations can be safely added to any project source code.

%package ant
Summary: SpotBugs Ant task integration
Group: Development/Java
BuildArch: noarch
Requires: spotbugs

%description ant
Ant task integration for SpotBugs.  Provides Ant targets and configuration for
executing SpotBugs analysis during builds, generating XML and HTML reports, and
customizing analysis parameters.

%package javadoc
Group: Development/Java
Summary: Javadoc for spotbugs

%description javadoc
This package contains javadoc for spotbugs.

%prep
%setup
%autopatch -p1

# Remove useless directory for RPM build(requires kotlin-dsl).
rm -rf buildSrc

%build
%gradle_publish

%install

%gradle_register --artifacts=spotbugs
%gradle_register_javadoc --artifacts=spotbugs

%gradle_install

%files
%_javadir/spotbugs/spotbugs.jar
%_mavenpomdir/spotbugs/spotbugs.pom

%files annotations
%_mavenmetadatadir/spotbugs.xml
%_javadir/spotbugs/spotbugs-annotations.jar
%_mavenpomdir/spotbugs/spotbugs-annotations.pom

%files ant
%_javadir/spotbugs/spotbugs-ant.jar
%_mavenpomdir/spotbugs/spotbugs-ant.pom

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Jun 26 2026 Anton Meleshnikov <alton@altlinux.org> 4.9.8-alt2
- FTBFS fix (bcel was renamed).

* Wed Nov 12 2025 Ivan Khanas <xeno@altlinux.org> 4.9.8-alt1
- First build for ALT.
