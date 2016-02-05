Name: invokebinder
Version: 1.2
Summary: A Java DSL for binding method handles forward, rather than backward
License: ASL 2.0
Url: http://github.com/headius/invokebinder/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: invokebinder = 1.2-1.fc22
Provides: mvn(com.headius:invokebinder) = 1.2
Provides: mvn(com.headius:invokebinder:pom:) = 1.2
Requires: java-headless
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: invokebinder-1.2-1.fc22.cpio

%description
This library hopes to provide a more friendly DSL for binding method handles.
Unlike the normal MethodHandle API, handles are bound forward from a source
MethodType and eventually adapted to a final target MethodHandle. Along the
way the transformations are pushed onto a stack and eventually applied in
reverse order, as the standard API demands.

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
* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Aug 29 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_8jpp7
- new release

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_4jpp7
- new release

