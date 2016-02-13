Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define fedora 23
# Conditionals to help breaking bookkeeper <-> hadoop dependency cycle
%if 0%{?fedora}
#def_with hadoop
%bcond_with hadoop
# Unavailable deps: log4cxx was retired
#def_with libhedwig
%bcond_with libhedwig
# Unsupported surefire plugin configuration
#[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.18.1:test (default-test) on project bookkeeper-server: ExecutionException: java.lang.RuntimeException: The forked VM terminated without properly saying goodbye. VM crash or System.exit called?
#def_with test
%bcond_with test
%endif

Name:          bookkeeper
Version:       4.3.2
Release:       alt1_2jpp8
Summary:       Replicated log service
License:       ASL 2.0
URL:           http://bookkeeper.apache.org/
Source0:       http://www.apache.org/dist/bookkeeper/%{name}-%{version}/%{name}-%{version}-src.tar.gz
# Add support for guava 18
Patch0:        bookkeeper-4.3.2-guava18.patch
# Add support for jline 2.+
Patch1:        bookkeeper-4.3.2-jline2.+.patch

BuildRequires: maven-local
BuildRequires: mvn(com.codahale.metrics:metrics-core)
BuildRequires: mvn(com.codahale.metrics:metrics-graphite)
BuildRequires: mvn(com.codahale.metrics:metrics-jvm)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.protobuf:protobuf-java)
BuildRequires: mvn(commons-cli:commons-cli)
BuildRequires: mvn(commons-collections:commons-collections)
BuildRequires: mvn(commons-configuration:commons-configuration)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(io.netty:netty:3)
BuildRequires: mvn(jline:jline) >= 2.12.1
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(net.java.dev.jna:jna)
BuildRequires: mvn(org.apache:apache:pom:)
BuildRequires: mvn(org.apache.derby:derby)
BuildRequires: mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires: mvn(org.apache.geronimo.specs:specs-parent:pom:)
%if %{with hadoop}
BuildRequires: mvn(org.apache.hadoop:hadoop-common)
BuildRequires: mvn(org.apache.hadoop:hadoop-hdfs)
%endif
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.zookeeper:zookeeper)
BuildRequires: mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-log4j12)
BuildRequires: protobuf-compiler

%if %{with test}
BuildRequires: mvn(commons-codec:commons-codec)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(commons-logging:commons-logging)
BuildRequires: mvn(org.apache.bookkeeper:bookkeeper-server)
#BuildRequires: mvn(org.apache.bookkeeper:bookkeeper-server:4.0.0)
#BuildRequires: mvn(org.apache.bookkeeper:bookkeeper-server:4.1.0)
#BuildRequires: mvn(org.apache.bookkeeper:bookkeeper-server:4.2.0)
BuildRequires: mvn(org.apache.bookkeeper:hedwig-server)
#BuildRequires: mvn(org.apache.bookkeeper:hedwig-server:4.0.0)
#BuildRequires: mvn(org.apache.bookkeeper:hedwig-server:4.1.0)
#BuildRequires: mvn(org.apache.bookkeeper:hedwig-server:4.2.0)
BuildRequires: mvn(org.apache.maven.plugins:maven-shade-plugin)
%endif

%if %{with libhedwig}
# hedwig-client cpp
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: boost-devel boost-devel-headers boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel
BuildRequires: libtool
BuildRequires: log4cxx-devel
BuildRequires: libssl-devel
BuildRequires: libprotobuf-devel
%else
BuildArch:     noarch
%endif
Source44: import.info

%description
BookKeeper is a replicated log service which can be used to
build replicated state machines. A log contains a sequence
of events which can be applied to a state machine. BookKeeper
guarantees that each replica state machine will see all the
same entries, in the same order.

%if %{with libhedwig}
%package -n libhedwig
Group: Development/Java
Summary:       Hedwig C client library

%description  -n libhedwig
This package provides a C client interface to Hedwig server.

%package -n libhedwig-devel
Group: Development/Java
Summary:       Development files for the Hedwig C client library
Requires:      libhedwig%{?_isa} = %{version}

%description  -n libhedwig-devel
Development files for the Hedwig C client library.
%endif

%if %{with hadoop}
%package benchmark
Group: Development/Java
Summary:       BookKeeper Benchmark
BuildArch:     noarch

