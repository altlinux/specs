Name: maven-doxia-sitetools
Version: 1.6
Summary: Doxia content generation framework
License: ASL 2.0
Url: http://maven.apache.org/doxia/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-doxia-sitetools = 1.6-2.fc23
Provides: mvn(org.apache.maven.doxia:doxia-decoration-model) = 1.6
Provides: mvn(org.apache.maven.doxia:doxia-decoration-model:pom:) = 1.6
Provides: mvn(org.apache.maven.doxia:doxia-doc-renderer) = 1.6
Provides: mvn(org.apache.maven.doxia:doxia-doc-renderer:pom:) = 1.6
Provides: mvn(org.apache.maven.doxia:doxia-site-renderer) = 1.6
Provides: mvn(org.apache.maven.doxia:doxia-site-renderer:pom:) = 1.6
Provides: mvn(org.apache.maven.doxia:doxia-sitetools:pom:) = 1.6
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-collections:commons-collections)
Requires: mvn(org.apache.maven.doxia:doxia-core)
Requires: mvn(org.apache.maven.doxia:doxia-logging-api)
Requires: mvn(org.apache.maven.doxia:doxia-module-apt)
Requires: mvn(org.apache.maven.doxia:doxia-module-fml)
Requires: mvn(org.apache.maven.doxia:doxia-module-fo)
Requires: mvn(org.apache.maven.doxia:doxia-module-xdoc)
Requires: mvn(org.apache.maven.doxia:doxia-module-xhtml)
Requires: mvn(org.apache.maven.doxia:doxia-sink-api)
Requires: mvn(org.apache.velocity:velocity)
Requires: mvn(org.codehaus.plexus:plexus-component-annotations)
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(org.codehaus.plexus:plexus-i18n)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.codehaus.plexus:plexus-velocity)
Requires: mvn(xalan:xalan)
Requires: mvn(xml-apis:xml-apis)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-doxia-sitetools-1.6-2.fc23.cpio

%description
Doxia is a content generation framework which aims to provide its
users with powerful techniques for generating static and dynamic
content. Doxia can be used to generate static sites in addition to
being incorporated into dynamic content generation systems like blogs,
wikis and content management systems.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_2jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp7
- update

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_5jpp7
- rebuild with maven-local

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_5jpp7
- fixed maven1 dependency

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_5jpp7
- fc update

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp7
- new release

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

