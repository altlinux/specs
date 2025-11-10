%define _unpackaged_files_terminate_build 1
%def_with check

Name: SimplyHTML
Version: 0.19.2
Release: alt1

Summary: SimplyHTML is an application for text processing
License: GPL-2.0-or-later
Group: Development/Java
Url: https://github.com/freeplane/shtml
Vcs: https://github.com/freeplane/shtml.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-11-compat
BuildRequires: javahelp2
BuildRequires: apache-commons-lang
BuildRequires: mnemonicsetter

%description
SimplyHTML is an application for text processing. It stores documents
as HTML files in combination with Cascading Style Sheets (CSS).

SimplyHTML is not intended to be used as an editor for web pages.
The application combines text processing features as known from
popular word processors with a simple and generic way of storing
textual information and styles.

%prep
%setup

%build
%gradle_publish

%install
%gradle_register

%gradle_install

%check
%gradle_check

%files -f .mfiles

%changelog
* Sun Nov 09 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.19.2-alt1
- New version after being removed from sisyphus.
- Build from the upstream git repo.
- Build with the xgradle.
- Build without javadoc.

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.16.18-alt1_6jpp8
- fc update & java 8 build

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.16.18-alt1_5jpp8
- java update

* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.16.18-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.16.18-alt1_3jpp8
- fc27 update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.16.18-alt1_2jpp8
- new version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.17-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.7-alt1_7jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.7-alt1_6jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.16.7-alt1_2jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.16.7-alt1_1jpp7
- new version

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.5-alt1_1jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.13.1-alt1_7jpp7
- new version
