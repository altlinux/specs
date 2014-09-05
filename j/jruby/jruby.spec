#filter_from_requires /rubypick/d
Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name jruby
%define version 1.7.2
%global jruby_vendordir %{_datadir}/%{name}/lib
%global jruby_sitedir %{_prefix}/local/share/%{name}/lib
%global rubygems_dir %{_datadir}/rubygems

%global yecht_commitversion 6009fd7
%global yecht_dlversion 0.0.2-0-g%{yecht_commitversion}
%global yecht_cluster olabini

#%%global preminorver dev
%global release 5
%global enable_check 0

%global jar_deps \\\
     objectweb-asm4/asm \\\
     objectweb-asm4/asm-analysis \\\
     objectweb-asm4/asm-commons \\\
     objectweb-asm4/asm-tree \\\
     objectweb-asm4/asm-util \\\
     bcprov \\\
     bcmail \\\
     bsf \\\
     bytelist \\\
     commons-logging \\\
     coro-mock \\\
     invokebinder \\\
     jansi \\\
     jarjar \\\
     jcodings \\\
     jffi \\\
     jline2 \\\
     jna \\\
     jnr-constants \\\
     jnr-enxio \\\
     jnr-ffi \\\
     jnr-netdb \\\
     jnr-posix \\\
     jnr-unixsocket \\\
     joda-time \\\
     joni \\\
     junit \\\
     junit4 \\\
     jzlib \\\
     nailgun \\\
     felix/org.osgi.core \\\
     snakeyaml \\\
     yecht \\\
     yydebug


Name:           jruby
Version:        1.7.2
Release:        alt1_5jpp7
Summary:        Pure Java implementation of the Ruby interpreter
Group:          Development/Java
# (CPL or GPLv2+ or LGPLv2+) - JRuby itself
# BSD - some files under lib/ruby/shared
# (GPLv2 or Ruby) - Ruby 1.8 stdlib
# (BSD or Ruby) - Ruby 1.9 stdlib
License:        (CPL or GPLv2+ or LGPLv2+) and BSD and (GPLv2 or Ruby) and (BSD or Ruby)
URL:            http://jruby.org/
BuildArch:      noarch
%if 0%{?preminorver:1}
Source0:        https://github.com/downloads/%{name}/%{name}/%{name}-src-%{version}.%{preminorver}.tar.gz
%else
Source0:        http://jruby.org.s3.amazonaws.com/downloads/%{version}/%{name}-src-%{version}.tar.gz
%endif
Source1:        http://github.com/%{yecht_cluster}/yecht/tarball/0.0.2/%{yecht_cluster}-yecht-%{yecht_dlversion}.tar.gz
### Patches for JRuby itself
# Adds $FEDORA_JAVA_OPTS, that is dynamically replaced by Fedora specific paths from the specfile
# This way we can use macros for the actual locations and not hardcode them in the patch
Patch0:         jruby-executable-add-fedora-java-opts-stub.patch
# Adds all the required jars to boot classpath
Patch1:         jruby-add-classpath-to-start-script.patch
# Following to patches make sure that we bundle no jars
Patch2:         jruby-dont-include-jar-dependencies-in-build-xml.patch
Patch3:         jruby-no-jar-bundling.patch
# this patch contained the following upstream change
# https://github.com/jruby/jruby/commit/6c1d41aedfde705c969abf10cf5384e2be69f10a
# -- now it changes the change to be ok downstream :)
Patch4:         jruby-remove-builtin-yecht-jar.patch
# We only want to build bindings, yecht is a package on its own
Patch5:         jruby-yecht-only-build-bindings.patch
# We don't want any directories defined by JRuby, everything is taken from Fedora's rubygems
Patch6:         jruby-remove-rubygems-dirs-definition.patch
# Fix Ant compatibility.
# https://github.com/jruby/jruby/issues/601
Patch7:         jruby-1.7.4-DSL-should-support-parameter-hash-with-symbol-keys.patch

