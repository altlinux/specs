Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           truth
Version:        0.23
Release:        alt1_6jpp8
Summary:        An assertion framework for Java unit tests
License:        ASL 2.0
URL:            https://github.com/google/truth
# Created from revision 3c4492b0f72290c8b4a32f1b313b13501e96f44d
# of git@github.com:google/truth.git using the following command:
# git archive --format=tar --prefix=truth-0.23/ 3c4492b |xz >truth-0.23.tar.xz
Source0:        truth-0.23.tar.xz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.google.auto.value:auto-value)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Source44: import.info

%description
Truth is a library provides alternative ways to express assertions in
unit tests. It can be used as a replacement for JUnit's assertions or FEST
or it can be used alongside where other approaches seem more suitable.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :gwt-maven-plugin core
%pom_remove_dep :gwt-user core
%pom_remove_dep :guava-gwt core
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration" "
          <testExcludes>
            <exclude>**/gwt/*.java</exclude>
          </testExcludes>" core

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%dir %{_javadir}/%{name}
%doc LICENSE
%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_5jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_4jpp8
- new version

