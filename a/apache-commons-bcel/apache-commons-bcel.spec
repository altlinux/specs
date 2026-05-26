Name:           apache-commons-bcel
Epoch:          1
Version:        6.12.0
Release:        alt1

Summary:        Byte Code Engineering Library
License:        Apache-2.0
Group:          Development/Java
URL:            https://commons.apache.org/bcel/
VCS:            https://github.com/apache/commons-bcel

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)

BuildArch:      noarch

%description
The Byte Code Engineering Library (Apache Commons BCEL) is intended to give
users a convenient way to analyze, create, and manipulate (binary) Java class
files (those ending with .class). Classes are represented by objects which
contain all the symbolic information of the given class: methods, fields and
byte code instructions, in particular.

Such objects can be read from an existing file, be transformed by a program
(e.g. a class loader at run-time) and written to a file again. An even more
interesting application is the creation of classes from scratch at run-time.
The Byte Code Engineering Library (BCEL) may be also useful if you want to
learn about the Java Virtual Machine (JVM) and the format of Java .class files.

BCEL contains a byte code verifier named JustIce, which usually gives you much
better information about what's wrong with your code than the standard JVM
message.

BCEL is already being used successfully in several projects such as compilers,
optimizers, obsfuscators, code generators and analysis tools. Unfortunately
there hasn't been much development going on over the past few years. Feel free
to help out or you might want to have a look into the ASM project at objectweb.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-source-plugin

%mvn_alias : bcel: apache:
%mvn_file : %name bcel

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%doc *.md

%changelog
* Thu May 21 2026 Evgeniy Serov <scala@altlinux.org> 1:6.12.0-alt1
- Updated to 6.12.0.
- Renamed package to apache-commons-bcel.

* Sat Nov 30 2024 Andrey Cherepanov <cas@altlinux.org> 1:6.8.2-alt1
- New version.
- Fix license according to SPDX.

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 1:6.5.0-alt1_2jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1:6.4.1-alt1_7jpp11
- update

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 1:6.4.1-alt1_2jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1:6.3.1-alt1_2jpp8
- new version

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 1:6.2-alt1_4jpp8
- fc update & java 8 build

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 1:6.2-alt1_2jpp8
- java update

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
