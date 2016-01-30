Name: felix-osgi-core
Version: 1.4.0
Summary: Felix OSGi R4 Core Bundle
License: ASL 2.0
Url: http://felix.apache.org/site/apache-felix-osgi-core.html
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: felix-osgi-core = 1.4.0-18.fc23
Provides: mvn(org.apache.felix:org.osgi.core) = 1.4.0
Provides: mvn(org.apache.felix:org.osgi.core:pom:) = 1.4.0
Provides: mvn(org.osgi:org.osgi.core) = 1.4.0
Provides: mvn(org.osgi:org.osgi.core:pom:) = 1.4.0
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt4jpp
Source: felix-osgi-core-1.4.0-18.fc23.cpio

%description
OSGi Service Platform Release 4 Core Interfaces and Classes.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt3_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt3_12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt3_10jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt2_10jpp7
- new release

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt2_6jpp6
- fixed build with java 7

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt1_6jpp6
- new version

