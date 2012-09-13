Name: jboss-interceptor
Version: 2.0.0
Summary: JBoss EJB Interceptor Library
License: ASL 2.0 and LGPLv2.1+
Url: http://www.jboss.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: guava
Requires: java
Requires: javassist
Requires: jboss-interceptors-1.1-api
Requires: jpackage-utils
Requires: slf4j

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jboss-interceptor-2.0.0-4.fc18.cpio

%description
JBoss EJB 3.1 Common Interceptor Library

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
* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

