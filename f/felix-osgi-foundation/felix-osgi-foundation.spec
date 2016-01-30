Name: felix-osgi-foundation
Version: 1.2.0
Summary: Felix OSGi Foundation EE Bundle
License: ASL 2.0
Url: http://felix.apache.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: felix-osgi-foundation = 1.2.0-19.fc23
Provides: mvn(org.apache.felix:org.osgi.foundation) = 1.2.0
Provides: mvn(org.apache.felix:org.osgi.foundation:pom:) = 1.2.0
Provides: mvn(org.osgi:org.osgi.foundation) = 1.2.0
Provides: mvn(org.osgi:org.osgi.foundation:pom:) = 1.2.0
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt4jpp
Source: felix-osgi-foundation-1.2.0-19.fc23.cpio

%description
OSGi Foundation Execution Environment (EE) Classes.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt3_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt3_12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt3_10jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_10jpp7
- new release

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_4jpp6
- fixed build with maven3

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_4jpp6
- new version

