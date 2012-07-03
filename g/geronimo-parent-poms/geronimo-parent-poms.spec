Name: geronimo-parent-poms
Version: 1.6
Summary: Parent POM files for geronimo-specs
License: ASL 2.0
Url: http://geronimo.apache.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: geronimo-specs
Requires: maven-compiler-plugin
Requires: maven-idea-plugin
Requires: maven-jar-plugin
Requires: maven-plugin-bundle
Requires: maven-pmd-plugin

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: geronimo-parent-poms-1.6-7.fc17.cpio

%description
The Project Object Model files for the geronimo-specs modules.

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
* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 1.6-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

