Name: jruby
Version: 1.7.20
Summary: Pure Java implementation of the Ruby interpreter
License: (CPL or GPLv2+ or LGPLv2+) and BSD and (GPLv2 or Ruby) and (BSD or Ruby)
Url: http://jruby.org
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jruby = 1.7.20-2.fc23
Provides: mvn(org.jruby:jruby) = 1.7.20
Provides: mvn(org.jruby:jruby-core) = 1.7.20
Provides: mvn(org.jruby:jruby-core:pom:) = 1.7.20
Provides: mvn(org.jruby:jruby-ext:pom:) = 1.7.20
Provides: mvn(org.jruby:jruby-lib:pom:) = 1.7.20
Provides: mvn(org.jruby:jruby-parent:pom:) = 1.7.20
Provides: mvn(org.jruby:jruby:pom:) = 1.7.20
Provides: mvn(org.jruby:readline) = 1.0
Provides: mvn(org.jruby:readline:pom:) = 1.0
Provides: mvn(org.jruby:ripper) = 1.7.20
Provides: mvn(org.jruby:ripper:pom:) = 1.7.20
Requires: /usr/bin/env
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.github.jnr:jffi)
Requires: mvn(com.github.jnr:jffi::native:)
Requires: mvn(com.github.jnr:jnr-constants)
Requires: mvn(com.github.jnr:jnr-enxio)
Requires: mvn(com.github.jnr:jnr-ffi)
Requires: mvn(com.github.jnr:jnr-netdb)
Requires: mvn(com.github.jnr:jnr-posix)
Requires: mvn(com.github.jnr:jnr-unixsocket)
Requires: mvn(com.github.jnr:jnr-x86asm)
Requires: mvn(com.headius:invokebinder)
Requires: mvn(com.headius:options)
Requires: mvn(com.jcraft:jzlib)
Requires: mvn(com.martiansoftware:nailgun-server)
Requires: mvn(jline:jline)
Requires: mvn(joda-time:joda-time)
Requires: mvn(org.apache.felix:org.apache.felix.framework)
Requires: mvn(org.jruby.extras:bytelist)
Requires: mvn(org.jruby.jcodings:jcodings)
Requires: mvn(org.jruby.joni:joni)
Requires: mvn(org.jruby:yecht)
Requires: mvn(org.ow2.asm:asm)
Requires: mvn(org.ow2.asm:asm-analysis)
Requires: mvn(org.ow2.asm:asm-commons)
Requires: mvn(org.ow2.asm:asm-util)
Requires: mvn(org.yaml:snakeyaml)

#BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jruby-1.7.20-2.fc23.cpio

%description
JRuby is a 100% Java implementation of the Ruby programming language.
It is Ruby for the JVM. JRuby provides a complete set of core "builtin"
classes and syntax for the Ruby language, as well as most of the Ruby
Standard Libraries.

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

%ifarch %ix86
rm -rf %buildroot/usr/share/jruby/lib/jni/arm*
rm -rf %buildroot/usr/share/jruby/lib/jni/x86_64*
sed -i /usr.share.jruby.lib.jni.arm/d %name-list
sed -i /usr.share.jruby.lib.jni.x86_64/d %name-list
%else
rm -rf %buildroot/usr/share/jruby/lib/jni/arm*
rm -rf %buildroot/usr/share/jruby/lib/jni/i?86*
sed -i /usr.share.jruby.lib.jni.arm/d %name-list
sed -i /usr.share.jruby.lib.jni.i.86/d %name-list
%endif

%files -f %name-list

%changelog
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7.20-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7.2-alt1_5jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6.3-alt3_3jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.3-alt2_3jpp7
- applied repocop patches

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.3-alt1_3jpp7
- fc build

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt3_3jpp5
- fixes for java6 support

* Wed Feb 11 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_3jpp5
- new version

* Wed Feb 11 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_3jpp5
- new version

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_0jpp5
- fixed build w/java5

* Sun Nov 25 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_0jpp1.7
- new version based on JPackage spec

