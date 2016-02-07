Name: svnkit
Version: 1.8.5
Summary: Pure java subversion client library
License: TMate
Url: http://www.svnkit.com/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.tmatesoft.svnkit:svnkit) = 1.8.5
Provides: mvn(org.tmatesoft.svnkit:svnkit:pom:) = 1.8.5
Provides: svnkit = 1.8.5-3.fc23
Requires: java-headless
Requires: jna
Requires: jna-contrib
Requires: jpackage-utils
Requires: jpackage-utils
Requires: jsch-agent-proxy-connector-factory
Requires: jsch-agent-proxy-trilead-ssh2
Requires: sequence-library
Requires: sqljet
Requires: subversion-javahl
Requires: tomcat-servlet-3.1-api
Requires: trilead-ssh2

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: svnkit-1.8.5-3.fc23.cpio

%description
SVNKit is a pure java Subversion client library. You would like to use SVNKit
when you need to access or modify Subversion repository from your Java
application, as a standalone program and plugin or web application. Being a
pure java program, SVNKit doesn't need any additional configuration or native
binaries to work on any OS that runs java.

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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt2_7jpp7
- new release

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt2_6jpp7
- target 5 build

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt1_6jpp7
- replaced by fc package

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1jpp6
- new version

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_2jpp5.0
- converted from JPackage by jppimport script

