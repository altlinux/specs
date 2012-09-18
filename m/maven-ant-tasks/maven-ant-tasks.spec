Name: maven-ant-tasks
Version: 2.1.1
Summary: Allow Maven artifact handling features to be used from within an Ant build
License: ASL 2.0
Url: http://maven.apache.org/ant-tasks/index.html
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /bin/sh
Requires: /bin/sh
Requires: java
Requires: jpackage-utils
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-ant-tasks-2.1.1-9.fc17.cpio

%description
Maven Ant Tasks allow several of Maven's artifact handling features to be
used from within an Ant build. These include:

* Dependency management - including transitive dependencies, scope recognition
  and SNAPSHOT handling
* Artifact deployment - deployment to a Maven repository (file integrated,
  other with extensions)
* POM processing - for reading and writing a Maven 2 pom.xml file

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

%post

echo -e "<dependencies>\n" > /etc/maven/maven2-depmap.xml
if [ -d /usr/share/maven-fragments ] && [ -n "`find /usr/share/maven-fragments -type f`" ]; then
cat /usr/share/maven-fragments/* >> /etc/maven/maven2-depmap.xml
fi
echo -e "</dependencies>\n" >> /etc/maven/maven2-depmap.xml

%postun

echo -e "<dependencies>\n" > /etc/maven/maven2-depmap.xml
if [ -d /usr/share/maven-fragments ] && [ -n "`find /usr/share/maven-fragments -type f`" ]; then
cat /usr/share/maven-fragments/* >> /etc/maven/maven2-depmap.xml
fi
echo -e "</dependencies>\n" >> /etc/maven/maven2-depmap.xml


%files -f %name-list

%changelog
* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

%changelog
* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.9-alt2_1jpp6
- build with velocity15

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.9-alt1_1jpp6
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.0.7-alt3_1jpp5
- java6 translation ready

* Thu Jun 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.7-alt2_1jpp5
- added non-versioned maven-artifact-ant symlink

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.7-alt1_1jpp5
- manually updated to 2.0.7 and added maven-artifact-ant provides

* Tue Feb 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_1jpp5
- import

