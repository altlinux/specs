Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          lzma-java
Version:       1.3
Release:       alt1_9jpp11
Summary:       LZMA library for Java
# Source files without license headers https://github.com/jponge/lzma-java/issues/13
# Public Domain: ./src/main/java/lzma/sdk/*  ./src/test/java/lzma/*
License:       ASL 2.0 and Public Domain
URL:           http://jponge.github.io/lzma-java/
Source0:       https://github.com/jponge/lzma-java/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(junit:junit)
# ./src/main/java/lzma/ http://www.7-zip.org/sdk.html
Provides:      bundled(lzma-sdk-java) = 16.02
BuildArch:     noarch
Source44: import.info

%description
This library is based on the Java LZMA SDK by Igor Pavlov.
It brings many improvements, including Java conventions and
a Java I/O streaming API.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-release-plugin

%mvn_file com.github.jponge:%{name} %{name}

%build

%mvn_build -- -Dmaven.compile.source=1.8 -Dmaven.compile.target=1.8 -Dmaven.javadoc.source=1.8

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.3-alt1_9jpp11
- update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_6jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_4jpp8
- java update

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3jpp8
- new version

