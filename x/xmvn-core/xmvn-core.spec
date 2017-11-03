Name: xmvn-core
Version: 3.0.0
Summary: XMvn Core
License: ASL 2.0
Url: https://fedora-java.github.io/xmvn/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.fedoraproject.xmvn:xmvn-core) = 3.0.0
Provides: mvn(org.fedoraproject.xmvn:xmvn-core:pom:) = 3.0.0
Provides: xmvn-core = 3.0.0-6.fc27
Requires: java-headless
Requires: javapackages-tools

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-core-3.0.0-6.fc27.cpio

%description
This package provides XMvn Core module, which implements the essential
functionality of XMvn such as resolution of artifacts from system
repository.

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
* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

