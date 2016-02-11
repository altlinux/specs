Name: tomcat-log4j
Version: 8.0.26
Summary: Log4j support for Apache Tomcat
License: ASL 2.0
Url: http://tomcat.apache.org/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: tomcat-log4j = 1:8.0.26-1.fc23
Requires: log4j

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: tomcat-log4j-8.0.26-1.fc23.cpio

%description
Log4j support for Apache Tomcat

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
* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 1:8.0.26-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

