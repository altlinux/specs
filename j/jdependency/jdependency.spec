Name: jdependency
Version: 0.9
Summary: This project provides an API to analyse class dependencies
License: ASL 2.0
Url: http://github.com/tcurdt/jdependency
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jdependency = 0.9-3.fc23
Provides: mvn(org.vafer:jdependency) = 0.9
Provides: mvn(org.vafer:jdependency:pom:) = 0.9
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-io:commons-io)
Requires: mvn(org.ow2.asm:asm)
Requires: mvn(org.ow2.asm:asm-analysis)
Requires: mvn(org.ow2.asm:asm-commons)
Requires: mvn(org.ow2.asm:asm-tree)
Requires: mvn(org.ow2.asm:asm-util)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jdependency-0.9-3.fc23.cpio

%description
jdependency is small library that helps you analyze class level
dependencies, clashes and missing classes.

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
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:0.9-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_6jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_4jpp7
- new fc release

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7-alt1_1jpp7
- fc version

* Sat Feb 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_5jpp6
- new version

