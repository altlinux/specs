Provides: /etc/derby.conf
Name: derby
Version: 10.11.1.1
Summary: Relational database implemented entirely in Java
License: ASL 2.0
Url: http://db.apache.org/derby/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: derby = 10.11.1.1-1.fc23
Provides: mvn(org.apache.derby:derby) = 10.11.1.1
Provides: mvn(org.apache.derby:derby-project:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derby:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_cs) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_cs:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_de_DE) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_de_DE:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_es) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_es:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_fr) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_fr:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_hu) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_hu:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_it) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_it:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_ja_JP) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_ja_JP:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_ko_KR) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_ko_KR:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_pl) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_pl:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_pt_BR) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_pt_BR:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_ru) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_ru:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_zh_CN) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_zh_CN:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_zh_TW) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyLocale_zh_TW:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyclient) = 10.11.1.1
Provides: mvn(org.apache.derby:derbyclient:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbynet) = 10.11.1.1
Provides: mvn(org.apache.derby:derbynet:pom:) = 10.11.1.1
Provides: mvn(org.apache.derby:derbytools) = 10.11.1.1
Provides: mvn(org.apache.derby:derbytools:pom:) = 10.11.1.1
Requires: /bin/bash
Requires: /bin/sh
Requires: /bin/sh
Requires: /bin/sh
Requires: java-headless
Requires: jpackage-utils
Requires: shadow-utils
Requires: systemd-units
Requires: systemd-units

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: derby-10.11.1.1-1.fc23.cpio

%description
Apache Derby, an Apache DB sub-project, is a relational database implemented
entirely in Java. Some key advantages include a small footprint, conformance
to Java, JDBC, and SQL standards and embedded JDBC driver.

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

%pre
getent group derby >/dev/null || groupadd -r derby
getent passwd derby >/dev/null || \
    useradd -r -g derby -d /var/lib/derby -s /sbin/nologin \
    -c "Apache Derby service account" derby
exit 0

%preun

if [ $1 -eq 0 ] ; then 
        # Package removal, not upgrade 
        systemctl --no-reload disable derby.service > /dev/null 2>&1 || : 
        systemctl stop derby.service > /dev/null 2>&1 || : 
fi

%post

if [ $1 -eq 1 ] ; then 
        # Initial installation 
        systemctl preset derby.service >/dev/null 2>&1 || : 
fi


%files -f %name-list

%changelog
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:10.11.1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun Sep 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:10.9.1.0-alt1_6jpp7
- new release

* Wed Jul 09 2014 Igor Vlasenko <viy@altlinux.ru> 0:10.9.1.0-alt1_2jpp7
- converted from JPackage by jppimport script

* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:10.6.2.1-alt3_2jpp6
- dropped felix dependency

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:10.6.2.1-alt2_2jpp6
- built with java 6

* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:10.6.2.1-alt1_2jpp6
- new version

* Sat Feb 28 2009 Igor Vlasenko <viy@altlinux.ru> 0:10.3.3.0-alt2_1jpp6
- packaged jdbc driver

* Thu Jan 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:10.3.3.0-alt1_1jpp6
- new version

* Wed Nov 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:10.1.1.0-alt2_1jpp1.7
- force build with java4

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:10.1.1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

