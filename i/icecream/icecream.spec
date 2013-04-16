%def_enable shared
%def_enable static
%def_without man
%def_disable clang
%define _libexecdir %_prefix/libexec
%define _localstatedir %_var

Name: icecream
%define lname libicecc
Version: 1.0.0
Release: alt1
Summary: Icecream is a distributed compile system for C and C++
License: GPLv2+ and LGPLv2.1+
Group: Development/Tools
URL: https://github.com/icecc/%name
Source: %name-%version.tar
Source1: iceccd.init.in
Source2: icecc-scheduler.init.in
Source3: %name.sysconfig.in
Source4: %name.logrotate.in
Patch: %name-%version-%release.patch
Provides: icecc = %version-%release
%{?_enable_shared:Requires: %lname = %version-%release}
Requires: gcc-c++

BuildRequires: gcc-c++ libcap-ng-devel

%description
Icecream is a distributed compile system for C and C++.
Icecream is created by SUSE and is based on ideas and code by distcc. Like distcc
it takes compile jobs from your build and distributes it to remote machines
allowing a parallel build on several machines you've got. But unlike distcc
Icecream uses a central server that schedules the compile jobs to the fastest
free server and is as this dynamic. This advantage pays off mostly for shared
computers, if you're the only user on x machines, you have full control over them
anyway.


%if_enabled shared
%package -n %lname
Summary: Icecream library
Group: System/Libraries
Provides: lib%name = %version-%release

%description -n %lname
Icecream is a distributed compile system for C and C++.
This package contains Icecream shared library.
%endif


%package -n %lname-devel
Summary: Files for development with libicecc
Group: Development/C++
Provides: lib%name-devel = %version-%release
Provides: %name-devel = %version-%release
Provides: icecc-devel = %version-%release
Requires: libstdc++-devel
Requires: %lname%{?_disable_shared:-devel-static} = %version-%release

%description -n %lname-devel
Icecream is a distributed compile system for C and C++.
This package contains files for development with libicecc.


%if_enabled static
%package -n %lname-devel-static
Summary: Static Icecream library
Group: Development/C++
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
Icecream is a distributed compile system for C and C++.
This package contains static Icecream library.
%endif


%prep
%setup -q
%patch -p1
%{?_without_man:sed -i '/^[[:blank:]]*doc[[:blank:]]/d' Makefile.am}
install -d -m 0755 ./altlinux
install -p -m 0644 %{S:1} %{S:2} %{S:3} %{S:4} ./altlinux/


%build
./autogen.sh
%configure \
	%{subst_enable shared} %{subst_enable static} \
	%{subst_enable clang}-rewrite-includes %{subst_enable clang}-wrappers \
	%{subst_with man}

%make_build

for f in altlinux/*.in; do
	sed 's|@logdir@|%_logdir|g;s|@cachedir@|%_cachedir|g;s|@initddir@|%_initddir|g' $f > ${f%%.in}
done


%install
%makeinstall_std
ln -sf icecc %buildroot%_bindir/icerun
install -d -m 0755 %buildroot{%_initddir,{%_cachedir,%_logdir}/%name}
for f in altlinux/*.init; do
	install -p -m 0755 $f %buildroot%_initddir/$(basename $f .init)
done
install -Dp -m 0644 altlinux/%name.sysconfig %buildroot%_sysconfdir/sysconfig/%name
install -Dp -m 0644 altlinux/%name.logrotate %buildroot%_logrotatedir/%name


%post
%post_service iceccd
%post_service icecc-scheduler


%preun
%preun_service iceccd
%preun_service icecc-scheduler


%pre
/usr/sbin/groupadd -r _%name 2>/dev/null ||:
/usr/sbin/useradd -r -g _%name -s /bin/false -c "Icecream Daemon" -d /var/cache/%name _%name 2>/dev/null ||:


%files
%doc BENCH NEWS README.md TODO
%_bindir/*
%_sbindir/*
%{?_with_man:%_man1dir/*}
%_libexecdir/*
%_initddir/*
%config %_logrotatedir/*
%config %_sysconfdir/sysconfig/*
%attr(0775,root,_%name) %dir %_cachedir/%name
%attr(0775,root,_%name) %dir %_logdir/%name


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif


%files -n %lname-devel
%_includedir/*
%{?_enable_shared:%_libdir/*.so}
%_pkgconfigdir/*


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%changelog
* Tue Apr 15 2013 Led <led@altlinux.ru> 1.0.0-alt1
- initial build
