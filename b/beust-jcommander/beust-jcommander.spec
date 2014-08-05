Name: beust-jcommander
Version: 1.30
Summary: Java framework for parsing command line parameters
License: ASL 2.0
Url: http://jcommander.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: java
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: beust-jcommander-1.30-2.fc18.2.cpio

%description
JCommander is a very small Java framework that makes it trivial to
parse command line parameters (with annotations).

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
* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

%changelog
* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_5jpp7
- new fc release

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_4jpp7
- new version

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.17-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