%description benchmark
BookKeeper Benchmark.
%endif

%package codahale-metrics-provider
Group: Development/Java
Summary:       BookKeeper Stats provider for Codahale Metrics
BuildArch:     noarch

%description codahale-metrics-provider
BookKeeper Stats provider for Codahale Metrics.

%package hedwig-client
Group: Development/Java
Summary:       BookKeeper Hedwig Client
BuildArch:     noarch

%description hedwig-client
BookKeeper Hedwig Client.

%package hedwig-client-jms
Group: Development/Java
Summary:       BookKeeper Hedwig Client JMS
BuildArch:     noarch

%description hedwig-client-jms
BookKeeper Hedwig Client JMS.

%package hedwig-protocol
Group: Development/Java
Summary:       BookKeeper Hedwig Protocol
BuildArch:     noarch

%description hedwig-protocol
BookKeeper Hedwig Protocol.

%package hedwig-server
Group: Development/Java
Summary:       BookKeeper Hedwig Server
BuildArch:     noarch

%description hedwig-server
BookKeeper Hedwig Server.

%package parent
Group: Development/Java
Summary:       BookKeeper Parent POM
BuildArch:     noarch

%description parent
This package provide BookKeeper Parent POM.

%package server
Group: Development/Java
Summary:       BookKeeper Server
BuildArch:     noarch
# Remove on F>24
Obsoletes:     %{name}-java < %{version}-%{release}
Provides:      %{name}-java = %{version}-%{release}

%description server
This package provide BookKeeper Server Library.

%package stats-api
Group: Development/Java
Summary:       BookKeeper Stats APIs
BuildArch:     noarch

%description stats-api
This package provide Stats API for BookKeeper.

%package stats-providers
Group: Development/Java
Summary:       BookKeeper Stats Providers Parent POM
BuildArch:     noarch

%description stats-providers
This package provide BookKeeper Stats Providers Parent POM.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch:     noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
find .  -name "*.jar" -print -delete
find .  -name "*.class" -print -delete

%patch0 -p1
%patch1 -p1

sed -i '/Xlint/d' pom.xml
%pom_xpath_remove pom:compilerArguments

%pom_xpath_set pom:properties/pom:netty.version 3
# Unavailable
%pom_remove_plugin -r :findbugs-maven-plugin
# Unwanted
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-assembly-plugin
%pom_remove_plugin -r :license-maven-plugin %{name}-server
%pom_remove_plugin -r :maven-clean-plugin %{name}-server
%pom_remove_plugin -r :maven-dependency-plugin %{name}-server
%pom_remove_plugin -r :maven-dependency-plugin hedwig-server

# Unavailable build deps
# com.twitter.common:stats:0.0.64
# com.twitter.common:net-http-handlers:0.0.39
# com.twitter.common:stats-time-series:0.0.36
# com.twitter.common:stats-jvm:0.0.33
# org.eclipse.jetty:jetty-server:8.1.4.v20120524
# org.eclipse.jetty:jetty-servlet:8.1.4.v20120524
%pom_disable_module twitter-science-provider %{name}-stats-providers
# com.twitter:ostrich_2.9.2:9.1.3
%pom_disable_module twitter-ostrich-provider %{name}-stats-providers

# package org.apache.commons.collections does not exist
%pom_add_dep commons-collections:commons-collections:3.2.1 %{name}-server

%pom_change_dep -r :log4j ::1.2.17 %{name}-server hedwig-client hedwig-client-jms hedwig-server

%pom_change_dep :geronimo-spec-jms org.apache.geronimo.specs:geronimo-jms_1.1_spec:1.1.1 hedwig-client-jms

%if %{without hadoop}
%pom_disable_module %{name}-benchmark
%endif

# Regenerate these files
rm -r bookkeeper-server/src/main/java/org/apache/bookkeeper/proto/DataFormats.java
rm -r hedwig-protocol/src/main/java/org/apache/hedwig/protocol/PubSubProtocol.java

