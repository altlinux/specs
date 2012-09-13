Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
# TODO: junit QA tests

Name:           jfreechart
Version:        1.0.14
Release:        alt1_2jpp7
Summary:        Java chart library

Group:          Development/Java
License:        LGPLv2+
URL:            http://www.jfree.org/jfreechart/
Source0:        http://download.sourceforge.net/sourceforge/jfreechart/%{name}-%{version}.tar.gz

Requires:       servlet jpackage-utils
Requires:       jcommon >= 1.0.17
BuildRequires:  %{requires} ant eclipse-swt servlet

BuildArch:      noarch
Source44: import.info

%description
JFreeChart is a free 100%% Java chart library that makes it easy for
developers to display professional quality charts in their applications.


%package swt
Summary:        Experimental swt extension for jfreechart
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       eclipse-swt jpackage-utils

%description swt
Experimental swt extension for jfreechart.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.



%description javadoc -l fr
Javadoc pour %{name}.

%prep
%setup -q

# Erase prebuilt files
find \( -name '*.jar' -o -name '*.class' \) -exec rm -f '{}' \;

%build
CLASSPATH=$(build-classpath jcommon servlet) \
        ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f ant/build.xml \
        compile javadoc
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f ant/build-swt.xml \
        -Dswt.jar=%{_libdir}/java/swt.jar \
        -Djcommon.jar=$(build-classpath jcommon) \
        -Djfreechart.jar=lib/jfreechart-%{version}.jar


%install
# Directory structure
install -d $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d $RPM_BUILD_ROOT%{_mavenpomdir}

# JARs and JavaDoc
install -m 644 lib/jfreechart-%{version}.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}.jar
install -m 644 lib/swtgraphics2d.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}/swtgraphics2d.jar
install -m 644 lib/jfreechart-%{version}-swt.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-swt.jar
cp -rp javadoc/. $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom

# DEPMAP
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}.jar
%doc ChangeLog licence-LGPL.txt NEWS README.txt

%files swt
%{_javadir}/%{name}/swtgraphics2d*.jar
%{_javadir}/%{name}/%{name}-swt*.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt1_2jpp7
- new version

* Wed Jan 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt3_3jpp6
- fixed repolib dep on jcommon

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt2_3jpp6
- new jpp relase

* Wed Oct 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt2_2jpp6
- fixed jcommon version in repolib

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt1_2jpp6
- added pom

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt2_4jpp5
- new jpp release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Oct 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.5-alt1_1jpp1.7
- updated to new jpackage release

* Tue Apr 26 2005 Eugene V. Horohorin <genix@altlinux.ru> 1.0.0-alt0.1pre2
- First build for ALTLinux
