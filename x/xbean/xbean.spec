Name: xbean
Version: 4.3
Summary: Java plugin based web server
License: ASL 2.0
Url: http://geronimo.apache.org/xbean/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.apache.xbean:xbean-bundleutils) = 4.3
Provides: mvn(org.apache.xbean:xbean-bundleutils:pom:) = 4.3
Provides: mvn(org.apache.xbean:xbean-classpath) = 4.3
Provides: mvn(org.apache.xbean:xbean-classpath:pom:) = 4.3
Provides: mvn(org.apache.xbean:xbean-finder) = 4.3
Provides: mvn(org.apache.xbean:xbean-finder:pom:) = 4.3
Provides: mvn(org.apache.xbean:xbean-naming) = 4.3
Provides: mvn(org.apache.xbean:xbean-naming:pom:) = 4.3
Provides: mvn(org.apache.xbean:xbean-reflect) = 4.3
Provides: mvn(org.apache.xbean:xbean-reflect:pom:) = 4.3
Provides: mvn(org.apache.xbean:xbean-telnet) = 4.3
Provides: mvn(org.apache.xbean:xbean-telnet:pom:) = 4.3
Provides: mvn(org.apache.xbean:xbean:pom:) = 4.3
Provides: xbean = 4.3-1.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.codehaus.groovy:groovy)
Requires: mvn(org.slf4j:slf4j-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xbean-4.3-1.fc23.cpio

%description
The goal of XBean project is to create a plugin based server
analogous to Eclipse being a plugin based IDE. XBean will be able to
discover, download and install server plugins from an Internet based
repository. In addition, we include support for multiple IoC systems,
support for running with no IoC system, JMX without JMX code,
lifecycle and class loader management, and a rock solid Spring
integration.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.13-alt1_4jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.13-alt1_1jpp7
- new version

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.12-alt1_4jpp7
- new version

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt4_3jpp7
- fixed build

* Mon Apr 01 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt3_3jpp7
- restored rcp dep

* Sun Mar 31 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt2_3jpp7
- bootstrapping eclipse - dropped eclipse-rcp dep

* Fri Sep 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.11.1-alt1_3jpp7
- new version

* Fri Sep 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.8-alt1_2jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.7-alt3_7jpp7
- fixed build

* Tue May 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.7-alt2_7jpp7
- added maven-xbean-plugin

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.7-alt1_7jpp7
- new version

* Tue Jan 25 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.4.3-alt1_2jpp6
- new version

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt1_1jpp5
- first build

