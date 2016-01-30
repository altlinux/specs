Name: multiverse
Version: 0.7.0
Summary: A software transactional memory implementation for the JVM
License: ASL 2.0
Url: http://multiverse.codehaus.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: multiverse = 0.7.0-4.fc23
Provides: mvn(org.multiverse:multiverse-core) = 0.7.0
Provides: mvn(org.multiverse:multiverse-core:pom:) = 0.7.0
Provides: mvn(org.multiverse:multiverse:pom:) = 0.7.0
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: multiverse-0.7.0-4.fc23.cpio

%description
A software transactional memory implementation for the JVM. Access (read and
writes) to shared memory is done through transactional references, that can be
compared to the AtomicReferences of Java. Access to these references will be
done under A (atomicity), C (consistency), I (isolation) semantics.

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
* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

