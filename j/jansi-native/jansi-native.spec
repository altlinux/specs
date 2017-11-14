Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora __isa_bits tmp hack
%ifarch x86_64
%define __isa_bits 64
%else
%define __isa_bits 32
%endif
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global bits %{__isa_bits}
%global debug_package %{nil}

Name:           jansi-native
Version:        1.7
Release:        alt1_3jpp8
Summary:        Jansi Native implements the JNI Libraries used by the Jansi project
Group:          Development/Other
License:        ASL 2.0
URL:            http://jansi.fusesource.org/
Source0:        https://github.com/fusesource/jansi-native/archive/jansi-native-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.fusesource:fusesource-pom:pom:)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-runtime) >= 1.9
BuildRequires:  mvn(org.fusesource.hawtjni:maven-hawtjni-plugin) >= 1.9
Source44: import.info

%description
Jansi is a small java library that allows you to use ANSI escape sequences
in your Java console applications. It implements ANSI support on platforms
which don't support it like Windows and provides graceful degradation for
when output is being sent to output devices which cannot support ANSI sequences.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch:        noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jansi-native-jansi-native-%{version}
%mvn_package :::linux%{bits}:

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc readme.md changelog.md
%doc license.txt

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_3jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_11jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_10jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt2_9jpp8
- %%_jnidir set to /usr/lib/java

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_9jpp8
- java 8 mass update

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_5jpp7
- new release

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp7
- new version

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp7
- new version

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_1jpp6
- fixed build

* Fri Feb 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp6
- new version

