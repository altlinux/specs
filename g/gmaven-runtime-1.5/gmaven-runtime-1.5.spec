Name: gmaven-runtime-1.5
Version: 1.3
Summary: Groovy 1.5 Runtime for gmaven
License: ASL 2.0
Url: http://groovy.codehaus.org/GMaven
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: gmaven-provider
Requires: gmaven
Requires: groovy15

BuildArch: noarch
Group: Development/Java
Release: alt4jpp
Source: gmaven-runtime-1.5-1.3-alt1_3jpp6.cpio

%description
Groovy 1.5 Runtime for gmaven.

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
* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt4jpp
- bootstrap jar pack to restore broken gmaven jars

