Name: objectweb-asm-javadoc
Version: 5.0.3
Summary: API documentation for objectweb-asm
License: BSD
Url: http://asm.ow2.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: objectweb-asm-javadoc = 5.0.3-2.fc23
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: objectweb-asm-javadoc-5.0.3-2.fc23.cpio

%description
This package provides API documentation for objectweb-asm.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:5.0.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

