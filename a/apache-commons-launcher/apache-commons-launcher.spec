Name: apache-commons-launcher
Version: 1.1
Summary: A cross platform Java application launcher
License: ASL 2.0
Url: http://commons.apache.org/launcher/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-commons-launcher = 1.1-16.20100521svn936225.fc23
Provides: mvn(commons-launcher:commons-launcher) = 1.1
Provides: mvn(commons-launcher:commons-launcher:pom:) = 1.1
Provides: mvn(org.apache.commons:commons-launcher) = 1.1
Provides: mvn(org.apache.commons:commons-launcher:pom:) = 1.1
Requires: java
Requires: java-headless
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: apache-commons-launcher-1.1-16.20100521svn936225.fc23.cpio

%description
Commons-launcher eliminates the need for a batch or shell script to launch a
Java class. Some situations where elimination of a batch or shell script may
be desirable are:

* You want to avoid having to determining where certain application paths are
e.g. your application's home directory, etc. Determining this dynamically in
a Windows batch scripts is very tricky on some versions of Windows or when
soft links are used on Unix platforms.

* You want to avoid having to handle native file and path separators or native
path quoting issues.

* You need to enforce certain system properties.

* You want to allow users to pass in custom JVM arguments or system properties
without having to parse and reorder arguments in your script. This can be
tricky and/or messy in batch and shell scripts.

* You want to bootstrap system properties from a configuration file instead
hard-coding them in your batch and shell scripts.

* You want to provide localized error messages which is very tricky to do in
batch and shell scripts.

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
* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_14.20100521svn936225jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_12.20100521svn936225jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt1_10.20100521svn936225jpp7
- fc update

* Sun Feb 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_0.r832060.5jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_4jpp5
- new jpackage release

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_3jpp1.7
- converted from JPackage by jppimport script

* Mon Mar 21 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt3
- rpm-build-java macroces
- cvs 20050321

* Sun Oct 24 2004 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt2
- 1.1-dev (cvs 20041024)

* Sat Sep 11 2004 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt1
- 1.1
- Rebuild for ALT Linux Sisyphus
- spec cleanup

* Fri Jan  9 2004 Kaj J. Niemi <kajtzu@fi.basen.net> - 0:0.9-1jpp
- First build for JPackage

* Wed Dec 17 2003 Kaj J. Niemi <kajtzu@fi.basen.net> - 0:0.9-0.2
- Fixed description
- Enabled javadocs

* Thu Dec  4 2003 Kaj J. Niemi <kajtzu@fi.basen.net> - 0:0.9-0.1
- Rebuilt w/o javadocs

