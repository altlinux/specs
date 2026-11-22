%define _unpackaged_files_terminate_build 1

Name: zxing
Version: 3.5.4
Release: alt1

Summary: Barcode encoding and decoding library for Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/zxing/zxing
VCS: https://github.com/zxing/zxing

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-11-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.jcommander:jcommander)
BuildRequires: mvn(com.github.jai-imageio:jai-imageio-core)
BuildRequires: mvn(biz.aQute.bnd:bnd-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)

BuildArch: noarch

%description
ZXing is a multi-format barcode image processing library. Its core supports
encoding and decoding one-dimensional and two-dimensional barcodes.

%package javase
Summary: Java SE extensions for ZXing
Group: Development/Java

%description javase
Java SE image handling and command line barcode tools for ZXing.

%package javadoc
Summary: API documentation for ZXing
Group: Development/Documentation

%description javadoc
API documentation for the ZXing core and Java SE libraries.

%prep
%setup -q

# Distribution builds do not publish releases, source JARs or style reports.
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-site-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin
%pom_remove_plugin org.apache.rat:apache-rat-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-assembly-plugin javase

# Use the available plugins and the newer packaged JCommander provider.
%pom_xpath_set \
    'pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:version' \
    3.14.0
%pom_xpath_set \
    'pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:version' \
    3.2.2
%pom_xpath_set \
    'pom:build/pom:pluginManagement/pom:plugins/pom:plugin[pom:artifactId="maven-surefire-plugin"]/pom:version' \
    3.5.6
%pom_xpath_set \
    'pom:build/pom:plugins/pom:plugin[pom:artifactId="bnd-maven-plugin"]/pom:version' \
    6.3.1 core
%pom_change_dep org.jcommander:jcommander org.jcommander:jcommander:3.0 javase

%mvn_package :javase javase
%mvn_file :core %name/core
%mvn_file :javase %name/javase

%build
# The separate zxing.org web application is outside the Java library build.
%mvn_build -- -P'!zxingorg'

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE
%doc CHANGES AUTHORS

%files javase -f .mfiles-javase

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 3.5.4-alt1
- Initial build for ALT.
