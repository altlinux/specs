Name: svnkit-javahl
Version: 1.8.5
Summary: Replacement for the native JavaHL API
License: TMate
Url: http://www.svnkit.com/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: svnkit-javahl = 1.8.5-3.fc23
Requires: subversion-javahl
Requires: svnkit

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: svnkit-javahl-1.8.5-3.fc23.cpio

%description
SVNKit provides a replacement for the native JavaHL API - the SVNClient  class
that does not use any native bindings. This SVNClient  also implements
SVNClientInterface (org.tigris.subversion.javahl) as the native one
but uses only the SVNKit library API (written in pure Java!).
If you have code written with using the native SVNClient class,
you may simply replace that class with the new one provided by SVNKit.

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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt2_7jpp7
- new release

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt2_6jpp7
- target 5 build

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.7.6-alt1_6jpp7
- replaced by fc package

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1jpp6
- new version

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1_2jpp5.0
- converted from JPackage by jppimport script

