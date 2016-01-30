Name: apache-parent
Version: 17
Summary: Parent POM file for Apache projects
License: ASL 2.0
Url: http://apache.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-parent = 17-2.fc23
Provides: mvn(org.apache:apache:pom:) = 17
Provides: mvn(org.apache:apache) = 17
Requires: apache-resource-bundles
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: apache-parent-17-2.fc23.cpio

%description
This package contains the parent pom file for apache projects.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 17-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_13jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_10jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_7jpp7
- rebuild with new apache-resource-bundles

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 10-alt1_7jpp7
- fc update

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 10-alt1_5jpp7
- new release

