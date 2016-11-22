# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:    appframework
Version: 1.03
Release: alt2_16jpp8
Summary: Swing Application Framework
License: LGPLv2+
URL:     https://appframework.dev.java.net/
Group:   Development/Other

Source0: https://appframework.dev.java.net/downloads/AppFramework-1.03-src.zip
Patch0:  %{name}-%{version}-no-local-storage.diff
Patch1:  %{name}-%{version}-openjdk.diff
Patch2:  %{name}-%{version}-disable-doclint.diff

BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: swing-layout >= 1.0.3


Requires: swing-layout >= 1.0.3

BuildArch: noarch
Source44: import.info

%description
The JSR-296 Swing Application Framework prototype implementation is a small 
set of Java classes that simplify building desktop applications.

%package javadoc
Summary: Javadoc for %{name}
Group:   Development/Java
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep

%setup -q -n AppFramework-%{version}

# remove all binary libs
find . -name "*.jar" -exec %{__rm} -f {} \;

%patch0 -b .sav
%patch1 -p1 -b .sav
%patch2 -b .sav

%build
%{ant} -Dlibs.swing-layout.classpath=%{_javadir}/swing-layout.jar dist

%install
# jar
%{__install} -d -m 755 %{buildroot}%{_javadir}
%{__install} -m 644 dist/AppFramework-1.03.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
%{__install} -d -m 755 %{buildroot}%{_javadocdir}/%{name}
%{__cp} -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*
%doc COPYING README

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_16jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_15jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_12jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_10jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_9jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_8jpp7
- update to new release by jppimport

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_7jpp6
- update to new release by jppimport

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_6jpp6
- added pom

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_6jpp6
- new build for netbeans

* Fri Dec 12 2008 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_4jpp6
- converted from JPackage by jppimport script

