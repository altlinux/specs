BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
AutoReq: yes,noosgi
Name: icu4j-eclipse
Version: 4.4.2.2
Summary: Eclipse plugin for icu4j
License: MIT and EPL
Url: http://site.icu-project.org/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: icu4j-eclipse-4.4.2.2-12.fc18.cpio

%description
Eclipse plugin support for icu4j.

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
* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.4.2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

