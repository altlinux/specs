Name: xml-commons-apis
Version: 1.4.01
Summary: APIs for DOM, SAX, and JAXP
License: ASL 2.0 and W3C and Public Domain
Url: http://xml.apache.org/commons/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(xerces:dom3-xml-apis) = 2.0.2
Provides: mvn(xerces:dom3-xml-apis:pom:) = 2.0.2
Provides: mvn(xml-apis:xml-apis) = 2.0.2
Provides: mvn(xml-apis:xml-apis-ext) = 1.3.04
Provides: mvn(xml-apis:xml-apis-ext:pom:) = 1.3.04
Provides: mvn(xml-apis:xml-apis:pom:) = 2.0.2
Provides: xml-commons = 1.4.01-19.fc23
Provides: xml-commons-apis = 1.4.01-19.fc23
Provides: xml-commons-jaxp-1.3-apis = 1.4.01-19.fc23
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: xml-commons-apis-1.4.01-19.fc23.cpio

%description
xml-commons-apis is designed to organize and have common packaging for
the various externally-defined standard interfaces for XML. This
includes the DOM, SAX, and JAXP.

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
* Sun Jan 24 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.01-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.01-alt1_14jpp7
- xml-commons replacement

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.01-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

