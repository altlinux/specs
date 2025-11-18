%define _unpackaged_files_terminate_build 1

Name: apiguardian
Version: 1.1.2
Release: alt2

Summary: API Guardian Java annotation
License: Apache-2.0
Group: Development/Java
Url: https://github.com/apiguardian-team/apiguardian
Vcs: https://github.com/apiguardian-team/apiguardian.git
BuildArch: noarch

Source0: https://github.com/apiguardian-team/apiguardian/archive/r%version.tar.gz
Patch0: 0001-Adapt-for-Gradle-8-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: /proc
BuildRequires: rpm-build-java-osgi
BuildRequires: jpackage-17-compat
BuildRequires: biz-aQute-bnd-gradle-plugins

%description
API Guardian indicates the status of an API element and therefore its
level of stability as well.  It is used to annotate public types,
methods, constructors, and fields within a framework or application in
order to publish their API status and level of stability and to
indicate how they are intended to be used by consumers of the API.

%{?javadoc_package}

%prep
%setup -q -n apiguardian-r%{version}
%autopatch -p1

%build
%gradle_publish -Dfile.encoding=UTF-8

%install
%gradle_register
%gradle_register_javadoc

%gradle_install

%files -f .mfiles
%doc --no-dereference LICENSE

%changelog
* Fri Nov 14 2025 Ivan Khanas <xeno@altlinux.org> 1.1.2-alt2
- Add JPMS support.
- Switch to xgradle.

* Fri Jul 01 2022 Igor Vlasenko <viy@altlinux.org> 1.1.2-alt1_3jpp11
- new version

* Wed Aug 04 2021 Igor Vlasenko <viy@altlinux.org> 1.1.1-alt1_3jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1.1.1-alt1_1jpp11
- new version

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_2jpp8
- new version

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_4jpp8
- explicit build with java8

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3jpp8
- fc29 update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_2jpp8
- new version

