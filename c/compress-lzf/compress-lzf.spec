Name:          compress-lzf
Version:       1.2.0
Release:       alt1

Summary:       High-performance, streaming/chunking Java LZF codec, compatible with standard C LZF package
License:       Apache-2.0
Group:         Development/Java
URL:           https://github.com/ning/compress
VCS:           https://github.com/ning/compress

Source0:       %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(com.fasterxml:oss-parent:pom:)

BuildArch:      noarch

%description
LZF-compress is a Java library for encoding and decoding data in LZF format,
written by Tatu Saloranta. Data format and algorithm based on original LZF
library by Marc A Lehmann.

%javadoc_package

%prep
%setup

%pom_remove_plugin :moditect-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin

# missing dep for tests
%pom_remove_dep :jazzer-junit
rm src/test/java/com/ning/compress/lzf/TestFuzzUnsafeLZF.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE VERSION.txt README.md

%changelog
* Wed Apr 15 2026 Evgeniy Serov <scala@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1.0.4-alt1_2jpp11
- new version

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_10jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_9jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_8jpp8
- java update

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_7jpp8
- new version

