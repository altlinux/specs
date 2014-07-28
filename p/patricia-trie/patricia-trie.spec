# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           patricia-trie
Version:        0.2
Release:        alt1_5.20091116svnjpp7
Summary:        Java prefix tree library

Group:          Development/Java
License:        ASL 2.0
URL:            http://patricia-trie.googlecode.com/
# svn export -r108 http://patricia-trie.googlecode.com/svn/trunk@108 patricia-trie
# tar czf patricia-trie.tar.gz patricia-trie
Source0:        %{name}.tar.gz

BuildRequires:  ant
BuildRequires:  java-devel-openjdk
BuildRequires:  jpackage-utils
Requires:       jpackage-utils

BuildArch:      noarch
Source44: import.info

%description
Patricia is a prefix-tree (trie) implementation written in Java.


%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc HTML documentation for %{name}.


%prep
%setup -q -n %{name}


%build
find -name '*.jar' -delete
ant


%install

install -d $RPM_BUILD_ROOT%{_javadir}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -p -m644 dist/%{name}-%{version}/%{name}-%{version}.jar \
        $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

cp -a dist/%{name}-%{version}/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%doc dist/%{name}-%{version}/LICENSE-2.0.txt
%doc dist/%{name}-%{version}/RELEASE-NOTES.txt


%files javadoc
%{_javadocdir}/%{name}


%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_5.20091116svnjpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_4.20091116svnjpp7
- new version