# somersaults out
%if %{without test}
%pom_remove_plugin -r :maven-shade-plugin %{name}-server
%pom_disable_module compat-deps
%pom_remove_dep :bookkeeper-server-compat400 %{name}-server
%pom_remove_dep :bookkeeper-server-compat410 %{name}-server
%pom_remove_dep :bookkeeper-server-compat420 %{name}-server
%pom_remove_dep :hedwig-server-compat400 hedwig-server
%pom_remove_dep :hedwig-server-compat410 hedwig-server
%pom_remove_dep :hedwig-server-compat420 hedwig-server
%else
# NoClassDefFoundError: org/jboss/bk_v4_1_0/netty/channel/socket/ClientSocketChannelFactory
sed -i "s|<include>org.jboss.*:*</include>|<include>io.netty:netty:3</include>|" compat-deps/*-server-compat-*/pom.xml

# java.lang.Exception: Unexpected exception, expected<org.apache.bookkeeper.util.DiskChecker$DiskWarnThresholdException> but was<java.lang.IllegalArgumentException>
# org.apache.bookkeeper.util.DiskChecker$DiskOutOfSpaceException: Space left on device 0 Used space fraction:1.0 < threshold 0.95
rm -r %{name}-server/src/test/java/org/apache/bookkeeper/util/TestDiskChecker.java
# org.apache.bookkeeper.bookie.LedgerDirsManager$NoWritableLedgerDirException: All ledger directories are non writable
rm -r %{name}-server/src/test/java/org/apache/bookkeeper/test/BookieClientTest.java \
 %{name}-server/src/test/java/org/apache/bookkeeper/test/ConcurrentLedgerTest.java \
 %{name}-server/src/test/java/org/apache/bookkeeper/bookie/EntryLogTest.java \
 %{name}-server/src/test/java/org/apache/bookkeeper/bookie/LedgerCacheTest.java
# java.io.IOException: No space left on device
rm -r %{name}-server/src/test/java/org/apache/bookkeeper/bookie/CreateNewLogTest.java \
 %{name}-server/src/test/java/org/apache/bookkeeper/bookie/BookieJournalTest.java \
 %{name}-server/src/test/java/org/apache/bookkeeper/bookie/IndexPersistenceMgrTest.java

%mvn_package :compat-deps __noinstall
%mvn_package :bookkeeper-server-compat400 __noinstall
%mvn_package :bookkeeper-server-compat410 __noinstall
%mvn_package :bookkeeper-server-compat420 __noinstall
%mvn_package :hedwig-server-compat400 __noinstall
%mvn_package :hedwig-server-compat410 __noinstall
%mvn_package :hedwig-server-compat420 __noinstall
%endif

%build

# Test skipped for unavailable test deps: bookkeeper-server-compat* hedwig-server-compat*
%if %{without test}
opts="-f"
%endif
%mvn_build -s $opts -- -Pprotobuf,codahale-metrics-provider

%if %{with libhedwig}
pushd hedwig-client/src/main/cpp
rm -rf autom4te.cache
libtoolize
autoreconf -fi
%configure --disable-static --disable-rpath
# thanks to Björn Esser get rid of unused-shlib-dep
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
# Remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{__make} %{?_smp_mflags}
popd
%endif

%install
%mvn_install

%if %{with libhedwig}
pushd hedwig-client/src/main/cpp
%{__make} install DESTDIR=%{buildroot}
popd

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -n libhedwig
%{_libdir}/libhedwig*.so.*
%doc hedwig-client/src/main/cpp/README
%doc LICENSE NOTICE

%files -n libhedwig-devel
%{_includedir}/hedwig-*/
%{_libdir}/libhedwig*.so
%{_libdir}/pkgconfig/hedwig-*.pc
%endif

%if %{with hadoop}
%files benchmark -f .mfiles-%{name}-benchmark
%endif

%files parent -f .mfiles-%{name}
%doc LICENSE NOTICE

%files codahale-metrics-provider -f .mfiles-codahale-metrics-provider

%files hedwig-client -f .mfiles-hedwig-client
%files hedwig-client-jms -f .mfiles-hedwig-client-jms
%files hedwig-protocol -f .mfiles-hedwig-protocol
%doc LICENSE NOTICE

%files hedwig-server -f .mfiles-hedwig-server
%files server -f .mfiles-%{name}-server

%files stats-api -f .mfiles-%{name}-stats-api
%doc CHANGES.txt README
%doc LICENSE NOTICE

%files stats-providers -f .mfiles-%{name}-stats-providers

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Feb 13 2016 Igor Vlasenko <viy@altlinux.ru> 4.3.2-alt1_2jpp8
- new version

