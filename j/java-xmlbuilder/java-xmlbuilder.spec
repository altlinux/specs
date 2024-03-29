Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          java-xmlbuilder
Version:       1.1
Release:       alt1_8jpp11
Summary:       XML Builder Java library for creating XML documents
License:       ASL 2.0
Url:           https://github.com/jmurty/java-xmlbuilder
Source0:       https://github.com/jmurty/java-xmlbuilder/archive/v%{version}.tar.gz
BuildRequires: sonatype-oss-parent
BuildRequires: base64
# test deps
BuildRequires: junit

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildArch:     noarch
Source44: import.info

%description
XML Builder is a utility that creates simple XML documents using relatively
sparse Java code.

It is intended to allow for quick and painless creation of XML documents 
where you might otherwise be tempted to use concatenated strings, and 
where you would rather not face the tedium and verbosity of coding with JAXP.

%package javadoc
Group: Development/Documentation
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

# Unwanted
%pom_remove_plugin :maven-gpg-plugin
# Unwanted - disable source jar
%pom_remove_plugin :maven-source-plugin
# Unwanted - disable javadoc jar
%pom_remove_plugin :maven-javadoc-plugin

# Fix CRLF
sed -i 's/\r//' LICENSE-2.0.txt

#pom_xpath_remove "pom:build/pom:pluginManagement"

%mvn_file :%{name} %{name}

%build

%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.md README.md
%doc --no-dereference LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE-2.0.txt

%changelog
* Tue Aug 16 2022 Igor Vlasenko <viy@altlinux.org> 0:1.1-alt1_8jpp11
- jdk17 support

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_8jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_7jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_2jpp8
- java 8 mass update

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.4-alt1_1jpp6
- new version

