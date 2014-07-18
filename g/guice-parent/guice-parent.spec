Name: guice-parent
Version: 3.1.2
Summary: Guice parent POM
License: ASL 2.0
Url: https://github.com/sonatype/sisu-guice
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: guice-parent-3.1.2-6.fc18.cpio

%description
Guice is a lightweight dependency injection framework for Java 5
and above. This package provides parent POM for Guice modules.

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
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 3.1.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

