Name: codehaus-parent
Version: 4
Summary: Parent pom file for codehaus projects
License: ASL 2.0
Url: http://codehaus.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: codehaus-parent = 4-9.fc23
Provides: mvn(org.codehaus:codehaus-parent:pom:) = 4
Provides: mvn(org.codehaus:codehaus-parent) = 4
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt3jpp
Source: codehaus-parent-4-9.fc23.cpio

%description
This package contains the parent pom file for codehaus projects.

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
* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 0:4-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:4-alt2_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:4-alt2_4jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:4-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:4-alt1_3jpp7
- shared FastInfoset.jar symlink as alternative

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:3-alt1_4jpp7
- fc version

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:3-alt1_1jpp6
- fixed build

