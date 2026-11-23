%define _unpackaged_files_terminate_build 1

Name: debugger-agent
Version: 1.193
Release: alt1

Summary: Java debugger instrumentation agent
License: Apache-2.0 AND BSD-3-Clause
Group: Development/Java
URL: https://github.com/JetBrains/debugger-agent
VCS: https://github.com/JetBrains/debugger-agent.git

Source: %name-%version.tar
Source1: capture-asm.rules
Patch0: 0001-Use-the-system-Gradle-toolchain.patch
Patch1: 0002-Use-system-ASM-for-capture.patch

BuildArch: noarch
BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: java-17-openjdk-devel
BuildRequires: unzip
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.openjdk.jmh:jmh-core)
BuildRequires: mvn(org.pantsbuild:jarjar)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-analysis)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(org.ow2.asm:asm-tree)
BuildRequires: mvn(org.ow2.asm:asm-util)

%description
A Java agent for collecting debugger events and instrumenting application
classes for IntelliJ IDEA debugger features.

%prep
%setup -q
%autopatch -p1

%build
mkdir -p capture-asm lib
for module in asm asm-analysis asm-commons asm-tree asm-util; do
    unzip -q -o "%_javadir/objectweb-asm/$module.jar" \
        'org/objectweb/asm/*' -d capture-asm
done
jar --create --file capture-asm.jar -C capture-asm org
java -cp '%_javadir/jarjar-pantsbuild/jarjar.jar:%_javadir/objectweb-asm/*' \
    org.pantsbuild.jarjar.Main process \
    %SOURCE1 capture-asm.jar lib/asm-capture.jar
install -pm644 %_docdir/objectweb-asm-*/LICENSE.txt ASM-LICENSE.txt

BUILD_NUMBER=%version %gradle_publish

%install
%gradle_register --artifacts=debugger-agent
%gradle_install

%check
%gradle_check

%files -f .mfiles
%doc LICENSE.txt ASM-LICENSE.txt

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 1.193-alt1
- Initial build for ALT.
