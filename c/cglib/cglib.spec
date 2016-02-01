Name: cglib
Version: 3.1
Summary: Code Generation Library for Java
License: ASL 2.0 and BSD
Url: http://cglib.sourceforge.net/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: cglib = 3.1-7.fc23
Provides: mvn(cglib:cglib) = 3.1
Provides: mvn(cglib:cglib-full) = 3.1
Provides: mvn(cglib:cglib-full:pom:) = 3.1
Provides: mvn(cglib:cglib-nodep) = 3.1
Provides: mvn(cglib:cglib-nodep:pom:) = 3.1
Provides: mvn(cglib:cglib:pom:) = 3.1
Provides: mvn(net.sf.cglib:cglib) = 3.1
Provides: mvn(net.sf.cglib:cglib:pom:) = 3.1
Provides: mvn(org.sonatype.sisu.inject:cglib) = 3.1
Provides: mvn(org.sonatype.sisu.inject:cglib:pom:) = 3.1
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils
Requires: objectweb-asm

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: cglib-3.1-7.fc23.cpio

%description
cglib is a powerful, high performance and quality code generation library
for Java. It is used to extend Java classes and implements interfaces
at runtime.

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
* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_17jpp7
- new release

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_15jpp7
- fc update

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_4jpp6
- added net.sf.cglib group id

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_4jpp6
- added pom

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_4jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_3jpp5
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_2jpp1.7
- converted from JPackage by jppimport script

* Wed May 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt4_2jpp1.7
- fixed provides to avoid unmets on cglib

* Fri May 25 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt3_2jpp1.7
- imported with jppimport script; note: bootstrapped version

* Thu May 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_2jpp1.7
- fixed cglib provides

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_2jpp1.7
- imported with jppimport script; note: bootstrapped version

