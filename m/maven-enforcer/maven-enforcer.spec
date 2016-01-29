Name: maven-enforcer
Version: 1.4
Summary: Maven Enforcer
License: ASL 2.0
Url: http://maven.apache.org/enforcer
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-enforcer = 1.4-2.fc23
Provides: mvn(org.apache.maven.enforcer:enforcer:pom:) = 1.4
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven:maven-parent:pom:)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-enforcer-1.4-2.fc23.cpio

%description
Enforcer is a build rule execution framework.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_4jpp7
- added BR: for xmvn

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_4jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt4_6jpp7
- fixed build

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt3_6jpp7
- new version

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt3_5jpp7
- new fc release

* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt3_4jpp7
- added maven-shared-enforcer-rule-api provides

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt2_4jpp7
- fixed depmap fragment

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_4jpp7
- fc version

* Mon Feb 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_3jpp6
- new jpp relase

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_0.2.b1.1.2jpp6
- new version

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.2.b1.1.2jpp6
- new version

