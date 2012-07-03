Name: maven-jxr
Version: 2.3
Summary: Source cross referencing tool
License: ASL 2.0
Url: http://maven.apache.org/doxia/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: apache-commons-collections
Requires: jakarta-oro
Requires: junit
Requires: plexus-utils
Requires: velocity

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: maven-jxr-2.3-2.fc17.cpio

%description
Maven JXR is a source cross referencing tool.

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
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

%changelog
* Tue Feb 28 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

