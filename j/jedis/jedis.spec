Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          jedis
Version:       2.7.2
Release:       alt1_7jpp8
Summary:       A redis Java client
License:       MIT
URL:           https://github.com/xetorthio/jedis
Source0:       https://github.com/xetorthio/jedis/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.commons:commons-pool2)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
Jedis is a blazingly small and sane Redis java client.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find . -name "*.bat" -delete
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-source-plugin
# Use default javadoc setting to override doclint issues
%pom_remove_plugin :maven-javadoc-plugin

# These tests fails. Caused by: java.net.ConnectException: Connection refused
rm -r src/test/java/redis/clients/jedis/tests/ConnectionCloseTest.java \
 src/test/java/redis/clients/jedis/tests/ConnectionTest.java \
 src/test/java/redis/clients/jedis/tests/JedisClusterTest.java \
 src/test/java/redis/clients/jedis/tests/JedisSentinelPoolTest.java \
 src/test/java/redis/clients/jedis/tests/JedisSentinelTest.java \
 src/test/java/redis/clients/jedis/tests/JedisPoolTest.java \
 src/test/java/redis/clients/jedis/tests/JedisTest.java \
 src/test/java/redis/clients/jedis/tests/PipeliningTest.java \
 src/test/java/redis/clients/jedis/tests/ShardedJedisPipelineTest.java \
 src/test/java/redis/clients/jedis/tests/ShardedJedisPoolTest.java \
 src/test/java/redis/clients/jedis/tests/ShardedJedisTest.java \
 src/test/java/redis/clients/jedis/tests/commands/AllKindOfValuesCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/BinaryValuesCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/BitCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/ClusterCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/ConnectionHandlingCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/ControlCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/HashesCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/HyperLogLogCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/ListCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/ObjectCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/PublishSubscribeCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/ScriptingCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/SetCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/SlowlogCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/SortedSetCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/SortingCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/StringValuesCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/TransactionCommandsTest.java \
 src/test/java/redis/clients/jedis/tests/commands/VariadicCommandsTest.java

%mvn_file : %{name}

%build

%mvn_build 

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.7.2-alt1_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.2-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.7.2-alt1_5jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.2-alt1_4jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.2-alt1_3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.7.2-alt1_2jpp8
- new version

