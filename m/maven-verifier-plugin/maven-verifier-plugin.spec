Name: maven-verifier-plugin
Version: 1.0
Summary: Maven Verifier Plugin
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-verifier-plugin/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-verifier-plugin = 1.0-14.fc23
Provides: mvn(org.apache.maven.plugins:maven-verifier-plugin) = 1.0
Provides: mvn(org.apache.maven.plugins:maven-verifier-plugin:pom:) = 1.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch: noarch
Group: Development/Java
Release: alt3jpp
Source: maven-verifier-plugin-1.0-14.fc23.cpio

%description
Assists in integration testing by means of evaluating
success/error conditions read from a configuration file.

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
* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_8jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_6jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6jpp7
- new fc release

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5jpp7
- new version

