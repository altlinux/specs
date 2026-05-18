Name:           netty-tcnative
Version:        2.0.75
Release:        alt1

Summary:        A fork of Apache Tomcat Native, based on finagle-native
License:        Apache-2.0
Group:          Development/Java
URL:            https://netty.io/wiki/forked-tomcat-native
VCS:            https://github.com/netty/netty-tcnative

Source0:        %name-%version.tar

Patch0:         0001-fix-pointer-cast-on-i586.patch

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  libapr1-devel
BuildRequires:  libssl-devel
BuildRequires:  netty-jni-util-source

Buildrequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(kr.motd.maven:os-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(io.netty:netty-jni-util)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-commons-net)
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-maven-plugin)

%description
netty-tcnative is a fork of Tomcat Native. It includes a set of changes
contributed by Twitter, Inc, such as:
 *  Simplified distribution and linkage of native library
 *  Complete mavenization of the project
 *  Improved OpenSSL support
To minimize the maintenance burden, we create a dedicated branch for each stable
upstream release and apply our own changes on top of it, while keeping the
number of maintained branches to minimum

%javadoc_package

%package        openssl-dynamic
Summary:        Netty/TomcatNative [OpenSSL - Dynamic]]
Group:          Development/Java

%description    openssl-dynamic
A Mavenized fork of Tomcat Native which incorporates various patches.
This artifact is dynamically linked to OpenSSL and Apache APR.

%prep
%setup
%autopatch -p1

%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin :japicmp-maven-plugin
%pom_remove_plugin :maven-source-plugin openssl-classes
%pom_remove_plugin :module-info

%pom_remove_dep :netty-build-common
%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test

sed -i '/<classifier>sources<\/classifier>/d' pom.xml

mkdir -p openssl-dynamic/src/main
cp -a %_usrsrc/netty-jni-util/src/main/c openssl-dynamic/src/main/

%pom_disable_module openssl-static
%pom_disable_module boringssl-static
%pom_disable_module libressl-static

%mvn_package :%name-classes
%mvn_package ":{*}::linux*:" @1
%mvn_package :%name-parent __noinstall

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.md

%files openssl-dynamic -f .mfiles-netty-tcnative

%changelog
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

