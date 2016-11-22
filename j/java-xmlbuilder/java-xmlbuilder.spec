Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          java-xmlbuilder
Version:       1.1
Release:       alt1_3jpp8
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

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGES.md README.md
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_3jpp8
- new fc release

* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_2jpp8
- java 8 mass update

* Wed Jan 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.4-alt1_1jpp6
- new version

