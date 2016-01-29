Name: groovy-lib
Version: 2.4.4
Summary: Groovy JAR artifact
License: ASL 2.0 and BSD and EPL and Public Domain and CC-BY
Url: http://groovy-lang.org
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: groovy-lib = 2.4.4-1.fc23
Provides: mvn(org.codehaus.groovy:groovy) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-all) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-all:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-ant) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-ant:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-backports-compat23) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-backports-compat23:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-bsf) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-bsf:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-console) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-console:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-docgenerator) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-docgenerator:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-groovydoc) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-groovydoc:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-groovysh) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-groovysh:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-jmx) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-jmx:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-json) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-json:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-jsr223) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-jsr223:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-nio) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-nio:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-servlet) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-servlet:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-sql) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-sql:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-swing) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-swing:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-templates) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-templates:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-test) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-test:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-testng) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-testng:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-xml) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy-xml:pom:) = 2.4.4
Provides: mvn(org.codehaus.groovy:groovy:pom:) = 2.4.4
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(bsf:bsf)
Requires: mvn(com.beust:jcommander)
Requires: mvn(com.thoughtworks.qdox:qdox)
Requires: mvn(commons-logging:commons-logging)
Requires: mvn(jline:jline)
Requires: mvn(junit:junit)
Requires: mvn(org.apache.ant:ant)
Requires: mvn(org.apache.ant:ant-antlr)
Requires: mvn(org.apache.ant:ant-junit)
Requires: mvn(org.apache.ant:ant-launcher)
Requires: mvn(org.testng:testng)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: groovy-lib-2.4.4-1.fc23.cpio

%description
This package contains Groovy JAR artifact.

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

ln -s groovy/groovy.jar %buildroot/usr/share/java/groovy.jar
echo /usr/share/java/groovy.jar >> %name-list

%files -f %name-list

%changelog
* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.4.4-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.9-alt1_5jpp7
- new release

* Sun Jul 20 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8.9-alt1_2jpp7
- update

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.7-alt1_1jpp7
- new version

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.6-alt2_2jpp7
- applied repocop patches

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.6-alt1_2jpp7
- new version

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt5_2jpp5
- fixed build with moved maven1

* Tue Aug 30 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt4_2jpp5
- use maven1

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt3_2jpp5
- selected java5 compiler explicitly

* Sun May 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_2jpp5
- disabled rebuild-java-repository

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp5
- converted from JPackage by jppimport script

* Sat Nov 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp1.7
- converted from JPackage by jppimport script

