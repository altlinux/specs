%define _unpackaged_files_terminate_build 1

Name: aho-corasick-double-array-trie
Version: 1.2.3
Release: alt1

Summary: Aho-Corasick string search using a double-array trie
License: Apache-2.0
Group: Development/Java
URL: https://github.com/hankcs/AhoCorasickDoubleArrayTrie
VCS: https://github.com/hankcs/AhoCorasickDoubleArrayTrie

Source0: %name-%version.tar
Source1: LICENSE.Apache-2.0
Patch0: skip-comparison-benchmark.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(junit:junit)

BuildArch: noarch

%description
An implementation of the Aho-Corasick string matching algorithm based on a
double-array trie.

%package javadoc
Summary: API documentation for %name
Group: Development/Documentation

%description javadoc
API documentation for %name.

%prep
%setup -q
%autopatch -p1
cp -p %SOURCE1 LICENSE

%pom_xpath_set pom:project/pom:properties/pom:java.version 8
%pom_remove_dep org.ahocorasick:ahocorasick
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin org.codehaus.sonar:sonar-maven3-plugin

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%name
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 1.2.3-alt1
- Initial build for ALT.
