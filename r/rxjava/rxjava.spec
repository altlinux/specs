Name: rxjava
Version: 3.1.12
Release: alt1

Summary: Reactive Extensions for the JVM
License: Apache-2.0
Group: Development/Java
Url: https://github.com/ReactiveX/RxJava
Vcs: https://github.com/ReactiveX/RxJava.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Remove-unwanted-plugins-alt-patch.patch
Patch1: 0002-Configure-publishing-with-maven-publish-alt-patch.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: java-17-openjdk-devel
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: biz-aQute-bnd-gradle-plugins
BuildRequires: badass-jar-plugin
BuildRequires: shadow-gradle-plugin
BuildRequires: reactive-streams-jvm

%description
RxJava a library for composing asynchronous and
event-based programs using observable sequences
for the Java VM.

%prep
%setup
%autopatch -p1

sed -i 's/3\.0\.0-SNAPSHOT/%version/g' gradle.properties

%build
%gradle_publish

%install
%gradle_register

%gradle_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Thu Nov 06 2025 Ivan Khanas <xeno@altlinux.org> 3.1.12-alt1
- New version.

* Tue Aug 16 2022 Igor Vlasenko <viy@altlinux.org> 1.1.8-alt1_6jpp11
- jdk17 support

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_6jpp8
- new version

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_4jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_3jpp8
- fc27 update

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_3jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_2jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.13-alt1_1jpp8
- new version

