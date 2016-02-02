Name: xalan-j2-xsltc
Version: 2.7.1
Summary: XSLT compiler
License: ASL 2.0 and W3C
Url: http://xalan.apache.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(xalan:xsltc) = 2.7.1
Provides: mvn(xalan:xsltc:pom:) = 2.7.1
Provides: xalan-j2-xsltc = 0:2.7.1-27.fc23
Requires: bcel
Requires: java-headless
Requires: java_cup
Requires: jpackage-utils
Requires: regexp
Requires: xerces-j2

BuildArch: noarch
Group: Development/Java
Release: alt3jpp
Source: xalan-j2-xsltc-2.7.1-27.fc23.cpio

%description
The XSLT Compiler is a Java-based tool for compiling XSLT stylesheets into
lightweight and portable Java byte codes called translets.

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
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt2_21jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt2_18jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt2_17jpp7
- update

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt2_16jpp7
- new release

* Sun Dec 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt2_1jpp6
- fixed xerces dependency in repolib

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.7.1-alt1_1jpp6
- added OSGi provides to serializer.jar

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt6_10jpp5
- fixed repocop warnings

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt6_9jpp5
- jpp5 build

* Tue May 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt6_7jpp1.7
- rebuild on x86_64; added explicit source and target 1.4
- obsoletes: xalan-j

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt5_7jpp1.7
- rebuild on x86_64; added explicit source and target 1.4
- obsoletes: xalan-j

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.7.0-alt3_7jpp1.7
- converted from JPackage by jppimport script

* Tue Jun 20 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.0-alt3
- Fixed the dependency in xalan-j-manual

* Sat Mar 04 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.0-alt2
- Install serializer.jar

* Sun Feb 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.0-alt1
- 2.7.0
- Use new xml-commons-external

* Sat Jan 15 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt3
- Enable xsltc by default
- Converted to rpm-build-java macros
- Stripped the source archive from unnecessary jars.
  Building from original archive is still available via --with origsrc

* Fri Aug 27 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt2
- Do not BuildRequire system stylebook as it BuildRequires xalan-j
- New alternatives format (ugh)
- Grouped everything under Development/Java

* Sat Apr 17 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt1
- New upstream release
- Updated manifest patch

* Mon Jan 12 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.2-alt3
- Migration to the new alternatives scheme

* Fri Dec 19 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.2-alt2
- Build using XML APIs and a JAXP parser installed in the system
- Enabled javadoc back
- Added update-alternatives to install-time dependencies
- Added xml-commons-apis to Requires

* Thu Dec 18 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.2-alt1
- New upstream release

* Sat Sep 13 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.1-alt1
- Ported to ALT Linux from JPackage project
- Don't build xsltc and demo for now, due to dependencies.
