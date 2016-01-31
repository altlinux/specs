Name: dom4j
Version: 1.6.1
Summary: Open Source XML framework for Java
License: BSD
Url: http://sourceforge.net/projects/dom4j
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: dom4j = 0:1.6.1-25.fc23
Provides: mvn(dom4j:dom4j) = 1.6.1
Provides: mvn(dom4j:dom4j:pom:) = 1.6.1
Provides: mvn(org.jvnet.hudson.dom4j:dom4j) = 1.6.1
Provides: mvn(org.jvnet.hudson.dom4j:dom4j:pom:) = 1.6.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(xml-apis:xml-apis)

BuildArch: noarch
Group: Development/Java
Release: alt5jpp
Source: dom4j-1.6.1-25.fc23.cpio

%description
dom4j is an Open Source XML framework for Java. dom4j allows you to read,
write, navigate, create and modify XML documents. dom4j integrates with
DOM and SAX and is seamlessly integrated with full XPath support.

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
* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt4_13jpp7
- update

* Fri Mar 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt4_13jpp6
- switched to jpp due to repolib and fixed build

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt3_7jpp7
- fc version

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_13jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_10jpp5
- use default jpp profile

* Wed Sep 10 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt2_8jpp5
- converted from JPackage by jppimport script

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_8jpp5
- converted from JPackage by jppimport script

* Sun May 06 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

* Mon Apr 25 2005 Vladimir Lettiev <crux@altlinux.ru> 1.6-alt1
- Initial release for ALT Linux Sisyphus

