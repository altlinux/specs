%define _unpackaged_files_terminate_build 1

Name: delight-rhino-sandbox
Version: 0.2.5
Release: alt1

Summary: Java sandbox for executing JavaScript with Rhino
License: (Apache-2.0 OR MIT OR GPL-3.0-only)
Group: Development/Java
URL: https://github.com/javadelight/delight-rhino-sandbox
VCS: https://github.com/javadelight/delight-rhino-sandbox.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.mozilla:rhino)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

BuildArch: noarch

%description
Delight Rhino Sandbox provides a Java API to execute JavaScript with Rhino
while restricting access to Java classes and limiting script execution time
and instruction count.

%package javadoc
Summary: API documentation for %name
Group: Development/Documentation

%description javadoc
API documentation for Delight Rhino Sandbox.

%prep
%setup -q
# Use the Rhino Maven publication available in Sisyphus.
%pom_xpath_set \
    'pom:project/pom:dependencies/pom:dependency[pom:groupId="org.mozilla" and pom:artifactId="rhino"]/pom:version' \
    1.7.14
%pom_xpath_set \
    'pom:project/pom:dependencies/pom:dependency[pom:groupId="junit" and pom:artifactId="junit"]/pom:version' \
    4.13.2
# Avoid upstream signing and remote publication steps during a local package build.
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
# The ALT Maven macro generates Javadoc through xmvn-mojo:javadoc.
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_xpath_set \
    'pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-bundle-plugin"]/pom:version' \
    5.1.9

%pom_xpath_set "//pom:argLine[.='-Xmx6g']" -- -Xmx1280m

%pom_xpath_inject '//pom:instructions[pom:Bundle-SymbolicName]' \
    '<_reproducible>true</_reproducible>'

%build
# The allocation stress test can exhaust the bounded Surefire heap.
%mvn_build -s -- \
    -Dtest='!TestNativeCallBypass#testDurationLimitWithWatchdog'

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE.TXT

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 0.2.5-alt1
- Initial build for ALT.
