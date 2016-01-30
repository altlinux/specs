Name: maven-failsafe-plugin
Version: 2.18.1
Summary: Maven plugin for running integration tests
License: ASL 2.0 and CPL
Url: http://maven.apache.org/surefire/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-failsafe-plugin = 0:2.18.1-2.fc23
Provides: mvn(org.apache.maven.plugins:maven-failsafe-plugin) = 2.18.1
Provides: mvn(org.apache.maven.plugins:maven-failsafe-plugin:pom:) = 2.18.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
Requires: mvn(org.apache.maven.shared:maven-shared-utils)
Requires: mvn(org.apache.maven.surefire:maven-surefire-common)
Requires: mvn(org.apache.maven.surefire:surefire-api)
Requires: mvn(org.apache.maven:maven-plugin-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-failsafe-plugin-2.18.1-2.fc23.cpio

%description
The Failsafe Plugin is designed to run integration tests while the
Surefire Plugins is designed to run unit. The name (failsafe) was
chosen both because it is a synonym of surefire and because it implies
that when it fails, it does so in a safe way.

If you use the Surefire Plugin for running tests, then when you have a
test failure, the build will stop at the integration-test phase and
your integration test environment will not have been torn down
correctly.

The Failsafe Plugin is used during the integration-test and verify
phases of the build lifecycle to execute the integration tests of an
application. The Failsafe Plugin will not fail the build during the
integration-test phase thus enabling the post-integration-test phase
to execute.

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
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.18.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.16-alt1_1jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.14-alt1_2jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.12.4-alt2_2jpp7
- rebuild with maven-local

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.12.4-alt1_2jpp7
- update

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt2_5jpp7
- fixed build

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt1_5jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

