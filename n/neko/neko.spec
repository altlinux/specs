Name: neko
Version: 2.2.0
Release: alt4.gitb68336c

# commit: b68336cbc250937fda2741dedc7866b4d5f14d27

Summary: The Neko Programming Language

License: LGPL
Group: Development/Other
Url: http://haxe.org

%define aversion %(echo "%version" | sed -e "s|\\.|-|g")
# Source-url: https://github.com/HaxeFoundation/neko/archive/v%aversion.tar.gz
Source: %name-%version.tar

Patch1: neko-apr-util.patch

BuildRequires: /proc

BuildRequires: rpm-macros-cmake cmake git-core

BuildRequires: apache2-devel libgc-devel libgtk+2-devel libssl-devel libmysqlclient-devel libpcre-devel libsqlite3-devel libmbedtls-devel libaprutil1-devel libapr1-devel

Requires: lib%name = %version-%release

# TODO: move to a separate package
# Apache modules
%add_verify_elf_skiplist %_libdir/neko/mod_tora2.ndll %_libdir/neko/mod_neko2.ndll

%description
Neko is an intermediate programming language. It has been designed to
provide a common runtime for several different languages. Learning and
using Neko is very easy, but you're not supposed to directly program in
Neko. Instead, you can write a generator from your preferred language to
Neko and then use the Neko runtime to compile, run, and access libraries.

Neko is a good way for language designers to focus on design and reuse a
fast and well-designed runtime, as well as existing libraries for
accessing filesystem, network, databases, xml...


%package -n lib%name
Summary: The Neko Programming Language
Group: System/Libraries

%description -n lib%name
This package provides %name shared libraries.

%package -n lib%name-devel
Summary: The Neko Programming Language
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel

This package provides development files for %name.


%prep
%setup
%patch1 -p2

%build
%cmake_insource -DCMAKE_INSTALL_LIBDIR=%_libdir
%make_build

%install
%makeinstall_std
# hack
mkdir -p %buildroot/usr/share/cmake/Modules/
mv %buildroot%_libdir/cmake/Neko %buildroot/usr/share/cmake/Modules/

%files
%doc README.md
%_bindir/%name
%_bindir/nekoc
%_bindir/nekoml
%_bindir/nekotools

%files -n lib%name
%_libdir/*.so.*
%_libdir/%name/

%files -n lib%name-devel
%_libdir/*.so
%dir %_datadir/cmake
%_datadir/cmake/Modules/
%_includedir/*.h


%changelog
* Mon Dec 24 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt4.gitb68336c
- fix build warning (hide Apache2 symbols)

* Mon Dec 24 2018 Leontiy Volodin <lvol@altlinux.org> 2.2.0-alt3.gitb68336c
- fix build
- build from git

* Tue Dec 04 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt2
- add libssl-devel buildreq
- add /proc buildreq (ALT bug 35723)

* Mon Jun 18 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)
- build from tarball

* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt3
- Fixed build with new glibc.

* Thu May 05 2016 Sergey Alembekov <rt@altlinux.ru> 2.0.0-alt2
- backport apache-2.4 support

* Mon Aug 05 2013 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALTLinux Sisyphus
