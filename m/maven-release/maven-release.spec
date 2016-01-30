Name: maven-release
Version: 2.2.1
Summary: Release a project updating the POM and tagging in the SCM
License: ASL 2.0
Url: http://maven.apache.org/plugins/maven-release-plugin/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-release = 2.2.1-13.fc21
Provides: mvn(org.apache.maven.release:maven-release:pom:) = 2.2.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.plugins:maven-compiler-plugin)
Requires: mvn(org.apache.maven:maven-parent:pom:)

BuildArch: noarch
Group: Development/Java
Release: alt5jpp
Source: maven-release-2.2.1-13.fc21.cpio

%description
This plugin is used to release a project with Maven, saving a lot of
repetitive, manual work. Releasing a project is made in two steps:
prepare and perform.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt4_9jpp7
- new release

* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt4_7jpp7
- added BR: for xmvn

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt3_7jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt3_4jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt2_4jpp7
- new fc release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt2_2jpp7
- applied repocop patches

* Wed Apr 04 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt1_2jpp7
- complete build

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.2.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

