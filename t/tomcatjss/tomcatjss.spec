%define _unpackaged_files_terminate_build 1

# JSS built with Java11
%define jss_version 5.1.0
%define tomcat_version 9.0.37
%define java_version 11

Name: tomcatjss
Version: 8.1.0
Release: alt1

Summary: JSSE module for Apache Tomcat that uses JSS
License: LGPLv2+
Group: System/Libraries
# Source-git: https://github.com/dogtagpki/tomcatjss.git
Url: http://www.dogtagpki.org/wiki/TomcatJSS

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: /proc
BuildRequires: java-devel >= %java_version
BuildRequires: jpackage-generic-compat
BuildRequires: apache-commons-logging
BuildRequires: ant
BuildRequires: jss >= %jss_version
BuildRequires: tomcat >= %tomcat_version

BuildArch: noarch
Requires: jss >= %jss_version
Requires: tomcat >= %tomcat_version
Requires: apache-commons-logging
Requires: java >= %java_version

%description
JSS Connector for Apache Tomcat, installed via the tomcatjss package,
is a Java Secure Socket Extension (JSSE) module for Apache Tomcat that
uses Java Security Services (JSS), a Java interface to Network Security
Services (NSS).

%prep
%setup
%autopatch -p1

%build
# get Tomcat <major>.<minor> version number
tomcat_version=`/usr/sbin/tomcat version | sed -n 's/Server number: *\([0-9]\+\.[0-9]\+\).*/\1/p'`
app_server=tomcat-$tomcat_version

ant -v -f build.xml \
    -Dversion=%version \
    -Dsrc.dir=$app_server \
    -Djnidir=%_jnidir \
    compile package

%install
ant -v -f build.xml \
    -Dversion=%version \
    -Dinstall.doc.dir=%buildroot%_docdir \
    -Dinstall.jar.dir=%buildroot%_javadir \
    install

%files
%doc %_docdir/%name/
%_javadir/tomcatjss.jar

%changelog
* Thu Mar 03 2022 Stanislav Levin <slev@altlinux.org> 8.1.0-alt1
- 8.0.0 -> 8.1.0.

* Thu Nov 25 2021 Stanislav Levin <slev@altlinux.org> 8.0.0-alt1
- 7.6.1 -> 8.0.0.

* Fri May 21 2021 Stanislav Levin <slev@altlinux.org> 7.6.1-alt2
- Built with Java11.

* Fri Feb 05 2021 Stanislav Levin <slev@altlinux.org> 7.6.1-alt1
- 7.6.0 -> 7.6.1.

* Tue Nov 03 2020 Stanislav Levin <slev@altlinux.org> 7.6.0-alt1
- 7.5.0 -> 7.6.0.

* Mon Sep 14 2020 Stanislav Levin <slev@altlinux.org> 7.5.0-alt1
- 7.4.1 -> 7.5.0.

* Mon Aug 26 2019 Stanislav Levin <slev@altlinux.org> 7.4.1-alt1
- 7.4.0 -> 7.4.1.

* Tue May 21 2019 Stanislav Levin <slev@altlinux.org> 7.4.0-alt1
- 7.3.6 -> 7.4.0.

* Wed Oct 10 2018 Stanislav Levin <slev@altlinux.org> 7.3.6-alt1
- 7.3.5 -> 7.3.6.

* Wed Aug 29 2018 Stanislav Levin <slev@altlinux.org> 7.3.5-alt1
- 7.3.0 -> 7.3.5.

* Thu May 24 2018 Stanislav Levin <slev@altlinux.org> 7.3.0-alt1
- 7.2.4 -> 7.3.0

* Wed Nov 08 2017 Stanislav Levin <slev@altlinux.org> 7.2.4-alt2
- Remove tomcat-native from Conflicts due to tomcat dependency on
  tomcat-native

* Fri Sep 22 2017 Stanislav Levin <slev@altlinux.org> 7.2.4-alt1
- Update to upstream's 7.2.4 version

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.4-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.3-alt1_2jpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 7.1.3-alt1_1jpp8
- new version

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 7.1.0-alt1_2
- new version

