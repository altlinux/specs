Name: slf4j
Version: 1.7.12
Summary: Simple Logging Facade for Java
License: MIT and ASL 2.0
Url: http://www.slf4j.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.slf4j:slf4j-api) = 1.7.12
Provides: mvn(org.slf4j:slf4j-api:pom:) = 1.7.12
Provides: mvn(org.slf4j:slf4j-nop) = 1.7.12
Provides: mvn(org.slf4j:slf4j-nop:pom:) = 1.7.12
Provides: mvn(org.slf4j:slf4j-simple) = 1.7.12
Provides: mvn(org.slf4j:slf4j-simple:pom:) = 1.7.12
Provides: slf4j = 0:1.7.12-2.fc23
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: slf4j-1.7.12-2.fc23.cpio

%description
The Simple Logging Facade for Java or (SLF4J) is intended to serve
as a simple facade for various logging APIs allowing to the end-user
to plug in the desired implementation at deployment time. SLF4J also
allows for a gradual migration path away from
Jakarta Commons Logging (JCL).

Logging API implementations can either choose to implement the
SLF4J interfaces directly, e.g. NLOG4J or SimpleLogger. Alternatively,
it is possible (and rather easy) to write SLF4J adapters for the given
API implementation, e.g. Log4jLoggerAdapter or JDK14LoggerAdapter..

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.5-alt1_3jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.4-alt1_1jpp7
- update

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt4_4jpp7
- more symlinks

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt3_4jpp7
- added compat symlinks

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt2_4jpp7
- rebuild with maven-local

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt1_4jpp7
- update

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7.1-alt1_1jpp7
- new version

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.6-alt1_2jpp7
- new version

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt3_5jpp7
- fc version

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_5jpp7
- fc version

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_5jpp6
- new version

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_4jpp6
- new version (full build)

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_4jpp6
- new version (bootstrap)

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.8-alt1_1jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Feb 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_2jpp1.7
- updated to new jpackage release

* Mon Dec 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt2_1jpp1.7
- added dependency on new excalibur

* Wed Nov 14 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

