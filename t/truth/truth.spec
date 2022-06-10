Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 1.0.1
%bcond_with protobuf
%global vertag release_%(echo %version | tr . _)

Name:           truth
Version:        1.0.1
Release:        alt1_2jpp11
Summary:        An assertion framework for Java unit tests
License:        ASL 2.0
URL:            https://github.com/google/truth
Source0:        https://github.com/google/truth/archive/%{vertag}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.auto.value:auto-value)
# This is in auto-value >= 1.6
#BuildRequires:  mvn(com.google.auto.value:auto-value-annotations)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
# A number of annotation and testing deps are missing and are removed below
#BuildRequires:  mvn(com.google.errorprone:error_prone_annotations)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(com.google.guava:guava-testlib)
%if %{with protobuf}
BuildRequires:  mvn(com.google.protobuf:protobuf-java)
BuildRequires:  mvn(com.google.protobuf:protobuf-javalite)
%endif
#BuildRequires:  mvn(com.google.testing.compile:compile-testing)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(io.github.java-diff-utils:java-diff-utils)
Source44: import.info
#BuildRequires:  mvn(org.checkerframework:checker-qual)

%description
Truth is a library provides alternative ways to express assertions in
unit tests. It can be used as a replacement for JUnit's assertions or FEST
or it can be used alongside where other approaches seem more suitable.

#{?javadoc_package}

%prep
%setup -q -n %{name}-%{vertag}

# Remove items with unpackaged dependencies
%pom_remove_parent
%pom_disable_module re2j extensions
%if %{without protobuf}
%pom_disable_module liteproto extensions
%pom_disable_module proto extensions
%endif
%pom_remove_plugin :gwt-maven-plugin core
# This is in auto-value >= 1.6
%pom_remove_dep -r :auto-value-annotations
%pom_remove_dep -r :compile-testing
%pom_remove_dep -r :error_prone_annotations
%pom_remove_dep :gwt-user core
%pom_remove_dep :guava-gwt core
%pom_remove_dep -r org.checkerframework:
%pom_remove_plugin -r :protobuf-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :animal-sniffer-maven-plugin
%pom_change_dep :protobuf-lite :protobuf-javalite extensions/liteproto/pom.xml
# Fails with missing class TestMessageLite2
rm extensions/liteproto/src/test/java/com/google/common/truth/extensions/proto/LiteProtoSubjectTest.java
# Fails with missing class TestMessage2
rm extensions/proto/src/test/java/com/google/common/truth/extensions/proto/OverloadResolutionTest.java

# Remove kr.motd.maven:os-maven-plugin extension
%pom_xpath_remove "pom:build/pom:extensions" extensions/liteproto/pom.xml extensions/proto/pom.xml

# Needed to fix javadoc build
%pom_add_dep javax.annotation:javax.annotation-api extensions/proto

# Exclude tests with missing dependencies
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:testExcludes" "
            <testExclude>**/gwt/*.java</testExclude>
            <testExclude>**/ComparableSubjectCompileTest.java</testExclude>" core

# Bump to Java 8 to fix this:
# [ERROR] /home/orion/fedora/truth/truth-release_0_42/core/src/test/java/com/google/common/truth/TruthAssertThatTest.java:[54,40] error: <anonymous com.google.common.truth.TruthAssertThatTest$2> is not abstract and does not override abstract method test(Method) in Predicate
sed -i 's/1\.7/1.8/' pom.xml

# Fix difflib
%pom_change_dep com.googlecode.java-diff-utils:diffutils io.github.java-diff-utils:java-diff-utils . core
find -name '*.java' -exec sed -i -e '/^import/s/ difflib\.Patch/ com.github.difflib.patch.Patch/' \
    -e '/^import/s/ difflib\.DiffUtils\.generateUnifiedDiff;/ com.github.difflib.UnifiedDiffUtils.generateUnifiedDiff;/' \
    -e '/^import/s/ difflib\./ com.github.difflib./'  {} +

# truth uses quite a few annotation libraries for code quality, which
# we don't have. This ugly regex is supposed to remove their usage from the code
annotations=$(
    find -name '*.java' \
    | xargs grep -h \
        -e '^import com\.google\.j2objc\.annotations' \
        -e '^import com\.google\.errorprone\.annotation' \
        -e '^import com\.google\.errorprone\.annotations' \
        -e '^import com\.google\.common\.annotations' \
        -e '^import static jsinterop\.annotations' \
        -e '^import jsinterop\.annotations' \
        -e '^import org\.codehaus\.mojo\.animal_sniffer' \
        -e '^import org\.checkerframework' \
    | sort -u \
    | sed 's/.*\.\([^.]*\);/\1/' \
    | paste -sd\|
)
find -name '*.java' | xargs sed -ri \
    "s/^import .*\.($annotations);//;s/@($annotations)"'\>\s*(\((("[^"]*")|([^)]*))\))?//g'

%build
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8 -DfailIfNoTests=false -Dtest='!SubjectTest*,!com.google.common.truth.ExpectFailureNonRuleTest$ExpectFailureThrowAfterSubject*,!com.google.common.truth.ExpectFailureNonRuleTest$ExpectFailureThrowIn*'

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Wed Jun 08 2022 Igor Vlasenko <viy@altlinux.org> 1.0.1-alt1_2jpp11
- new version

* Wed May 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2_6jpp8
- fixed build with maven-javadoc-plugin 3

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_5jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_4jpp8
- new version

