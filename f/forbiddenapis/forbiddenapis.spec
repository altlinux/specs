%define _unpackaged_files_terminate_build 1

Name: forbiddenapis
Version: 3.11
Release: alt1

Summary: Forbidden API bytecode checker with Maven and Ant integrations
License: Apache-2.0
Group: Development/Java
URL: https://github.com/policeman-tools/forbidden-apis
VCS: https://github.com/policeman-tools/forbidden-apis.git

Source: %name-%version.tar
Patch0: %name-%version-alt-maven.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: rpm-build-java
BuildRequires: java-17-openjdk-devel
BuildRequires: objectweb-asm
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.ow2.asm:asm-commons)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.ant:ant-antunit)
BuildRequires: mvn(ant-contrib:ant-contrib)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)

%description
Forbidden APIs checks Java bytecode for invocations of configured forbidden
classes, methods and fields. This package includes the core checker and
Maven, Ant and command-line integrations, using system libraries.
The upstream Gradle integration is outside this package's scope.

%javadoc_package

%prep
%setup
%autopatch -p1
# Keep Gradle Java/Groovy sources away from implicit javac/Javadoc discovery.
mkdir .alt-excluded
mv src/main/java/de/thetaphi/forbiddenapis/gradle .alt-excluded/gradle-java
mv src/main/java/org/gradle .alt-excluded/gradle-stubs
mv src/main/groovy .alt-excluded/gradle-groovy
# Generate the bundled-signature index, as upstream's Ant compile target does.
find src/main/resources/de/thetaphi/forbiddenapis/signatures -maxdepth 1 \
 -name '*.txt' ! -name 'incr-*' -printf '%%f\n' | \
 sed 's/\.txt$//' | LC_ALL=C sort > src/main/resources/de/thetaphi/forbiddenapis/signatures/list
%mvn_file :forbiddenapis forbiddenapis
%mvn_package :forbiddenapis forbiddenapis

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-forbiddenapis
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Oct 27 2026 Ivan Khanas <xeno@altlinux.org> 3.11-alt1
- Initial build for ALT.
