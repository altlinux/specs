Name: xml-security
Version: 2.0.4
Summary: Implementation of W3C security standards for XML
License: ASL 2.0
Url: http://santuario.apache.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.apache.santuario:xmlsec) = 2.0.4
Provides: mvn(org.apache.santuario:xmlsec:pom:) = 2.0.4
Provides: xml-security = 0:2.0.4-2.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-codec:commons-codec)
Requires: mvn(org.codehaus.woodstox:woodstox-core-asl)
Requires: mvn(org.slf4j:slf4j-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xml-security-2.0.4-2.fc23.cpio

%description
The XML Security project is aimed at providing implementation
of security standards for XML. Currently the focus is on the
W3C standards :
- XML-Signature Syntax and Processing; and
- XML Encryption Syntax and Processing.

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
* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt3_1jpp7
- rebuild with maven-local

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt2_1jpp7
- fixed build

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.5-alt1_1jpp7
- update

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0:1.4.5-alt1_4jpp7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for xml-security

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.5-alt1_4jpp7
- new release

* Sun Mar 20 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt3_0jpp6
- added depmap for org.apache.santuario:xmlsec:jar

* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt2_0jpp6
- added jbossas42 compatible repolib

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3-alt1_0jpp6
- new version (closes: #20786)

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.2-alt1_5jpp6
- new version

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt2_2jpp5
- use default jpp profile

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_2jpp5
- jpp5 build

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

