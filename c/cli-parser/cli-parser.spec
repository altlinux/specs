%define _unpackaged_files_terminate_build 1

Name: cli-parser
Version: 1.1.6
Release: alt1

Summary: Command Line Interface Parser for Java
License: Apache-2.0
Group: Development/Java
URL: https://github.com/spullara/cli-parser
VCS: https://github.com/spullara/cli-parser

Source0: %name-%version.tar.gz
Source1: LICENSE.Apache-2.0
Patch0: cli-parser-jdk8.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-21-openjdk-devel
BuildRequires: mvn(junit:junit)
BuildRequires: maven-local

BuildArch: noarch

%description
An annotation-based command line interface parser.

%package javadoc
Group: Development/Java
Summary: Javadoc for %name

%description javadoc
This package contains javadoc for %name.

%prep
%setup -q -n %name-%name-%version
%autopatch -p1
cp -p %SOURCE1 LICENSE

%pom_remove_plugin :maven-gpg-plugin

%mvn_file : %name

%build
%mvn_build -s -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles-cli-parser
%doc LICENSE

%files javadoc -f .mfiles-javadoc

%changelog
* Sun Nov 22 2026 Ivan Khanas <xeno@altlinux.org> 1.1.6-alt1
- New version.

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_10jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_9jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_8jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_7jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_6jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_5jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.2-alt1_4jpp8
- new version
