%filter_from_requires /.usr.lib.*jffi/d

Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: gcc-c++ rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jruby
%global jruby_vendordir %{_datadir}/%{name}/lib
%global jruby_sitedir %{_prefix}/local/share/%{name}/lib
%global rubygems_dir %{_datadir}/rubygems

Name:           jruby
Version:        1.7.22
Release:        alt1_5jpp8
Summary:        Pure Java implementation of the Ruby interpreter
# (CPL or GPLv2+ or LGPLv2+) - JRuby itself
# BSD - some files under lib/ruby/shared
# (GPLv2 or Ruby) - Ruby 1.8 stdlib
# (BSD or Ruby) - Ruby 1.9 stdlib
License:        (CPL or GPLv2+ or LGPLv2+) and BSD and (GPLv2 or Ruby) and (BSD or Ruby)
URL:            http://jruby.org
Source0:        http://jruby.org.s3.amazonaws.com/downloads/%{version}/%{name}-src-%{version}.tar.gz

# Adds all the required jars to boot classpath
Patch0:         jruby-add-classpath-to-start-script.patch
# Adds $FEDORA_JAVA_OPTS, that is dynamically replaced by Fedora specific paths from the specfile
# This way we can use macros for the actual locations and not hardcode them in the patch
Patch1:         jruby-executable-add-fedora-java-opts-stub.patch
# upstream jline JAR bundles jansi, we need to include it explicitly in Fedora
Patch2:         jruby-include-unbundled-jansi.patch
# We don't want any directories defined by JRuby, everything is taken from Fedora's rubygems
Patch3:         jruby-remove-rubygems-dirs-definition.patch
# Port to latest snakeyaml
# TODO: rebase for JRuby 9000 master and send upstream
Patch4:         jruby-snakeyaml-1.16.patch

# BRs generated automatically using xmvn-builddep, sanitized manually
BuildRequires:  maven-local
BuildRequires:  mvn(bsf:bsf)
BuildRequires:  mvn(com.github.jnr:jffi)
BuildRequires:  mvn(com.github.jnr:jffi::native:)
BuildRequires:  mvn(com.github.jnr:jnr-constants)
BuildRequires:  mvn(com.github.jnr:jnr-enxio)
BuildRequires:  mvn(com.github.jnr:jnr-ffi)
BuildRequires:  mvn(com.github.jnr:jnr-netdb)
BuildRequires:  mvn(com.github.jnr:jnr-posix)
BuildRequires:  mvn(com.github.jnr:jnr-unixsocket)
BuildRequires:  mvn(com.github.jnr:jnr-x86asm)
BuildRequires:  mvn(com.headius:coro-mock)
BuildRequires:  mvn(com.headius:invokebinder)
BuildRequires:  mvn(com.headius:options)
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(com.martiansoftware:nailgun-server)
BuildRequires:  mvn(jline:jline)
BuildRequires:  mvn(joda-time:joda-time)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.framework)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:buildnumber-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:properties-maven-plugin)
BuildRequires:  mvn(org.jruby.extras:bytelist)
BuildRequires:  mvn(org.jruby.jcodings:jcodings)
BuildRequires:  mvn(org.jruby.joni:joni)
BuildRequires:  mvn(org.jruby:yecht)
BuildRequires:  mvn(org.osgi:org.osgi.core)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.ow2.asm:asm-analysis)
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.ow2.asm:asm-util)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.yaml:snakeyaml)
BuildRequires:  git
# unavailable now, see: https://bugzilla.redhat.com/show_bug.cgi?id=1152246
#BuildRequires: joda-timezones

Provides:       ruby(release) = 1.9.3
Provides:       ruby(release) = 1.8.7
# For rubypick
Provides:       ruby(runtime_executable)

BuildArch:      noarch
# yecht is in a separate package now
Obsoletes:      %{name}-yecht < %{version}-%{release}
Source44: import.info

%description
JRuby is a 100% Java implementation of the Ruby programming language.
It is Ruby for the JVM. JRuby provides a complete set of core "builtin"
classes and syntax for the Ruby language, as well as most of the Ruby
Standard Libraries.

%package        devel
Group: Development/Java
Summary:        JRuby development environment
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description    devel
Macros for building JRuby-specific libraries.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# delete windows specific files
find -name "*.exe" -delete
find -name "*.dll" -delete

# delete all vcs files
find -name ".gitignore" -delete
find -name ".cvsignore" -delete

# remove hidden .document files
find lib/ruby/ -name "*.document" -delete

# lib/ruby scripts shouldn't contain shebangs as they are not executable on their own
find lib/ruby/ -name "*.rb" -exec sed --in-place "s|^#!/usr/local/bin/ruby||" '{}' \;
find lib/ruby/ -name "*.rb" -exec sed --in-place "s|^#!/usr/bin/env ruby||" '{}' \;

# FIXME: remove when joda-timezones pkg is available in Fedora
%pom_remove_dep org.jruby:joda-timezones core

# work around "error: package org.osgi.framework.wiring does not exist"
%pom_add_dep org.apache.felix:org.apache.felix.framework core

# JDK8 should provide these
%pom_remove_dep com.headius:unsafe-mock core
%pom_remove_dep com.headius:jsr292-mock core

# do not bundle jffi-native
%pom_remove_plugin :maven-dependency-plugin core

