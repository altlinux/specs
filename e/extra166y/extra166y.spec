Name: extra166y
Version: 1.7.0
Summary: Concurrency JSR-166 - Collections supporting parallel operations
License: Public Domain
Url: http://gee.cs.oswego.edu/dl/concurrency-interest
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: extra166y = 1.7.0-4.fc23
Provides: mvn(org.codehaus.jsr166-mirror:extra166y) = 1.7.0
Provides: mvn(org.codehaus.jsr166-mirror:extra166y:pom:) = 1.7.0
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: extra166y-1.7.0-4.fc23.cpio

%description
Implementation of Java collections supporting parallel operations using
Fork-Join concurrent framework provided by JSR-166.

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
* Sat Jan 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

