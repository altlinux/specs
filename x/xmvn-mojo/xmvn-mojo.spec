%filter_from_requires /^java-headless/d
Name: xmvn-mojo
Version: 2.5.0
Summary: XMvn MOJO
License: ASL 2.0
Url: http://mizdebsk.fedorapeople.org/xmvn
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.fedoraproject.xmvn:xmvn-mojo) = 2.5.0
Provides: mvn(org.fedoraproject.xmvn:xmvn-mojo:pom:) = 2.5.0
Provides: xmvn-mojo = 2.5.0-6.fc24
Requires: jpackage-utils
Requires: mvn(com.google.inject:guice::no_aop:)
Requires: mvn(javax.inject:javax.inject)
Requires: mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
Requires: mvn(org.apache.maven:maven-artifact)
Requires: mvn(org.apache.maven:maven-core)
Requires: mvn(org.apache.maven:maven-model)
Requires: mvn(org.apache.maven:maven-plugin-api)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
Requires: mvn(org.fedoraproject.xmvn:xmvn-core)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-mojo-2.5.0-6.fc24.cpio

%description
This package provides XMvn MOJO, which is a Maven plugin that consists
of several MOJOs.  Some goals of these MOJOs are intended to be
attached to default Maven lifecycle when building packages, others can
be called directly from Maven command line.

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

