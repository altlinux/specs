Name: jackson-dataformat-xml-javadoc
Version: 2.5.0
Summary: Javadoc for jackson-dataformat-xml
License: ASL 2.0
Url: http://wiki.fasterxml.com/JacksonExtensionXmlDataBinding
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jackson-dataformat-xml-javadoc = 2.5.0-2.fc23
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jackson-dataformat-xml-javadoc-2.5.0-2.fc23.cpio

%description
This package contains javadoc for jackson-dataformat-xml.

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
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

