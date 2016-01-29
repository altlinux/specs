Name: felix-bundlerepository
Version: 1.6.6
Summary: Bundle repository service
License: ASL 2.0 and MIT
Url: http://felix.apache.org/site/apache-felix-osgi-bundle-repository.html
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: felix-bundlerepository = 1.6.6-18.fc23
Provides: mvn(org.apache.felix:org.apache.felix.bundlerepository) = 1.6.6
Provides: mvn(org.apache.felix:org.apache.felix.bundlerepository:pom:) = 1.6.6
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.apache.felix:org.apache.felix.utils)
Requires: mvn(org.osgi:org.osgi.core)

BuildArch: noarch
Group: Development/Java
Release: alt3jpp
Source: felix-bundlerepository-1.6.6-18.fc23.cpio

%description
Bundle repository service

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt2_15jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt2_9jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt2_7jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.6-alt1_7jpp7
- new release

