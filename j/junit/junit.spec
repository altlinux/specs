Name: junit
Version: 4.12
Summary: Java regression test package
License: EPL
Url: http://www.junit.org/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: junit = 1:4.12-3.fc23
Provides: junit4 = 1:4.12-3.fc23
Provides: mvn(junit:junit) = 4.12
Provides: mvn(junit:junit:pom:) = 4.12
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.hamcrest:hamcrest-core)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: junit-4.12-3.fc23.cpio

%description
JUnit is a regression testing framework written by Erich Gamma and Kent Beck.
It is used by the developer who implements unit tests in Java. JUnit is Open
Source Software, released under the Common Public License Version 1.0 and
hosted on GitHub.

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
ln -s junit.jar %buildroot/usr/share/java/junit4.jar

%files -f %name-list
/usr/share/java/junit4.jar

%changelog
* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.11-alt3_1jpp7
- replacement for junit4

* Thu Sep 04 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.11-alt2_1jpp7
- bugfix (closes: #30279)

* Tue Aug 12 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.11-alt1_1jpp7
- new version

* Thu Jul 24 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.10-alt5_6jpp7
- bumped epoch for junit-junit4

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:4.10-alt4_6jpp7
- made junit-junit4 provider default

* Fri Mar 29 2013 Igor Vlasenko <viy@altlinux.ru> 0:4.10-alt3_6jpp7
- added junit-junit4 provider

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.10-alt2_6jpp7
- added OSGi manifest

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.10-alt1_6jpp7
- new version

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.8.2-alt1_5jpp6
- new jpp relase

* Fri Feb 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.8.2-alt1_4jpp6
- new version

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:4.5-alt1_4jpp5
- new version

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:4.4-alt1_1jpp5
- converted from JPackage by jppimport script

* Fri Nov 09 2007 Igor Vlasenko <viy@altlinux.ru> 4.3.1-alt1_1.1jpp1.7
- new version
- resolved conflict with junit3.

* Sun Mar 25 2007 Denis Smirnov <mithraen@altlinux.ru> 4.1-alt2
- Update from upstream
- Add conflict with junit 3.8

* Sun Jul 02 2006 Mikhail Zabaluev <mhz@altlinux.ru> 4.1-alt1
- New package for JUnit 4.x
- Patch0: ignore a test relying on Java VM exit code that fails
- Relocated samples to /usr/share/junit4
