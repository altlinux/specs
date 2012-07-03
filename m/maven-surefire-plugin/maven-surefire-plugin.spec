Name: maven-surefire-plugin
Version: 2.12
Summary: Surefire plugin for maven
License: ASL 2.0
Url: http://maven.apache.org/surefire/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: maven-surefire-maven-plugin
Provides: maven2-plugin-surefire
Requires: maven-surefire
Requires: maven-surefire-provider-junit

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-surefire-plugin-2.12-2.fc18.cpio

%description
Maven surefire plugin for running tests via the surefire framework.

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
* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.12-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

