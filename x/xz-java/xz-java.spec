Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with bootstrap

Name:           xz-java
Version:        1.8
Release:        alt1_12jpp11
Summary:        Java implementation of XZ data compression
License:        Public Domain
URL:            http://tukaani.org/xz/java.html
BuildArch:      noarch

Source0:        http://tukaani.org/xz/xz-java-%{version}.zip

BuildRequires:  javapackages-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  ant
%endif
Source44: import.info

%description
A complete implementation of XZ data compression in Java.

It features full support for the .xz file format specification version 1.0.4,
single-threaded streamed compression and decompression, single-threaded
decompression with limited random access support, raw streams (no .xz headers)
for advanced users, including LZMA2 with preset dictionary.

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c %{name}-%{version}

%mvn_file : %{name} xz

%build
# During documentation generation the upstream build.xml tries to download
# package-list from oracle.com. Create a dummy package-list to prevent that.
mkdir -p extdoc && touch extdoc/package-list

%ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  maven -Dsourcever=1.6

%install
%mvn_artifact build/maven/xz-%{version}.pom build/jar/xz.jar

%mvn_install -J build/doc

%files -f .mfiles
%doc README THANKS
%doc --no-dereference COPYING

%files javadoc -f .mfiles-javadoc
%doc --no-dereference COPYING

%changelog
* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.8-alt1_12jpp11
- update

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.8-alt1_9jpp11
- update

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_6jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_4jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.8-alt1_2jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_4jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1_2jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_5jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_4jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_1jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_1jpp7
- new version

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2jpp7
- fc update

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_1jpp7
- new version

