Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           memoryfilesystem
Version:        0.6.7
Release:        alt1_7jpp8
Summary:        An in memory implementation of a JSR-203 file system
License:        MIT
URL:            https://github.com/marschall/%{name}
Source0:        https://github.com/marschall/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-plugin-bundle maven-surefire-plugin
BuildRequires:  hamcrest easymock springframework-test junit
BuildRequires:  springframework-context logback jcl-over-slf4j
Source44: import.info

%description
An in memory implementation of a JSR-203 file system

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides API documentation for %{name}.

%prep
%setup -q

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin com.github.marschall:jdeps-maven-plugin
%pom_remove_plugin org.jboss.jandex:jandex-maven-plugin

%pom_remove_dep com.github.marschall:zipfilesystem-standalone
%pom_remove_dep org.openjdk.jol:jol-core

# maven-jandex-plugin is currently not packaged
sed -i '/jandex.idx/d' pom.xml
# remove test which need jol-core and zipfilesystem-standalone
rm -rf ./src/test/java/com/github/marschall/memoryfilesystem/MemoryFileTest.java
rm -rf ./src/test/java/com/github/marschall/memoryfilesystem/ZipFileSystemInteropabilityTest.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference src/main/resources/LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.7-alt1_7jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.7-alt1_5jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.7-alt1_4jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.7-alt1_3jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.7-alt1_2jpp8
- new fc release

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.6.7-alt1_1jpp8
- new version

