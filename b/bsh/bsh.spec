Name: bsh
Version: 1.3.0
Summary: Lightweight Scripting for Java
License: (SPL or LGPLv2+) and Public Domain
Url: http://www.beanshell.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: bsh = 0:1.3.0-33.fc23
Provides: mvn(bsh:bsh) = 1.3.0
Provides: mvn(bsh:bsh-bsf) = 1.3.0
Provides: mvn(bsh:bsh-bsf:pom:) = 1.3.0
Provides: mvn(bsh:bsh:pom:) = 1.3.0
Provides: mvn(org.beanshell:bsh) = 1.3.0
Provides: mvn(org.beanshell:bsh:pom:) = 1.3.0
Requires: bsf
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt5jpp
Source: bsh-1.3.0-33.fc23.cpio

%description
BeanShell is a small, free, embeddable, Java source interpreter with
object scripting language features, written in Java.  BeanShell
executes standard Java statements and expressions, in addition to
obvious scripting commands and syntax.  BeanShell supports scripted
objects as simple method closures like those in Perl and
JavaScript(tm).  You can use BeanShell interactively for Java
experimentation and debugging or as a simple scripting engine for your
applications.  In short: BeanShell is a dynamically interpreted Java,
plus some useful stuff.  Another way to describe it is to say that in
many ways BeanShell is to Java as Tcl/Tk is to C: BeanShell is
embeddable - You can call BeanShell from your Java applications to
execute Java code dynamically at run-time or to provide scripting
extensibility for your applications.  Alternatively, you can call your
Java applications and objects from BeanShell; working with Java
objects and APIs dynamically.  Since BeanShell is written in Java and
runs in the same space as your application, you can freely pass
references to "real live" objects into scripts and return them as
results.

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
* Mon Jan 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt5jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt4_24jpp7
- new release

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt4_20jpp7
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt3_20jpp7
- fc update

* Thu Jan 27 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt3_15jpp6
- new jpp release

* Tue Mar 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt3_13jpp5
- fixed bug in component-info.xml in repolib

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt2_13jpp5
- new jpackage release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt2_11jpp5
- converted from JPackage by jppimport script

* Tue Oct 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_11jpp1.7
- updated to new jpackage release

* Tue May 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.0-alt1_10jpp1.7
- converted from JPackage by jppimport script

