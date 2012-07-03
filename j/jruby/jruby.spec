Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global yecht_commitversion 157cf13
%global yecht_dlversion 0.0.2-0-g157cf13
%global yecht_cluster olabini

Name:           jruby
Version:        1.6.3
Release:        alt1_3jpp7
Summary:        Pure Java implementation of the Ruby interpreter
Group:          Development/Java
License:        (CPL or GPLv2+ or LGPLv2+) and ASL 1.1 and MIT and Ruby
URL:            http://jruby.org/
BuildArch:      noarch
Source0:        http://jruby.org.s3.amazonaws.com/downloads/%{version}/jruby-src-%{version}.tar.gz
Source1:        http://github.com/%{yecht_cluster}/yecht/tarball/0.0.2/%{yecht_cluster}-yecht-%{yecht_dlversion}.tar.gz
Patch1:         add-classpath-to-jruby-start-script.patch
Patch2:         dont-include-jar-dependencies-in-build-xml.patch
Patch3:         remove-invoke-dynamic-support.patch
Patch5:         jruby-dont-use-jruby-until-build-is-complete.patch

# this patch contains the following upstream change
# https://github.com/jruby/jruby/commit/6c1d41aedfde705c969abf10cf5384e2be69f10a
Patch6:         remove-builtin-yecht-jar.patch

Patch7:         yecht-only-build-bindings.patch

BuildRequires:  jpackage-utils >= 1.5
BuildRequires:  ant >= 1.6
BuildRequires:  objectweb-asm
BuildRequires:  bytelist >= 1.0.8
BuildRequires:  jnr-constants
BuildRequires:  jline
BuildRequires:  jcodings >= 1.0.5
BuildRequires:  joni >= 1.1.2
BuildRequires:  jna
BuildRequires:  jnr-ffi >= 0.5.10
BuildRequires:  jffi >= 1.0.10
BuildRequires:  joda-time
BuildRequires:  yydebug
BuildRequires:  nailgun
BuildRequires:  emma
BuildRequires:  jgrapht
BuildRequires:  bsf
BuildRequires:  jnr-netdb
BuildRequires:  yecht
BuildRequires:  jakarta-commons-logging
BuildRequires:  jarjar
BuildRequires:  ant-junit
BuildRequires:  junit4
BuildRequires:  felix-osgi-core >= 1.4.0
BuildRequires:  snakeyaml18
BuildRequires:  jnr-posix >= 1.1.8

# these normally get installed as gems during the test process
#BuildRequires:  rubygem(rake)
#BuildRequires:  rubygem(rspec-core)
#BuildRequires:  rubygem(rspec-mocks)
#BuildRequires:  rubygem(rspec-expectations)
#BuildRequires:  rubygem(ruby-debug)
#BuildRequires:  rubygem(ruby-debug-base)
#BuildRequires:  rubygem(columnize)
BuildRequires:  ruby-rake

Requires:  objectweb-asm
Requires:  bytelist >= 1.0.8
Requires:  jnr-constants
Requires:  jline
Requires:  jcodings >= 1.0.1
Requires:  joni >= 1.1.2
Requires:  jna
Requires:  jnr-ffi >= 0.5.10
Requires:  jffi >= 1.0.10
Requires:  joda-time
Requires:  yydebug
Requires:  nailgun
Requires:  emma
Requires:  jgrapht
Requires:  bsf
Requires:  jnr-netdb
Requires:  jruby-yecht
Requires:  jnr-posix >= 1.1.8
Source44: import.info


%description
JRuby is a 100%% Java implementation of the Ruby programming language.
It is Ruby for the JVM. JRuby provides a complete set of core "builtin"
classes and syntax for the Ruby language, as well as most of the Ruby
Standard Libraries.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

# yecht / jruby bindings
# http://jira.codehaus.org/browse/JRUBY-5352
%package        yecht
Summary:        Bindings used to load yecht in jruby
Group:          Development/Java
BuildRequires:  yecht
Requires:       yecht
Requires:       %{name} = %{version}-%{release}

%description yecht
The bindings for the yecht library for internal use in jruby

%prep
%setup -q -n %{name}-%{version}
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch5 -p0
%patch6 -p0

tar xzvf %{SOURCE1}
mv %{yecht_cluster}-yecht-%{yecht_commitversion} yecht

