Name: objectweb-pom
Version: 1.5
Summary: Objectweb POM
License: ASL 2.0
Url: http://gitorious.ow2.org/ow2/pom/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.ow2:ow2:pom:) = 1.5
Provides: objectweb-pom = 1.5-3.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: objectweb-pom-1.5-3.fc23.cpio

%description
This package provides Objectweb parent POM used by different
Objectweb packages.

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
* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

