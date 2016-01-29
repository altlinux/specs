Name: maven-shared
Version: 21
Summary: Maven Shared Components
License: ASL 2.0
Url: http://maven.apache.org/shared/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-shared = 21-2.fc23
Provides: mvn(org.apache.maven.shared:maven-shared-components:pom:) = 21
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven:maven-parent:pom:)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-shared-21-2.fc23.cpio

%description
Maven Shared Components

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:21-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:19-alt1_4jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:19-alt1_3jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:15-alt10_28jpp7
- rebuild with maven-local

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:15-alt9_28jpp7
- update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt9_24jpp7
- new fc release

* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt9_23jpp7
- dropped versioned requires

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt8_23jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

