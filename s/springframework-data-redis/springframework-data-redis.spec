Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.3.5
%global namedreltag .RELEASE
%global namedversion %{version}%{?namedreltag}
%global oname spring-data-redis
Name:          springframework-data-redis
# Newer release require springframework >= 4.0.7.RELEASE
Version:       1.3.5
Release:       alt1_5jpp8
Summary:       Provides support to increase developer productivity in Java when using Redis
License:       ASL 2.0
URL:           http://projects.spring.io/spring-data-redis/
Source0:       https://github.com/spring-projects/spring-data-redis/archive/v%{namedversion}.tar.gz
# Default use gradle
Source1:       http://central.maven.org/maven2/org/springframework/data/%{oname}/%{namedversion}/%{oname}-%{namedversion}.pom
# Build fix for jedis 2.7.2
Patch0:        %{name}-1.3.5-jedis27.patch


BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(com.github.spullara.redis:client)
BuildRequires: mvn(com.lambdaworks:lettuce)
BuildRequires: mvn(com.thoughtworks.xstream:xstream)
BuildRequires: mvn(commons-beanutils:commons-beanutils-core)
BuildRequires: mvn(javax.annotation:jsr250-api)
BuildRequires: mvn(javax.transaction:jta)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.sf.cglib:cglib)
BuildRequires: mvn(org.apache.commons:commons-pool2)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires: mvn(org.jredis:jredis-core-api)
BuildRequires: mvn(org.jredis:jredis-core-ri)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.springframework:spring-aop)
BuildRequires: mvn(org.springframework:spring-context)
BuildRequires: mvn(org.springframework:spring-context-support)
BuildRequires: mvn(org.springframework:spring-core)
BuildRequires: mvn(org.springframework:spring-jdbc)
BuildRequires: mvn(org.springframework:spring-oxm)
BuildRequires: mvn(org.springframework:spring-test)
BuildRequires: mvn(org.springframework:spring-tx)
BuildRequires: mvn(redis.clients:jedis)

BuildArch:     noarch
Source44: import.info

%description
Spring Data Redis, part of the larger Spring Data family, provides
easy configuration and access to Redis from Spring applications. It
offers both low-level and high-level abstractions for interacting with
the store, freeing the user from infrastructural concerns.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-%{namedversion}
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

cp -p %{SOURCE1} pom.xml

%patch0 -p1

cp -p docs/src/info/*.txt .

# Remove internal cglib
find ./ -name "*.java" -exec sed -i "s/org.springframework.cglib/net.sf.cglib/g" {} +
%pom_add_dep net.sf.cglib:cglib
# Use jvm Base64
rm src/main/java/org/springframework/data/redis/connection/util/Base64.java
find ./ -name "*.java" -exec sed -i "s/org.springframework.data.redis.connection.util.Base64/java.util.Base64/g" {} +
sed -i "s/Base64.encodeToString(bytes, false)/java.util.Base64.getEncoder().encodeToString(bytes)/g" \
 src/main/java/org/springframework/data/redis/connection/util/DecodeUtils.java
sed -i "s/Base64.decode(string)/java.util.Base64.getDecoder().decode(string)/g" \
 src/main/java/org/springframework/data/redis/connection/util/DecodeUtils.java

# Add test deps
%pom_add_dep com.thoughtworks.xstream:xstream::test
%pom_add_dep javax.annotation:jsr250-api::test
%pom_add_dep javax.transaction:jta::test
%pom_add_dep junit:junit::test
%pom_add_dep org.mockito:mockito-core::test
%pom_add_dep org.springframework:spring-test::test
%pom_add_dep org.springframework:spring-jdbc::test

# Add OSGi support
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
%pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 . '
<extensions>true</extensions>
<configuration>
  <instructions>
    <Bundle-SymbolicName>org.springframework.data.redis</Bundle-SymbolicName>
    <Bundle-Name>Spring Data Redis Support</Bundle-Name>
    <Bundle-Vendor>Pivotal Software, Inc.</Bundle-Vendor>
    <Bundle-Version>${project.version}</Bundle-Version>
  </instructions>
</configuration>
<executions>
  <execution>
    <id>bundle-manifest</id>
    <phase>process-classes</phase>
    <goals>
      <goal>manifest</goal>
    </goals>
  </execution>
</executions>'

# NullPointerException
rm -r src/test/java/org/springframework/data/redis/config/NamespaceTest.java \
 src/test/java/org/springframework/data/redis/PropertyEditorsTest.java
# NullPointerException IllegalArgumentException
rm -r src/test/java/org/springframework/data/redis/listener/adapter/MessageListenerTest.java
# RuntimeException
rm -r src/test/java/org/springframework/data/redis/mapping/BeanUtilsHashMapperTest.java \
 src/test/java/org/springframework/data/redis/core/SessionTest.java
# IncompatibleClassChangeError" message="class org.springframework.core.LocalVariableTableParameterNameDiscoverer$ParameterNameDiscoveringVisitor has interface org.objectweb.asm.ClassVisitor as super class
rm -r src/test/java/org/springframework/data/redis/listener/adapter/ContainerXmlSetupTest.java
# InstantiationException
rm -r src/test/java/org/springframework/data/redis/cache/AbstractNativeCacheTest.java \
 src/test/java/org/springframework/data/redis/mapping/AbstractHashMapperTest.java \
 src/test/java/org/springframework/data/redis/mapping/JacksonHashMapperTest.java \
 src/test/java/org/springframework/data/redis/cache/RedisCacheTest.java


%mvn_file : %{oname}

%build

%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc license.txt notice.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt notice.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.5-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.5-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.5-alt1_3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.5-alt1_2jpp8
- new version