### Patches for tests
# UDP multicast test hangs
# http://jira.codehaus.org/browse/JRUBY-6758
Patch100:         jruby-skip-network-tests.patch
# Fedora has different name for jarjar.jar => downstream only
Patch101:         jruby-remove-version-from-jarjar-jar-in-specs.patch
# https://github.com/jruby/jruby/pull/551/files
Patch102:         jruby-raise-written-chunk-in-spec-to-block.patch

BuildRequires:  ant >= 1.6
BuildRequires:  ant-junit
BuildRequires:  jpackage-utils >= 1.5

BuildRequires:  apache-commons-logging
BuildRequires:  bouncycastle
BuildRequires:  bouncycastle-mail
BuildRequires:  bsf
BuildRequires:  bytelist >= 1.0.8
BuildRequires:  coro-mock
BuildRequires:  felix-osgi-core >= 1.4.0
BuildRequires:  invokebinder
BuildRequires:  jansi
BuildRequires:  jarjar
BuildRequires:  jline2 >= 2.7
BuildRequires:  jffi >= 1.0.10
BuildRequires:  jna
BuildRequires:  jnr-constants
BuildRequires:  jnr-enxio
BuildRequires:  jnr-ffi >= 0.5.10
BuildRequires:  jnr-netdb
BuildRequires:  jnr-posix >= 1.1.8
BuildRequires:  jnr-unixsocket
BuildRequires:  jzlib
BuildRequires:  joda-time
BuildRequires:  joni >= 1.1.2
BuildRequires:  junit4
BuildRequires:  jzlib
BuildRequires:  nailgun
BuildRequires:  objectweb-asm4
BuildRequires:  snakeyaml
BuildRequires:  yydebug
BuildRequires:  yecht

# these normally get installed as gems during the test process
# TODO: create a condition to be able to test with system gems
# generally, requiring MRI during JRuby build would be nice to avoid
#BuildRequires:  rubygem(rake)
#BuildRequires:  rubygem(rspec-core)
#BuildRequires:  rubygem(rspec-mocks)
#BuildRequires:  rubygem(rspec-expectations)
#BuildRequires:  rubygem(ruby-debug)
#BuildRequires:  rubygem(ruby-debug-base)
#BuildRequires:  rubygem(columnize)

# Java Requires
Requires:  apache-commons-logging
Requires:  bouncycastle
Requires:  bouncycastle-mail
Requires:  bsf
Requires:  bytelist >= 1.0.8
Requires:  felix-osgi-core >= 1.4.0
Requires:  invokebinder
Requires:  jansi
Requires:  jcodings >= 1.0.1
Requires:  jffi >= 1.0.10
Requires:  jline2 >= 2.7
Requires:  jna
Requires:  jnr-constants
Requires:  jnr-enxio
Requires:  jnr-ffi >= 0.5.10
Requires:  jnr-netdb
Requires:  jnr-posix >= 1.1.8
Requires:  jnr-unixsocket
Requires:  joda-time
Requires:  joni >= 1.1.2
Requires:  jruby-yecht
Requires:  jzlib
Requires:  nailgun
Requires:  objectweb-asm4
Requires:  snakeyaml
Requires:  yydebug

# Other Requires
Requires:  jpackage-utils
Requires:  rubygems
#Requires:  rubypick

Provides:  ruby(release) = 1.9.1
Provides:  ruby(release) = 1.8
# For rubypick
Provides:  ruby(runtime_executable)
Source44: import.info

%description
JRuby is a 100% Java implementation of the Ruby programming language.
It is Ruby for the JVM. JRuby provides a complete set of core "builtin"
classes and syntax for the Ruby language, as well as most of the Ruby
Standard Libraries.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

# yecht / jruby bindings
# http://jira.codehaus.org/browse/JRUBY-5352
%package        yecht
Summary:        Bindings used to load yecht in jruby
License:        MIT
Group:          Development/Java
BuildRequires:  yecht
Requires:       yecht
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description yecht
The bindings for the yecht library for internal use in jruby

%package        devel
Summary:        JRuby development environment
Group:          Development/Java
Requires:       jruby
Requires:       jpackage-utils

