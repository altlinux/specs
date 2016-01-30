Name: httpcomponents-project
Version: 7
Summary: Common POM file for HttpComponents
License: ASL 2.0
Url: http://hc.apache.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: httpcomponents-project = 7-2.fc23
Provides: mvn(org.apache.httpcomponents:project:pom:) = 7
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
Requires: mvn(org.apache.maven.plugins:maven-jar-plugin)
Requires: mvn(org.apache:apache:pom:)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: httpcomponents-project-7-2.fc23.cpio

%description
Common Maven POM  file for HttpComponents. This project should be
required only for building dependant packages with Maven. Please don't
use it as runtime requirement.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 7-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 6-alt2_4jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 6-alt2_2jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 6-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 6-alt1_1jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1_4jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

