Name: apache-commons-logging-javadoc
Version: 1.2
Summary: API documentation for apache-commons-logging
License: ASL 2.0
Url: http://commons.apache.org/logging
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-commons-logging-javadoc = 1.2-4.fc23
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: apache-commons-logging-javadoc-1.2-4.fc23.cpio

%description
API documentation for apache-commons-logging.

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
* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

