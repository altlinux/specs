Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           guava20
Version:        20.0
Release:        alt1_9jpp8
Summary:        Google Core Libraries for Java
# Most of the code is under ASL 2.0
# Few classes are under CC0, grep for creativecommons
License:        ASL 2.0 and CC0
URL:            https://github.com/google/guava
BuildArch:      noarch

Source0:        https://github.com/google/guava/archive/v%{version}.tar.gz
Patch0:         0001-Avoid-presizing-arrays.patch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
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
%setup -q -n guava-%{version}

%patch0 -p1

find . -name '*.jar' -delete

%pom_disable_module guava-gwt
%pom_remove_plugin -r :animal-sniffer-maven-plugin 
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_dep jdk:srczip guava
%pom_remove_dep :caliper guava-tests
%mvn_package :guava-parent guava
%mvn_package :guava-tests __noinstall

# javadoc generation fails due to strict doclint in JDK 1.8.0_45
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_xpath_inject /pom:project/pom:build/pom:plugins/pom:plugin/pom:configuration/pom:instructions "<_nouses>true</_nouses>" guava/pom.xml

%pom_remove_dep -r :animal-sniffer-annotations
%pom_remove_dep -r :error_prone_annotations
%pom_remove_dep -r :j2objc-annotations

annotations=$(
    fgrep -hr -e com.google.j2objc.annotations \
        -e com.google.errorprone.annotation -e org.codehaus.mojo.animal_sniffer \
    | sort -u \
    | sed 's/.*\.\([^.]*\);/\1/' \
    | paste -sd\|
)
# guava started using quite a few annotation libraries for code quality, which
# we don't have. This ugly regex is supposed to remove their usage from the code
find -name '*.java' | xargs sed -ri \
    "s/^import .*\.($annotations);//;s/@($annotations)"'\>\s*(\((("[^"]*")|([^)]*))\))?//'

%build
%mvn_compat_version : 20.0 19.0 18.0 17.0 16.0.1 16.0 15.0 14.0.1 14.0 13.0.1 13.0 12.0.1 12.0 11.0.2 11.0.1 11.0 10.0.1 10.0
%mvn_alias :guava com.google.collections:google-collections com.google.guava:guava-jdk5
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
* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 20.0-alt1_9jpp8
- new version

* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 20.0-alt1_5jpp8
- new version

