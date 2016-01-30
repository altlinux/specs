Name: felix-framework
Version: 5.0.0
Summary: Apache Felix Framework
License: ASL 2.0
Url: http://felix.apache.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: felix-framework = 5.0.0-1.fc23
Provides: mvn(org.apache.felix:org.apache.felix.framework) = 5.0.0
Provides: mvn(org.apache.felix:org.apache.felix.framework:pom:) = 5.0.0
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: felix-framework-5.0.0-1.fc23.cpio

%description
Apache Felix Framework Interfaces and Classes.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1_1jpp7
- new version

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt1_4jpp7
- new version

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.2-alt1_3jpp7
- new release

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.5-alt1_3jpp6
- new jpp release

