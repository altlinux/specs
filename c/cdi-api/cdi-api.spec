Name: cdi-api
Version: 1.1
Summary: CDI API
License: ASL 2.0
Url: http://seamframework.org/Weld
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: cdi-api = 1.1-11.fc23
Provides: javax.enterprise.inject
Provides: mvn(javax.enterprise:cdi-api) = 1.1
Provides: mvn(javax.enterprise:cdi-api:pom:) = 1.1
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(javax.annotation:jsr250-api)
Requires: mvn(javax.el:javax.el-api)
Requires: mvn(javax.inject:javax.inject)
Requires: mvn(org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: cdi-api-1.1-11.fc23.cpio

%description
APIs for JSR-299: Contexts and Dependency Injection for Java EE

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list
sed -i -e '/\[/d' %name-list
#sed -i -e 's,\[,\\[,g;s,\],\\],g;' %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list


%changelog
* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_9.SP4jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_6.SP4jpp7
- fc update

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_4.SP4jpp7
- new version