%description    devel
Macros for building JRuby-specific libraries.

%prep
%setup -q -n %{name}-%{version}%{?preminorver:.%{preminorver}}

%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch7 -p1

%patch100 -p0
%patch101 -p0
%patch102 -p1

tar xzvf %{SOURCE1}
mv %{yecht_cluster}-yecht-%{yecht_commitversion} yecht

# delete all embedded jars - don't delete test jars!
find -path './test' -prune -o -path './spec' -prune -o -type f -name '*.jar' -exec rm -f '{}' \;

# delete windows specific files
find -name *.exe -exec rm -f '{}' \;
find -name *.dll -exec rm -f '{}' \;

# delete all vcs files
find -name .gitignore -exec rm -f '{}' \;
find -name .cvsignore -exec rm -f '{}' \;

# replace them with symlinks
# these sorted to able to check them against new releases easily
# don't forget to also change these in jruby-add-classpath-to-start-script.patch
build-jar-repository -s -p build_lib %{jar_deps}

# required as jruby was shipping the core java tools jar
ln -s %{_prefix}/lib/jvm/java/lib/tools.jar build_lib/apt-mirror-api.jar

# remove hidden .document files
find lib/ruby/ -name '*.document' -exec rm -f '{}' \;

# change included stdlib to use jruby rather than some arcane ruby install
find lib/ruby/ -name '*.rb' -exec sed --in-place "s|^#!/usr/local/bin/ruby|#!/usr/bin/env jruby|" '{}' \;

# lib/ruby scripts shouldn't contain shebangs as they are not executable on their own
find lib/ruby/ -name '*.rb' -exec sed --in-place "s|^#!/usr/local/bin/ruby||" '{}' \;
find lib/ruby/ -name '*.rb' -exec sed --in-place "s|^#!/usr/bin/env ruby||" '{}' \;

# the yecht library needs to be accessible from ruby
pushd yecht
mkdir -p lib/ build/classes/ruby
%patch5 -p0
popd

%build
ant
ant apidocs

