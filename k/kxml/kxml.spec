Name: kxml
Version: 2.3.0
Summary: Small XML pull parser
License: MIT
Url: http://kxml.sourceforge.net/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: kxml = 2.3.0-8.fc23
Provides: mvn(net.sf.kxml:kxml2) = 2.3.0
Provides: mvn(net.sf.kxml:kxml2-min) = 2.3.0
Provides: mvn(net.sf.kxml:kxml2-min:pom:) = 2.3.0
Provides: mvn(net.sf.kxml:kxml2:pom:) = 2.3.0
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils
Requires: xpp3

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: kxml-2.3.0-8.fc23.cpio

%description
kXML is a small XML pull parser, specially designed for constrained
environments such as Applets, Personal Java or MIDP devices.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_3jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt4_12jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt3_12jpp7
- added jpp compatible symlink

