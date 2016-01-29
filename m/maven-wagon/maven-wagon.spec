Name: maven-wagon
Version: 2.9
Summary: Tools to manage artifacts and deployment
License: ASL 2.0
Url: http://maven.apache.org/wagon
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-wagon = 0:2.9-4.fc23
Provides: mvn(org.apache.maven.wagon:wagon:pom:) = 2.9
Requires: java-headless
Requires: jpackage-utils
Requires: maven-wagon-file
Requires: maven-wagon-ftp
Requires: maven-wagon-http
Requires: maven-wagon-http-lightweight
Requires: maven-wagon-http-shared
Requires: maven-wagon-provider-api
Requires: maven-wagon-providers
Requires: maven-wagon-scm
Requires: maven-wagon-ssh
Requires: maven-wagon-ssh-common
Requires: maven-wagon-ssh-external
Requires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
Requires: mvn(org.apache.maven:maven-parent:pom:)
Requires: mvn(org.codehaus.plexus:plexus-component-metadata)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-wagon-2.9-4.fc23.cpio

%description
Maven Wagon is a transport abstraction that is used in Maven's
artifact and repository handling code. Currently wagon has the
following providers:
* File
* HTTP
* FTP
* SSH/SCP
* WebDAV
* SCM (in progress)

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.9-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5-alt1_2jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt0.2jpp
- rebuild to add provides

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt10_6jpp7
- added maven-local BR:

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt9_6jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt9_3jpp7
- complete build

* Sun Mar 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt8jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

