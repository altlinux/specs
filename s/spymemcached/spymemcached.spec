Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          spymemcached
Version:       2.11.4
Release:       alt1_7jpp8
Summary:       Java client for memcached
# ASL src/scripts/write-version-info.sh
License:       ASL 2.0 and MIT
Url:           https://github.com/dustin/java-memcached-client
Source0:       https://github.com/dustin/java-memcached-client/archive/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.codahale.metrics:metrics-core)
BuildRequires: mvn(log4j:log4j:1.2.17)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.springframework:spring-beans)

%if 0
# test deps
BuildRequires: mvn(jmock:jmock) >= 1.2.0
BuildRequires: mvn(junit:junit)
%endif

Requires:      mvn(log4j:log4j:1.2.17)

BuildArch:     noarch
Source44: import.info

%description
A simple, asynchronous, single-threaded memcached client written in java.

%package javadoc
Group: Development/Documentation
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n java-memcached-client-%{version}
find -name '*.jar' -delete
find -name '*.class' -delete

sed -i "s|2.999.999-SNAPSHOT|%{version}|" pom.xml
sed -i.log4j12 "s|<version>1.2.16|<version>1.2.17|" pom.xml

native2ascii -encoding UTF-8 src/main/java/net/spy/memcached/MemcachedConnection.java \
 src/main/java/net/spy/memcached/MemcachedConnection.java

# Unavailable test dep
%pom_remove_dep :jmock

%mvn_file :%{name} %{name}
%mvn_alias :%{name} spy:spymemcached spy:memcached

%build

%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc README.markdown
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.11.4-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.11.4-alt1_6jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.11.4-alt1_5jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.11.4-alt1_3jpp8
- new version

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt2_1jpp6
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_1jpp6
- new version

