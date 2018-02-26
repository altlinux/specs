Name: maven-archetype
Version: 2.0
Epoch: 0
Summary: Maven Archetype 2
License: Apache Software License 2.0
Url: http://maven.apache.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: geronimo-jta-1.0.1B-api
Requires: apache-commons-io
Requires: jchardet
Requires: maven-shared-invoker
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-archetype2-2.0-alt5_0.a3.2jpp6.cpio

Provides: maven-archetype2 = %version
Obsoletes: maven-archetype2 < %version

%description
Maven Archetypes

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
list=`pwd`/%name-list
pushd $RPM_BUILD_ROOT/
 rm usr/share/maven2/plugins/archetype2-plugin.jar
 mv usr/share/maven2/plugins/archetype2-plugin-2.0.jar usr/share/java/maven-archetype2/plugin-2.0.jar
 ln -s plugin-2.0.jar usr/share/java/maven-archetype2/plugin.jar
 mv usr/share/maven2/poms/JPP.maven2.plugins-archetype2-plugin.pom usr/share/maven2/poms/JPP.maven-archetype2-plugin.pom
 sed -i -e 's,JPP/maven2/plugins,JPP/maven-archetype2,;s,archetype2-plugin,plugin,' etc/maven/fragments/maven-archetype2
 find */*/* | awk '{print "/" $1}' > $list
popd


%files -f %name-list

%changelog
* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

