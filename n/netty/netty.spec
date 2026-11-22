%def_with check
%define mvn_version %version.Final
%ifarch %ix86
%define native_classifier linux-x86_32
%define conscrypt_classifier linux-x86
%define brotli_classifier linux-x86_32
%else
%ifarch aarch64
%define native_classifier linux-aarch_64
%define netty_maven_profiles -P!boringssl-linux-aarch64
%define conscrypt_classifier linux-aarch_64
%define brotli_classifier linux-aarch64
%else
%define native_classifier linux-%_arch
%define conscrypt_classifier linux-%_arch
%define brotli_classifier linux-%_arch
%endif
%endif

Name:           netty
Version:        4.2.20
Release:        alt1

Summary:        Netty project - an event-driven asynchronous network application framework
License:        Apache-2.0
Group:          Development/Java
URL:            https://netty.io/
VCS:            https://github.com/netty/netty

Source0:        %name-%version.tar
Source1:        package-prepare.py
Source2:        codegen.groovy
Source3:        quiche-boringssl-headers.tar
Patch1:         0001-Look-up-the-native-access-check-with-MethodHandles-f.patch
Patch2:         0002-Pass-existing-JNI-include-variable-from-the-Maven-ru.patch
Patch3:         0003-Close-HTTP-2-test-channels-before-releasing-their-ev.patch
Patch4:         0004-Build-QUIC-JNI-with-the-selected-Quiche-SDK.patch
Patch5:         0005-Bound-the-two-UDT-rendezvous-test-peers.patch
Patch6:         0006-Run-native-transport-suites-with-offline-fixtures-an.patch
Patch7:         0007-Build-the-Protobuf-codec-without-the-legacy-Nano-API.patch
Patch8:         0008-Resolve-the-packaged-QUIC-runtime-through-the-HTTP-3.patch
Patch9:         0009-Preserve-native-addresses-across-JNI-on-32-bit-Linux.patch
Patch10:        0010-Keep-QUIC-musl-compatibility-shims-on-the-64-bit-ABI.patch
Patch11:        0011-Allow-the-TLS-1.2-session-ticket-test-to-finish-on-i.patch
Patch12:        0012-Preserve-large-file-offsets-in-the-epoll-transport.patch
Patch13:        0013-Allow-the-HTTP-2-TLS-1.3-handshake-test-to-finish-on.patch
Patch14:        0014-Check-the-QUIC-transport-parameters-configured-by-ea.patch

BuildRequires(pre):  rpm-macros-java
BuildRequires:  java-17-openjdk-devel
BuildRequires:  java-21-openjdk-devel
BuildRequires:  maven-local
BuildRequires:  mvn(io.netty:netty-jni-util::sources:)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(kr.motd.maven:os-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jctools:jctools-core)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-1.2-api)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:  mvn(com.ning:compress-lzf)
BuildRequires:  mvn(com.github.jponge:lzma-java)
BuildRequires:  mvn(io.netty:netty-tcnative-classes)
BuildRequires:  mvn(io.netty:netty-tcnative::%native_classifier:)
BuildRequires:  mvn(org.bouncycastle:bctls-jdk18on)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-maven-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  groovy
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(io.github.dmlloyd.module-info:module-info)
BuildRequires:  mvn(org.apache.groovy:groovy-ant)
BuildRequires:  mvn(com.carrotsearch:hppc)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(org.conscrypt:conscrypt-openjdk::%conscrypt_classifier:)
BuildRequires:  mvn(io.projectreactor.tools:blockhound)
BuildRequires:  mvn(org.jetbrains:annotations)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-api:2)
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(org.jboss.marshalling:jboss-marshalling)
BuildRequires:  mvn(com.fasterxml:aalto-xml)
BuildRequires:  mvn(com.google.protobuf:protobuf-java)
BuildRequires:  mvn(com.barchart.udt:barchart-udt-bundle)
BuildRequires:  mvn(org.graalvm.sdk:nativeimage)
BuildRequires:  libquiche-devel-static
BuildRequires:  mvn(org.codehaus.mojo:flatten-maven-plugin)
BuildRequires:  mvn(com.sun.activation:jakarta.activation:1.2.2)
BuildRequires:  mvn(org.rxtx:rxtx)
BuildRequires:  mvn(at.yawk.lz4:lz4-java)
BuildRequires:  mvn(com.github.luben:zstd-jni)
BuildRequires:  mvn(com.aayushatharva.brotli4j:brotli4j)
BuildRequires:  mvn(com.aayushatharva.brotli4j:native-%brotli_classifier)
BuildRequires:  mvn(org.bouncycastle:bcprov-jdk18on)
BuildRequires:  mvn(org.bouncycastle:bcpkix-jdk18on)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)

