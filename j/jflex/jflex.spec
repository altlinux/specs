Provides: /etc/java/jflex.conf
Name: jflex
Version: 1.6.1
Summary: Fast Scanner Generator
License: BSD
Url: http://jflex.de/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jflex = 1.6.1-2.fc23
Provides: mvn(de.jflex:jflex) = 1.6.1
Provides: mvn(de.jflex:jflex:pom:) = 1.6.1
Requires: /bin/bash
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(java_cup:java_cup)
Requires: mvn(org.apache.ant:ant)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jflex-1.6.1-2.fc23.cpio

%description
JFlex is a lexical analyzer generator (also known as scanner
generator) for Java, written in Java.  It is also a rewrite of the
very useful tool JLex which was developed by Elliot Berk at Princeton
University.  As Vern Paxson states for his C/C++ tool flex: They do
not share any code though.  JFlex is designed to work together with
the LALR parser generator CUP by Scott Hudson, and the Java
modification of Berkeley Yacc BYacc/J by Bob Jamison.  It can also be
used together with other parser generators like ANTLR or as a
standalone tool.

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
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt5_16jpp7
- new release

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt5_10jpp7
- fc release

* Fri Apr 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt5_1jpp6
- fixed build

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt4_1jpp6
- fixed build with java 7

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt3_1jpp6
- added maven2-plugin-resources dep

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt2_1jpp6
- new version (full build)

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt1_1jpp6
- new version (bootstrap build)

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_3jpp5
- new jpp release

* Tue Dec 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_1jpp5
- fixed classpath

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_1jpp5
- jpp5 build

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.5-alt1_2jpp1.7
- converted from JPackage by jppimport script

