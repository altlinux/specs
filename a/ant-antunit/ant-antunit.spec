Group: Development/Other
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           ant-antunit
Version:        1.4.1
Release:        alt1_3jpp11
Summary:        Unit Test Framework for Ant Tasks
License:        ASL 2.0
URL:            https://ant.apache.org/antlibs/antunit
BuildArch:      noarch

Source0:        https://archive.apache.org/dist/ant/antlibs/antunit/source/apache-%{name}-%{version}-src.tar.bz2
Source1:        https://archive.apache.org/dist/ant/antlibs/antunit/source/apache-%{name}-%{version}-src.tar.bz2.asc
Source2:        https://archive.apache.org/dist/ant/KEYS

BuildRequires:  gnupg2
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-testutil)
Source44: import.info

%description
This library contains tasks that enables Ant task developers to test their tasks
with Ant and without JUnit.  It contains a few assertion tasks and an antunit
task that runs build files instead of test classes and is modelled after the
JUnit task.

%{?javadoc_package}

%prep

%setup -q -n apache-%{name}-%{version}


find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

mv %{name}-%{version}.pom pom.xml

%pom_xpath_inject pom:project/pom:build '
    <resources>
      <resource>
        <directory>${project.basedir}/src/main</directory>
        <includes>
          <include>**/antlib.xml</include>
        </includes>
      </resource>
    </resources>'

# EatYourOwnDogFoodTest
sed -i 's|build/test-classes|target/test-classes|g' src/etc/testcases/antunit/java-io.xml

# AssertTest
sed -i 's|build/classes|target/classes|g' src/etc/testcases/assert.xml src/tests/junit/org/apache/ant/antunit/AssertTest.java

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.compiler.release=8

%check
# enable tests
%pom_xpath_set pom:maven.test.skip false

# compile tests
xmvn test-compile -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

# run tests
java -cp target/classes:target/test-classes:$(build-classpath junit hamcrest ant/ant-testutil ant ant/ant-launcher) \
       org.junit.runner.JUnitCore \
       $(find src/tests/junit/ -name '*.java' -printf '%%P\n' | cut -f 1 -d '.' | tr / .)

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference common/LICENSE NOTICE

%changelog
* Sun Jun 12 2022 Igor Vlasenko <viy@altlinux.org> 1.4.1-alt1_3jpp11
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 1.4-alt1_2jpp11
- new version

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_13jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_11jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_10jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_8jpp8
- fc27 update

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_4jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_12jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_6jpp7
- new release

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_4jpp7
- build with ant-junit

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_4jpp7
- new fc release

* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp7
- new version

