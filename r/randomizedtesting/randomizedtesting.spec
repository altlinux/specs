Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:          randomizedtesting
Version:       2.3.1
Release:       alt1_2jpp8
Summary:       Java Testing Framework
License:       ASL 2.0
URL:           http://labs.carrotsearch.com/randomizedtesting.html
Source0:       https://github.com/carrotsearch/randomizedtesting/archive/release/%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(dom4j:dom4j)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.ant:ant)
BuildRequires: mvn(org.apache.ant:ant-junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.hamcrest:hamcrest-core)
BuildRequires: mvn(org.ow2.asm:asm)
BuildRequires: mvn(org.simpleframework:simple-xml)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires: mvn(stax:stax-api)

BuildArch:     noarch
Source44: import.info

%description
Foundation classes and rules for applying the
principles of Randomized Testing.

%package junit4-ant
Group: Development/Java
Summary:       RandomizedTesting JUnit4 ANT Task
Requires:      %{name} = %{version}

%description junit4-ant
RandomizedTesting JUnit4 ANT Task.

%package junit4-maven-plugin
Group: Development/Java
Summary:       RandomizedTesting JUnit4 Maven Plugin
Requires:      %{name} = %{version}

%description junit4-maven-plugin
RandomizedTesting JUnit4 Maven Plugin.

%package runner
Group: Development/Java
Summary:       RandomizedTesting Randomized Runner
Requires:      %{name} = %{version}

%description runner
RandomizedRunner is a JUnit runner, so it is capable of
running @Test-annotated test cases.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-release-%{version}
find . -name "*.class" -delete
find . -name "*.jar" -delete
find . -name "*.dll" -delete
find . -name "*.dylib" -delete
find . -name "*.so" -delete

# Remove bundled JavaScript libraries
find . -name "*.js" -print -delete
sed -i '/jquery/d' \
 junit4-ant/src/main/resources/com/carrotsearch/ant/tasks/junit4/templates/json/index.html \
 junit4-ant/src/main/java/com/carrotsearch/ant/tasks/junit4/listeners/json/JsonReport.java
sed -i '/script.js/d' \
 junit4-ant/src/main/resources/com/carrotsearch/ant/tasks/junit4/templates/json/index.html \
 junit4-ant/src/main/java/com/carrotsearch/ant/tasks/junit4/listeners/json/JsonReport.java

%pom_disable_module examples/ant
%pom_disable_module examples/maven
%pom_disable_module examples/security-manager
%pom_disable_module junit4-maven-plugin-tests

# Disable repackaged and shaded deps
%pom_remove_plugin com.pyx4me:proguard-maven-plugin junit4-ant
%pom_remove_plugin :maven-dependency-plugin junit4-ant

# Fix deps scope
%pom_xpath_remove "pom:scope[text()='provided']" junit4-ant

# Convert from dos to unix line ending
for file in CHANGES.txt CONTRIBUTING.txt README.txt; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

# package org.hamcrest does not exist
%pom_add_dep org.hamcrest:hamcrest-core randomized-runner

# Use junit 4.10 org.junit.internal.runners.rules.ValidationError:
# The @Rule 'ruleChain' must not be static or it must be annotated with @ClassRule.
rm -r randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestClassMethodFiltering.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestContextRandom.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestCustomMethodProvider.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestExpected.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestFailurePropagationCompatibility.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestFilteringWarnings.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestIgnoredRunCount.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestJ9SysThreads.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestListenersAnnotation.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestMacSysThreads.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestNightlyMode.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestOutOfScopeRandomUse.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestOverridingDefaultExceptionHandler.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestParameterized.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestParameterizedShufflesOrder.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestRepeatTestWithComplexDescription.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestResourceDisposal.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestRules.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestSeedDecorator.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestSeedFixingWithProperties.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestSeedParameterOptional.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestStackAugmentation.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestTargetMethod.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestTestFiltering.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestTestCaseInstanceProviders.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestTestCaseOrdering.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestTestGroups.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestUncaughtExceptionsDuplicated.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/TestValidation.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/contracts \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/rules \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test001TimeoutSuite.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test002TimeoutMethod.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test003ThreadLeaksMethod.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test004ThreadLeaksSuite.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test005ThreadLeaksSystemThreads.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test006TimeoutAndThreadLeak.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test007UncaughtExceptions.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test008SeedsAnnotation.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test009TimeoutOrNotIdenticalSequence.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test010Zombies.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test013ThreadLeaksScopeNone.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test014Timeout.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test015TimeoutOverride.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test016ThreadLeaksCustomFilters.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test017ThreadLeaksCustomFiltersException.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test018TimeoutStacks.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test019ThreadLeakGroup.java \
 randomized-runner/src/test/java/com/carrotsearch/randomizedtesting/timeouts/Test020SuiteTimeoutStopsTests.java

# org.apache.tools.ant.BuildException:
# At least one slave process threw an exception,
# first: Forked JVM's classpath must include a junit4 JAR.
# [junit4:junit4] ERROR: JVM J0 ended with an exception: Forked JVM's classpath must include a junit4 JAR.
%pom_xpath_remove "pom:executions/pom:execution[pom:id = 'surefire-it']" junit4-ant
 
%mvn_package :%{name}-parent %{name}-runner

%build

%mvn_build -s

%install
%mvn_install

%files
%doc CHANGES.txt CONTRIBUTING.txt README.txt
%doc LICENSE.txt

%files junit4-ant -f .mfiles-junit4-ant
%files junit4-maven-plugin -f .mfiles-junit4-maven-plugin
%files runner -f .mfiles-%{name}-runner

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_2jpp8
- new version

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.3-alt1_3jpp8
- java 8 mass update

