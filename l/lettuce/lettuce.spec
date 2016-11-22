Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          lettuce
Version:       2.3.3
Release:       alt1_2jpp8
Summary:       Scalable Java Redis client
License:       ASL 2.0
# Newer release available @ https://github.com/mp911de/lettuce
URL:           http://redis.paluch.biz/
Source0:       https://github.com/wg/lettuce/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(io.netty:netty:3)
BuildRequires: mvn(junit:junit)

BuildArch:     noarch
Source44: import.info

%description
Lettuce is a scalable thread-safe Redis client providing both synchronous and
asynchronous connections. Multiple threads may share one connection provided
they avoid blocking and transactional operations such as BLPOP, and MULTI/EXEC.
Multiple connections are efficiently managed by the netty NIO framework.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

%pom_remove_plugin :maven-gpg-plugin

%pom_xpath_set "pom:dependency[pom:artifactId = 'netty']/pom:version" 3

%mvn_file : %{name}

%build

# Tests disabled: use web connection Caused by: java.net.ConnectException: Connection refused: localhost/127.0.0.1:6379
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_2jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_1jpp8
- new version

