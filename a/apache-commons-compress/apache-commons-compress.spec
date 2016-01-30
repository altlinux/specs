Name: apache-commons-compress
Version: 1.10
Summary: Java API for working with compressed files and archivers
License: ASL 2.0
Url: http://commons.apache.org/compress/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-commons-compress = 1.10-0.2.svn1684406.fc23
Provides: mvn(commons:commons-compress) = 1.10.SNAPSHOT
Provides: mvn(commons:commons-compress:pom:) = 1.10.SNAPSHOT
Provides: mvn(org.apache.commons:commons-compress) = 1.10.SNAPSHOT
Provides: mvn(org.apache.commons:commons-compress:pom:) = 1.10.SNAPSHOT
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: apache-commons-compress-1.10-0.2.svn1684406.fc23.cpio

%description
The Apache Commons Compress library defines an API for working with
ar, cpio, Unix dump, tar, zip, gzip, XZ, Pack200 and bzip2 files.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.5-alt1_1jpp7
- new version

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt3_2jpp7
- added maven-local BR:

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.1-alt1_2jpp7
- new version

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_0.r831574.6jpp6
- new version

