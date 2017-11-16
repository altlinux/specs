Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          lzma-java
Version:       1.3
Release:       alt1_3jpp8
Summary:       LZMA library for Java
# Source files without license headers https://github.com/jponge/lzma-java/issues/13
# Public Domain: ./src/main/java/lzma/sdk/*  ./src/test/java/lzma/*
License:       ASL 2.0 and Public Domain
URL:           http://jponge.github.io/lzma-java/
Source0:       https://github.com/jponge/lzma-java/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
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

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-release-plugin

%mvn_file com.github.jponge:%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3jpp8
- new version

