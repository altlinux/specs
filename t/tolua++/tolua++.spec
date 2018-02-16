%define solib tolua++-5.3

Name: tolua++
Version: 1.0.93
Release: alt2.1
Summary: A tool to integrate C/C++ code with Lua
Group: System/Libraries
License: MIT
Url: https://github.com/LuaDist/toluapp
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: http://www.codenix.com/~tolua/%name-%version.tar.bz2
Patch0: tolua++-1.0.93-no-buildin-bytecode.patch
Patch1: tolua++-1.0.93-lua53.patch

BuildRequires: scons
BuildRequires: lua-devel >= 5.3

%description
tolua++ is an extended version of tolua, a tool to integrate C/C++ code with
Lua. tolua++ includes new features oriented to C++

%package devel
Summary: Development files for tolua++
Group: Development/C++
Requires: tolua++ = %version-%release
Requires: lua-devel >= 5.3

%description devel
Development files for tolua++

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i 's/\r//' doc/%name.html

%build
scons %{?_smp_mflags} -Q CCFLAGS="%optflags  -I%_includedir" tolua_lib=%solib LINKFLAGS="-Wl,-soname,lib%solib.so" shared=1
#Recompile the exe without the soname. An ugly hack.
gcc -o bin/%name src/bin/tolua.o -Llib -l%solib -llua -ldl -lm

%install

mkdir -p %buildroot%_bindir
mkdir %buildroot%_libdir
mkdir %buildroot%_includedir
install -m0755 bin/%name  %buildroot%_bindir
install -m0755 lib/lib%solib.so %buildroot%_libdir
ln -s lib%solib.so %buildroot%{_libdir}/libtolua++.so
install -m0644 include/%name.h %buildroot%_includedir
# For use with Patch2 (not working yet)
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 src/bin/lua/*.lua $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%doc README
%_libdir/lib%solib.so
%{_datadir}/%{name}

%files devel
%doc doc/*
%_bindir/%name
%_libdir/libtolua++.so
%_includedir/%name.h

%changelog
* Fri Feb 16 2018 Grigory Ustinov <grenka@altlinux.org> 1.0.93-alt2.1
- NMU: update url.

* Wed Feb 08 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.93-alt2
- build with lua 5.3

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
