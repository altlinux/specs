Group: System/Libraries
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:    jnr-netdb
Version: 1.1.6
Release: alt1_12jpp11
Summary: Network services database access for java
License: ASL 2.0
URL:     https://github.com/jnr/%{name}/
Source0: https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jnr-ffi)
BuildRequires:  mvn(junit:junit)
Source44: import.info

%description
jnr-netdb is a java interface to getservbyname(3), getservbyport(3)

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Fix javadoc generation on java 11
%pom_xpath_inject pom:project "<build><plugins><plugin>
<artifactId>maven-javadoc-plugin</artifactId>
<configuration>
<source>1.6</source>
<detectJavaApiLink>false</detectJavaApiLink>
</configuration>
</plugin></plugins></build>"


%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -Dmaven.compiler.source=1.6 -Dmaven.compiler.target=1.6

%install
%mvn_install

%files  -f .mfiles
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Fri Jun 11 2021 Igor Vlasenko <viy@altlinux.org> 1.1.6-alt1_12jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.1.6-alt1_10jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_7jpp8
- fc update

* Sat Jul 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_5jpp8
- fc update & java 8 build

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_2jpp8
- new version

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

