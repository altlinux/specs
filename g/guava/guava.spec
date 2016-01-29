Name: guava
Version: 18.0
Summary: Google Core Libraries for Java
License: ASL 2.0
Url: https://github.com/google/guava
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: guava = 18.0-4.fc23
Provides: mvn(com.google.collections:google-collections) = 18.0
Provides: mvn(com.google.collections:google-collections:pom:) = 18.0
Provides: mvn(com.google.guava:guava) = 18.0
Provides: mvn(com.google.guava:guava-jdk5) = 18.0
Provides: mvn(com.google.guava:guava-jdk5:pom:) = 18.0
Provides: mvn(com.google.guava:guava-parent:pom:) = 18.0
Provides: mvn(com.google.guava:guava:pom:) = 18.0
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: guava-18.0-4.fc23.cpio

%description
Guava is a suite of core and expanded libraries that include
utility classes, Google collections, io classes, and much
much more.
This project is a complete packaging of all the Guava libraries
into a single jar.  Individual portions of Guava can be used
by downloading the appropriate module and its dependencies.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_3jpp7
- new release

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 13.0-alt1_1jpp7
- new version

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 09-alt1_2jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 09-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

