Name: ehcache-core
Version: 2.6.7
Summary: Easy Hibernate Cache
License: ASL 2.0
Url: http://ehcache.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: ehcache-core = 2.6.7-9.fc23
Provides: mvn(net.sf.ehcache:ehcache) = 2.6.7
Provides: mvn(net.sf.ehcache:ehcache-core) = 2.6.7
Provides: mvn(net.sf.ehcache:ehcache-core:pom:) = 2.6.7
Provides: mvn(net.sf.ehcache:ehcache:pom:) = 2.6.7
Requires: hibernate3
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(javax.servlet:javax.servlet-api)
Requires: mvn(javax.transaction:jta)
Requires: mvn(net.sf.ehcache:sizeof-agent)
Requires: mvn(org.slf4j:slf4j-api)
Requires: mvn(org.slf4j:slf4j-jdk14)

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: ehcache-core-2.6.7-9.fc23.cpio

%description
Ehcache is a pure Java, in-process cache.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6.7-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.7-alt1_3jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt1_2jpp7
- new version

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.3.1-alt1_1jpp6
- new version

