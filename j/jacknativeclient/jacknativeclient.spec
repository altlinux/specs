Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%global gitdate  20120218
%global gittag   e547893deebde5a1340a72bc05f19b9caab1774a
%global shorttag %(echo %{gittag} | cut -b -7)
%global user     nettoyeurny

Name:           jacknativeclient
Version:        0
Release:        alt2_0.11.20120218gitjpp8
Summary:        Java bindings for JACK clients

License:        LGPLv3+
URL:            https://github.com/%{user}/%{name}/
Source0:        https://github.com/%{user}/%{name}/tarball/%{gittag}/%{user}-%{name}-%{gittag}.tar.gz

BuildRequires:  ant
BuildRequires:  libjack-devel
BuildRequires:  java-javadoc
BuildRequires: javapackages-tools rpm-build-java

Requires: javapackages-tools rpm-build-java
Source44: import.info

%description
This package exposes the JACK audio interface to Java clients.

%package javadoc
Group: Development/Java
Summary:        Javadoc documentation for %{name}
Requires:       %{name} = %{version}
BuildArch:      noarch

%description javadoc
Javadoc documentation for %{name}.

%prep
%setup -q -n %{user}-%{name}-%{shorttag}

# Remove prebuilt objects
rm -fr lib

# Change the load path as required by Fedora
sed -i "s|\(System.load\).*|\1(\"%{_libdir}/%{name}/libjacknative.so\");|" \
    src/com/noisepages/nettoyeur/jack/JackNativeClient.java

%build
# Build the Java interface
ant javah

# Build a jar
cd bin
jar cf ../%{name}.jar com
cd ..

# Build the javadoc documentation
javadoc -d api -link file://%{_javadocdir}/java \
  -sourcepath src -classpath bin com.noisepages.nettoyeur.jack

# build.xml tries to build both 32-bit and 64-bit shared libraries, and
# also doesn't use our CFLAGS.  Fix both problems with a manual build.
cd src/com/noisepages/nettoyeur/jack
gcc $RPM_OPT_FLAGS -I%{_jvmdir}/java/include -I%{_jvmdir}/java/include/linux \
  -I%{_includedir}/jack -I. -shared -fPIC -o ../../../../../libjacknative.so \
  jacknative.c $RPM_LD_FLAGS -ljack

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
install -m 644 %{name}.jar %{buildroot}%{_libdir}/%{name}
install -m 755 libjacknative.so %{buildroot}%{_libdir}/%{name}

mkdir -p %{buildroot}%{_jnidir}
ln -s %{_libdir}/%{name}/%{name}.jar %{buildroot}%{_jnidir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}
cp -a api %{buildroot}%{_javadocdir}/%{name}

%files
%doc README
%doc LICENSE
%{_libdir}/%{name}/
%{_jnidir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}/

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt2_0.11.20120218gitjpp8
- new fc release

* Thu Feb 11 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt2_0.10.20120218gitjpp8
- %%_jnidir set to /usr/lib/java

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.10.20120218gitjpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.4.20120218gitjpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.3.20120218gitjpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.2.20120218gitjpp7
- new version

