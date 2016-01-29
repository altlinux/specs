Name: javacc
Version: 5.0
Summary: A parser/scanner generator for java
License: BSD
Url: http://javacc.java.net/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: javacc = 0:5.0-13.fc23
Provides: mvn(net.java.dev.javacc:javacc) = 4.2
Provides: mvn(net.java.dev.javacc:javacc:pom:) = 4.2
Requires: /bin/sh
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt5jpp
Source: javacc-5.0-13.fc23.cpio

%description
Java Compiler Compiler (JavaCC) is the most popular parser generator for use
with Java applications. A parser generator is a tool that reads a grammar
specification and converts it to a Java program that can recognize matches to
the grammar. In addition to the parser generator itself, JavaCC provides other
standard capabilities related to parser generation such as tree building (via
a tool called JJTree included with JavaCC), actions, debugging, etc.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt4_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt4_8jpp7
- new release

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt4_7jpp7
- applied repocop patches

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt3_7jpp7
- new fc release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt3_5jpp7
- applied repocop patches

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt2_5jpp7
- added bindir/javacc for the sake of openjpa

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt1_5jpp7
- fc version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt1_5jpp6
- new jpp relase

* Thu Apr 15 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2-alt1_1jpp5.qa1
- NMU (by repocop): the following fixes applied:
  * pkg-contains-cvs-or-svn-control-dir for javacc-manual
  * postclean-05-filetriggers for spec file

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2-alt1_1jpp5
- new jpackage release

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

* Fri Mar 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 4.0-alt1
- 4.0
- Use macros from rpm-build-java
- Patch0: set target version for javac

* Tue Sep 09 2003 Mikhail Zabaluev <mhz@altlinux.ru> 3.2-alt1
- Released for ALT Linux
