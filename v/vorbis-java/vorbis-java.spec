Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
%define fedora 30
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Conditionals to help breaking vorbis-java-tika <-> tika dependency cycle
%if 0%{?fedora}
%bcond_without tika
%endif

Name:          vorbis-java
Version:       0.8
Release:       alt1_5jpp8
Summary:       Ogg and Vorbis toolkit for Java
License:       ASL 2.0
URL:           https://github.com/Gagravarr/VorbisJava
Source0:       https://github.com/Gagravarr/VorbisJava/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
%if %{without tika}
BuildRequires: mvn(org.apache.tika:tika-core)
%endif

BuildArch:     noarch
Source44: import.info

%description
This library is a pure Java, for working with Ogg and
Vorbis, FLAC, Opus, Speex and Theora files.

%if %{without tika}
%package tika
Group: Development/Java
Summary:       VorbisJava Apache Tika plugin

%description tika
This package contains Apache Tika plugin for Ogg,
Vorbis and FLAC.
%endif

%package tools
Group: Development/Java
Summary:       VorbisJava Tools

%description tools
This package contains VorbisJava Ogg and Vorbis tools for Java.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n VorbisJava-%{name}-%{version}
find . -name "*.class" -delete
find . -name "*.jar" -delete

%if %{with tika}
%pom_disable_module tika
%pom_xpath_remove "pom:dependency[pom:scope = 'test']" tika
%endif

# disable embedded core copy
%pom_remove_plugin :maven-assembly-plugin tools

%pom_remove_plugin :maven-gpg-plugin parent
%pom_remove_plugin :maven-source-plugin parent
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions" parent

%mvn_package :%{name} %{name}
%mvn_package :%{name}-parent %{name}
%mvn_package :%{name}-core %{name}

%build

# Skip test @ random fails on arm builder
%mvn_build -s -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-%{name}
%doc CHANGES.txt README.txt TODO.txt
%doc --no-dereference LICENSE.txt NOTICE.txt

%if %{without tika}
%files tika -f .mfiles-%{name}-tika
%doc --no-dereference LICENSE.txt NOTICE.txt
%endif

%files tools -f .mfiles-%{name}-tools
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

%changelog
* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_5jpp8
- new version; bootstrap build w/o tika

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_2jpp8
- unbootstrap build

