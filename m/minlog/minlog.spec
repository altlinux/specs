Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          minlog
Version:       1.3.0
Release:       alt1_5jpp8
Summary:       Minimal overhead Java logging
License:       BSD
URL:           https://github.com/EsotericSoftware/minlog
Source0:       https://github.com/EsotericSoftware/minlog/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch:     noarch
Source44: import.info

%description
MinLog is a Java logging library. Key features:

A. Zero overhead Logging statements below a given level
  can be automatically removed by javac at compile time.
  This means applications can have detailed trace and
  debug logging without having any impact on the finished product.

A. Simple and efficient The API is concise and the code
  is very efficient at run-time.

A. Extremely lightweight The entire project consists of a single
  Java file with ~100 non-comment lines of code.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find -name "*.class" -delete
find -name "*.jar" -delete

%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin' ]/pom:executions"

sed -i 's/\r//' license.txt

%mvn_file :%{name} %{name}
%mvn_alias :%{name} "com.googlecode:%{name}" "com.esotericsoftware.%{name}:%{name}"
%mvn_package ":%{name}::tests:"

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Wed Nov 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_5jpp8
- fc update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_3jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_2jpp8
- new version

