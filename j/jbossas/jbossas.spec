BuildRequires(pre): rpm-build-java
Name: jbossas
Version: 4.2.3
Summary: JBoss Application Server
License: LGPLv2+
Url: http://www.jboss.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
BuildArch: noarch
Group: Development/Java
Release: alt28jpp
Source: jbossas-4.2.3-alt23_24jpp6.cpio

# jboss4 compat provides
Provides: jboss4-common = %version
Provides: jboss4-connector = %version
Provides: jboss4-j2ee = %version
Provides: jboss4-jmx = %version
Provides: jboss4-server = %version
Provides: jboss4-system = %version

%description
JBoss Application Server is the #1 most widely used Java application server
on the market. A J2EE certified platform for developing and deploying
enterprise Java applications, Web applications, and Portals,
JBoss Application Server provides the full range of J2EE 1.4 features as
well as extended enterprise services including clustering, caching, and
persistence.

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

mkdir -p $RPM_BUILD_ROOT%_javadir/jboss4
ln -s ../jbossas/jbossall-client.jar $RPM_BUILD_ROOT%_javadir/jboss4/jboss-common.jar
ln -s ../jbossas/jbossall-client.jar $RPM_BUILD_ROOT%_javadir/jboss4/jboss-client.jar
ln -s ../jbossas/jboss-jmx.jar $RPM_BUILD_ROOT%_javadir/jboss4/jboss-jmx.jar
ln -s ../jbossas/jboss-system.jar $RPM_BUILD_ROOT%_javadir/jboss4/jboss-system.jar
ln -s ../jbossas/jboss.jar $RPM_BUILD_ROOT%_javadir/jboss4/jboss.jar
ln -s ../jbossas/jboss-common-jdbc-wrapper.jar $RPM_BUILD_ROOT%_javadir/jboss4/jboss-common-jdbc-wrapper.jar
ln -s ../jbossas/jboss-j2ee.jar $RPM_BUILD_ROOT%_javadir/jboss4/jboss-j2ee.jar

%files -f %name-list
%dir %_javadir/jboss4
%_javadir/jboss4/jboss-common.jar
%_javadir/jboss4/jboss-client.jar
%_javadir/jboss4/jboss-jmx.jar
%_javadir/jboss4/jboss-system.jar
%_javadir/jboss4/jboss.jar
%_javadir/jboss4/jboss-common-jdbc-wrapper.jar
%_javadir/jboss4/jboss-j2ee.jar

%changelog
* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt28jpp
- dropped requires

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt27jpp
- added compat provides for jboss4

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt26jpp
- dropped old jboss* deps

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt25jpp
- dropped quartz deps

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt24jpp
- reduced to bootstrap pack of jars til the end of jboss update transaction

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt23_24jpp6
- fixed build with new commons-codec

* Mon Apr 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt22_24jpp6
- fixed build

* Tue Jan 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt21_24jpp6
- built with new antlr 

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt20_24jpp6
- built with new jboss-remoting

* Fri Mar 18 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt19_24jpp6
- fixed build with new ant

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt18_24jpp6
- build with joramtests 1.5

* Wed Feb 09 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt17_24jpp6
- build with compat jbossweb20

* Tue Feb 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt16_24jpp6
- build with compat hibernate 3.2

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt15_24jpp6
- build with jgroups24

* Thu Feb 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt14_24jpp6
- fixed build

* Mon Jan 31 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt13_24jpp6
- fixed build

* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt12_24jpp6
- fixed build

* Tue Jan 04 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt11_24jpp6
- fixed build with new commons beanutils, httpclient and fileupload

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt10_24jpp6
- rebuild with gnu-getopt 1.0.13

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt9_24jpp6
- rebuild with new commons-codec repolib

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt8_24jpp6
- fixed build

* Sun Dec 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt7_24jpp6
- rebuild with new commons-lang repolib

* Mon Nov 01 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt6_24jpp6
- build with wstx 3.2.8

* Sat Oct 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt5_24jpp6
- build with cglib 2.2
- added ghosted .cat

* Wed Oct 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt4_24jpp6
- built with cglib21 and new commmons-digester

* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt3_24jpp6
- tmp hack: added ExclusiveArch: x86_64 to keep incoming alive

* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt2_24jpp6
- ant 18 fixes; fixed build in jpp 6 environment

* Wed Oct 13 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt1_24jpp5.M51.1
- init script fixes

* Tue Mar 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt1_24jpp5
- full build

* Fri Mar 05 2010 Igor Vlasenko <viy@altlinux.ru> 0:4.2.3-alt0.1jpp
- bootstrap for jbossas

