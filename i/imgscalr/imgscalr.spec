%define _unpackaged_files_terminate_build 1

Name: imgscalr
Version: 4.2
Release: alt1

Summary: Java image scaling library
License: Apache-2.0
Group: Development/Java
URL: https://github.com/rkalla/imgscalr
VCS: https://github.com/thebuzzmedia/imgscalr

Source0: %name-%version.tar
Patch0: imgscalr-java17-tests.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires: mvn(junit:junit)

BuildArch: noarch

%description
imgscalr is a Java library for image scaling and manipulation using Java 2D.

%package javadoc
Summary: Javadoc for %name
Group: Development/Java

%description javadoc
API documentation for %name.

%prep
%setup -q
# Java2D CMM precision differs from the historical grayscale PNGs.
# Keep their bounded comparison and require exact current-JDK oracle pixels.
%patch0 -p1
%pom_remove_plugin :maven-source-plugin
%pom_xpath_inject pom:properties \
    '<maven.compiler.source>8</maven.compiler.source>'
%pom_xpath_inject pom:properties \
    '<maven.compiler.target>8</maven.compiler.target>'
%pom_xpath_set \
    "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:version" \
    3.12.0
%pom_xpath_inject \
    "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']" \
    '<configuration><doclint>none</doclint></configuration>'

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-imgscalr-lib
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 4.2-alt1
- Initial build for ALT.
