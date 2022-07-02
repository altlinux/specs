Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           spec-version-maven-plugin
Version:        1.5
Release:        alt1_6jpp11
Summary:        Spec Version Maven Plugin
License:        CDDL or GPLv2 with exceptions

# project moved to eclipse-ee4j for versions > 1.5
# https://github.com/eclipse-ee4j/glassfish-spec-version-maven-plugin
URL:            https://github.com/javaee/spec-version-maven-plugin
Source0:        https://github.com/javaee/spec-version-maven-plugin/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
Source44: import.info

%description
Maven Plugin to configure APIs version and specs in a MANIFEST.MF file.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q


sed -i "s|mvn|mvn-rpmbuild|" src/main/resources/checkVersion.sh

# Build for JDK 1.8 instead of 1.6
sed -i 's/1\.6/1.8/g' pom.xml

# remove unnecessary dependency on parent POM
%pom_remove_parent

# remove unnecessary maven plugins
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-checkstyle-plugin

%mvn_file :%{name} %{name}


%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8


%install
%mvn_install


%files -f .mfiles
%doc --no-dereference LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE


%changelog
* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1.5-alt1_6jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.5-alt1_1jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_15jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_13jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_11jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_10jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_9jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_8jpp8
- new fc release

* Sun Jan 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_7jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_1jpp7
- new release

