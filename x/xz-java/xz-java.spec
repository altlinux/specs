%define _unpackaged_files_terminate_build 1

Name: xz-java
Version: 1.10
Release: alt1

Summary: Java implementation of XZ data compression
License: 0BSD
Group: Development/Java
Url: http://tukaani.org/xz/java.html
VCS: https://github.com/tukaani-project/xz-java.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: javapackages-local
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
BuildRequires: ant

%description
A complete implementation of XZ data compression in Java.

It features full support for the .xz file format specification version 1.0.4,
single-threaded streamed compression and decompression, single-threaded
decompression with limited random access support, raw streams (no .xz headers)
for advanced users, including LZMA2 with preset dictionary.

%package javadoc
Group: Development/Java
Summary: Javadocs for xz-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for xz-java.

%prep
%setup

%mvn_file :xz xz-java/xz

%build
# During documentation generation the upstream build.xml tries to download
# package-list from oracle.com. Create a dummy package-list to prevent that.
mkdir -p extdoc && touch extdoc/package-list

%ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8  maven

%install
%mvn_artifact build/maven/xz-%version.pom build/jar/xz.jar

%mvn_install -J build/doc

%files -f .mfiles
%doc README.md THANKS.md
%doc --no-dereference COPYING

%files javadoc -f .mfiles-javadoc
%doc --no-dereference COPYING

%changelog
* Thu Aug 07 2025 Ivan Khanas <xeno@altlinux.org> 1.10-alt1
- New version.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1.9-alt1_3jpp11
- new version

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

