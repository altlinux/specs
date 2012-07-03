Name: animal-sniffer
Version: 1.7
Summary: Tools to assist verifying backward compatibility of Java classes
License: MIT
Url: http://mojo.codehaus.org/animal-sniffer/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: /bin/bash
Requires: ant
Requires: java
Requires: maven
Requires: mojo-signatures
Requires: objectweb-asm

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: animal-sniffer-1.7-3.fc18.cpio

%description
Tools to assist verifying that classes compiled with a newer JDK/API
are compatible with an older JDK/API

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
* Sun Mar 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.7-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

