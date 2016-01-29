Name: slf4j-jboss-logmanager
Version: 1.0.0
Summary: SLF4J backend for JBoss LogManager
License: LGPLv2+
Url: http://www.jboss.org
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.jboss.slf4j:slf4j-jboss-logmanager) = 1.0.0.GA
Provides: mvn(org.jboss.slf4j:slf4j-jboss-logmanager:pom:) = 1.0.0.GA
Provides: slf4j-jboss-logmanager = 1.0.0-9.fc22
Requires: java-headless
Requires: jboss-logmanager
Requires: jpackage-utils
Requires: jpackage-utils
Requires: slf4j

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: slf4j-jboss-logmanager-1.0.0-9.fc22.cpio

%description
This package contains SLF4J backend for JBoss LogManager

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- new version

