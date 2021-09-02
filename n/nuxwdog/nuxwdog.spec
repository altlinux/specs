%define _unpackaged_files_terminate_build 1

Name: nuxwdog
Version: 1.0.5
Release: alt1.2

Summary: Watchdog server to start and stop processes, and prompt for passwords
License: %lgpl2plus, %perl_license
Group: Networking/Other
Url: https://www.dogtagpki.org/wiki/Nuxwdog
# Source-git: https://github.com/dogtagpki/nuxwdog.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses rpm-macros-java

%if "%{version}" == "1.0.5"
# this old wersion can't be  built with java 11
BuildRequires: java-1.8.0-devel
%else
# but latest upstream versions shoud be ok
BuildRequires: java-devel-default
%endif
BuildRequires: ant jpackage-utils
BuildRequires: gcc-c++
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
Requires: lib%name = %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
This package contains the header files needed to build clients
that call WatchdogClient functions, so that clients can interact with
the nuxwdog watchdog server.

%package -n lib%name-java
Summary: Nuxwdog Watchdog client JNI Package
License: %lgpl2plus
Group: Development/Java
Requires: lib%name = %EVR
Provides: %name-client-java = %EVR
Provides: /usr/lib/java/nuxwdog.jar

%description -n lib%name-java
This package contains a JNI interface to the nuxwdog
client code, so that Java clients can interact with the nuxwdog watchdog
server.

%package -n lib%name-perl
Summary: Nuxwdog Watchdog client perl bindings
License: %perl_license
Group: Development/Perl
Requires: lib%name = %EVR
Provides: %name-client-perl = %EVR

%description -n lib%name-perl
This package contains a perl interface to nuxwdog.

%prep
%setup
%patch -p1
# ALT uses alternatives-list intead of alternatives
grep -q 'javac_exe=`/usr/sbin/alternatives --display javac | grep link | cut -c27-`' \
m4/nuxwdog.m4 || exit 1
sed -i 's/javac_exe=`\/usr\/sbin\/alternatives --display javac | grep link | cut -c27-`/javac_exe=`alternatives-list \/usr\/bin\/javac | cut -d\x22 \x22 -f4`/g' m4/nuxwdog.m4

# nspr paths
grep -qr '#include[[:space:]]\+<nspr4' || exit 1
grep -rl '#include[[:space:]]\+<nspr4' | \
xargs sed -i 's/#include[[:space:]]\+<nspr4\//#include <nspr\//g'

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
mv %buildroot%prefix/jars/nuxwdog.jar %buildroot/%_libdir/nuxwdog-jni/nuxwdog-%version.jar
mkdir -p %buildroot%_jnidir/
ln -s `relative %_libdir/nuxwdog-jni/nuxwdog-%version.jar %_jnidir/nuxwdog.jar` \
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
* Thu Sep 02 2021 Igor Vlasenko <viy@altlinux.org> 1.0.5-alt1.2
- NMU: java 11 migration support

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1.1
- rebuild with new perl 5.28.1

* Tue Dec 04 2018 Stanislav Levin <slev@altlinux.org> 1.0.5-alt1
- 1.0.3 -> 1.0.5.

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

