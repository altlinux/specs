%define _unpackaged_files_terminate_build 1

Name: intellij-deps-commons-imaging
Version: 1.0
Release: alt1.rc1

Summary: JetBrains fork of Apache Commons Imaging
License: Apache-2.0
Group: Development/Java
URL: https://github.com/JetBrains/intellij-deps-commons-imaging
VCS: https://github.com/JetBrains/intellij-deps-commons-imaging.git

Source: %name-%version.tar
Patch0: 0001-Check-the-exception-on-current-JDKs.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(org.apache.commons:commons-parent:pom:)
BuildRequires: fontconfig
BuildRequires: fonts-ttf-liberation

%description
JetBrains' fork of Apache Commons Imaging, a pure Java image parsing and
writing library used by the IntelliJ Platform.

%package javadoc
Summary: Javadoc for %name
Group: Development/Documentation

%description javadoc
API documentation for the JetBrains Commons Imaging fork.

%prep
%setup -q
%autopatch -p1
# Use the current compatible system Commons parent POM (the upstream 43 is absent).
%pom_xpath_set 'pom:project/pom:parent/pom:version' 107
%pom_xpath_inject 'pom:project/pom:properties' \
    '<commons.build-helper.version>3.6.1</commons.build-helper.version>'
# The Java 17 signature artifact has no Sisyphus provider; omit this test-only gate.
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin
# Sources JARs are not product outputs and this offline plugin version is unavailable.
%pom_remove_plugin :maven-source-plugin

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-commons-imaging
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 1.0-alt1.rc1
- Initial build for ALT.
