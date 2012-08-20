BuildRequires: rpm-build-java
Name: mojo-maven2-plugin-exec
Version: 17
Summary: Exec plugin from mojo-maven2-plugins
License: ASL, MIT, GPL, LGPL
Url: http://mojo.codehaus.org
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: mojo-maven2-plugins
Requires: maven2
Requires: plexus-container-default
Requires: plexus-utils

BuildArch: noarch
Group: Development/Java
Release: alt21_0jpp
Source: mojo-maven2-plugin-exec-17-alt20_8jpp6.cpio

%description
Exec plugin from mojo-maven2-plugins.

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

ver=1.1-beta-2
nam=exec-maven-plugin
%add_to_maven_depmap org.codehaus.mojo ${nam} ${ver} JPP/mojo ${nam}

%files -f %name-list
%_mavendepmapfragdir/*

%changelog
* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:17-alt21_0jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

