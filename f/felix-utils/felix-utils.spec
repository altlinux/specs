Name: felix-utils
Version: 1.8.0
Summary: Utility classes for OSGi
License: ASL 2.0
Url: http://felix.apache.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: felix-utils = 1.8.0-2.fc23
Provides: mvn(org.apache.felix:org.apache.felix.utils) = 1.8.0
Provides: mvn(org.apache.felix:org.apache.felix.utils:pom:) = 1.8.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.osgi:org.osgi.compendium)
Requires: mvn(org.osgi:org.osgi.core)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: felix-utils-1.8.0-2.fc23.cpio

%description
Utility classes for OSGi

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_3jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt2_5jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_5jpp7
- new release

