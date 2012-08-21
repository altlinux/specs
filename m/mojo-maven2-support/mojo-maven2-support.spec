Name: mojo-maven2-support
Version: 17
Summary: Support lib from mojo-maven2-plugins
License: ASL, MIT, GPL, LGPL
Url: http://mojo.codehaus.org
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: mojo-maven2-plugins
Requires: maven2
Requires: ant
Requires: jakarta-commons-jexl
Requires: jakarta-commons-lang
Requires: jakarta-commons-logging

BuildArch: noarch
Group: Development/Java
Release: alt21jpp
Source: mojo-maven2-support-17-alt20_8jpp6.cpio

%description
Support lib from mojo-maven2-plugins.

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
* Tue Aug 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:17-alt21jpp
- bootstrap jar pack for mojo translation

