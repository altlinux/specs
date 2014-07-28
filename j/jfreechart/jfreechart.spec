Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%define fedora 21
# TODO: junit QA tests

Name:           jfreechart
Version:        1.0.14
Release:        alt3_9jpp7
Summary:        Java chart library

Group:          Development/Java
License:        LGPLv2+
URL:            http://www.jfree.org/jfreechart/
Source0:        http://download.sourceforge.net/sourceforge/jfreechart/%{name}-%{version}.tar.gz
Source1:        bnd.properties

Requires:       servlet jpackage-utils
Requires:       jcommon >= 1.0.17
BuildRequires:  %{requires} ant servlet
%if 0%{?fedora}
BuildRequires:  eclipse-swt
%endif
# Required for converting jars to OSGi bundles
BuildRequires:  aqute-bnd

BuildArch:      noarch
Patch0:         remove_itext_dep.patch
Source44: import.info

%description
JFreeChart is a free 100% Java chart library that makes it easy for
developers to display professional quality charts in their applications.

%if 0%{?fedora}
%package swt
Summary:        Experimental swt extension for jfreechart
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       eclipse-swt jpackage-utils

%description swt
Experimental swt extension for jfreechart.
%endif

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
%patch0

%build
CLASSPATH=$(build-classpath jcommon servlet) \
        ant -f ant/build.xml \
        compile javadoc
%if 0%{?fedora}
# See RHBZ#912664. There seems to be some dispute about build-classpath.
# So don't use it for swt.
ant -f ant/build-swt.xml \
        -Dswt.jar=%{_libdir}/eclipse/swt.jar \
        -Djcommon.jar=$(build-classpath jcommon) \
        -Djfreechart.jar=lib/jfreechart-%{version}.jar
%endif
# Convert to OSGi bundle
java -Djfreechart.bundle.version="%{version}" -jar $(build-classpath aqute-bnd) \
   wrap -output lib/%{name}-%{version}.bar -properties %{SOURCE1} lib/%{name}-%{version}.jar

%install
# Directory structure
install -d $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d $RPM_BUILD_ROOT%{_mavenpomdir}

# JARs and JavaDoc
install -m 644 lib/jfreechart-%{version}.bar  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}.jar
%if 0%{?fedora}
install -m 644 lib/swtgraphics2d.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}/swtgraphics2d.jar
install -m 644 lib/jfreechart-%{version}-swt.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-swt.jar
%endif
cp -rp javadoc/. $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# POM
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom

# DEPMAP
%add_maven_depmap -a "%{name}:%{name}" JPP.%{name}-%{name}.pom %{name}/%{name}.jar
ln -s %{name}/%{name}.jar %buildroot%{_javadir}/%{name}.jar

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}.jar
%doc ChangeLog licence-LGPL.txt NEWS README.txt
%{_javadir}/%{name}.jar

%if 0%{?fedora}
%files swt
%{_javadir}/%{name}/swtgraphics2d*.jar
%{_javadir}/%{name}/%{name}-swt*.jar
%endif

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt3_9jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt3_3jpp7
- new fc release

* Sat Sep 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt3_2jpp7
- added jpp compat symlink

* Sat Sep 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.14-alt2_2jpp7
- added jfreechart:jfreechart depmap

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
