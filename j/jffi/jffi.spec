# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global commit_hash 52af1f2
%global tag_hash f2d7914
%global sofile_version 1.2

Name:    jffi
Version: 1.2.6
Release: alt1_1jpp7
Summary: An optimized Java interface to libffi 

Group:   System/Libraries
License: LGPLv3+ or ASL 2.0
URL:     http://github.com/jnr/%{name}/
Source0: https://github.com/jnr/%{name}/tarball/%{version}/jnr-%{name}-%{version}-0-g%{commit_hash}.tar.gz
Patch0:  jffi-fix-dependencies-in-build-xml.patch
Patch1:  jffi-add-built-jar-to-test-classpath.patch
Patch2:  jffi-fix-compilation-flags.patch

BuildRequires: jpackage-utils
BuildRequires: libffi-devel

BuildRequires: ant
BuildRequires: ant-nodeps
BuildRequires: ant-junit
BuildRequires: junit4

Requires: jpackage-utils
Source44: import.info

%description
An optimized Java interface to libffi 

%prep
%setup -q -n jnr-%{name}-%{tag_hash}
%patch0
%patch1
%patch2

# ppc{,64} fix
# https://bugzilla.redhat.com/show_bug.cgi?id=561448#c9
sed -i.cpu -e '/m\$(MODEL)/d' jni/GNUmakefile libtest/GNUmakefile
%ifnarch %{ix86} x86_64
rm -rf test/
%endif

# remove random executable bit
chmod 0644 jni/jffi/jffi.h

# remove uneccessary directories
rm -rf archive/* jni/libffi/ jni/win32/ lib/CopyLibs/ lib/junit*

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
build-jar-repository -s -p lib/ junit

ant -Duse.system.libffi=1

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_jnidir}/

cp -p dist/%{name}-complete.jar $RPM_BUILD_ROOT%{_jnidir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%check
# don't fail on unused parameters... (TODO: send patch upstream)
sed -i 's|-Werror||' libtest/GNUmakefile
ant -Duse.system.libffi=1 test

%files
%doc COPYING.GPL COPYING.LESSER LICENSE
%{_jnidir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.6-alt1_1jpp7
- new version

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt3_1jpp7
- fixed build

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt2_1jpp7
- gcc47 build

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.10-alt1_1jpp7
- new version

