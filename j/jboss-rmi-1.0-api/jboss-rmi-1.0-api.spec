Name: jboss-rmi-1.0-api
Version: 1.0.4
Summary: Java Remote Method Invocation 1.0 API
License: GPLv2 with exceptions
Url: http://www.jboss.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jboss-rmi-1.0-api = 1.0.4-11.fc22
Provides: mvn(org.jboss.spec.javax.rmi:jboss-rmi-api_1.0_spec) = 1.0.4.Final
Provides: mvn(org.jboss.spec.javax.rmi:jboss-rmi-api_1.0_spec:pom:) = 1.0.4.Final
Requires: jacorb
Requires: java-headless
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: jboss-rmi-1.0-api-1.0.4-11.fc22.cpio

%description
Java Remote Method Invocation 1.0 API classes.

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
* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_8jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_7jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_5jpp7
- new fc release

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3jpp7
- new version

