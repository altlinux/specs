Name: findbugs
Version: 3.0.1
Summary: Find bugs in Java code
License: LGPLv2+
Url: http://findbugs.sourceforge.net/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: findbugs = 3.0.1-4.fc23
Provides: mvn(com.google.code.findbugs:annotations) = 3.0.1
Provides: mvn(com.google.code.findbugs:annotations:pom:) = 3.0.1
Provides: mvn(com.google.code.findbugs:findbugs) = 3.0.1
Provides: mvn(com.google.code.findbugs:findbugs:pom:) = 3.0.1
Provides: mvn(net.sourceforge.findbugs:annotations) = 3.0.1
Provides: mvn(net.sourceforge.findbugs:annotations:pom:) = 3.0.1
Provides: mvn(net.sourceforge.findbugs:findbugs) = 3.0.1
Provides: mvn(net.sourceforge.findbugs:findbugs:pom:) = 3.0.1
Requires: /bin/sh
Requires: /usr/bin/perl
Requires: apache-commons-lang
Requires: findbugs-bcel
Requires: jFormatString
Requires: java
Requires: java-headless
Requires: jaxen
Requires: jcip-annotations
Requires: jpackage-utils
Requires: jpackage-utils
Requires: jsr-305
Requires: junit
Requires: objectweb-asm

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: findbugs-3.0.1-4.fc23.cpio

%description
Findbugs is a program which uses static analysis to look for bugs in Java code.
It can check for null pointer exceptions, multithreaded code errors, and other
bugs.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list
sed -i -e '/ /d' %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.0.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Aug 02 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.9-alt2_15jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.9-alt2_12jpp7
- converted from JPackage by jppimport script

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.9-alt2_5jpp6
- build with saxon6

* Fri Feb 10 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.9-alt1_5jpp6
- new release

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.9-alt1_2jpp6
- new version

* Mon Nov 17 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.4-alt2_2jpp5
- removed obsolete update_menus

