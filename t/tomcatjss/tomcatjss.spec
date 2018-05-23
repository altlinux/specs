%define _unpackaged_files_terminate_build 1

Name: tomcatjss
Version: 7.3.0
Release: alt1%ubt

Summary: JSSE module for Apache Tomcat that uses JSS
License: LGPLv2+
Group: System/Libraries
# Source-git: https://github.com/dogtagpki/tomcatjss.git
Url: http://www.dogtagpki.org/wiki/TomcatJSS

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
BuildRequires: ant
BuildRequires: apache-commons-lang
BuildRequires: jss
BuildRequires: tomcat

BuildArch: noarch
Requires: apache-commons-lang
Requires: apache-commons-logging
Requires: java-headless
Requires: jss
Requires: tomcat

%description
JSS Connector for Apache Tomcat, installed via the tomcatjss package,
is a Java Secure Socket Extension (JSSE) module for Apache Tomcat that
uses Java Security Services (JSS), a Java interface to Network Security
Services (NSS).

%prep
%setup

%build
ant -v -f build.xml \
    -Djnidir=%_jnidir dist

%install
ant -v -f build.xml \
    -Djnidir=%_jnidir \
    -Dinstall.doc.dir=%buildroot%_docdir/%name-%version \
    -Dinstall.jar.dir=%buildroot%_javadir \
    install

%files
%doc README LICENSE
%_javadir/*

%changelog
* Thu May 24 2018 Stanislav Levin <slev@altlinux.org> 7.3.0-alt1%ubt
- 7.2.4 -> 7.3.0

* Wed Nov 08 2017 Stanislav Levin <slev@altlinux.org> 7.2.4-alt2%ubt
- Remove tomcat-native from Conflicts due to tomcat dependency on
  tomcat-native

* Fri Sep 22 2017 Stanislav Levin <slev@altlinux.org> 7.2.4-alt1%ubt
- Update to upstream's 7.2.4 version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.4-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.3-alt1_2jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.3-alt1_1jpp8
- new version

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 7.1.0-alt1_2
- new version

