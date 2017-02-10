%define solib tolua++-5.1

Name: libtolua++-lua5.1
Version: 1.0.93
Release: alt4
Summary: A tool to integrate C/C++ code with Lua
Group: System/Libraries
License: MIT
Url: http://www.codenix.com/~tolua/

Source: http://www.codenix.com/~tolua/tolua++-%version.tar.bz2
Patch0: tolua++-1.0.93-lua51.patch
Patch1: tolua++-1.0.93-lua-include-path.patch

BuildRequires: scons
BuildRequires: liblua5.1-devel

Conflicts: tolua++ < 1.0.93-alt2
Obsoletes: tolua++ < 1.0.93-alt2

%description
tolua++ is an extended version of tolua, a tool to integrate C/C++ code with
Lua. tolua++ includes new features oriented to C++

%package devel
Summary: Development files for tolua++
Group: Development/C++
Requires: %name = %version-%release
Requires: liblua5.1-devel
Conflicts: tolua++-devel

%description devel
Development files for tolua++ (for lua 5.1)

%prep
%setup -q -n tolua++-%version
%patch0 -p1
%patch1 -p1
sed -i 's/\r//' doc/tolua++.html

%build
scons %{?_smp_mflags} -Q CCFLAGS="%optflags  -I%_includedir" tolua_lib=%solib LINKFLAGS="-Wl,-soname,lib%solib.so" shared=1
# from fedora's compat-tolua-5.1
# Relink the tolua++ binary, there are 2 reasons for this:
# -Link it without the soname which we add to LINKFLAGS to build a shared lib
# -On non x86_64 link it against the pre-generated toluabind rather then the
#  bootstapped one as something goes wrong with the bootstrap on ARM, x86_32
#  (rhbz#1094103) and ppc (rhbz#704372) causing a segfault for unknown reasons.
%ifarch x86_64
gcc -o bin/tolua++ src/bin/tolua.o src/bin/toluabind.o -Llib -l%{solib} -llua-5.1 -ldl -lm
%else
gcc -o bin/tolua++ src/bin/tolua.o src/bin/toluabind_default.o -Llib -l%{solib} -llua-5.1 -ldl -lm
%endif

%install

mkdir -p %buildroot%_bindir
mkdir %buildroot%_libdir
mkdir %buildroot%_includedir
install -m0755 bin/tolua++  %buildroot%_bindir
install -m0755 lib/lib%solib.so %buildroot%_libdir
install -m0644 include/tolua++.h %buildroot%_includedir
cd %buildroot%_libdir
ln -s lib%solib.so libtolua++.so

%files
%_libdir/lib%solib.so
%doc README

%files devel
%doc doc/*
%_bindir/tolua++
%_libdir/libtolua++.so
%_includedir/tolua++.h

%changelog
* Fri Feb 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.93-alt4
- Obsoletes and conflict on old tolua++

* Thu Feb 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.93-alt3
- added conflict on old tolua++ for smooth upgrade

* Wed Feb 08 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.93-alt2
- build with compat lua 5.1

* Mon Jul 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.93-alt1
- 1.0.93 (ALT #25847)

* Wed Mar 16 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.92-alt4
- rebuild for debuginfo

* Tue Dec 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.92-alt3
- rebuild for soname set-version

* Mon Nov 09 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.92-alt2
- remove %%post_ldconfig

* Wed Jun 04 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.92-alt1
- build for ALT

* Thu Mar 13 2008 Tim Niemueller <tim@niemueller.de> - 1.0.92-7
- Added patch to make tolua++ compatible with GCC 4.3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.92-6
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Ian Chapman <packages@amiga-hardware.com> 1.0.92-5
- Release bump for F8 mass rebuild
- Updated license due to new guidelines

* Mon Aug 28 2006 Ian Chapman <packages@amiga-hardware.com> 1.0.92-4
- Release bump for FC6 mass rebuild

* Sat Jun 03 2006 Ian Chapman <packages@amiga-hardware.com> 1.0.92-3
- Fixed issue with where tolua++ was tagged with an soname the same as the lib
  meaning ld would fail to locate the library.

* Fri Jun 02 2006 Ian Chapman <packages@amiga-hardware.com> 1.0.92-2
- Changed license from Freeware Style to just Freeware
- Changed => to more conventional >= for (build)requires
- Moved %%{_bindir}/tolua++ to devel package
- Now adds soname to library

* Fri Jun 02 2006 Ian Chapman <packages@amiga-hardware.com> 1.0.92-1
- Initial Release
