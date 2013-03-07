Name: maven-plugins-pom
Version: 23
Summary: Maven Plugins POM
License: ASL 2.0
Url: http://maven.apache.org/plugins/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-plugins-pom-23-6.fc19.cpio

%description
This package provides Maven Plugins parent POM used by different
Apache Maven plugins.

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
* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 23-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

