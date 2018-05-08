Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jnr-unixsocket
Version:        0.18
Release:        alt1_5jpp8
Summary:        Unix sockets for Java
License:        ASL 2.0
URL:            https://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jnr-constants)
BuildRequires:  mvn(com.github.jnr:jnr-enxio) >= 0.16
BuildRequires:  mvn(com.github.jnr:jnr-ffi)
BuildRequires:  mvn(com.github.jnr:jnr-posix)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

Requires:  mvn(com.github.jnr:jnr-enxio) >= 0.16
Source44: import.info

%description
Unix sockets for Java.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# remove unnecessary wagon extension
%pom_xpath_remove pom:build/pom:extensions

# Unnecessary for RPM builds
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-javadoc-plugin

# Can't run integration tests
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :exec-maven-plugin

# Remove enxio classes to avoid split-package problems, see https://github.com/jnr/jnr-unixsocket/pull/41
rm -r src/main/java/jnr/enxio

# Fix jar plugin usage
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions"

find ./ -name '*.jar' -delete 
find ./ -name '*.class' -delete

%build
# Tests fails on some arches
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_5jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_3jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_3jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_3jpp8
- java 8 mass update

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_1jpp7
- new release

