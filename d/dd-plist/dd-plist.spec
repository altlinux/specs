%define _unpackaged_files_terminate_build 1

Name: dd-plist
Version: 1.31
Release: alt1

Summary: Java library for working with Apple property lists
License: MIT
Group: Development/Java
URL: https://github.com/3breadt/dd-plist
VCS: https://github.com/3breadt/dd-plist

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.moditect:moditect-maven-plugin)

BuildArch: noarch

%description
A Java library for reading and writing Apple property lists in XML, binary,
and ASCII formats.

%package javadoc
Group: Development/Documentation
Summary: Javadoc for %name

%description javadoc
Javadoc for %name.

%prep
%setup -q -n %name-%version
%pom_change_dep org.junit.jupiter:junit-jupiter:6.0.0 \
    org.junit.jupiter:junit-jupiter:5.14.4
%pom_remove_plugin com.diffplug.spotless:spotless-maven-plugin
%pom_remove_plugin org.apache.felix:maven-bundle-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-assembly-plugin
%pom_xpath_set \
    'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:version' \
    3.14.0
%pom_xpath_set \
    'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-surefire-plugin"]/pom:version' \
    3.5.6
%pom_xpath_set \
    'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:version' \
    3.2.2
%pom_xpath_remove 'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration/pom:archive/pom:manifestFile'

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt
%doc CHANGELOG.md

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 1.31-alt1
- Initial build for ALT.
