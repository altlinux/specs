Name: shrinkwrap-resolver
Version: 1.0.0
Summary: ShrinkWrap Resolver
License: ASL 2.0
Url: http://www.jboss.org/shrinkwrap
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: aether
Requires: java
Requires: jpackage-utils
Requires: maven
Requires: maven-model
Requires: maven-wagon
Requires: shrinkwrap

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: shrinkwrap-resolver-1.0.0-0.2.beta7.fc18.cpio

%description
This package contains the ShrinkWrap Resolver.

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
* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

