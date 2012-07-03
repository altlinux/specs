Name: maven-surefire-report-plugin
Version: 2.12
Summary: Surefire reports plugin for maven
License: ASL 2.0
Url: http://maven.apache.org/surefire/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-surefire-report-maven-plugin
Provides: maven2-plugin-surefire-report
Requires: maven-surefire

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-surefire-report-plugin-2.12-2.fc18.cpio

%description
Plugin for generating reports from surefire test runs.

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
* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

%changelog
* Mon Feb 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4.3-alt3_6jpp6
- added requires on maven-surefire-provider-junit

* Sat Feb 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.4.3-alt2_6jpp6
- new version

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.4.3-alt2_5jpp6
- rebuild with new maven

* Mon Jan 31 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.4.3-alt2_4jpp6
- fixed build

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.3-alt1_4jpp6
- build w/o plexus-ftp

* Fri Sep 17 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.3-alt0.1jpp
- bootstrap for maven2

