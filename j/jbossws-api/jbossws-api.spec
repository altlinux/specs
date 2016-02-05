Name: jbossws-api
Version: 1.0.2
Summary: JBossWS API
License: LGPLv2+
Url: http://www.jboss.org/jbossws
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jbossws-api = 1.0.2-0.4.CR1.fc21
Provides: mvn(org.jboss.ws:jbossws-api) = 1.0.2.CR1
Provides: mvn(org.jboss.ws:jbossws-api:pom:) = 1.0.2.CR1
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jbossws-api-1.0.2-0.4.CR1.fc21.cpio

%description
JBoss WS public API

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
* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1jpp7
- update

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp7
- new version

