Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global oname redis
Name:          redis-protocol
Version:       0.7
Release:       alt1_3jpp8
Summary:       Java client and server implementation of Redis
License:       ASL 2.0
URL:           http://github.com/spullara/redis-protocol
Source0:       https://github.com/spullara/redis-protocol/archive/%{oname}-%{version}.tar.gz
# https://github.com/spullara/redis-protocol/issues/45
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: maven-local
BuildRequires: mvn(com.github.spullara.cli-parser:cli-parser)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(junit:junit)

BuildArch:     noarch
Source44: import.info

%description
A very fast Redis client for the JVM.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{oname}-%{version}

find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

# These modules use com.github.spullara.java:concurrent6
%pom_disable_module netty
# https://bugzilla.redhat.com/show_bug.cgi?id=849496
# org.webbitserver:webbit::test
%pom_disable_module netty-client
# io.netty:netty-all:4.0.0.CR3
%pom_disable_module netty4
%pom_disable_module netty4-client
%pom_disable_module netty4-server

# com.github.spullara.mustache.java:compiler:0.8.9
%pom_disable_module redisgen

%pom_remove_plugin :maven-assembly-plugin benchmark

%build

# use web connection
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_3jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_2jpp8
- new version

