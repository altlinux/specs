Epoch: 0
Group: Development/Other
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:             joni
Version:          2.1.20
Release:          alt1_1jpp11
Summary:          Java port of Oniguruma regexp library

License:          MIT
URL:              https://github.com/jruby/%{name}
Source0:          https://github.com/jruby/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jruby.jcodings:jcodings)
BuildRequires:  mvn(org.ow2.asm:asm)

BuildArch: noarch
Source44: import.info

%description
joni is a port of Oniguruma, a regular expressions library,
to java. It is used by jruby.

%package javadoc
Group: Development/Java
Summary: API documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{name}-%{version}

find -name '*.class' -delete
find -name '*.jar' -delete

%mvn_file : %{name}

# Remove pointless parent pom
%pom_remove_parent

# Remove wagon extension
%pom_xpath_remove "pom:build/pom:extensions"

# Remove plugins not relevant for downstream RPM builds
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

# fixes rpmlint warning about wrong-file-end-of-line-encoding
sed -i -e 's|\r||' test/org/joni/test/TestC.java
sed -i -e 's|\r||' test/org/joni/test/TestU.java
sed -i -e 's|\r||' test/org/joni/test/TestA.java

# Generate OSGi metadata by using bundle packaging
%pom_xpath_set pom:packaging "bundle"
%pom_add_plugin org.apache.felix:maven-bundle-plugin "<extensions>true</extensions>"

%build
# Work around xmvn bug with generating javadoc from modular projects: https://github.com/fedora-java/xmvn/issues/58
# Disable default javadoc generation with -j then generate separately with
# explicit invokation of javadoc mojo without the module definition present
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8
find -name module-info.java -delete
xmvn --batch-mode --offline org.fedoraproject.xmvn:xmvn-mojo:javadoc

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:2.1.20-alt1_1jpp11
- new version

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_11jpp8
- fc update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_9jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_8jpp8
- fc29 update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_7jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_6jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_5jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_3jpp8
- new fc release

* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_2jpp8
- build with objectweb-asm

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.9-alt1_3jpp7
- new release

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.9-alt1_1jpp7
- new version

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_7jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_6jpp7
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_2jpp5
- fixes for java6 support

* Mon Sep 29 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_2jpp5
- converted from JPackage by jppimport script

