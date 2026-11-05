%define _unpackaged_files_terminate_build 1

Name: jsinterop-annotations
Version: 2.1.0
Release: alt1

Summary: Java annotations for JavaScript interoperability
License: Apache-2.0
Group: Development/Java
URL: https://github.com/google/jsinterop-annotations
VCS: https://github.com/google/jsinterop-annotations.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local

%description
JsInterop annotations describe Java APIs exposed to JavaScript by J2CL and
GWT. The Java annotation library has no external runtime dependencies.

%package javadoc
Summary: API documentation for JsInterop annotations
Group: Development/Documentation

%description javadoc
Generated Java API documentation for JsInterop annotations.

%prep
%setup
sed -e 's/__GROUP_ID__/com.google.jsinterop/g' \
    -e 's/__ARTIFACT_ID__/%name/g' \
    -e 's/__VERSION__/%version/g' \
    maven/pom-annotations.xml > pom.xml

%build
mkdir -p target/classes target/apidocs
find java -name '*.java' -print | sort > target/sources.list
javac --release 8 -encoding UTF-8 -d target/classes @target/sources.list
jar --create --file target/%name.jar -C target/classes .
javadoc --release 8 -encoding UTF-8 -d target/apidocs @target/sources.list
%mvn_artifact pom.xml target/%name.jar

%install
%mvn_install -J target/apidocs

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Nov 04 2026 Ivan Khanas <xeno@altlinux.org> 2.1.0-alt1
- Initial build for ALT.
