BuildRequires: apache-parent
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          portals-pom
Version:       1.3
Release:       alt3_14jpp8
Summary:       Apache Portals parent pom
License:       ASL 2.0
Url:           http://portals.apache.org/
# svn export http://svn.apache.org/repos/asf/portals/portals-pom/tags/portals-pom-1.3
# tar czf portals-pom-1.3-src-svn.tar.gz portals-pom-1.3
Source0:       %{name}-%{version}-src-svn.tar.gz
BuildRequires: maven-local
BuildRequires: maven-install-plugin
BuildArch:     noarch
Source44: import.info

%description
Apache Portals is a collaborative software development project
dedicated to providing robust, full-featured, commercial-quality,
and freely available Portal related software on a wide variety of
platforms and programming languages. This project is managed in
cooperation with various individuals worldwide (both independent and
company-affiliated experts), who use the Internet to communicate, plan,
and develop Portal software and related documentation.

%prep
%setup -q

%pom_remove_plugin :ianal-maven-plugin

for d in LICENSE NOTICE ; do
  iconv -f iso8859-1 -t utf-8 $d > $d.conv && mv -f $d.conv $d
  sed -i 's/\r//' $d
done

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt3_14jpp8
- added BR: apache-parent for javapackages 5

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_14jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_13jpp8
- new fc release

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_12jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3jpp7
- new version

