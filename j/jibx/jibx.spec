Name: jibx
Version: 1.2.6
Summary: Framework for binding XML data to Java objects
License: BSD and ASL 1.1
Url: http://sourceforge.net/projects/jibx/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jibx = 1.2.6-3.fc23
Provides: mvn(org.jibx.config:main-reactor:pom:) = 1.2.6
Provides: mvn(org.jibx:jibx-bind) = 1.2.6
Provides: mvn(org.jibx:jibx-bind:pom:) = 1.2.6
Provides: mvn(org.jibx:jibx-extras) = 1.2.6
Provides: mvn(org.jibx:jibx-extras:pom:) = 1.2.6
Provides: mvn(org.jibx:jibx-run) = 1.2.6
Provides: mvn(org.jibx:jibx-run:pom:) = 1.2.6
Provides: mvn(org.jibx:jibx-schema) = 1.2.6
Provides: mvn(org.jibx:jibx-schema:pom:) = 1.2.6
Provides: mvn(org.jibx:jibx-tools) = 1.2.6
Provides: mvn(org.jibx:jibx-tools:pom:) = 1.2.6
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(bcel:bcel)
Requires: mvn(com.thoughtworks.qdox:qdox)
Requires: mvn(dom4j:dom4j)
Requires: mvn(joda-time:joda-time)
Requires: mvn(log4j:log4j)
Requires: mvn(org.jdom:jdom)
Requires: mvn(xpp3:xpp3)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jibx-1.2.6-3.fc23.cpio

%description
JiBX is a framework for binding XML data to Java objects. It lets you
work with data from XML documents using your own class structures.

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
* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.5-alt1_5jpp7
- new release

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.5-alt1_2jpp7
- update

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.2.4-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.4-alt1_6jpp7
- new version

* Wed Aug 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt2_1jpp6
- applied repocop patches

* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.3-alt1_1jpp6
- new version

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6a-alt2_1jpp5
- selected java5 compiler explicitly

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.6a-alt1_1jpp5
- new jpp release

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.5-alt1_1jpp1.7
- updated to new jpackage release

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_0.b3.1jpp1.7
- converted from JPackage by jppimport script

