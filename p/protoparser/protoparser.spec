%define _unpackaged_files_terminate_build 1

Name: protoparser
Version: 4.0.3
Release: alt1

Summary: Java parser for .proto schema declarations
License: Apache-2.0
Group: Development/Java
URL: https://github.com/square/protoparser
VCS: https://github.com/square/protoparser.git

Source: %name-%version.tar
Patch: system-auto-value.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local
BuildRequires: mvn(com.google.auto.value:auto-value)
BuildRequires: mvn(com.google.auto.value:auto-value-annotations)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.assertj:assertj-core)
BuildRequires: mvn(org.sonatype.oss:oss-parent:pom:)

BuildArch: noarch

%description
ProtoParser reads Protocol Buffers schema declarations and represents them
as Java objects.

%javadoc_package

%prep
%setup
%patch -p1
%pom_remove_plugin :maven-checkstyle-plugin
%mvn_file : %name

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%changelog
* Fri Nov 20 2026 Ivan Khanas <xeno@altlinux.org> 4.0.3-alt1
- New version.

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt1_7jpp8
- fc update

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt1_6jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt1_2jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.1.5-alt1_1jpp8
- new version

