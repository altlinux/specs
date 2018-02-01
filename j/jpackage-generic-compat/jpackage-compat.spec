Name: jpackage-generic-compat
Version: 0.27
Release: alt1

Summary: ALT to JPackage build compatibility adaptor.
Group: Development/Java
License: GPL2+ or Apache
Url: http://www.sisyphus.ru/packages/viy/srpms

BuildPreReq: rpm-build-java /proc

Requires: docbook-style-xsl

# sun java requires it
Requires: /proc
Requires(pre): rpm-build-java
Requires: jpackage-utils
# as in jdepend; should be detected by peering in SOURCEDIR
Requires: unzip
# as in fedora biarch packages; could be detected by peering in SPEC
Requires: zip

Requires: java-devel java
Requires: java-javadoc

%description
JPackage compatibility package. The main goal is to provide all nessssary 
symlinks, Requires and BuildRequires for ALTLinux to create a build environment
compatible with JPackage.org.

%package -n jpackage-1.5.0-compat
Summary: JPackage build environment with java-1.5.0.
Group: Development/Java

Requires(pre): java-devel = 1.5.0 java = 1.5.0
# hack
Conflicts: java-devel > 1.5.99 java > 1.5.99 java-headless > 1.5.99

Requires: jpackage-generic-compat
Obsoletes: jpackage-1.5.0-core < %version-%release

%description -n jpackage-1.5.0-compat
JPackage compatibility package. the main goal is to provide all nessssary symlinks,
Requires and BuildRequires for ALT to be build compatible with JPackage.
Provides JPackage build environment with java-1.5.0.

%package -n jpackage-1.6.0-compat
Summary: JPackage build environment with java-1.6.0.
Group: Development/Java

Requires(pre): java-devel = 1.6.0 java = 1.6.0
# hack
Conflicts: java-devel > 1.6.99 java > 1.6.99 java-headless > 1.6.99

Requires: jpackage-generic-compat
Obsoletes: jpackage-1.6.0-core < %version-%release

%description -n jpackage-1.6.0-compat
JPackage compatibility package. the main goal is to provide all nessssary symlinks,
Requires and BuildRequires for ALT to be build compatible with JPackage.
Provides JPackage build environment with java-1.6.0.

%package -n jpackage-1.7.0-compat
Summary: JPackage build environment with java-1.7.0.
Group: Development/Java

Requires(pre): java-devel = 1.7.0 java = 1.7.0
# hack
Conflicts: java-devel > 1.7.99 java > 1.7.99 java-headless > 1.7.99

Requires: jpackage-generic-compat

%description -n jpackage-1.7.0-compat
JPackage compatibility package. the main goal is to provide all nessssary symlinks,
Requires and BuildRequires for ALT to be build compatible with JPackage.
Provides JPackage build environment with java-1.7.0.

%package -n jpackage-1.8-compat
Summary: JPackage build environment with java-1.8.0.
Group: Development/Java

Requires(pre): java-devel >= 1.8.0 java >= 1.8.0
# hack
Conflicts: java-devel > 1.8.99 java > 1.8.99 java-headless > 1.8.99

Requires: jpackage-generic-compat
Provides: jpackage-core = %version-%release
#Provides: jpackage-1.4-compat = %version-%release
#Provides: jpackage-1.5-compat = %version-%release
#Provides: jpackage-1.6-compat = %version-%release
#Provides: jpackage-1.7-compat = %version-%release
Provides: jpackage-compat = %version-%release
# arch dependent - fake provides
Provides: jpackage-for-%_target_cpu
%ifnarch %ix86 x86_64 
Provides: jpackage-1.5.0-compat = %version-%release
Provides: jpackage-1.6.0-compat = %version-%release
%endif
Obsoletes: jpackage-1.4-compat < %version
Obsoletes: jpackage-1.5-compat < %version
Obsoletes: jpackage-1.6-compat < %version
Obsoletes: jpackage-1.6-core < %version
Obsoletes: jpackage-1.7-compat < %version

%description -n jpackage-1.8-compat
JPackage compatibility package. the main goal is to provide all nessssary symlinks,
Requires and BuildRequires for ALT to be build compatible with JPackage.
Provides JPackage build environment with java-1.8.0.

