BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
AutoReq: yes,noosgi
Name: tycho-extras
Version: 0.16.0
Summary: Additional plugins for Tycho
License: EPL
Url: http://eclipse.org/tycho/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: java
Requires: jgit
Requires: jpackage-utils
Requires: tycho

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: tycho-extras-0.16.0-1.e58861.fc18.cpio

%description
A small set of plugins that work with Tycho to provide additional functionality
when building projects of an OSGi nature.

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
* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

