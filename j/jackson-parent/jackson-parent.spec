Name: jackson-parent
Version: 2.5
Summary: Parent pom for all Jackson components
License: ASL 2.0
Url: https://github.com/FasterXML/jackson-parent
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jackson-parent = 2.5-2.fc23
Provides: mvn(com.fasterxml.jackson:jackson-parent:pom:) = 2.5
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.fasterxml:oss-parent:pom:)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jackson-parent-2.5-2.fc23.cpio

%description
Project for parent pom for all Jackson components.

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
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

