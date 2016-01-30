Name: aqute-bndlib
Version: 2.4.1
Summary: BND library
License: ASL 2.0
Url: http://www.aqute.biz/Bnd/Bnd
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: aqute-bndlib = 2.4.1-2.fc23
Provides: mvn(biz.aQute.bnd:biz.aQute.bndlib) = 2.4.1
Provides: mvn(biz.aQute.bnd:biz.aQute.bndlib:pom:) = 2.4.1
Provides: mvn(biz.aQute.bnd:bndlib) = 2.4.1
Provides: mvn(biz.aQute.bnd:bndlib:pom:) = 2.4.1
Provides: mvn(biz.aQute:bndlib) = 2.4.1
Provides: mvn(biz.aQute:bndlib:pom:) = 2.4.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.eclipse.osgi:org.eclipse.osgi)
Requires: mvn(org.eclipse.osgi:org.eclipse.osgi.services)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: aqute-bndlib-2.4.1-2.fc23.cpio

%description
BND library.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.50.0-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.50.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.50.0-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.50.0-alt1_3jpp7
- new version

* Fri Mar 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.0.363-alt2_1jpp6
- fixed build

* Mon Oct 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.0.363-alt1_1jpp6
- new version

* Mon Feb 23 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.0.203-alt4_2jpp5
- fixed build

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.0.203-alt3_2jpp5
- rebuild with eclipse 3.4

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.0.203-alt2_2jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.0.203-alt1_2jpp5
- converted from JPackage by jppimport script

