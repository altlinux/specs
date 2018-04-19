Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           javaewah
Version:        1.1.6
Release:        alt1_3jpp8
Summary:        A word-aligned compressed variant of the Java bitset class

License:        ASL 2.0
URL:            https://github.com/lemire/javaewah
Source0:        https://github.com/lemire/javaewah/archive/JavaEWAH-%{version}.tar.gz

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
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -qn javaewah-JavaEWAH-%{version}

# Plugins that are unnecessary for RPM build
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :jacoco-maven-plugin

# Avoids JVM startup error when jacoco-maven-plugin is not in use
%pom_xpath_inject "pom:project/pom:properties" "<argLine/>"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG README.md
%doc --no-dereference LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE-2.0.txt

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_3jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_2jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.6-alt1_1jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_7jpp8
- new fc release

* Tue Nov 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_6jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt1_5jpp8
- new version

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 0.8.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

