Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           patricia-trie
Version:        0.2
Release:        alt1_11.20091116svnjpp8
Summary:        Java prefix tree library
License:        ASL 2.0
URL:            http://patricia-trie.googlecode.com/
# https://github.com/rkapsi/patricia-trie/archive/patricia-trie-0.6.tar.gz
# svn export -r108 http://patricia-trie.googlecode.com/svn/trunk@108 patricia-trie
# tar czf patricia-trie.tar.gz patricia-trie
Source0:        %{name}.tar.gz

BuildRequires:  ant
BuildRequires: javapackages-tools rpm-build-java
Requires: javapackages-tools rpm-build-java

BuildArch:      noarch
Source44: import.info

%description
Patricia is a prefix-tree (trie) implementation written in Java.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
Javadoc HTML documentation for %{name}.

%prep
%setup -q -n %{name}
find -name '*.jar' -delete

%build

ant

%install

install -d $RPM_BUILD_ROOT%{_javadir}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -p -m644 dist/%{name}-%{version}/%{name}-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
%add_maven_depmap org.ardverk:patricia-trie:%{version} %{name}.jar

cp -a dist/%{name}-%{version}/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files -f .mfiles
%doc dist/%{name}-%{version}/LICENSE-2.0.txt
%doc dist/%{name}-%{version}/RELEASE-NOTES.txt

%files javadoc
%{_javadocdir}/%{name}
%doc dist/%{name}-%{version}/LICENSE-2.0.txt

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_11.20091116svnjpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_10.20091116svnjpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_6.20091116svnjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_5.20091116svnjpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_4.20091116svnjpp7
- new version

