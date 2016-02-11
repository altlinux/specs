Name: eclipse-equinox-osgi
Version: 4.5.1
Summary: Eclipse OSGi - Equinox
License: EPL
Url: http://www.eclipse.org/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: eclipse-equinox-osgi = 1:4.5.1-1.fc23
Provides: mvn(org.eclipse.osgi:compatibility.state) = 1.0.100.v20151005.1500
Provides: mvn(org.eclipse.osgi:compatibility.state:pom:) = 1.0.100.v20151005.1500
Provides: mvn(org.eclipse.osgi:org.eclipse.osgi) = 3.10.101.v20151005.1500
Provides: mvn(org.eclipse.osgi:org.eclipse.osgi.compatibility.state) = 1.0.100.v20151005.1500
Provides: mvn(org.eclipse.osgi:org.eclipse.osgi.compatibility.state:pom:) = 1.0.100.v20151005.1500
Provides: mvn(org.eclipse.osgi:org.eclipse.osgi.services) = 3.5.0.v20151005.1500
Provides: mvn(org.eclipse.osgi:org.eclipse.osgi.services:pom:) = 3.5.0.v20151005.1500
Provides: mvn(org.eclipse.osgi:org.eclipse.osgi.util) = 3.3.100.v20151005.1500
Provides: mvn(org.eclipse.osgi:org.eclipse.osgi.util:pom:) = 3.3.100.v20151005.1500
Provides: mvn(org.eclipse.osgi:org.eclipse.osgi:pom:) = 3.10.101.v20151005.1500
Provides: mvn(org.eclipse.osgi:services) = 3.5.0.v20151005.1500
Provides: mvn(org.eclipse.osgi:services:pom:) = 3.5.0.v20151005.1500
Provides: mvn(org.eclipse.osgi:util) = 3.3.100.v20151005.1500
Provides: mvn(org.eclipse.osgi:util:pom:) = 3.3.100.v20151005.1500
Provides: mvn(org.eclipse.tycho:org.eclipse.osgi) = 3.10.101.v20151005.1500
Provides: mvn(org.eclipse.tycho:org.eclipse.osgi.compatibility.state) = 1.0.100.v20151005.1500
Provides: mvn(org.eclipse.tycho:org.eclipse.osgi.compatibility.state:pom:) = 1.0.100.v20151005.1500
Provides: mvn(org.eclipse.tycho:org.eclipse.osgi:pom:) = 3.10.101.v20151005.1500
Provides: mvn(org.eclipse:osgi) = 3.10.101.v20151005.1500
Provides: mvn(org.eclipse:osgi:pom:) = 3.10.101.v20151005.1500
Provides: osgi(org.eclipse.osgi) = 3.10.101
Provides: osgi(org.eclipse.osgi.compatibility.state) = 1.0.100
Provides: osgi(org.eclipse.osgi.services) = 3.5.0
Provides: osgi(org.eclipse.osgi.util) = 3.3.100
Provides: osgi(system.bundle) = 1:4.5.1



BuildArch: noarch
Group: Development/Java
Release: alt0.2jpp
Source: eclipse-equinox-osgi-4.5.1-1.tar

%description
Eclipse OSGi - Equinox

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
tar xf %{SOURCE0}

%build
tar tf %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.1-alt0.2jpp
- added osgi provides

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.5.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

