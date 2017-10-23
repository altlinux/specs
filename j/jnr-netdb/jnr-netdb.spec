# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:    jnr-netdb
Version: 1.1.5
Release: alt1_3jpp8
Summary: Network services database access for java

Group:   System/Libraries
License: ASL 2.0
URL:     http://github.com/jnr/%{name}/
Source0: https://github.com/jnr/%{name}/archive/%{version}.tar.gz
BuildArch: noarch

BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: jnr-ffi
BuildRequires: junit
BuildRequires: jffi

BuildRequires:  maven-local
BuildRequires:  sonatype-oss-parent

Requires: jpackage-utils
Requires: jnr-ffi
Source44: import.info

%description
jnr-netdb is a java interface to getservbyname(3), getservbyport(3)

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
%mvn_build

%install
%mvn_install

%files  -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt1_3jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.5-alt1_1jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_2jpp8
- java 8 mass update

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_2jpp7
- new version

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_7jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_6jpp7
- new version

