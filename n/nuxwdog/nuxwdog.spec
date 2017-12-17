Name: nuxwdog
Version: 1.0.3
Release: alt4.1

Summary: Watchdog server to start and stop processes, and prompt for passwords
License: %lgpl2plus, %perl_license
Group: Networking/Other
Url: https://fedorahosted.org/nuxwdog/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses rpm-macros-java

BuildRequires: gcc-c++ ant java-devel-default jpackage-utils
BuildRequires: libnspr-devel
BuildRequires: libnss-devel
BuildRequires: libselinux-devel
BuildRequires: perl-devel
BuildRequires: libkeyutils-devel
BuildRequires: chrpath

%define nuxwdog_docdir %_docdir/%name-%version

%description
This package supplies the nuxwdog watchdog daemon,
used to start,stop, prompt for passwords and monitor processes.
It also contains C/C++ and Perl client code to allow clients to
interact with the nuxwdog watchdog daemon.

%package -n lib%name
Summary: The nuxwdog shared library
License: %lgpl2plus
Group: Networking/Other

%description -n lib%name
Watchdog server to start and stop processes, and prompt for passwords.
This package supplies the nuxwdog shared library.

%package -n lib%name-devel
Summary: Development files for the Nuxwdog Watchdog
License: %lgpl2plus
Group: Development/C++
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release

%description -n lib%name-devel
This package contains the header files needed to build clients
that call WatchdogClient functions, so that clients can interact with
the nuxwdog watchdog server.

%package -n lib%name-java
Summary: Nuxwdog Watchdog client JNI Package
License: %lgpl2plus
Group: Development/Java
Requires: lib%name = %version-%release
Provides: %name-client-java = %version-%release
Provides: /usr/lib/java/nuxwdog.jar

%description -n lib%name-java
This package contains a JNI interface to the nuxwdog
client code, so that Java clients can interact with the nuxwdog watchdog
server.

%package -n lib%name-perl
Summary: Nuxwdog Watchdog client perl bindings
License: %perl_license
Group: Development/Perl
Requires: lib%name = %version-%release
Provides: %name-client-perl = %version-%release


%description -n lib%name-perl
This package contains a perl interface to nuxwdog.

%prep
%setup
%patch -p1

%build
%autoreconf
%ant \
	-Dproduct.ui.flavor.prefix="" \
	-Dproduct.prefix="" \
	-Dproduct="nuxwdog" \
	-Dversion="%version"
%configure \
%ifarch x86_64 aarch64
	--enable-64bit \
%endif
	--disable-static

# just make; %%make_build seems to fail on multi-core CPU's
make licensedir=%nuxwdog_docdir

%install
%makeinstall_std licensedir=%nuxwdog_docdir

# java stuff #
mkdir -p %buildroot/%_libdir/nuxwdog-jni
mv %buildroot%_libdir/libnuxwdog-jni.so %buildroot/%_libdir/nuxwdog-jni
mv %buildroot%{_prefix}/jars/nuxwdog.jar %buildroot/%_libdir/nuxwdog-jni/nuxwdog-%{version}.jar
mkdir -p %buildroot%_jnidir/
ln -s `relative %_libdir/nuxwdog-jni/nuxwdog-%{version}.jar %_jnidir/nuxwdog.jar` \
   %buildroot%_jnidir/nuxwdog.jar
rmdir %buildroot/usr/jars
# end java #

chrpath -d %buildroot%_libdir/perl5/auto/Nuxwdogclient/Nuxwdogclient.so

%files
%doc %nuxwdog_docdir/
%_bindir/*
%_man1dir/nuxwdog.1*

%files -n lib%name
%_libdir/libnuxwdog.so.*

%files -n lib%name-devel
%_includedir/nuxwdog/
%_libdir/libnuxwdog.so

%files -n lib%name-java
%_libdir/nuxwdog-jni
%_jnidir/*

%files -n lib%name-perl
%perl_vendorarch/Nuxwdogclient.pm
%perl_vendorarch/auto/Nuxwdogclient
#_man3dir/Nuxwdogclient.3pm*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt4.1
- rebuild with new perl 5.26.1

* Fri Sep 29 2017 Stanislav Levin <slev@altlinux.org> 1.0.3-alt4
- fix Provides of libnuxwdog-java package

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt3.1
- rebuild with new perl 5.24.1

* Sat Feb 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt3
- NMU: fixed java stuff location

* Fri Feb 12 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2
- NMU:
  * fixes in java BR: && R:
  * added compat provides for perl && java
  * %%_jnidir changed location, package should be rebuilt.

* Wed Dec 09 2015 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1
- Initial build.

