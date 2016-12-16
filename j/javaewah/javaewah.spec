# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global commit c6a7fca48eb10572c57e8f644c11633456611d8f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           javaewah
Version:        0.8.4
Release:        alt1_7jpp8
Summary:        A word-aligned compressed variant of the Java bitset class

Group:          Development/Other
License:        ASL 2.0
URL:            http://code.google.com/p/javaewah/
Source0:        https://github.com/lemire/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info


%description
JavaEWAH is a word-aligned compressed variant of the Java bitset class.
It uses a 64-bit run-length encoding (RLE) compression scheme.

The goal of word-aligned compression is not to achieve the best
compression, but rather to improve query processing time. Hence, we try
to save CPU cycles, maybe at the expense of storage. However, the EWAH
scheme we implemented is always more efficient storage-wise than an
uncompressed bitmap (implemented in Java as the BitSet class). Unlike
some alternatives, javaewah does not rely on a patented scheme.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -qn %{name}-%{commit}

%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG README.md LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_7jpp8
- new fc release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_6jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_5jpp8
- new version

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

