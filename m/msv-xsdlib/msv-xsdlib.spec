Name: msv-xsdlib
Version: 2013.6.1
Summary: Multi-Schema Validator XML Schema Library
License: BSD and ASL 1.1
Url: http://msv.java.net/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: msv-xsdlib = 1:2013.6.1-6.fc23
Provides: mvn(com.sun.msv.datatype.xsd:xsdlib) = 2013.6.1
Provides: mvn(com.sun.msv.datatype.xsd:xsdlib:pom:) = 2013.6.1
Provides: mvn(net.java.dev.msv:xsdlib) = 2013.6.1
Provides: mvn(net.java.dev.msv:xsdlib:pom:) = 2013.6.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(relaxngDatatype:relaxngDatatype)
Requires: mvn(xml-resolver:xml-resolver)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: msv-xsdlib-2013.6.1-6.fc23.cpio

%description
Multi-Schema Validator XML Schema Library.

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
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:2013.6.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:2013.5.1-alt1_6jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1:2013.2.3-alt1_1jpp7
- new version

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1:2009.1-alt4_12jpp7
- dropped compat msv provides

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 1:2009.1-alt3_12jpp7
- fixed deps

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 1:2009.1-alt2_12jpp7
- applied repocop patches

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:2009.1-alt1_12jpp7
- new version

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_0.20050722.7jpp6
- ant 18 support; added description (closes: #22125)

* Sun Jan 11 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt4_0.20050722.6jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_0.20050722.6jpp5
- fixed docdir ownership

* Fri Sep 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_0.20050722.6jpp5
- converted from JPackage by jppimport script

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.20050722.6jpp5
- converted from JPackage by jppimport script

* Sun Jul 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.20050722.3jpp1.7
- build without bootstrap

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1_0.20050722.3jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 25 2005 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt0.1
- Initial build for ALT Linux Sisyphus
- cvs version 20050424
