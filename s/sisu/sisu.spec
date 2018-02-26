Name: sisu
Version: 2.2.3
Epoch: 0
Summary: Sonatype dependency injection framework
License: ASL 2.0 and EPL
Url: http://github.com/sonatype/sisu
Packager: Igor Vlasenko <viy@altlinux.ru>
#Requires: /bin/sh
#Requires: /bin/sh
Requires: forge-parent
Requires: google-guice
#Requires: java
#Requires: jpackage-utils
#Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: sisu-2.2.3-3.fc17.cpio

%description
Java dependency injection framework with backward support for plexus and bean
style dependency injection.

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
* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

%changelog
* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.3.2-alt1_1jpp6
- new version

* Thu Jul 02 2009 Alexey I. Froloff <raorn@altlinux.org> 0.70.5-alt2
- Rebuilt with Ruby 1.9

* Sat May 09 2009 Vitaly Lipatov <lav@altlinux.ru> 0.70.5-alt1
- new version 0.70.5 (with rpmrb script)

* Tue Jan 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.64.0-alt1
- new version 0.64.0
- use ruby macroses, fix requires

* Sat Nov 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.62.2-alt1
- new version 0.62.2 (with rpmrb script)

* Thu Jul 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.55.2-alt1
- new version 0.55.2 (with rpmrb script)
- change license to GPL3

* Tue Mar 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.50.3-alt1
- new version 0.50.3 (with rpmrb script)

* Sun Feb 04 2007 Vitaly Lipatov <lav@altlinux.ru> 0.49.0-alt0.1
- new version 0.49.0 (with rpmrb script)

* Sat Sep 23 2006 Vitaly Lipatov <lav@altlinux.ru> 0.47.2-alt0.1
- new version 0.47.2 (with rpmrb script)

* Sat Sep 23 2006 Vitaly Lipatov <lav@altlinux.ru> 0.48.0-alt0.1
- new version 0.48.0 (with rpmrb script)

* Sat Sep 23 2006 Vitaly Lipatov <lav@altlinux.ru> 0.47.0-alt0.1
- new version 0.47.0 (with rpmrb script)

* Sat Jul 29 2006 Vitaly Lipatov <lav@altlinux.ru> 0.43.0-alt0.1
- new version 0.43.0 (with rpmrb script)

* Sat Jul 29 2006 Vitaly Lipatov <lav@altlinux.ru> 0.41.2-alt0.1
- new version 0.41.2 (with rpmrb script)

* Sun Jun 18 2006 Vitaly Lipatov <lav@altlinux.ru> 0.41.4-alt0.1
- new version 0.41.4
- fix Source URL
- remove examples (see site if needed)

* Sat Mar 25 2006 Vitaly Lipatov <lav@altlinux.ru> 0.37.8-alt0.1
- new version 0.37.8 (with rpmrb script)

* Fri Feb 10 2006 Vitaly Lipatov <lav@altlinux.ru> 0.36.12-alt0.1
- new version

* Wed Feb 08 2006 Vitaly Lipatov <lav@altlinux.ru> 0.36.9-alt0.1
- new version

* Wed Dec 28 2005 Vitaly Lipatov <lav@altlinux.ru> 0.35.0-alt0.1
- new version

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 0.34.0-alt0.1
- new version

* Sun Nov 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.31.0-alt0.1
- initial build for ALT Linux Sisyphus