# we don't have this plugin in fedora
%pom_remove_plugin :tesla-polyglot-maven-plugin lib

# a lot of missing "gem" artifacts, skip them for now
%pom_xpath_remove 'pom:dependencies' lib

# do not bundle other JARs inside jruby.jar
%pom_remove_plugin :maven-shade-plugin core

# generate Requires on jline dependency
%pom_xpath_replace 'pom:dependency[pom:artifactId[text()="jline"]]/pom:scope' '<scope>compile</scope>' ext/readline

# install JARs to %%{_javadir}/%%{name} and symlink them to %%{jruby_vendordir}
%mvn_file :{jruby-core}:jar:: %{name}/@1 %{jruby_vendordir}/%{name}
%mvn_file :{ripper}:jar:: %{name}/@1 %{jruby_vendordir}/ruby/shared/@1
%mvn_file :{readline}:jar:: %{name}/@1 %{jruby_vendordir}/ruby/shared/readline/@1

# TODO: build proper org.jruby:jruby artifact
%mvn_alias org.jruby:jruby-core org.jruby:jruby

%build
%mvn_build

%install
%mvn_install

install -d -m 755 %{buildroot}%{_datadir}
install -p -d -m 755 %{buildroot}%{_datadir}/%{name}/bin

# stdlib
cp -ar lib/* %{buildroot}%{jruby_vendordir}/

# symlink jffi .so files (this is pretty ugly :/)
install -d -m 755 %{buildroot}%{jruby_vendordir}/jni/{arm-Linux,i386-Linux,x86_64-Linux}
ln -s %{_prefix}/lib/jffi/arm-Linux/libjffi.so %{buildroot}%{jruby_vendordir}/jni/arm-Linux/
ln -s %{_prefix}/lib/jffi/i386-Linux/libjffi.so %{buildroot}%{jruby_vendordir}/jni/i386-Linux/
ln -s %{_prefix}/lib64/jffi/x86_64-Linux/libjffi.so %{buildroot}%{jruby_vendordir}/jni/x86_64-Linux/

# jline in Fedora doesn't bundle jansi, we need to symlink it manually
ln -s `build-classpath jansi/jansi` %{buildroot}%{jruby_vendordir}/ruby/shared/readline/
xmvn-subst %{buildroot}%{jruby_vendordir}/ruby/shared/readline/

# remove what shouldn't be in lib/ dir
rm %{buildroot}%{jruby_vendordir}/pom*

# startup scripts
cp -a bin/{{j,}gem,{j,}irb,jruby} %{buildroot}%{_datadir}/%{name}/bin/

# /usr prefix startup scripts
install -d -m 755 %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/bin/jgem  %{buildroot}%{_bindir}/gem-jruby
ln -s %{_datadir}/%{name}/bin/jirb  %{buildroot}%{_bindir}/irb-jruby
ln -s %{_datadir}/%{name}/bin/jruby %{buildroot}%{_bindir}/jruby

# Fedora integration stuff
# modify the JRuby executable to contain Fedora specific paths redefinitons
# we need to modify jruby{,sh,bash} to be sure everything is ok
sed -i 's|$FEDORA_JAVA_OPTS|-Dvendor.dir.general=%{jruby_vendordir}\
                            -Dsite.dir.general=%{jruby_sitedir}\
                            -Dvendor.dir.rubygems=%{rubygems_dir}|' \
    %{buildroot}%{_datadir}/%{name}/bin/jruby*

# install JRuby specific bits into system RubyGems
mkdir -p %{buildroot}%{rubygems_dir}/rubygems/defaults
cp -a lib/ruby/shared/rubygems/defaults/jruby.rb %{buildroot}%{rubygems_dir}/rubygems/defaults/

# Dump the macros into macros.jruby to use them to build other JRuby libraries.
mkdir -p %{buildroot}%{_rpmmacrosdir}
cat >> %{buildroot}%{_rpmmacrosdir}/macros-jruby << \EOF
%%jruby_libdir %%{_datadir}/%{name}/lib/ruby/2.0

# This is the general location for libs/archs compatible with all
# or most of the Ruby versions available in the Fedora repositories.
%%jruby_vendordir vendor_ruby
%%jruby_vendorlibdir %%{jruby_libdir}/%%{jruby_vendordir}
%%jruby_vendorarchdir %%{jruby_vendorlibdir}
EOF

%files  -f .mfiles
%doc COPYING LICENSE.RUBY LEGAL
%{_bindir}/%{name}
%{_bindir}/gem-jruby
%{_bindir}/irb-jruby
%{_datadir}/%{name}
# own the JRuby specific files under RubyGems dir
%{rubygems_dir}/rubygems/defaults/jruby.rb
# exclude bundled gems
#%exclude %{jruby_vendordir}/ruby/1.9/rdoc*
#%exclude %{jruby_vendordir}/ruby/1.9/rake*
#%exclude %{jruby_vendordir}/ruby/gems
# exclude all of the rubygems stuff
#%exclude %{jruby_vendordir}/ruby/shared/*ubygems*
#%exclude %{jruby_vendordir}/ruby/shared/rbconfig

%files devel
%{_rpmmacrosdir}/macros-jruby

%files javadoc -f .mfiles-javadoc
%doc COPYING LICENSE.RUBY LEGAL

%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.7.22-alt1_5jpp8
- fixed build

* Thu Dec 15 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7.22-alt1_2jpp8
- new version

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

