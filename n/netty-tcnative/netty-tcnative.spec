%define _unpackaged_files_terminate_build 1

Name: netty-tcnative
Version: 2.0.85
Release: alt1

Summary: Native OpenSSL support for Netty
License: Apache-2.0
Group: Development/Java
URL: https://netty.io/wiki/forked-tomcat-native
VCS: https://github.com/netty/netty-tcnative
Source0: %name-%version.tar
Patch0: 0001-fix-pointer-cast-on-i586.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-17-openjdk-devel
BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: libapr1-devel
BuildRequires: libssl-devel
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(kr.motd.maven:os-maven-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(io.netty:netty-jni-util::sources:)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-commons-net)
BuildRequires: mvn(ant-contrib:ant-contrib)
BuildRequires: mvn(org.fusesource.hawtjni:hawtjni-maven-plugin)
BuildRequires: mvn(io.github.dmlloyd.module-info:module-info)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires: mvn(org.apiguardian:apiguardian-api)

%description
Netty's fork of Tomcat Native provides Java bindings to OpenSSL and APR.
This package builds the shared Java API and the system OpenSSL implementation.

%package classes
Summary: Java API for Netty native TLS implementations
Group: Development/Java
BuildArch: noarch
Obsoletes: netty-tcnative < %version-%release

%description classes
The complete Java API shared by Netty's native TLS implementations.

%javadoc_package

%package openssl-dynamic
Summary: Netty native TLS linked to system OpenSSL and APR
Group: Development/Java

%description openssl-dynamic
The JNI implementation dynamically linked to system OpenSSL and Apache APR.

%prep
%setup
%autopatch -p1
# HawtJNI copies custom native-package files without filtering them.
sed -i -e 's/@PROJECT_NAME@/netty_tcnative/g' \
    -e 's/@VERSION@/%version.Final/g' \
    openssl-dynamic/src/main/native-package/configure.ac
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin :japicmp-maven-plugin
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
# netty-build-common supplies test tooling; these tests use JUnit directly.
%pom_remove_dep :netty-build-common
%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test
%pom_disable_module openssl-static
%pom_disable_module boringssl-static
%pom_disable_module libressl-static
%mvn_package :%name-classes classes
%mvn_package :%name openssl-dynamic
%mvn_package :%name-parent classes

%build
CFLAGS="%optflags -fvisibility=hidden" \
    %mvn_build

%install
%mvn_install
# The separate JNI file also supplies normal ELF automatic dependencies.
install -d %buildroot%_jnidir
find openssl-dynamic/target/native-lib-only -name libnetty_tcnative.so \
    -exec install -m755 '{}' %buildroot%_jnidir/ ';'
test -f %buildroot%_jnidir/libnetty_tcnative.so

%files classes -f .mfiles-classes
%doc LICENSE.txt NOTICE.txt license/*.txt

%files openssl-dynamic -f .mfiles-openssl-dynamic
%_jnidir/libnetty_tcnative.so

%changelog
* Thu Nov 05 2026 Ivan Khanas <xeno@altlinux.org> 2.0.85-alt1
- New version.

* Mon May 18 2026 Evgeniy Serov <scala@altlinux.org> 2.0.75-alt1
- Updated to 2.0.75.
- Build only openssl-classes
- Returned to Sisyphus.

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.30-alt3_10jpp8
- java update

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.30-alt3_9jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.30-alt3_8jpp8
- added BR: maven-remote-resources-plugin for javapackages 5

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.30-alt2_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.30-alt2_6jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.30-alt2_3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.30-alt2_2jpp8
- %%_jnidir set to /usr/lib/java

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.30-alt1_2jpp8
- new version

