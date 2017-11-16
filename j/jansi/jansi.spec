Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
Requires: fusesource-pom
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             jansi
Version:          1.16
Release:          alt1_2jpp8
Summary:          Jansi is a java library for generating and interpreting ANSI escape sequences
License:          ASL 2.0
URL:              http://jansi.fusesource.org/

Source0:          https://github.com/fusesource/jansi/archive/jansi-project-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    maven-local
BuildRequires:    jansi-native
BuildRequires:    maven-plugin-bundle
BuildRequires:    fusesource-pom
Source44: import.info

%description
Jansi is a small java library that allows you to use ANSI escape sequences
in your Java console applications. It implements ANSI support on platforms
which don't support it like Windows and provides graceful degradation for
when output is being sent to output devices which cannot support ANSI sequences.

%package javadoc
Group: Development/Java
Summary:          Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jansi-jansi-project-%{version}

%pom_disable_module example
%pom_xpath_remove "pom:build/pom:extensions"

%pom_remove_plugin -r :maven-site-plugin

# No maven-uberize-plugin
%pom_remove_plugin -r :maven-uberize-plugin

# Remove unnecessary deps for jansi-native builds
pushd jansi
%pom_remove_dep :jansi-windows32
%pom_remove_dep :jansi-windows64
%pom_remove_dep :jansi-osx
%pom_remove_dep :jansi-freebsd32
%pom_remove_dep :jansi-freebsd64
# it's there only to be bundled in uberjar and we disable uberjar generation
%pom_remove_dep :jansi-linux32
%pom_remove_dep :jansi-linux64
popd

# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin -r :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc license.txt
%doc readme.md changelog.md

%files javadoc -f .mfiles-javadoc
%doc license.txt

%changelog
* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.16-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_12jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_10jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_9jpp8
- unbootsrap build

* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_3jpp7
- new release

* Thu Oct 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_1jpp7
- new release

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt3_4jpp7
- added Requires: fusesource-pom

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_4jpp7
- added jansi:jansi depmap for jpp packages

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_2jpp7
- fixed pom

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp7
- fc version

* Sat Feb 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp6
- new version

