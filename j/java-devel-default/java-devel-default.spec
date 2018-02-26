%define defjavaver 1.7.0
Packager: Igor Vlasenko <viy@altlinux.ru>
Name: java-devel-default
Version: 1.6.0
Release: alt2

Summary: chooser of default ALT Linux java compiler.
Group: Development/Java
License: GPL2+ or Apache
Url: http://www.sisyphus.ru/packages/viy/srpms

BuildArch: noarch
Requires(pre): rpm-build-java /proc
Requires(pre): java-devel = %defjavaver java = %defjavaver

Requires: java-javadoc
Requires: jpackage-utils

%description
A virtual package that provides default ALT Linux java compiler.
It is recommended that packages should Build Require
java-devel-default instead of relaying on specific compiler version.

%prep

%build

%install
install -d $RPM_BUILD_ROOT/usr

%files

%changelog
* Mon Apr 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt2
- temporary selected java7 as default

* Fri Jul 30 2010 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1
- selected java6 as default

* Sun May 30 2010 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt4
- restored java5 defaults

* Fri May 21 2010 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt3
- temporary selected java6 as default

* Thu Dec 18 2008 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2
- fixed by repocop

* Sun Aug 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1
- initial build.