# remove bat files
rm bin/*.bat

pushd yecht
ant ext-ruby-jar
popd

%install
install -d -m 755 %{buildroot}%{_datadir}
install -p -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -ar lib/     %{buildroot}%{_datadir}/%{name}/ # stdlib + jruby.jar
cp -ar bin/     %{buildroot}%{_datadir}/%{name}/ # startup scripts

# /usr prefix startup scripts
install -d -m 755 %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/bin/jgem  %{buildroot}%{_bindir}/gem-jruby
ln -s %{_datadir}/%{name}/bin/jirb  %{buildroot}%{_bindir}/irb-jruby
ln -s %{_datadir}/%{name}/bin/jruby %{buildroot}%{_bindir}/jruby

## Fedora integration stuff
# modify the JRuby executable to contain Fedora specific paths redefinitons
# we need to modify jruby{,sh,bash} to be sure everything is ok
sed -i 's|$FEDORA_JAVA_OPTS|-Dvendor.dir.general=%{jruby_vendordir}\
                            -Dsite.dir.general=%{jruby_sitedir}\
                            -Dvendor.dir.rubygems=%{rubygems_dir}|' \
  %{buildroot}%{_datadir}/%{name}/bin/jruby*

# install JRuby specific bits into system RubyGems
mkdir -p %{buildroot}%{rubygems_dir}/rubygems/defaults
cp -a lib/ruby/shared/rubygems/defaults/* %{buildroot}%{rubygems_dir}/rubygems/defaults
# Apply patch6 here to not break tests by changing the rubygems dirs
pushd %{buildroot}%{rubygems_dir}
patch -p0 < %{PATCH6}
popd

# Dump the macros into macros.jruby to use them to build other JRuby libraries.
mkdir -p %{buildroot}%{_sysconfdir}/rpm
cat >> %{buildroot}%{_sysconfdir}/rpm/macros.jruby << \EOF
%%jruby_libdir %%{_datadir}/%{name}/lib/ruby/1.9

# This is the general location for libs/archs compatible with all
# or most of the Ruby versions available in the Fedora repositories.
%%jruby_vendordir vendor_ruby
%%jruby_vendorlibdir %%{jruby_libdir}/%%{jruby_vendordir}
%%jruby_vendorarchdir %%{jruby_vendorlibdir}
EOF

# javadoc
install -p -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -a docs/api/* %{buildroot}%{_javadocdir}/%{name}

# jruby-yecht
install -d -m 755 %{buildroot}%{_javadir}
cp yecht/lib/yecht-ruby-0.0.2.jar %{buildroot}%{_datadir}/%{name}-yecht.jar
ln -s ../../..%{_datadir}/%{name}-yecht.jar %{buildroot}%{_javadir}/%{name}-yecht.jar

# java dir
install -d -m 755 %{buildroot}%{_javadir}
ln -s ../../..%{_datadir}/%{name}/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# poms
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
cp -a pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}-shared.pom
%add_maven_depmap JPP-%{name}-shared.pom
cp -a maven/jruby/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# Remove copied bouncycastle jars
rm %{buildroot}%{_datadir}/%{name}/lib/ruby/shared/bc*.jar

%check
%if 0%{?enable_check}
cp yecht/lib/yecht-ruby-0.0.2.jar build_lib/%{name}-yecht.jar
cp lib/%{name}.jar build_lib/%{name}.jar
# explicitly set path to jruby.jar and jruby-yecht.jar, as they can't found by "build-classpath" used in bin/jruby
export JRUBY_CP=$(pwd)/build_lib/jruby.jar:$(pwd)/build_lib/jruby-yecht.jar
# some tests are not run via bin/jruby, so we have to specify CLASSPATH explictly for them to work
export CLASSPATH=$(build-classpath %{jar_deps}):$(pwd)/build_lib/jruby.jar:$(pwd)/build_lib/jruby-yecht.jar
# make sure that we don't install jruby-launcher, as it will first need to be patched upstream
# to be able to find unbundled jars
sed -i 's|depends="install-dev-gems,install-jruby-launcher-gem"|depends="install-dev-gems"|' build.xml

# TODO: tests fail because JRuby is split into multiple jars that can't be found on execution
# of custom built jars in this test, it seems that using proper Class-Path in manifest should fix this
sed -i 's|test_loading_compiled_ruby_class_from_jar|test_loading_compiled_ruby_class_from_jar\nreturn|' test/test_load_compiled_ruby_class_from_classpath.rb

export LANG=en_US.utf8
ant test
%endif

%files -f .mfiles
%doc COPYING LICENSE.RUBY
%doc docs/CodeConventions.txt docs/README.test

%{_bindir}/%{name}
%{_bindir}/gem-jruby
%{_bindir}/irb-jruby
%{_datadir}/%{name}
# exclude bundled gems
%exclude %{jruby_vendordir}/ruby/1.9/json*
%exclude %{jruby_vendordir}/ruby/1.9/rdoc*
%exclude %{jruby_vendordir}/ruby/1.9/rake*
%exclude %{jruby_vendordir}/ruby/gems
# exclude all of the rubygems stuff
%exclude %{jruby_vendordir}/ruby/shared/*ubygems*
%exclude %{jruby_vendordir}/ruby/shared/rbconfig
# own the JRuby specific files under RubyGems dir
%{rubygems_dir}/rubygems/defaults/jruby.rb
# exclude jruby_native.rb that erroneously ended up in .dev tarball
#exclude %{rubygems_dir}/rubygems/defaults/jruby_native.rb
%{_javadir}/%{name}.jar

%files javadoc
%doc COPYING LICENSE.RUBY
#%doc samples
#%{_javadocdir}/%{name}

%files yecht
%doc yecht/LICENSE
%{_datadir}/%{name}-yecht.jar
%{_javadir}/%{name}-yecht.jar

%files devel
%config(noreplace) %{_sysconfdir}/rpm/macros.jruby

%changelog
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

