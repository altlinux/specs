Name: maven-shared-utils
Version: 0.8
Summary: Maven shared utility classes
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-shared-utils
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-shared-utils = 0.8-1.fc23
Provides: mvn(org.apache.maven.shared:maven-shared-utils) = 0.8
Provides: mvn(org.apache.maven.shared:maven-shared-utils:pom:) = 0.8
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.google.code.findbugs:jsr305)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-shared-utils-0.8-1.fc23.cpio

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

