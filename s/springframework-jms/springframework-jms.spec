Name: springframework-jms
Version: 3.2.14
Summary: Spring jms
License: ASL 2.0
Url: http://projects.spring.io/spring-framework/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.springframework:spring-jms) = 3.2.14.RELEASE
Provides: mvn(org.springframework:spring-jms:pom:) = 3.2.14.RELEASE
Provides: springframework-jms = 0:3.2.14-2.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.jboss.spec.javax.resource:jboss-connector-api_1.7_spec)
Requires: mvn(org.springframework:spring-aop)
Requires: mvn(org.springframework:spring-beans)
Requires: mvn(org.springframework:spring-context)
Requires: mvn(org.springframework:spring-core)
Requires: mvn(org.springframework:spring-tx)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: springframework-jms-3.2.14-2.fc23.cpio

%description
This package provide Java Message Service 1.0.2/1.1 support.

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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.2.14-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0:3.1.1-alt1_10jpp7.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for springframework

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt1_10jpp7
- first build
