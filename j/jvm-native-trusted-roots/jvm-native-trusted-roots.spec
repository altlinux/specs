%define _unpackaged_files_terminate_build 1
%global _without_javadoc 1

Name: jvm-native-trusted-roots
Version: 1.1.7
Release: alt1

Summary: Platform-native trusted certificate handling for Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/jvm-native-trusted-roots
VCS: https://github.com/JetBrains/jvm-native-trusted-roots

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(net.java.dev.jna:jna-platform)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: openssl
BuildRequires: mvn(org.jetbrains:annotations)
BuildRequires: mvn(org.bouncycastle:bcpkix-jdk18on)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.hamcrest:hamcrest-core)

BuildArch: noarch

%description
A Java library that retrieves trusted certificates from the operating system
using platform-specific APIs.

%prep
%setup -q
%pom_change_dep org.jetbrains:annotations:26.0.1 \
    org.jetbrains:annotations:26.1.0
%pom_change_dep org.bouncycastle:bcpkix-jdk18on:1.80 \
    org.bouncycastle:bcpkix-jdk18on:1.84
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_xpath_set pom:project/pom:version %version
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

%build
./src/test/gen-mock-ca.sh
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-jvm-native-trusted-roots
%doc LICENSE

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 1.1.7-alt1
- Initial build for ALT.
