Name: maven-shared-utils
Version: 3.1.0
Summary: Maven shared utility classes
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-shared-utils
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-shared-utils = 3.1.0-5.fc27
Provides: mvn(org.apache.maven.shared:maven-shared-utils) = 3.1.0
Provides: mvn(org.apache.maven.shared:maven-shared-utils:pom:) = 3.1.0
Requires: java-headless
Requires: javapackages-tools
Requires: mvn(commons-io:commons-io)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-shared-utils-3.1.0-5.fc27.cpio

%description
This project aims to be a functional replacement for plexus-utils in Maven.

It is not a 100% API compatible replacement though but a replacement with
improvements: lots of methods got cleaned up, generics got added and we dropped
a lot of unused code.

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
* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_3jpp8
- new version

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_2jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt0.2jpp
- rebuild to add provides

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