%prep

%build

%install
install -d $RPM_BUILD_ROOT%_javadir

%files
%ifarch %ix86 x86_64
#files -n jpackage-1.5.0-compat
#files -n jpackage-1.6.0-compat
%endif

%files -n jpackage-1.7.0-compat
%files -n jpackage-1.8-compat

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- removed java 5/6 support

* Thu Jan 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- selected java8 as default

* Thu Jan 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- preparation for java-1.8.0
- TODO: set upper limits for java-1.8.0 when it will be released

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- efficient arch hack (using arch-dependent provides)

* Sun Mar 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- package is arch specific due to arm support

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- arm support (thanks to sbolshakov@)

* Thu Jan 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- moved compat symlink into docbook-style-xsl

* Thu Oct 04 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- dropped jpackage-*-core

* Sun Sep 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- dropped ant-antlr from greneric environment

* Wed Mar 14 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- selected java7 as default

* Mon Apr 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2
- fixed misprint thanks to manowar@

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- added jpackage-1.5.0-core/jpackage-1.6-core subpackages

* Tue Oct 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5.6
- restored java6 defaults

* Tue Oct 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5.5
- temporary selected java5 as default

* Sat Sep 18 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5.4
- restored java6 defaults

* Sat Sep 18 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5.3
- temporary selected java5 as default

* Thu Sep 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5.2
- restored java6 defaults

* Thu Sep 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5.1
- temporary selected java5 as default

* Fri Jul 30 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5
- selected java6 as default

* Sun May 30 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt4
- restored java5 defaults

* Fri May 21 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt3
- temporary selected java6 as default

* Tue May 18 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2
- restored java5 defaults

* Mon May 17 2010 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- removed obsolete jpackage-1.4.2-compat subpackage
- added jpackage-1.5.0-compat subpackage
- temporary switched default compiler to java6

* Mon May 10 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt6
- restored java5 defaults

* Sat May 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt5
- temporary switched default compiler to java6

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt4
- restored java5 defaults

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt3
- temporary switched default compiler to java6

* Mon Oct 05 2009 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2
- tambourine dance around /usr/share/xml/docbook/xsl-stylesheets 
  auto dependency // does not resolved in hasher :(

* Sun Oct 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- added requires: on rpm-build-java

* Mon Jun 15 2009 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- added /usr/share/sgml/docbook/xsl-stylesheets symlink
  TODO: move it to  docbook-style-xsl someday

* Wed Feb 25 2009 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- added ant-nodeps to generic environment

* Sun Aug 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.12-alt3
- Added Requires: /proc

* Fri Aug 01 2008 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2
- java-devel is now Required(pre).

* Thu Jul 24 2008 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added jpackage-1.4.2-compat
- added Provides: jpackage-compat (for default compiler choice)

* Wed Jun 25 2008 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- removed jpackage-1.4-compat (provides by jpackage-1.5-compat)

* Mon Apr 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- added gnu-crypto-sasl-jdk1.4 to jpackage-1.4-compat

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- consolidated jpackage-*-compat's into one spec
- added zip to environment
- added jpackage-1.6-compat 

* Tue Jul 03 2007 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- added 'generic' subpackage
- removed hack for ant-apache-bcf

* Tue Jul 03 2007 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- added hack for ant-apache-bcf
- removed hack for ant-apache-resolver

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added java-javadoc dependency

* Thu May 24 2007 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3
- added hack for ant-apache-resolver (and company)

* Wed May 23 2007 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- Requires: ant-trax

* Tue May 22 2007 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- Requires: ant-junit ant-antlr
- removed xerces-j/xni hack

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- removed ant hack (thanks to damir@ for fix)
- added xerces-j/xni hack (waiting for Eugene (eostapets@) to fix)

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added quick hack around ant compatibility

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- added explicit /proc

* Fri Apr 27 2007 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added requires: ant

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- removed fake xerces-j2 (moved to jpackage-1.5-compat)
- changed dependencies to get java-1.4

* Sat Apr 21 2007 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added conflict to java-devel 1.6

* Sat Mar 24 2007 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial build.
