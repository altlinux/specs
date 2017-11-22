Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without jna

Name:           bcel
Version:        6.1
Release:        alt1_2jpp8
Epoch:          1
Summary:        Byte Code Engineering Library
License:        ASL 2.0
URL:            http://commons.apache.org/proper/commons-bcel/
Source0:        http://archive.apache.org/dist/commons/bcel/source/bcel-%{version}-src.tar.gz

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%if %{with jna}
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.java.dev.jna:jna-platform)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
%endif
Source44: import.info

%description
The Byte Code Engineering Library (formerly known as JavaClass) is
intended to give users a convenient possibility to analyze, create, and
manipulate (binary) Java class files (those ending with .class). Classes
are represented by objects which contain all the symbolic information of
the given class: methods, fields and byte code instructions, in
particular.  Such objects can be read from an existing file, be
transformed by a program (e.g. a class loader at run-time) and dumped to
a file again. An even more interesting application is the creation of
classes from scratch at run-time. The Byte Code Engineering Library
(BCEL) may be also useful if you want to learn about the Java Virtual
Machine (JVM) and the format of Java .class files.  BCEL is already
being used successfully in several projects such as compilers,
optimizers, obfuscators and analysis tools, the most popular probably
being the Xalan XSLT processor at Apache.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{name}-%{version}-src

%pom_remove_plugin :maven-source-plugin

%pom_xpath_set /pom:project/pom:packaging bundle
%pom_add_plugin org.apache.felix:maven-bundle-plugin '
<extensions>true</extensions>
<configuration>
  <instructions>
    <_nouses>true</_nouses>
    <Export-Package>org.apache.bcel.*</Export-Package>
  </instructions>
</configuration>
'

%mvn_alias : bcel: apache:
%mvn_file : %{name}

# different path in test
sed -i '\|lib/dt\.jar|s|javaHome|javaHome.substring(0, javaHome.length() - 4)|' \
        src/test/java/org/apache/bcel/PerformanceTest.java

%build
%if %{without jna}
%mvn_build -f
%else
%mvn_build
%endif

%install
%mvn_install

%files -f .mfiles
%doc RELEASE-NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:6.1-alt1_2jpp8
- new version

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 1:6.0-alt1_0.7.20140406svn1592769jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:6.0-alt1_0.6.20140406svn1592769jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:6.0-alt1_0.5.20140406svn1592769jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1:6.0-alt1_0.4.20140406svn1592769jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:5.2-alt4_17jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:5.2-alt4_15jpp7
- new release

* Fri Mar 15 2013 Igor Vlasenko <viy@altlinux.ru> 1:5.2-alt4_13jpp7
- fc update

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1:5.2-alt4_3jpp5
- build with saxon6-scripts

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 1:5.2-alt3_3jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 1:5.2-alt2_3jpp5
- use maven1

* Sat May 02 2009 Igor Vlasenko <viy@altlinux.ru> 1:5.2-alt1_3jpp5
- reverted to 5.2

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 1:5.1-alt1_16jpp5
- downgrade to match 5.0; added repolib

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.2-alt2_3jpp1.7
- updated to new jpackage release

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:5.2-alt2_2jpp1.7
- updated to new jpackage release

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:5.2-alt2_1jpp1.7
- fixed [Bug 11852] Misprint in package description

* Mon Jul 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:5.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 5.1-alt3
- added jpackage compatible symlinks
- rebuild with java-1.4

* Sun Feb 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 5.1-alt2
- Patch0: disambiguated use of the Deprecated class to build with JDK 1.5
- Updated Patch1: fixes to build with JDK 1.5
- Use macros from rpm-build-java

* Thu Sep 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 5.1-alt1
- New version
- Patch0 gone upstream
- Removed doc package due to absence of the docs in the source tarball
- Fix the build.xml crack [Patch1]

* Wed Nov 20 2002 Mikhail Zabaluev <mhz@altlinux.ru> 5.0-alt1
- Adopted from JPackage
