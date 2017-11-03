Name: xmvn-connector-ivy
Version: 3.0.0
Summary: XMvn Connector for Apache Ivy
License: ASL 2.0
Url: https://fedora-java.github.io/xmvn/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.fedoraproject.xmvn:xmvn-connector-ivy) = 3.0.0
Provides: mvn(org.fedoraproject.xmvn:xmvn-connector-ivy:pom:) = 3.0.0
Provides: xmvn-connector-ivy = 3.0.0-6.fc27
Requires: java-headless
Requires: javapackages-tools
Requires: mvn(org.fedoraproject.xmvn:xmvn-api)
Requires: mvn(org.slf4j:slf4j-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-connector-ivy-3.0.0-6.fc27.cpio

%description
This package provides XMvn Connector for Apache Ivy, which provides
integration of Apache Ivy with XMvn.  It provides an adapter which
allows XMvn resolver to be used as Ivy resolver.

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

