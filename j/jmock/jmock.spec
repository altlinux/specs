Name: jmock
Version: 2.8.1
Summary: Java library for testing code with mock objects
License: BSD
Url: http://www.jmock.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jmock = 2.8.1-2.fc23
Provides: mvn(org.jmock:jmock) = 2.8.1
Provides: mvn(org.jmock:jmock-example) = 2.8.1
Provides: mvn(org.jmock:jmock-example:pom:) = 2.8.1
Provides: mvn(org.jmock:jmock-junit3) = 2.8.1
Provides: mvn(org.jmock:jmock-junit3::tests:) = 2.8.1
Provides: mvn(org.jmock:jmock-junit3:pom:) = 2.8.1
Provides: mvn(org.jmock:jmock-junit4) = 2.8.1
Provides: mvn(org.jmock:jmock-junit4:pom:) = 2.8.1
Provides: mvn(org.jmock:jmock-legacy) = 2.8.1
Provides: mvn(org.jmock:jmock-legacy:pom:) = 2.8.1
Provides: mvn(org.jmock:jmock-parent:pom:) = 2.8.1
Provides: mvn(org.jmock:jmock-script) = 2.8.1
Provides: mvn(org.jmock:jmock-script::tests:) = 2.8.1
Provides: mvn(org.jmock:jmock-script:pom:) = 2.8.1
Provides: mvn(org.jmock:jmock-testjar) = 2.8.1
Provides: mvn(org.jmock:jmock-testjar:pom:) = 2.8.1
Provides: mvn(org.jmock:jmock::tests:) = 2.8.1
Provides: mvn(org.jmock:jmock:pom:) = 2.8.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(cglib:cglib)
Requires: mvn(junit:junit)
Requires: mvn(org.beanshell:bsh)
Requires: mvn(org.hamcrest:hamcrest-library)
Requires: mvn(org.objenesis:objenesis)
Requires: mvn(org.ow2.asm:asm)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jmock-2.8.1-2.fc23.cpio

%description
Mock objects help you design and test the interactions between the objects in
your programs.
The jMock library:
  * makes it quick and easy to define mock objects, so you don't break the
    rhythm of programming.
  * lets you precisely specify the interactions between your objects, reducing
    the brittleness of your tests.
  * works well with the auto-completion and re-factoring features of your IDE
  * plugs into your favorite test framework
  * is easy to extend.

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
* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.8.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_3jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_2jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.5.1-alt1_1jpp7
- fc update

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt4_3jpp6
- build with objectweb-asm

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_3jpp6
- new jpp release

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt3_2jpp5
- fixed build; use cglib21 (with old asm)

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt2_2jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.0-alt1_1jpp1.7
- updated to new jpackage release

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_4jpp1.7
- converted from JPackage by jppimport script

