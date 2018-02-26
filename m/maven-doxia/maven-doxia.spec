Name: maven-doxia
Version: 1.2
Summary: Content generation framework
License: ASL 2.0
Url: http://maven.apache.org/doxia/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: apache-commons-collections
Requires: apache-commons-logging
Requires: apache-commons-validator
Requires: classworlds
Requires: fop
Requires: geronimo-jms
Requires: geronimo-parent-poms
Requires: httpcomponents-client
Requires: httpcomponents-project
Requires: jakarta-oro
Requires: java
Requires: javamail
Requires: jpackage-utils
Requires: junit
Requires: plexus-container-default
Requires: plexus-i18n
Requires: plexus-utils
Requires: plexus-velocity
Requires: velocity

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-doxia-1.2-3.fc17.cpio

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
* Tue Feb 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt10_0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

