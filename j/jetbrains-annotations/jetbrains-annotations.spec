Name: jetbrains-annotations
Version: 24.1.0
Release: alt1

Summary: IntelliJ IDEA Annotations
License: Apache-2.0
Group: Development/Java
Url: http://www.jetbrains.org
VCS: https://github.com/JetBrains/java-annotations.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Adapt-for-Gradle-8-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: jpackage-generic-compat
BuildRequires: xgradle

%description
A set of annotations used for code inspection support and code documentation.

%package javadoc
Group: Development/Documentation
Summary: Javadoc for %name
BuildArch: noarch

%description javadoc
This package contains javadoc for %name.

%prep
%setup
%autopatch -p1

%build
%gradle_publish

%install
%gradle_register
%gradle_register_javadoc

%gradle_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Sat Nov 01 2025 Ivan Khanas <xeno@altlinux.org> 24.1.0-alt1
- New version.

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:15.0-alt1_8jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:15.0-alt1_7jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:15.0-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:15.0-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:15.0-alt1_4jpp8
- new jpp release

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:15.0-alt1_3jpp8
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.0.2-alt2_2jpp5
- fixes for java6 support

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:6.0.2-alt1_2jpp5
- new jpp release

* Mon Sep 15 2008 Igor Vlasenko <viy@altlinux.ru> 0:6.0.2-alt1_1jpp5
- jpp5 build

