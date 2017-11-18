BuildRequires: javapackages-local
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%define _without_gcj 1
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           swing-layout
Version:        1.0.4
Release:        alt2_13jpp8
Summary:        Natural layout for Swing panels
License:        LGPLv2
URL:            https://swing-layout.dev.java.net/
# https://svn.java.net/svn/swing-layout~svn/trunk/
Source0:        %{name}-%{version}-src.zip
# from http://java.net/jira/secure/attachment/27303/pom.xml
Source1:        %{name}-pom.xml
# use javac target/source 1.5
Patch0:         %{name}-%{version}-project_properties.patch
Patch1:         %{name}-%{version}-fix-incorrect-fsf-address.patch

BuildRequires:  jpackage-utils >= 1.6
BuildRequires:  java-devel >= 1.3
BuildRequires:  ant
BuildRequires:  dos2unix
Requires:       java >= 1.3

BuildArch:      noarch
Source44: import.info

%description
Extensions to Swing to create professional cross platform layout.

%if 0
%package javadoc
Group: Development/Java
Summary:        Javadoc documentation for Swing Layout
BuildArch: noarch

%description javadoc
Documentation for Swing Layout code.
%endif

%prep
%setup -q
dos2unix releaseNotes.txt
%patch0 -p0
%patch1 -p0
sed -i 's/\r//' COPYING

cp -p %{SOURCE1} pom.xml
sed -i "s|<version>1.0.3</version>|<version>%{version}</version>|" pom.xml

%build

%{ant} jar \
#   [javadoc] Loading source files for package org.jdesktop.layout...
#   [javadoc] 1 error
#   [javadoc] java.lang.IllegalStateException: endPosTable already set
%if 0
 javadoc dist
%endif
 
%install

mkdir -p %{buildroot}%{_javadir}

%if 0
install -m 644 dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
%else
install -m 644 dist/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
%endif

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%if 0
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%endif

%files -f .mfiles
%doc releaseNotes.txt
%doc COPYING

%if 0
%files javadoc
%{_javadocdir}/%{name}
%doc COPYING
%endif

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_13jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_13jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_12jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_11jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_7jpp7
- new release

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_5jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_4jpp7
- update to new release by jppimport

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3jpp6
- update to new release by jppimport

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_6jpp6
- added pom

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4jpp6
- new build for netbeans

* Mon Dec 08 2008 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2jpp5
- converted from JPackage by jppimport script

