Name: objectweb-asm
Version: 5.0.3
Summary: Java bytecode manipulation and analysis framework
License: BSD
Url: http://asm.ow2.org/
Epoch: 0
Provides: /etc/java/objectweb-asm.conf
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.ow2.asm:asm) = 5.0.3
Provides: mvn(org.ow2.asm:asm-all) = 5.0.3
Provides: mvn(org.ow2.asm:asm-all:pom:) = 5.0.3
Provides: mvn(org.ow2.asm:asm-analysis) = 5.0.3
Provides: mvn(org.ow2.asm:asm-analysis:pom:) = 5.0.3
Provides: mvn(org.ow2.asm:asm-commons) = 5.0.3
Provides: mvn(org.ow2.asm:asm-commons:pom:) = 5.0.3
Provides: mvn(org.ow2.asm:asm-debug-all) = 5.0.3
Provides: mvn(org.ow2.asm:asm-debug-all:pom:) = 5.0.3
Provides: mvn(org.ow2.asm:asm-parent:pom:) = 5.0.3
Provides: mvn(org.ow2.asm:asm-tree) = 5.0.3
Provides: mvn(org.ow2.asm:asm-tree:pom:) = 5.0.3
Provides: mvn(org.ow2.asm:asm-util) = 5.0.3
Provides: mvn(org.ow2.asm:asm-util:pom:) = 5.0.3
Provides: mvn(org.ow2.asm:asm-xml) = 5.0.3
Provides: mvn(org.ow2.asm:asm-xml:pom:) = 5.0.3
Provides: mvn(org.ow2.asm:asm:pom:) = 5.0.3
Provides: objectweb-asm = 5.0.3-2.fc23
Provides: objectweb-asm4 = 5.0.3-2.fc23
Requires: /bin/bash
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: objectweb-asm-5.0.3-2.fc23.cpio

%description
ASM is an all purpose Java bytecode manipulation and analysis
framework.  It can be used to modify existing classes or dynamically
generate classes, directly in binary form.  Provided common
transformations and analysis algorithms allow to easily assemble
custom complex transformations and code analysis tools.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_7jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_4jpp7
- update

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt5_4jpp6
- updated OSGi manifest to match version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt4_4jpp6
- added pom groupid asm

* Sun Oct 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt3_4jpp6
- fixed poms

* Fri Sep 16 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt2_4jpp6
- removed asm2 pom provides

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt1_4jpp6
- new version

* Sat Feb 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_2jpp6
- added osgi manifest

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_2jpp6
- new version

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt2_5jpp5
- added OSGi manifest

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_3jpp5
- converted from JPackage by jppimport script

* Mon Jan 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

