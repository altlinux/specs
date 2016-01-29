Name: buildnumber-maven-plugin
Version: 1.3
Summary: Build Number Maven Plugin
License: MIT and ASL 2.0
Url: http://svn.codehaus.org/mojo/tags/buildnumber-maven-plugin-1.3
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: buildnumber-maven-plugin = 1.3-4.fc23
Provides: mvn(org.codehaus.mojo:buildnumber-maven-plugin) = 1.3
Provides: mvn(org.codehaus.mojo:buildnumber-maven-plugin:pom:) = 1.3
Requires: java-headless
Requires: java-headless
Requires: jna
Requires: jpackage-utils
Requires: jpackage-utils
Requires: maven
Requires: maven-project
Requires: maven-scm
Requires: mojo-parent
Requires: mvn(net.java.dev.jna:jna)
Requires: mvn(org.apache.maven.scm:maven-scm-api)
Requires: mvn(org.apache.maven.scm:maven-scm-manager-plexus)
Requires: mvn(org.apache.maven.scm:maven-scm-provider-bazaar)
Requires: mvn(org.apache.maven.scm:maven-scm-provider-clearcase)
Requires: mvn(org.apache.maven.scm:maven-scm-provider-cvsexe)
Requires: mvn(org.apache.maven.scm:maven-scm-provider-gitexe)
Requires: mvn(org.apache.maven.scm:maven-scm-provider-hg)
Requires: mvn(org.apache.maven.scm:maven-scm-provider-perforce)
Requires: mvn(org.apache.maven.scm:maven-scm-provider-starteam)
Requires: mvn(org.apache.maven.scm:maven-scm-provider-svn-commons)
Requires: mvn(org.apache.maven.scm:maven-scm-provider-svnexe)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.apache.maven:maven-project)
Requires: mvn(org.apache.maven:maven-settings:2.0.6)
Requires: mvn(org.codehaus.plexus:plexus-container-default)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: plexus-containers-container-default
Requires: plexus-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: buildnumber-maven-plugin-1.3-4.fc23.cpio

%description
This mojo is designed to get a unique build number for each time you build
your project. So while your version may remain constant at 1.0-SNAPSHOT
for many iterations until release, you will have a build number that can
uniquely identify each build during that time. The build number is obtained
from scm, and in particular, at this time, from svn. You can then place that
build number in metadata, which can be accessed from your app, if desired.

The mojo also has a couple of extra functions to ensure you get the proper
build number. First, your local repository is checked to make sure it is
up to date. Second, your local repository is automatically updated, so that
you get the latest build number. Both these functions can be suppressed,
if desired.

Optionally, you can configure this mojo to produce a revision based on a
timestamp, or on a sequence, without requiring any interaction with an
SCM system. Note that currently, the only supported SCM is subversion.

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
* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_6jpp7
- new release

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_3jpp7
- patched out dependency on maven2 (patch33)

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_2jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_2jpp7
- new version

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_5jpp7
- complete build

* Tue Mar 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

