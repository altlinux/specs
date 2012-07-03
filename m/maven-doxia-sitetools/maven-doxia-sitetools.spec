Name: maven-doxia-sitetools
Version: 1.2
Summary: Doxia content generation framework
License: ASL 2.0
Url: http://maven.apache.org/doxia/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /usr/share/java/javamail/mail.jar
Requires: apache-commons-collections
Requires: apache-commons-configuration
Requires: apache-commons-logging
Requires: apache-commons-validator
Requires: classworlds
Requires: jakarta-oro
Requires: java
Requires: jpackage-utils
Requires: junit
Requires: maven-doxia
Requires: plexus-container-default
Requires: plexus-containers-container-default
Requires: plexus-i18n
Requires: plexus-utils
Requires: plexus-velocity
Requires: velocity

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-doxia-sitetools-1.2-3.fc17.cpio

%description
Doxia is a content generation framework which aims to provide its
users with powerful techniques for generating static and dynamic
content. Doxia can be used to generate static sites in addition to
being incorporated into dynamic content generation systems like blogs,
wikis and content management systems.

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
* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

%changelog
* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp6
- rebuild to restore plexus components info

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_2jpp6
- set target 5

* Fri Jan 28 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp6
- 28 release

* Tue Sep 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_0.1.a10.2jpp6
- build for new maven2 version

* Mon Sep 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt0.1jpp
- bootstrap for maven2

