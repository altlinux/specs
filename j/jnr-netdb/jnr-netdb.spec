# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:    jnr-netdb
Version: 1.1.5
Release: alt1_1jpp8
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

