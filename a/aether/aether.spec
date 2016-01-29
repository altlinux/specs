Name: aether
Version: 1.0.2
Summary: Library to resolve, install and deploy artifacts the Maven way
License: EPL
Url: http://eclipse.org/aether
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: aether = 1:1.0.2-2.fc23
Provides: mvn(org.eclipse.aether:aether:pom:) = 1.0.2.v20150114
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.codehaus.mojo:build-helper-maven-plugin)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: aether-1.0.2-2.fc23.cpio

%description
Aether is a standalone library to resolve, install and deploy artifacts
the Maven way.

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
* Tue Jan 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Sun Aug 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt6_7jpp7
- xmvn build

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt6_4jpp7
- more compat symlinks added

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt5_4jpp7
- added compat symlink

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt4_4jpp7
- rebuild with maven-local

* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt3_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt1_4jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.13.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