%if_with check
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher)
BuildRequires:  mvn(org.junit.platform:junit-platform-testkit)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.reflections:reflections)
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-core)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.jboss.marshalling:jboss-marshalling-serial)
BuildRequires:  mvn(org.jboss.marshalling:jboss-marshalling-river)
BuildRequires:  mvn(org.tukaani:xz)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
%endif

%description
Netty is an asynchronous event-driven network application framework for rapid
development of maintainable high performance protocol servers & clients.

%javadoc_package

%package        bom
Group:          Development/Java
Summary:        Netty Bill of Materials
BuildArch:      noarch

%description    bom
%summary.

%package        testlib
Summary:        Upstream common test helpers for Netty
Group:          Development/Java
BuildArch:      noarch

%description    testlib
The genuine Netty common test helper library from the same source release.

%prep
%setup -a3
%autopatch -p1

%ifarch %ix86
# Concurrent buffer tests can exhaust direct memory on the 32-bit JVM.
sed -i '/^junit\.jupiter\.execution\.parallel\.enabled/s/ = true$/ = false/' \
    buffer/src/test/resources/junit-platform.properties
%endif
# Whole source stays present; this explicit profile selects current JVM/Linux.
%if_with check
python3 %SOURCE1 --native-classifier %native_classifier \
    --conscrypt-classifier %conscrypt_classifier \
    --brotli-classifier %brotli_classifier --libdir %_libdir --with-check
%else
python3 %SOURCE1 --native-classifier %native_classifier \
    --conscrypt-classifier %conscrypt_classifier \
    --brotli-classifier %brotli_classifier --libdir %_libdir
%endif
# Resolve the upstream-managed SLF4J 2 API to the system publication.
%pom_xpath_set \
    'pom:dependencyManagement/pom:dependencies/pom:dependency[pom:groupId="org.slf4j"][pom:artifactId="slf4j-api"]/pom:version' \
    2
%if_with check
%pom_add_dep org.apiguardian:apiguardian-api:1.1.2:test transport
%ifarch %ix86
# Release direct-memory caches between buffer test classes on the 32-bit JVM.
surefire='pom:project/pom:build/pom:plugins/pom:plugin'
%pom_xpath_inject "$surefire[pom:artifactId='maven-surefire-plugin']/pom:configuration" \
    '<reuseForks>false</reuseForks>' buffer

# The Bzip2 suite reproduces an encoder failure in the 32-bit OpenJDK 21 VM.
%pom_xpath_inject pom:project/pom:properties \
    '<testJvm>%_jvmdir/java-17-openjdk/bin/java</testJvm>' codec-compression
%endif
%endif
%mvn_package :netty-bom bom
# Publish the genuine dependency aggregate POM without a metadata-only JAR.
%mvn_package :netty-all:jar: __noinstall
%mvn_package :netty-testsuite-common testlib
# Match the exact classifier before the general suite rule.
%mvn_package :netty-testsuite:jar:tests: __noinstall
%mvn_package :netty-testsuite testlib
%mvn_package :netty-testsuite-http2 testlib
%mvn_package :netty-testsuite-native __noinstall
%mvn_package :netty-transport-blockhound-tests __noinstall
%mvn_package :netty-transport-native-unix-common-tests testlib
%mvn_package :netty-dev-tools __noinstall
%mvn_package :netty-jfr-stub __noinstall
%mvn_package :netty-varhandle-stub __noinstall
%mvn_package :netty-ffm-stub __noinstall
# Attached native classifiers already exist in the upstream XMvn reactor.
for netty_mod in transport-native-epoll transport-native-io_uring \
    transport-native-unix-common codec-native-quic; do
    %mvn_package \
        "io.netty:netty-$netty_mod:jar:%native_classifier:%mvn_version"
    %mvn_file \
        "io.netty:netty-$netty_mod:jar:%native_classifier:%mvn_version" \
        "netty/netty-$netty_mod-%native_classifier"
