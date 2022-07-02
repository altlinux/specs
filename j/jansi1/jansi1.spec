Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           jansi1
Version:        1.18
Release:        alt1_11jpp11
Summary:        Generate and interpret ANSI escape sequences in Java
License:        ASL 2.0
URL:            https://fusesource.github.io/jansi/

Source0:        https://github.com/fusesource/jansi/archive/jansi-project-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.fusesource:fusesource-pom:pom:)
BuildRequires:  mvn(org.fusesource.hawtjni:hawtjni-runtime)
BuildRequires:  mvn(org.fusesource.jansi:jansi-native)
Source44: import.info

%description
Jansi is a small Java library that allows you to use ANSI escape
sequences in your Java console applications.  It implements ANSI support
on platforms which don't support it like Windows and provides graceful
degradation when output is sent to output devices which cannot support
ANSI sequences.

%package        javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description    javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jansi-jansi-project-%{version}


%pom_disable_module example
%pom_xpath_remove "pom:build/pom:extensions"

%pom_remove_plugin -r :maven-site-plugin

# No maven-uberize-plugin
%pom_remove_plugin -r :maven-uberize-plugin

# Remove unnecessary deps for jansi-native builds
cd jansi
%pom_remove_dep :jansi-windows32
%pom_remove_dep :jansi-windows64
%pom_remove_dep :jansi-osx
%pom_remove_dep :jansi-freebsd32
%pom_remove_dep :jansi-freebsd64
# it's there only to be bundled in uberjar and we disable uberjar generation
%pom_remove_dep :jansi-linux32
%pom_remove_dep :jansi-linux64
cd -

# javadoc generation fails due to strict doclint in JDK 8
%pom_remove_plugin -r :maven-javadoc-plugin

# Build for JDK 1.8 at a minimum for JDK 17 compatibility
%pom_xpath_set //pom:source 1.8
%pom_xpath_set //pom:target 1.8

%build
%mvn_compat_version org.fusesource.jansi:jansi %{version} 1
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference license.txt
%doc readme.md changelog.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference license.txt

%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1.18-alt1_11jpp11
- update

* Fri Jun 04 2021 Igor Vlasenko <viy@altlinux.org> 1.18-alt1_7jpp11
- new version

