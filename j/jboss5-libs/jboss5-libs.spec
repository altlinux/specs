Name: jboss5-libs
Version: 5.1.0
Summary: JBoss libraries
Epoch: 0
License: LGPLv2+
Url: http://www.jboss.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /bin/sh
Requires: /bin/sh
Requires: concurrent
Requires: gjt-jpl-pattern
Requires: gjt-jpl-util
Requires: jboss-aop2
Requires: jboss-bootstrap
Requires: jboss-common-core
Requires: jboss-common-logging-spi
Requires: jboss-deployers
Requires: jboss-integration
Requires: jboss-jacc-1.1-api
Requires: jboss-javaee
Requires: jboss-man
Requires: jboss-microcontainer2
Requires: jboss-test
Requires: jboss-vfs2
Requires: jbossws
Requires: jbossxb2
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jboss5-libs-5.1.0-8.jpp6.cpio

%description
JBoss libraries.

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
if [ -d /etc/maven/fragments ] && [ -n "`find /etc/maven/fragments -type f`" ]; then
cat /etc/maven/fragments/* >> /etc/maven/maven2-depmap.xml
fi
echo -e "</dependencies>\n" >> /etc/maven/maven2-depmap.xml

%postun

echo -e "<dependencies>\n" > /etc/maven/maven2-depmap.xml
if [ -d /etc/maven/fragments ] && [ -n "`find /etc/maven/fragments -type f`" ]; then
cat /etc/maven/fragments/* >> /etc/maven/maven2-depmap.xml
fi
echo -e "</dependencies>\n" >> /etc/maven/maven2-depmap.xml


%files -f %name-list

%changelog
* Thu Feb 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

