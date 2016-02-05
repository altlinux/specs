Name: jboss-logmanager
Version: 1.5.2
Summary: JBoss Log Manager
License: LGPLv2+
Url: https://github.com/jboss-logging/jboss-logmanager
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jboss-logmanager = 1.5.2-2.fc21
Provides: mvn(org.jboss.logmanager:jboss-logmanager) = 1.5.2.Final
Provides: mvn(org.jboss.logmanager:jboss-logmanager:pom:) = 1.5.2.Final
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jboss-logmanager-1.5.2-2.fc21.cpio

%description
This package contains the JBoss Log Manager

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
* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.5.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5.1-alt1_1jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt1_3jpp7
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.0-alt1_3jpp6
- new version

