Name: xmvn-connector-gradle
Version: 3.0.0
Summary: XMvn Connector for Gradle
License: ASL 2.0
Url: https://fedora-java.github.io/xmvn/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.fedoraproject.xmvn:xmvn-connector-gradle) = 3.0.0
Provides: mvn(org.fedoraproject.xmvn:xmvn-connector-gradle:pom:) = 3.0.0
Provides: xmvn-connector-gradle = 3.0.0-6.fc27
Requires: java-headless
Requires: javapackages-tools
Requires: mvn(org.fedoraproject.xmvn:xmvn-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-connector-gradle-3.0.0-6.fc27.cpio

%description
This package provides XMvn Connector for Gradle, which provides
integration of Gradle with XMvn.  It provides an adapter which allows
XMvn resolver to be used as Gradle resolver.

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
* Fri Nov 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

