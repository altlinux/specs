Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          compress-lzf
Version:       1.0.3
Release:       alt1_7jpp8
Summary:       Basic LZF codec, compatible with standard C LZF package
License:       ASL 2.0
URL:           https://github.com/ning/compress
Source0:       https://github.com/ning/compress/archive/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.surefire:surefire-testng)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
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

find . -name "*.class" -print -delete
find . -name "*.jar" -type f -print -delete

%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:project/pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"

%pom_add_dep junit:junit::test

%mvn_file : %{name}

%build

%mvn_build -- -Poffline-testing

%install
%mvn_install

%files -f .mfiles
%doc README.md VERSION.txt
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_7jpp8
- new version

