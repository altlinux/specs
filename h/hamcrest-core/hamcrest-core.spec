Name: hamcrest-core
Version: 1.3
Summary: Core API of hamcrest matcher framework.
License: BSD
Url: http://code.google.com/p/hamcrest/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: hamcrest-core = 0:1.3-13.fc23
Provides: mvn(org.hamcrest:hamcrest-core) = 1.3
Provides: mvn(org.hamcrest:hamcrest-core:pom:) = 1.3
Provides: mvn(org.hamcrest:hamcrest-parent:pom:) = 1.3
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: hamcrest-core-1.3-13.fc23.cpio

%description
The core API of hamcrest matcher framework to be used by third-party framework providers.
This includes the a foundation set of matcher implementations for common operations.

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
* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_5jpp7
- new release

* Tue Aug 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_1jpp7
- new version

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt4_21jpp7
- source and target to 1.5

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_21jpp7
- fix for arm

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_21jpp7
- fc update

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_19jpp7
- java6 build for jmock2

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_19jpp7
- fc release

* Tue Oct 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_9.2jpp6
- added OSGi manifest for eclipse

* Fri Jan 16 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_8jpp5
- rebuild to fix jmock2

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp5
- converted from JPackage by jppimport script

