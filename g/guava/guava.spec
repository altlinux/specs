Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           guava
Version:        25.0
Release:        alt1_4jpp8
Summary:        Google Core Libraries for Java
# Most of the code is under ASL 2.0
# Few classes are under CC0, grep for creativecommons
License:        ASL 2.0 and CC0
URL:            https://github.com/google/guava
BuildArch:      noarch

Source0:        https://github.com/google/guava/archive/v%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info

%description
Guava is a suite of core and expanded libraries that include
utility classes, Googlea.'s collections, io classes, and much
much more.
This project is a complete packaging of all the Guava libraries
into a single jar.  Individual portions of Guava can be used
by downloading the appropriate module and its dependencies.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%package testlib
Group: Development/Java
Summary:        The guava-testlib artifact

%description testlib
guava-testlib provides additional functionality for conveninent unit testing

%prep
%setup -q

find . -name '*.jar' -delete

%pom_disable_module guava-gwt
%pom_disable_module guava-tests

%pom_remove_plugin -r :animal-sniffer-maven-plugin
# Downloads JDK source for doc generation
%pom_remove_plugin :maven-dependency-plugin guava

%pom_remove_dep :caliper guava-tests

%mvn_package :guava-parent guava

# javadoc generation fails due to strict doclint in JDK 1.8.0_45
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_xpath_inject /pom:project/pom:build/pom:plugins/pom:plugin/pom:configuration/pom:instructions "<_nouses>true</_nouses>" guava/pom.xml

%pom_remove_dep -r :animal-sniffer-annotations
%pom_remove_dep -r :error_prone_annotations
%pom_remove_dep -r :j2objc-annotations
%pom_remove_dep -r org.checkerframework:

annotations=$(
    find -name '*.java' \
    | xargs fgrep -h \
        -e 'import com.google.j2objc.annotations' \
        -e 'import com.google.errorprone.annotation' \
        -e 'import org.codehaus.mojo.animal_sniffer' \
        -e 'import org.checkerframework' \
    | sort -u \
    | sed 's/.*\.\([^.]*\);/\1/' \
    | paste -sd\|
)
# guava started using quite a few annotation libraries for code quality, which
# we don't have. This ugly regex is supposed to remove their usage from the code
find -name '*.java' | xargs sed -ri \
    "s/^import .*\.($annotations);//;s/@($annotations)"'\>\s*(\((("[^"]*")|([^)]*))\))?//g'

%build
# Tests fail on Koji due to insufficient memory,
# see https://bugzilla.redhat.com/show_bug.cgi?id=1332971
%mvn_build -s -f

%install
%mvn_install

%files -f .mfiles-guava
%doc CONTRIBUTORS README*
%doc --no-dereference COPYING

%files javadoc -f .mfiles-javadoc
%doc --no-dereference COPYING

%files testlib -f .mfiles-guava-testlib

%changelog
* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 25.0-alt1_4jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 25.0-alt1_1jpp8
- java update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 24.0-alt1_2jpp8
- java update

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 18.0-alt2_11jpp8
- fc update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 18.0-alt2_10jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt2_8jpp8
- new fc release

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt2_4jpp8
- added osgi provides

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 18.0-alt1_4jpp8
- unbootsrap build

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

