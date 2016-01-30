Name: jtidy
Version: 1.0
Summary: HTML syntax checker and pretty printer
License: zlib
Url: http://jtidy.sourceforge.net/
Epoch: 3
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jtidy = 2:1.0-0.21.20100930svn1125.fc23
Provides: mvn(jtidy:jtidy) = 8.0.SNAPSHOT
Provides: mvn(jtidy:jtidy:pom:) = 8.0.SNAPSHOT
Provides: mvn(net.sf.jtidy:jtidy) = 8.0.SNAPSHOT
Provides: mvn(net.sf.jtidy:jtidy:pom:) = 8.0.SNAPSHOT
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils
Requires: jpackage-utils
Requires: xml-commons-apis

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: jtidy-1.0-0.21.20100930svn1125.fc23.cpio

%description
JTidy is a Java port of HTML Tidy, a HTML syntax checker and pretty
printer.  Like its non-Java cousin, JTidy can be used as a tool for
cleaning up malformed and faulty HTML.  In addition, JTidy provides a
DOM interface to the document that is being processed, which
effectively makes you able to use JTidy as a DOM parser for real-world
HTML.

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
* Tue Jan 26 2016 Igor Vlasenko <viy@altlinux.ru> 3:1.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 3:1.0-alt1_0.13.20100930svn1125jpp7
- new release

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 3:1.0-alt1_0.10.20100930svn1125jpp6
- new version

* Tue Oct 21 2008 Igor Vlasenko <viy@altlinux.ru> 2:8.0-alt1_0.813.1jpp5
- jpackage 5.0

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 2:1.0-alt2.2_0.2.r7dev.1jpp5
- rebuild with java 5

