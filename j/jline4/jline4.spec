%define _unpackaged_files_terminate_build 1

Name: jline4
Version: 4.4.6
Release: alt1

Summary: Java library for handling console input
License: BSD-3-Clause
Group: Development/Java
Url: https://jline.org
VCS: https://github.com/jline/jline3.git

Source0: %name-%version.tar

Patch0: 0001-load-native-library-fix.patch
Patch1: 0002-jdk17-compatible-lint-flags.patch
Patch2: 0003-term-test-independent-of-term.patch
Patch3: 0004-skip-history-permission-test-without-mountinfo.patch
Patch4: 0005-remove-awaitility-test-dependency.patch
Patch5: 0006-use-system-juniversalchardet-module-name.patch
Patch6: 0007-builtins-tests-system-prerequisites.patch
Patch7: 0008-remote-telnet-module-name.patch

# Maven plugins and dependencies used by the reactor
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc
BuildRequires: java-17-openjdk-devel
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: nano
BuildRequires: mvn(com.github.albfernandez:juniversalchardet)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.google.jimfs:jimfs)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.apiguardian:apiguardian-api)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.easymock:easymock)
BuildRequires: mvn(org.slf4j:slf4j-jdk14)

%description
JLine 4 is a Java library for handling console input. It is similar in
functionality to BSD editline and GNU readline, with additional features
that make it suitable for interactive shells and command-line applications.

%package        jansi
Summary: JLine Jansi bundle
Group: Development/Java
BuildArch: noarch
%description    jansi
%summary.

%package        jansi-core
Summary: JLine Jansi core
Group: Development/Java
BuildArch: noarch
%description    jansi-core
%summary.

%package        core
Summary: JLine core
Group: Development/Java
BuildArch: noarch
%description    core
%summary.

%package        builtins
Summary: JLine builtins
Group: Development/Java
BuildArch: noarch
%description    builtins
%summary.

%package        console
Summary: JLine console
Group: Development/Java
BuildArch: noarch
%description    console
%summary.

%package        console-ui
Summary: JLine console UI
Group: Development/Java
BuildArch: noarch
%description    console-ui
%summary.

%package        native
Summary: JLine native support library
Group: Development/Java
%description    native
%summary.

%package        picocli
Summary: JLine Picocli integration
Group: Development/Java
BuildArch: noarch
%description    picocli
%summary.

%package        prompt
Summary: JLine prompt module
Group: Development/Java
BuildArch: noarch
%description    prompt
%summary.

%package        reader
Summary: JLine reader
Group: Development/Java
BuildArch: noarch
%description    reader
%summary.

%package        remote-ssh
Summary: JLine remote SSH
Group: Development/Java
BuildArch: noarch
%description    remote-ssh
%summary.

%package        remote-telnet
Summary: JLine remote telnet
Group: Development/Java
BuildArch: noarch
%description    remote-telnet
%summary.

%package        shell
Summary: JLine shell framework
Group: Development/Java
BuildArch: noarch
%description    shell
%summary.

%package        style
Summary: JLine style support
Group: Development/Java
BuildArch: noarch
%description    style
%summary.

%package        terminal
Summary: JLine terminal
Group: Development/Java
BuildArch: noarch
%description    terminal
%summary.

%package        terminal-jni
Summary: JLine JNI terminal provider
Group: Development/Java
BuildArch: noarch
%description    terminal-jni
%summary.

%prep
%setup
%autopatch -p1

# This is a fixed upstream release; do not require the release-time Maven extensions.
find . -name pom.xml -exec \
    sed -i 's/${nisse.jgit.dynamicVersion}/%{version}/g' {} +
sed -i 's/${nisse.jgit.date}/2026-09-23T09:10:06Z/' pom.xml
rm -f .mvn/extensions.xml

# Do not ship upstream prebuilt native binaries for unrelated platforms.
find native/src/main/resources/org/jline/nativ \
    -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} +

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :spotless-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :exec-maven-plugin native
%pom_remove_dep :picocli-codegen native
%pom_remove_dep org.awaitility:awaitility shell
%pom_remove_dep org.awaitility:awaitility builtins

# System JUnit annotations require API Guardian on the test compilation path.
%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test

%pom_disable_module groovy
%pom_disable_module demo
%pom_disable_module graal
# JDK Console provider and FFM require Java 22 internal APIs.
%pom_disable_module console-provider
%pom_disable_module terminal-ffm
%pom_remove_dep :jline-terminal-ffm jline
%pom_xpath_remove "//pom:artifactItem[pom:artifactId='jline-terminal-ffm']" jline
%pom_xpath_remove "//pom:execution[pom:id='jdk22']" jline

mkdir -p .xmvn
%mvn_package :jline-parent __noinstall
%mvn_file org.jline:{*} jline4/@1
%mvn_compat_version org.jline:{*} 4.4.6

%build
%add_optflags -Wall -fPIC -fvisibility=hidden -shared
%add_optflags -I native/src/main/native
%add_optflags -I %_jvmdir/jre/include
%add_optflags -I %_jvmdir/jre/include/linux %{?__global_ldflags}
gcc %optflags -o libjlinenative.so \
    native/src/main/native/{jlinenative,clibrary}.c -lutil
# The reactor's aggregate Javadoc fails on packages duplicated by bundle modules.
%mvn_build -j -s -- \
    -Dproject.build.outputTimestamp=2026-09-23T09:10:06Z \
    -Dlibrary.jline.path=$PWD

%install
%mvn_install
install -d -m 755 %buildroot%_libdir/%name
install -p -m 755 libjlinenative.so %buildroot%_libdir/%name/

%files core -f .mfiles-jline
%doc LICENSE.txt README.md

%files jansi -f .mfiles-jansi
%files jansi-core -f .mfiles-jansi-core
%files builtins -f .mfiles-jline-builtins
%files console -f .mfiles-jline-console
%files console-ui -f .mfiles-jline-console-ui
%files native -f .mfiles-jline-native
%_libdir/%name/libjlinenative.so
%files picocli -f .mfiles-jline-picocli
%files prompt -f .mfiles-jline-prompt
%files reader -f .mfiles-jline-reader
%files remote-ssh -f .mfiles-jline-remote-ssh
%files remote-telnet -f .mfiles-jline-remote-telnet
%files shell -f .mfiles-jline-shell
%files style -f .mfiles-jline-style
%files terminal -f .mfiles-jline-terminal
%files terminal-jni -f .mfiles-jline-terminal-jni

%changelog
* Thu Oct 29 2026 Ivan Khanas <xeno@altlinux.org> 4.4.6-alt1
- Initial build for ALT.
