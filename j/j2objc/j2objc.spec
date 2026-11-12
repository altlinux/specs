%define _unpackaged_files_terminate_build 1

Name: j2objc
Version: 3.1
Release: alt1

Summary: Java to Objective-C translator sources and annotations
License: Apache-2.0
Group: Development/Java
URL: https://github.com/google/j2objc
VCS: https://github.com/google/j2objc.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel

%description
J2ObjC translates Java source code to Objective-C for Apple platforms.
This complete upstream SOURCE builds its portable Java annotations.
The translator and Objective-C runtime are supported on macOS/iOS only.

%package -n j2objc-annotations
Summary: Java annotations for J2ObjC translation
Group: Development/Java

%description -n j2objc-annotations
Java annotations used by the J2ObjC translator and Java libraries to describe
translation properties. Includes the Java module descriptor and Java 8 API.

%prep
%setup
cd annotations
# The official release tag retains a development version in its POM.
%pom_xpath_set pom:project/pom:version %version
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin
%mvn_file : j2objc-annotations

%build
cd annotations
%mvn_build -j

%install
cd annotations
%mvn_install

%files -n j2objc-annotations -f annotations/.mfiles
%doc LICENSE

%changelog
* Mon Nov 09 2026 Ivan Khanas <xeno@altlinux.org> 3.1-alt1
- Initial build for ALT.
