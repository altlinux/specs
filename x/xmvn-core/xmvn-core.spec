%filter_from_requires /^java-headless/d
Name: xmvn-core
Version: 2.5.0
Summary: XMvn Core
License: ASL 2.0
Url: http://mizdebsk.fedorapeople.org/xmvn
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.fedoraproject.xmvn:xmvn-core) = 2.5.0
Provides: mvn(org.fedoraproject.xmvn:xmvn-core:pom:) = 2.5.0
Provides: xmvn-core = 2.5.0-6.fc24
Requires: jpackage-utils
Requires: mvn(com.google.inject:guice::no_aop:)
Requires: mvn(javax.inject:javax.inject)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
Requires: mvn(org.fedoraproject.xmvn:xmvn-api)
Requires: mvn(org.slf4j:slf4j-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-core-2.5.0-6.fc24.cpio

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
* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

