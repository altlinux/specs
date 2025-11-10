%define _unpackaged_files_terminate_build 1
# Broken due to mockito.
# Link: https://bugzilla.altlinux.org/56779
%def_without check

Name: mnemonicsetter
Version: 0.6
Release: alt1

Summary: Automatically assigns mnemonics to menu items and toolbar elements
License: Apache-2.0
Group: Development/Java
Url: https://mvnrepository.com/artifact/org.freeplane.dpolivaev.mnemonicsetter/mnemonicsetter
Vcs: https://github.com/dpolivaev/mnemonicsetter.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-11-compat
%if_with check
BuildRequires: hamcrest
BuildRequires: mockito
%endif

%description
Automatically assigns mnemonics to menu items
and toolbar elements (Java Swing).

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register

%gradle_install

%check
%gradle_check

%files -f .mfiles

%changelog
* Sun Nov 09 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.6-alt1
- New version after being removed from sisyphus.
- Build from the upstream git repo.
- Build with the xgradle.

* Thu Jul 18 2019 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_5jpp8
- fc update & java 8 build

* Mon Jul 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_4jpp8
 -build with mockito1

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_3jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_2jpp8
- new jpp release

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1jpp8
- new version
