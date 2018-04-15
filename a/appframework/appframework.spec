# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:    appframework
Version: 1.03
Release: alt2_19jpp8
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
BuildRequires: java-devel >= 1.6.0
BuildRequires: swing-layout >= 1.0.3

Requires: java >= 1.6.0
Requires: javapackages-tools

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
find . -name "*.jar" -exec rm -f {} \;

%patch0 -b .sav
%patch1 -p1 -b .sav
%patch2 -b .sav

%build
%{ant} -Dlibs.swing-layout.classpath=%{_javadir}/swing-layout.jar dist

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/AppFramework-1.03.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*
%doc COPYING README

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_19jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2_18jpp8
- fc27 update

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