done
%mvn_file :{*} netty/@1

%build
java -cp "$(build-classpath groovy hppc/hppc ant ant-launcher)" \
    groovy.ui.GroovyMain %SOURCE2 "$PWD/common"
CFLAGS="%optflags" CXXFLAGS="%optflags" \
    %mvn_build -j -- \
        --fail-at-end %{?netty_maven_profiles} \
    -Dmaven.source.skip=true \
    -Dmaven.compiler.release= \
    -Dmaven.compiler.fork=true \
    -Dmaven.compiler.executable=%_jvmdir/java-17-openjdk/bin/javac

xmvn --batch-mode --offline \
    -Dmaven.compiler.release= -Dmaven.compiler.source=8 \
    org.fedoraproject.xmvn:xmvn-mojo:javadoc

%install
%mvn_install -J target/xmvn-apidocs
install -d %buildroot%_jnidir
find transport-native-epoll/target transport-native-io_uring/target \
    -type f -name 'libnetty_transport_native_*.so' \
    -exec install -m755 '{}' %buildroot%_jnidir/ ';'
test -n "$(find %buildroot%_jnidir -name '*epoll*.so' -print -quit)"
test -n "$(find %buildroot%_jnidir -name '*io_uring*.so' -print -quit)"
find codec-native-quic/target/native-lib-only -type f -name 'libnetty_quiche42_*.so' \
    -exec install -m755 '{}' %buildroot%_jnidir/ ';'
test -n "$(find %buildroot%_jnidir -name '*quiche42*.so' -print -quit)"

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt quiche-boringssl-headers/LICENSE
%_jnidir/libnetty_transport_native_*.so
%_jnidir/libnetty_quiche42_*.so

%files bom -f .mfiles-bom

%files testlib -f .mfiles-testlib

%changelog
* Fri Nov 20 2026 Ivan Khanas <xeno@altlinux.org> 4.2.20-alt1
- New version.
- Fix FTBFS: fix i586 JNI and large-file transfers.

* Thu Jun 25 2026 Evgeniy Serov <scala@altlinux.org> 4.1.130-alt1
- Updated to 4.1.130.
- Switched netty-bom to noarch packaging.

* Mon May 18 2026 Evgeniy Serov <scala@altlinux.org> 4.1.100-alt1
- Updated to 4.1.100.
- Returned to Sisyphus.

* Thu Jun 03 2021 Igor Vlasenko <viy@altlinux.org> 4.1.51-alt1_1jpp8
- new version, use jvm8

* Mon May 10 2021 Igor Vlasenko <viy@altlinux.org> 4.1.13-alt1_14jpp8
- update

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 4.1.13-alt1_12jpp8
- update

* Tue Apr 02 2019 Igor Vlasenko <viy@altlinux.ru> 4.1.13-alt1_9jpp8
- fixed build (closes: #36463)

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 4.1.13-alt1_6jpp8
- java update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 4.1.13-alt1_5jpp8
- java fc28+ update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 4.1.13-alt1_2jpp8
- java update

* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 4.1.13-alt1_1jpp8
- new version

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.42-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.28-alt1_3jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.28-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 3.6.6-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 3.6.3-alt1_3jpp7
- new version

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 3.5.11-alt3_1jpp7
- added BR: for xmvn

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.5.11-alt2_1jpp7
- rebuild with maven-local

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 3.5.11-alt1_1jpp7
- fc update

* Mon Oct 08 2012 Igor Vlasenko <viy@altlinux.ru> 3.5.8-alt1_1jpp7
- new version

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 3.5.3-alt1_1jpp7
- new version

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 3.2.4-alt1_2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies