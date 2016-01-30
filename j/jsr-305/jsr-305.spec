Name: jsr-305
Version: 0
Summary: Correctness annotations for Java code
License: BSD and CC-BY
Url: http://jsr-305.googlecode.com/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jsr-305 = 0-0.18.20130910svn.fc23
Provides: mvn(com.google.code.findbugs:jsr305) = 0.1.SNAPSHOT
Provides: mvn(com.google.code.findbugs:jsr305:pom:) = 0.1.SNAPSHOT
Provides: mvn(org.jsr-305:jsr-305:pom:) = 0.1.SNAPSHOT
Provides: mvn(org.jsr-305:ri) = 0.1.SNAPSHOT
Provides: mvn(org.jsr-305:ri:pom:) = 0.1.SNAPSHOT
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt3jpp
Source: jsr-305-0-0.18.20130910svn.fc23.cpio

%description
This package contains reference implementations, test cases, and other
documents for Java Specification Request 305: Annotations for Software Defect
Detection.

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Sat Jan 23 2016 Igor Vlasenko <viy@altlinux.ru> 1:0-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:0-alt2_0.16.20130910svnjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:0-alt2_0.13.20090319svnjpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:0-alt2_0.10.20090319svnjpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:0-alt1_0.10.20090319svnjpp7
- new version

* Sat Mar 12 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_3jpp6
- jpp 6 release

* Fri May 22 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_2jpp5
- new jpp release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.1-alt1_1jpp5
- converted from JPackage by jppimport script

