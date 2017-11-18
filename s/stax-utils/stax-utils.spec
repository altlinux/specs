BuildRequires: javapackages-local
Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global svnrev 238

Name:           stax-utils
Version:        0
Release:        alt2_0.11.20110309svn238jpp8
Summary:        StAX utility classes
License:        BSD
URL:            http://java.net/projects/stax-utils/
# svn export -r 238 https://svn.java.net/svn/stax-utils~svn/trunk/ stax-utils-svn238
# rm -rf stax-utils-svn238/lib
# tar caf stax-utils-svn238.tar.xz stax-utils-svn238
Source0:        %{name}-svn%{svnrev}.tar.xz
# This is the only pom I could find.  I'm updating the version after download.
Source1:        http://repo1.maven.org/maven2/net/java/dev/stax-utils/stax-utils/20060502/stax-utils-20060502.pom

# This patch fixes several things:
# 1. Use Java 1.7 as the build source and target
# 2. Remove dependency on jsr 173 code
# 3. Do not attempt to pull docs from the web
Patch0:         %{name}-build-fixes.patch
BuildArch:      noarch

BuildRequires: java-devel
BuildRequires: ant
BuildRequires: ant-junit
BuildRequires: jpackage-utils
Requires:      jpackage-utils
Source44: import.info

%description
This is a set of utility classes that make it easy for developers to
integrate StAX into their existing XML processing applications.

%package javadoc
Group: Development/Java
Summary:      API documentation for %{name}
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n stax-utils-svn%{svnrev}
%patch0 -p1

%build
ant jar
ant javadoc

%check
ant test

%install
install -d -m 755 %{buildroot}%{_javadir}
cp -p build/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

install -d -m 755 %{buildroot}%{_mavenpomdir}
cp -p %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
# Reflect latest commit date in version
sed -i -e 's/20060502/20110309/' %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

install -d -m 755 %{buildroot}%{_javadocdir}
cp -rp build/javadoc %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc docs/COPYRIGHT.TXT LICENSE

%files javadoc
%doc docs/COPYRIGHT.TXT LICENSE
%{_javadocdir}/%{name}

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 1:0-alt2_0.11.20110309svn238jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 1:0-alt1_0.11.20110309svn238jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:0-alt1_0.10.20110309svn238jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:0-alt1_0.9.20110309svn238jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:0-alt1_0.5.20110309svn238jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:0-alt1_0.4.20110309svn238jpp7
- new release

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 1:0-alt1_0.2.20110309svn238jpp7
- fc update

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt1_0.20070216.3jpp6
- new jpp relase

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt1_0.20070216.1jpp5
- new jpackage release

* Mon Dec 03 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt1_0.20060502.1jpp1.7
- new version

* Wed Oct 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.0-alt1_0.20050302.3jpp1.7
- converted from JPackage by jppimport script

