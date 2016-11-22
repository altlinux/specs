Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           xz-java
Version:        1.5
Release:        alt1_5jpp8
Summary:        Java implementation of XZ data compression
License:        Public Domain
URL:            http://tukaani.org/xz/java.html
BuildArch:      noarch

Source0:        http://tukaani.org/xz/xz-java-%{version}.zip

BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant

Requires: javapackages-tools rpm-build-java
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

%build
# During documentation generation the upstream build.xml tries to download
# package-list from oracle.com. Create a dummy package-list to prevent that.
mkdir -p extdoc && touch extdoc/package-list

ant maven

%install
# jar
install -dm 755 %{buildroot}%{_javadir}
install -m 644 build/jar/xz.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/xz.jar
# javadoc
install -dm 755 %{buildroot}%{_javadocdir}
cp -R build/doc %{buildroot}%{_javadocdir}/%{name}
# pom
install -dm 755 %{buildroot}%{_mavenpomdir}
install -pm 644 build/maven/xz-%{version}.pom %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

%files -f .mfiles
%doc COPYING README THANKS
%{_javadir}/xz.jar

%files javadoc
%doc COPYING
%{_javadocdir}/%{name}

%changelog
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

