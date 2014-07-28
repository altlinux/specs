Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
%global gitdate  20120218
%global gittag   e547893deebde5a1340a72bc05f19b9caab1774a
%global shorttag %(echo %{gittag} | cut -b -7)
%global user     nettoyeurny

Name:           jacknativeclient
Version:        0
Release:        alt1_0.3.20120218gitjpp7
Summary:        Java bindings for JACK clients

License:        LGPLv3+
URL:            https://github.com/%{user}/%{name}/
Source0:        https://github.com/%{user}/%{name}/tarball/%{gittag}/%{user}-%{name}-%{gittag}.tar.gz

BuildRequires:  ant
BuildRequires:  libjack-devel
BuildRequires:  jpackage-utils

Requires:       jpackage-utils
Source44: import.info

%description
This package exposes the JACK audio interface to Java clients.

%package javadoc
Group: Development/Java
Summary:        Javadoc documentation for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
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
javadoc -d api -sourcepath src -classpath bin com.noisepages.nettoyeur.jack

# build.xml tries to build both 32-bit and 64-bit shared libraries, and
# also doesn't use our CFLAGS.  Fix both problems with a manual build.
cd src/com/noisepages/nettoyeur/jack
gcc $RPM_OPT_FLAGS -I%{_jvmdir}/java/include -I%{_jvmdir}/java/include/linux \
  -I%{_includedir}/jack -I. -shared -fPIC -o ../../../../../libjacknative.so \
  jacknative.c -ljack

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
install -m 644 %{name}.jar $RPM_BUILD_ROOT%{_libdir}/%{name}
install -m 755 libjacknative.so $RPM_BUILD_ROOT%{_libdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc LICENSE README
%{_libdir}/%{name}/

%files javadoc
%{_javadocdir}/%{name}/

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.3.20120218gitjpp7
- new release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.2.20120218gitjpp7
- new version

