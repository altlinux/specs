Name: maven-shared-resources
Version: 1
Summary: A collection of templates that are specific to the Maven project
License: ASL 2.0
Url: http://maven.apache.org/shared/maven-shared-resources/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.apache.maven.shared:maven-shared-resources)
Requires: java
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-shared-resources-1-1.fc19.cpio

%description
This is a collection of templates that are specific to the Maven project.
They are probably not of interest to projects other than Apache Maven.

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
* Sun Aug 24 2014 Igor Vlasenko <viy@altlinux.ru> 1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

