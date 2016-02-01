Name: mockito
Version: 1.10.19
Summary: A Java mocking framework
License: MIT
Url: http://mockito.org
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mockito = 1.10.19-4.fc23
Provides: mvn(org.mockito:mockito-all) = 1.10.19
Provides: mvn(org.mockito:mockito-all:pom:) = 1.10.19
Provides: mvn(org.mockito:mockito-core) = 1.10.19
Provides: mvn(org.mockito:mockito-core:pom:) = 1.10.19
Requires: cglib
Requires: hamcrest
Requires: java-headless
Requires: jpackage-utils
Requires: junit
Requires: mvn(net.sf.cglib:cglib)
Requires: mvn(org.hamcrest:hamcrest-core)
Requires: mvn(org.objenesis:objenesis)
Requires: objenesis

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: mockito-1.10.19-4.fc23.cpio

%description
Mockito is a mocking framework that tastes really good. It lets you write
beautiful tests with clean & simple API. Mockito doesn't give you hangover
because the tests are very readable and they produce clean verification
errors.

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
* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10.19-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt2_9jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.9.0-alt1_9jpp7
- new version

* Tue Sep 04 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt5_0.1jpp6
- fixed build

* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt4_0.1jpp6
- fixed build with new testng and xbean

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt3_0.1jpp6
- fixed build

* Mon Jan 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt2_0.1jpp6
- fixed build

* Mon Oct 18 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.8.5-alt1_0.1jpp6
- new version

