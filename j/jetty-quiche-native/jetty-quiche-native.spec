%define _unpackaged_files_terminate_build 1

Name: jetty-quiche-native
Version: 0.30.0
Release: alt1

Summary: Native Quiche resource library for Jetty
License: BSD-2-Clause AND BSD-3-Clause AND MIT AND Apache-2.0 AND ISC AND MPL-2.0 AND Unicode-3.0 AND Zlib
Group: Development/Java
URL: https://github.com/jetty-project/jetty-quiche-native
VCS: https://github.com/jetty-project/jetty-quiche-native.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: libquiche-devel
Requires: libquiche0

%description
The Quiche native resource library used by Jetty's QUIC and HTTP/3
implementations. The target platform library is built from the Quiche
SOURCE package; foreign platform prebuilt libraries are not used.

%prep
%setup
%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin com.mycila:license-maven-plugin
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions/pom:execution[pom:id='empty-javadoc-jar']"
rm -r src/main/resources
mkdir -p src/main/resources

%build
java -version
native_arch=$(java -XshowSettings:properties -version 2>&1 | sed -n 's/^[[:space:]]*os.arch = //p')
case "$native_arch" in
    amd64|x86_64) native_arch=x86-64 ;;
    i?86) native_arch=x86 ;;
esac
test -n "$native_arch"
install -Dm644 %_libdir/libquiche.so.0 src/main/resources/linux-$native_arch/libquiche.so
install -Dm644 %_docdir/quiche-common-%version/COPYING src/main/resources/META-INF/quiche/COPYING
cp -a %_docdir/quiche-common-%version/vendor-notices src/main/resources/META-INF/quiche/
%mvn_build -s -- -Dmaven.compiler.release=11

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE.txt NOTICE.txt README.md

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 0.30.0-alt1
- Initial build for ALT.
