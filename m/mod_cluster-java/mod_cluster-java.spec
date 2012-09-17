Name: mod_cluster-java
Version: 1.2.1
Summary: Java bindings for mod_cluster
License: LGPLv2
Url: http://jboss.org/mod_cluster
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: jboss-logging
Requires: jboss-servlet-3.0-api
Requires: jcip-annotations
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: mod_cluster-java-1.2.1-3.fc18.cpio

%description
This package contains Java part of mod_cluster.

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
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

