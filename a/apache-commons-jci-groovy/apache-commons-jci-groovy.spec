Name: apache-commons-jci-groovy
Version: 1.1
Summary: Commons Java Compiler Interface - groovy
License: ASL 2.0
Url: http://commons.apache.org/jci/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-commons-jci-groovy = 1.1-2.fc23
Provides: mvn(org.apache.commons:commons-jci-groovy) = 1.1
Provides: mvn(org.apache.commons:commons-jci-groovy:pom:) = 1.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.commons:commons-jci-core)
Requires: mvn(org.codehaus.groovy:groovy)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: apache-commons-jci-groovy-1.1-2.fc23.cpio

%description
Commons JCI compiler implementation for the groovy compiler.

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
* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt4_10jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt4_7jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt4_5jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt3_5jpp7
- fixed build

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt2_5jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_5jpp7
- fc update

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_4jpp7
- fc release

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_0.r831715.4jpp6
- fixed build with new asm

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_0.r831715.4jpp6
- fixed build with maven3

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_0.r831715.4jpp6
- new version

