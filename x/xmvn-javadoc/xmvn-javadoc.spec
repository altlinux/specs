%filter_from_requires /^java-headless/d
Name: xmvn-javadoc
Version: 2.5.0
Summary: API documentation for xmvn
License: ASL 2.0
Url: http://mizdebsk.fedorapeople.org/xmvn
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: xmvn-javadoc = 2.5.0-6.fc24

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xmvn-javadoc-2.5.0-6.fc24.cpio

%description
This package provides API documentation for xmvn.

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
* Fri Dec 09 2016 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

