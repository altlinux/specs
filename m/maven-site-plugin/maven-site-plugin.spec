Name: maven-site-plugin
Version: 3.0
Summary: Maven Site Plugin
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-site-plugin/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven2-plugin-site
Obsoletes: maven2-plugin-site <= 0:2.0.8
Requires: java
#Requires: jetty
#Requires: jetty-parent
Requires: jpackage-utils
Requires: maven
Requires: maven-artifact-manager
Requires: maven-doxia-tools
Requires: maven-project
Requires: maven-reporting-exec
Requires: maven-shared-reporting-api
Requires: maven-wagon
Requires: plexus-archiver
Requires: plexus-containers-container-default
Requires: plexus-i18n
Requires: plexus-utils
Requires: plexus-velocity
Requires: servlet25

BuildArch: noarch
Group: Development/Java
Release: alt0.3jpp
Source: maven-site-plugin-3.0-4.fc17.cpio
Source22: JPP-maven-site-plugin.pom

%description
The Maven Site Plugin is a plugin that generates a site for the current project.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list
rm usr/share/maven-poms/JPP-maven-site-plugin.pom
install -m644 %{S:22} usr/share/maven-poms/JPP-maven-site-plugin.pom

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Thu Apr 05 2012 Igor Vlasenko <viy@altlinux.ru> 3.0-alt0.3jpp
- added obsoletes on maven2-plugin-site

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 3.0-alt0.2jpp
- added oro dependency to pom

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 3.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

