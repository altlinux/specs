Name: xerces-j2
Version: 2.11.0
Summary: Java XML parser
License: ASL 2.0
Url: http://xerces.apache.org/xerces2-j/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jaxp_parser_impl = 1.4
Provides: mvn(apache:xerces-j2) = 2.11.0
Provides: mvn(apache:xerces-j2:pom:) = 2.11.0
Provides: mvn(xerces:xerces) = 2.11.0
Provides: mvn(xerces:xerces:pom:) = 2.11.0
Provides: mvn(xerces:xercesImpl) = 2.11.0
Provides: mvn(xerces:xercesImpl:pom:) = 2.11.0
Provides: mvn(xerces:xmlParserAPIs) = 2.11.0
Provides: mvn(xerces:xmlParserAPIs:pom:) = 2.11.0
Provides: xerces-j2 = 2.11.0-23.fc23
Provides: xerces-j2-scripts = 2.11.0-23.fc23
Requires: /bin/sh
Requires: /bin/sh
Requires: /bin/sh
Requires: chkconfig
Requires: chkconfig
Requires: java-headless
Requires: java-headless
Requires: jaxp_parser_impl
Requires: jaxp_parser_impl
Requires: jpackage-utils
Requires: jpackage-utils
Requires: xalan-j2
Requires: xml-commons-apis
Requires: xml-commons-resolver

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: xerces-j2-2.11.0-23.fc23.cpio

%description
Welcome to the future! Xerces2 is the next generation of high performance,
fully compliant XML parsers in the Apache Xerces family. This new version of
Xerces introduces the Xerces Native Interface (XNI), a complete framework for
building parser components and configurations that is extremely modular and
easy to program.

The Apache Xerces2 parser is the reference implementation of XNI but other
parser components, configurations, and parsers can be written using the Xerces
Native Interface. For complete design and implementation documents, refer to
the XNI Manual.

Xerces2 is a fully conforming XML Schema processor. For more information,
refer to the XML Schema page.

Xerces2 also provides a complete implementation of the Document Object Model
Level 3 Core and Load/Save W3C Recommendations and provides a complete
implementation of the XML Inclusions (XInclude) W3C Recommendation. It also
provides support for OASIS XML Catalogs v1.1.

Xerces2 is able to parse documents written according to the XML 1.1
Recommendation, except that it does not yet provide an option to enable
normalization checking as described in section 2.13 of this specification. It
also handles name spaces according to the XML Namespaces 1.1 Recommendation,
and will correctly serialize XML 1.1 documents if the DOM level 3 load/save
APIs are in use.

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

%preun
{
  [ $1 = 0 ] || exit 0
  update-alternatives --remove jaxp_parser_impl /usr/share/java/xerces-j2.jar
} >/dev/null 2>&1 || :

%post
update-alternatives --install /usr/share/java/jaxp_parser_impl.jar \
  jaxp_parser_impl /usr/share/java/xerces-j2.jar 40


%files -f %name-list

%changelog
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.11.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.11.0-alt1_16jpp7
- new release

* Thu Jul 31 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.11.0-alt1_14jpp7
- new release

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.11.0-alt1_11jpp7
- fc update

* Sat Mar 30 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt4_2jpp6
- bugfixes

* Fri Mar 29 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt3_2jpp6
- added pom

* Sat Mar 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt2_2jpp6
- build w/java6

* Fri Dec 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.9.1-alt1_2jpp6
- added OSGi provides

* Tue Jan 13 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.9.0-alt6_12jpp5
- added repolib as in jpp 5.0 template

* Sat Apr 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.9.0-alt5_2jpp1.7
- fixed script permissions

* Wed Feb 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.9.0-alt4_2jpp1.7
- converted from JPackage by jppimport script

* Wed Feb 06 2008 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt4
- added Provides: xerces-j2-demo to demo.
- demo subpackage is now xerces-j2 compatible.

* Tue Aug 21 2007 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt3
- rebuilt with java-1.5.0

* Mon May 21 2007 Igor Vlasenko <viy@altlinux.ru> 2.9.0-alt2
- NMU: 
  * fixes for X-less build
  * fixed bug in alternatives (jaxp_parser_impl.jar)
  * javadocs are split almost as they should be
  * added scripts subpackage

* Tue Apr 24 2007 Eugene Ostapets <eostapets@altlinux.ru> 2.9.0-alt1
- 2.9.0 

* Tue Apr 24 2007 Eugene Ostapets <eostapets@altlinux.ru> 2.8.1-alt2
- fix build with java-1.6-sun
- add compatibility with JPackage

* Wed Nov 15 2006 Eugene Ostapets <eostapets@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Sat Mar 11 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.8.0-alt1
- 2.8.0
- Updated Patch1

* Sun Feb 26 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.1-alt2
- Fixes to build with JDK 1.5

* Wed Jul 27 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.1-alt1
- New upstream release

* Mon Jun 27 2005 Mikhail Zabaluev <mhz@altlinux.ru> 2.7.0-alt1
- New upstream release
- Raised jaxp_parser_impl.jar alternative level to 130
  to reflect the JAXP 1.3 implementation
- Updated Patch1
- Use rpm-build-java macros
- Conditionally build samples, disabled by default
  (can not compile with 1.4.2)

* Tue Aug 31 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt2
- New alternatives format

* Mon Mar 08 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt1
- Remove JDK version hardcoding

* Sun Feb 22 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.2-alt0.1
- Updated to upstream release 2.6.2

* Wed Jan 21 2004 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt3.1
- Temporarily hardcode the JDK

* Sat Dec 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt3
- Patches from Alexey Borovskoy
- Use xvfb-run to start fake X server
- Migration to new alternatives scheme

* Sat Dec 20 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt2
- Added update-alternatives to install-time dependencies
- Corrected timing of updating alternatives during uninstall/upgrade
- Set JAVA_HOME to the commonly known J2SE directory

* Thu Dec 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.6.0-alt1
- New upstream release

* Thu Sep 11 2003 Mikhail Zabaluev <mhz@altlinux.ru> 2.5.0-alt1
- Updated to 2.5.0, renamed to xerces-j because xerces 1.x is obsolete
- Dropped README from the docs as it contains nothing but build instructions
- Remove JAXP api docs from javadoc, link to xml-commons-apis instead

* Sun Nov 17 2002 Mikhail Zabaluev <mhz@altlinux.ru> 2.2.1-alt1
- Ported the package over from the JPackage project. Thank you guys.
