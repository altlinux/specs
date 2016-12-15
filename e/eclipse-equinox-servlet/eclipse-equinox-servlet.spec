Name: eclipse-equinox-servlet
Version: 4.6.0
Summary: Eclipse OSGi - Equinox
License: EPL
Url: http://www.eclipse.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: eclipse-platform = 1:4.6.0-1
Provides: mvn(org.eclipse.equinox.http:servlet) = 1.3.0.v20160511.1000
Provides: mvn(org.eclipse.equinox.http:servlet:pom:) = 1.3.0.v20160511.1000

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: eclipse-equinox-servlet-4.6.0-1.tar

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
* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 4.6.0-alt0.1jpp
- bootstrap pack of jars

* Wed Feb 24 2016 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt0.3jpp
- added org.eclipse.core.resources (for maven-eclipse-plugin)

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt0.2jpp
- added mvn provides

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 4.5.1-alt0.1jpp
- bootstrap pack of jars
- temporary package to satisfy circular dependencies

