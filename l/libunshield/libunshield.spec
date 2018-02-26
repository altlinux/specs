%define origname unshield
%def_disable static

Name: lib%origname
Version: 0.6
Release: alt3

Summary: A program to extract InstallShield cabinet files
License: MIT
Group: Archiving/Compression

Url: http://synce.sourceforge.net
Source: %origname-%version.tar.gz
Packager: Mobile Development Team <mobile@packages.altlinux.org>

# Automatically added by buildreq on Fri Oct 12 2007
BuildRequires: gcc-c++ libssl-devel zlib-devel

%description
Cabinet (.CAB) files are a form of archive, which is used by
the InstallShield installer software. The unshield program
simply unpacks such files.

See %url for more information.

%package devel
Summary: Headers for library to extract InstallShield cabinet files
Group: Development/C
Requires: %name = %version
Requires: zlib-devel

%description devel
Cabinet (.CAB) files are a form of archive, which is used by
the InstallShield installer software. The unshield program
simply unpacks such files.

%if_enabled static
%package devel-static
Summary: Static library to extract InstallShield cabinet files Compression Library
Group: Development/C
Requires: %name-devel = %version

%description devel-static
See %url for more information.
%endif

%prep
%setup -n %origname-%version

%build
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' configure
%configure %{subst_enable static} --disable-rpath --with-ssl
%make

%install
%makeinstall_std

%files
%doc README LICENSE
%_bindir/unshield
%_libdir/libunshield.so.*
%_man1dir/*

%files devel
%_includedir/libunshield.h
%_libdir/libunshield.so
%_libdir/pkgconfig/*.pc

%if_enabled static
%files devel-static
%_libdir/libunshield.a
%endif

%changelog
* Thu Jan 19 2012 Michael Shigorin <mike@altlinux.org> 0.6-alt3
- drop RPATH
- minor spec cleanup

* Tue Oct 05 2010 Alexey Shabalin <shaba@altlinux.ru> 0.6-alt2
- rebuild with new openssl

* Mon Aug 24 2009 Alexey Shabalin <shaba@altlinux.ru> 0.6-alt1
- 0.6

* Sat Oct 04 2008 Alexey Shabalin <shaba@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Sat Dec 08 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.5-alt3
- update to SVN 20071207 version

* Fri Oct 12 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.5-alt2
- fix #13081 (linking with crypto lib), thanks to Slava Semushin

* Sun Jul 24 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.5-alt1
- 0.5

* Fri Sep 03 2004 Michael Shigorin <mike@altlinux.ru> 0.4-alt1
- built for ALT Linux (synce-kde dependency)


