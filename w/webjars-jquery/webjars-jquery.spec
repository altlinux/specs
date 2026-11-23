%define _unpackaged_files_terminate_build 1

Name: webjars-jquery
Version: 4.0.0
Release: alt1

Summary: jQuery packaged as a WebJar Maven artifact
License: MIT
Group: Development/Java
URL: https://www.webjars.org/
VCS: https://github.com/jquery/jquery.git

Source: %name-%version.tar
Source1: webjars-jquery.pom

BuildArch: noarch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: rpm-build-java

%description
The jQuery JavaScript library, published in the org.webjars:jquery Maven
coordinate. The package provides the WebJar resource layout and the published
Maven POM for use by Java and Kotlin builds.

%prep
%setup -q

%build
assets=target/webjar/META-INF/resources/webjars/jquery/%version
mkdir -p "$assets"
cp -a dist/. "$assets/"
jar --create --file target/jquery-%version.jar -C target/webjar .

%install
%mvn_artifact %SOURCE1 target/jquery-%version.jar
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 4.0.0-alt1
- Initial build for ALT.
