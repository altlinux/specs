%filter_from_requires /^java-headless/d
Name: xmvn-bisect
Version: 2.5.0
Summary: XMvn Bisect
License: ASL 2.0
Url: http://mizdebsk.fedorapeople.org/xmvn
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.fedoraproject.xmvn:xmvn-bisect) = 2.5.0
Provides: mvn(org.fedoraproject.xmvn:xmvn-bisect:pom:) = 2.5.0
Provides: xmvn-bisect = 2.5.0-6.fc24
Requires: /bin/sh
Requires: jpackage-utils
Requires: mvn(com.beust:jcommander)
Requires: mvn(com.google.inject:guice::no_aop:)
Requires: mvn(javax.inject:javax.inject)
Requires: mvn(org.apache.maven.shared:maven-invoker)
Requires: mvn(org.codehaus.plexus:plexus-utils)
Requires: mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
Requires: mvn(org.fedoraproject.xmvn:xmvn-core)
Requires: mvn(org.slf4j:slf4j-simple)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-bisect-2.5.0-6.fc24.cpio

%description
This package provides XMvn Bisect, which is a debugging tool that can
diagnose build failures by using bisection method.

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

