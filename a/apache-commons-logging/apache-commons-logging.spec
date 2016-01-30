Name: apache-commons-logging
Version: 1.2
Summary: Apache Commons Logging
License: ASL 2.0
Url: http://commons.apache.org/logging
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-commons-logging = 1.2-4.fc23
Provides: mvn(apache:commons-logging) = 1.2
Provides: mvn(apache:commons-logging:pom:) = 1.2
Provides: mvn(commons-logging:commons-logging) = 1.2
Provides: mvn(commons-logging:commons-logging-api) = 1.1
Provides: mvn(commons-logging:commons-logging-api:pom:) = 1.1
Provides: mvn(commons-logging:commons-logging:pom:) = 1.2
Provides: mvn(org.apache.commons:commons-logging) = 1.2
Provides: mvn(org.apache.commons:commons-logging-api) = 1.1
Provides: mvn(org.apache.commons:commons-logging-api:pom:) = 1.1
Provides: mvn(org.apache.commons:commons-logging:pom:) = 1.2
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: apache-commons-logging-1.2-4.fc23.cpio

%description
The commons-logging package provides a simple, component oriented
interface (org.apache.commons.logging.Log) together with wrappers for
logging systems. The user can choose at runtime which system they want
to use. In addition, a small number of basic implementations are
provided to allow users to use the package standalone.
commons-logging was heavily influenced by Avalon's Logkit and Log4J. The
commons-logging abstraction is meant to minimize the differences between
the two, and to allow a developer to not tie himself to a particular
logging implementation.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_2jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt8_20jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt7_20jpp7
- fixed build

* Tue Jul 15 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt6_20jpp7
- fixed build

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt5_20jpp7
- added jakarta cpmpat symlinks

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt4_20jpp7
- no not package repolib in main commons-logging

* Tue Aug 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt3_20jpp7
- new release

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt3_6jpp6
- fixed build

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_6jpp6
- synced osgi manifest

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_6jpp6
- new version

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_2jpp6
- new version

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_8jpp5
- updated OSGi manifest

* Fri Jul 04 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_7jpp5
- rebuild with osgi provides

* Mon May 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_4jpp1.7
- updated to new jpackage release

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_3jpp1.7
- added eclipse manifest

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_3jpp1.7
- updated to new jpackage release

* Fri Nov 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_2jpp1.7
- updated to new jpackage release

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt4
- added JPackage compatibility stuff

* Sun Aug 29 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt3
- Disabled check by default due to a circular build dependency

* Thu Jul 15 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt2
- Disabled avalon by default

* Thu Jun 17 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.4-alt1
- New upstream release
- Patch0 obsoleted

* Thu Feb 26 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.3-alt1
- Adapted for Sisyphus from the JPackage project
