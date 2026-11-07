%define _unpackaged_files_terminate_build 1

Name: format-ripper
Version: 1.3.0
Release: alt1

Summary: Binary format parsing and signature verification for JVM
License: Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/format-ripper
VCS: https://github.com/JetBrains/format-ripper.git
BuildArch: noarch

Source: %name-%version.tar
Patch: offline-jvm.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: java-17-openjdk-devel
BuildRequires: kotlin-compiler
BuildRequires: kotlin-gradle-plugin
BuildRequires: rpm-build-java
BuildRequires: xgradle
BuildRequires: mvn(org.jetbrains.kotlin:kotlin-stdlib)
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: kotlinx-coroutines
BuildRequires: mvn(org.bouncycastle:bcprov-jdk18on)
BuildRequires: mvn(org.bouncycastle:bcpkix-jdk18on)
BuildRequires: mvn(org.bouncycastle:bcutil-jdk18on)
BuildRequires: mvn(org.apache.commons:commons-compress)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mockito
BuildRequires: mockito-junit-jupiter

%description
Format Ripper parses binary formats and verifies cryptographic signatures.
The JVM library supports ELF, Mach-O, PE, MSI and PowerShell files.
The complete upstream project and its test data are retained in the source
package.

%prep
%setup
%patch -p1

%build
cd jvm
%gradle_publish --no-daemon \
    -Dorg.gradle.java.home=%_jvmdir/java-17-openjdk \
    -Pkotlin.compiler.execution.strategy=in-process

%install
cd jvm
%gradle_register --artifacts=format-ripper-
%gradle_install

%check
cd jvm
%gradle_check --no-daemon \
    -Dorg.gradle.java.home=%_jvmdir/java-17-openjdk \
    -Pkotlin.compiler.execution.strategy=in-process

%files -f jvm/.mfiles
%doc LICENSE

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 1.3.0-alt1
- Initial build for ALT.
