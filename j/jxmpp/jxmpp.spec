Name: jxmpp
Version: 1.1.0
Release: alt1

Summary: An Open Source XMPP Java base-library
License: Apache-2.0
Group: Development/Java
Url: https://github.com/igniterealtime/jxmpp
Vcs: https://github.com/igniterealtime/jxmpp.git
BuildArch: noarch

Source0: %name-%version.tar
Patch0: 0001-Adapt-build-without-custom-upstream-plugins.patch

BuildRequires(pre): rpm-macros-gradle
BuildRequires: xgradle
BuildRequires: rpm-build-java
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
BuildRequires: maven-local
BuildRequires: junit5
BuildRequires: libidn-java
BuildRequires: icu4j

%description
JXMPP is an Open Source Java base library for XMPP. It
provides often used functionality needed to build a XMPP stack.

%package core
Group: Development/Java
Summary: JXMPP Core

%description core
JXMPP core components.

%package jid
Group: Development/Java
Summary: JXMPP JID

%description jid
JID classes from JXMPP.

%package stringprep-libidn
Group: Development/Java
Summary: JXMPP Stringprep Libidn

%description stringprep-libidn
JXMPP Stringprep with libidn.

%package stringprep-icu4j
Group: Development/Java
Summary: JXMPP Stringprep icu4j

%description stringprep-icu4j
JXMPP Stringprep with icu4j.

%package util-cache
Group: Development/Java
Summary: JXMPP Util Cache

%description util-cache
A minimalistic and efficient bounded LRU Cache
with optional expiration.

%package javadoc
Group: Development/Java
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

%check
%gradle_check

%files core
%_mavenpomdir/jxmpp/jxmpp-core.pom
%_javadir/jxmpp/jxmpp-core.jar
%doc --no-dereference LICENSE

%files jid
%_mavenpomdir/jxmpp/jxmpp-jid.pom
%_javadir/jxmpp/jxmpp-jid.jar
%doc --no-dereference LICENSE

%files stringprep-libidn
%_mavenpomdir/jxmpp/jxmpp-stringprep-libidn.pom
%_javadir/jxmpp/jxmpp-stringprep-libidn.jar
%doc --no-dereference LICENSE

%files stringprep-icu4j
%_mavenpomdir/jxmpp/jxmpp-stringprep-icu4j.pom
%_javadir/jxmpp/jxmpp-stringprep-icu4j.jar
%doc --no-dereference LICENSE

%files util-cache
%_mavenpomdir/jxmpp/jxmpp-util-cache.pom
%_javadir/jxmpp/jxmpp-util-cache.jar
%doc README.md
%doc --no-dereference LICENSE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE

%changelog
* Wed Nov 05 2025 Ivan Khanas <xeno@altlinux.org> 1.1.0-alt1
- New version.
- Add jxmpp-stringprep-icu4j subpackage.
- Switch to xgradle.

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_8jpp8
- new version

* Tue Dec 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_7jpp8
- built w/o libidn support

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_4jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_3jpp8
- new fc release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1_2jpp8
- new version

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_3jpp8
- new version

