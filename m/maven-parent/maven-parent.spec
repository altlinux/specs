Name: maven-parent
Version: 26
Summary: Apache Maven parent POM
License: ASL 2.0
Url: http://maven.apache.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-parent = 26-2.fc23
Provides: mvn(org.apache.maven:maven-parent:pom:) = 26
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache:apache:pom:)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-parent-26-2.fc23.cpio

%description
Apache Maven parent POM file used by other Maven projects.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 26-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 20-alt1_5jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 20-alt1_4jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt1_3jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt1_2jpp7
- complete build

* Sun Mar 11 2012 Igor Vlasenko <viy@altlinux.ru> 20-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