# delete all embedded jars
find -name *.jar -exec rm -f '{}' \;

# delete windows specific files
find -name *.exe -exec rm -f '{}' \;
find -name *.dll -exec rm -f '{}' \;

# delete prebuilt gems in the build dir
rm build_lib/*.gem

# delete all vcs files
find -name .gitignore -exec rm -f '{}' \;
find -name .cvsignore -exec rm -f '{}' \;

# replace them with symlinks
build-jar-repository -s -p build_lib \
     objectweb-asm/asm objectweb-asm/asm-util \
     objectweb-asm/asm-commons objectweb-asm/asm-analysis objectweb-asm/asm-tree \
     bytelist constantine jline jcodings joni jna jaffl jffi joda-time  felix/org.osgi.core \
     yydebug nailgun emma jnr-posix jgrapht bsf jnr-netdb commons-logging jarjar junit junit4 \
     yecht snakeyaml18 emma_ant

# required as jruby was shipping the core java tools jar
ln -s /usr/lib/jvm/java/lib/tools.jar build_lib/apt-mirror-api.jar

# remove hidden .document files
find lib/ruby/ -name '*.document' -exec rm -f '{}' \;

# We don't have source to support accessing the jar this accesses
rm src/org/jruby/runtime/invokedynamic/InvokeDynamicSupport.java
rm src/org/jruby/compiler/impl/InvokeDynamicInvocationCompiler.java

# change included stdlib to use jruby rather than some arcane ruby install
#find lib/ruby/ -name '*.rb' -exec sed --in-place "s|^#!/usr/local/bin/ruby|#!/usr/bin/env jruby|" '{}' \;

# lib/ruby scripts shouldn't contain shebangs as they are not executable on their own
find lib/ruby/ -name '*.rb' -exec sed --in-place "s|^#!/usr/local/bin/ruby||" '{}' \;
find lib/ruby/ -name '*.rb' -exec sed --in-place "s|^#!/usr/bin/env ruby||" '{}' \;

# this file needs to be marked as executable for one of the tests to pass
chmod +x test/org/jruby/util/shell_launcher_test

# the yecht library needs to be accessible from ruby
pushd yecht
mkdir -p lib/ build/classes/ruby
%patch7 -p0

%build
ant
ant apidocs

# remove bat files
rm bin/*.bat

pushd yecht
ant ext-ruby-jar

%install
install -d -m 755 %{buildroot}%{_datadir}
install -p -d -m 755 %{buildroot}%{_datadir}/%{name}
cp -ar samples/ %{buildroot}%{_datadir}/%{name}/ # samples
cp -ar lib/     %{buildroot}%{_datadir}/%{name}/ # stdlib + jruby.jar
cp -ar bin/     %{buildroot}%{_datadir}/%{name}/ # startup scripts

ln -s %{_datadir}/%{name}/lib/%{name}.jar %{buildroot}%{_datadir}/%{name}.jar

# /usr prefix startup scripts
install -d -m 755 %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/bin/jruby %{buildroot}%{_bindir}/jruby
ln -s %{_datadir}/%{name}/bin/jirb  %{buildroot}%{_bindir}/jirb

# javadoc
install -p -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -a docs/api/* %{buildroot}%{_javadocdir}/%{name}

# jruby-yecht
install -d -m 755 %{buildroot}%{_javadir}
cp yecht/lib/yecht-ruby-0.0.2.jar %{buildroot}%{_datadir}/%{name}-yecht.jar
ln -s %{_datadir}/%{name}-yecht.jar %{buildroot}%{_javadir}/%{name}-yecht.jar

# pom
%add_to_maven_depmap org.jruby %{name} %{version} JPP %{name}
mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
cp pom.xml  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-java.pom

# java dir
install -d -m 755 %{buildroot}%{_javadir}
ln -s %{_datadir}/%{name}/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

%check
#ant test

%files
%doc COPYING
%doc docs/CodeConventions.txt docs/README.test

%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/jirb
%{_datadir}/%{name}
%{_datadir}/%{name}.jar
%{_javadir}/%{name}.jar

%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/*

%files javadoc
%{_javadocdir}/%{name}

%files yecht
%{_datadir}/%{name}-yecht.jar
%{_javadir}/%{name}-yecht.jar

%changelog
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

