Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          compress-lzf
Version:       1.0.4
Release:       alt1_2jpp11
Summary:       Basic LZF codec, compatible with standard C LZF package
License:       ASL 2.0
URL:           https://github.com/ning/compress
Source0:       %{url}/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.fasterxml:oss-parent:pom:)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.testng:testng)

BuildArch:     noarch
Source44: import.info

%description
Compression codec for LZF encoding for particularly encoding/decoding,
with reasonable compression. Compressor is basic Lempel-Ziv codec,
without Huffman (deflate/gzip) or statistical post-encoding. See
"http://oldhome.schmorp.de/marc/liblzf.html" for more on
original LZF package.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n compress-%{name}-%{version}

%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"

%pom_add_dep junit:junit::test

%mvn_file : %{name}

%build
%mvn_build -- -Dmaven.compile.source=1.8 -Dmaven.compile.target=1.8 -Dmaven.javadoc.source=1.8 -Poffline-testing -Dmaven.test.skip=true

%install
%mvn_install

%files -f .mfiles
%doc README.md VERSION.txt
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
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

