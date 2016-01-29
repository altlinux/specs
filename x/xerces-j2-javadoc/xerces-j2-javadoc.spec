Name: xerces-j2-javadoc
Version: 2.11.0
Summary: Javadocs for xerces-j2
License: ASL 2.0
Url: http://xerces.apache.org/xerces2-j/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: xerces-j2-javadoc = 2.11.0-23.fc23
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: xerces-j2-javadoc-2.11.0-23.fc23.cpio

%description
This package contains the API documentation for xerces-j2.

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
