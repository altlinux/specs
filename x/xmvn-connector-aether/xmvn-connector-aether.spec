%filter_from_requires /^java-headless/d
Name: xmvn-connector-aether
Version: 2.5.0
Summary: XMvn Connector for Eclipse Aether
License: ASL 2.0
Url: http://mizdebsk.fedorapeople.org/xmvn
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.fedoraproject.xmvn:xmvn-connector-aether) = 2.5.0
Provides: mvn(org.fedoraproject.xmvn:xmvn-connector-aether:pom:) = 2.5.0
Provides: xmvn-connector-aether = 2.5.0-6.fc24
Requires: jpackage-utils
Requires: mvn(com.google.inject:guice::no_aop:)
Requires: mvn(javax.inject:javax.inject)
Requires: mvn(org.apache.maven:maven-artifact)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model)
Requires: mvn(org.apache.maven:maven-model-builder)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.eclipse.aether:aether-api)
Requires: mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
Requires: mvn(org.fedoraproject.xmvn:xmvn-core)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-connector-aether-2.5.0-6.fc24.cpio

%description
This package provides XMvn Connector for Eclipse Aether, which
provides integration of Eclipse Aether with XMvn.  It provides an
adapter which allows XMvn resolver to be used as Aether workspace
reader.

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

