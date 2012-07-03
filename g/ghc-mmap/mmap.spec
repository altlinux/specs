%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define h_pkg_name mmap
%define f_pkg_name mmap
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.5.7
Release: alt1
License: BSD3
Group: Development/Haskell
URL: http://hackage.haskell.org/package/mmap
Packager: Alexey Voinov <voins@altlinux.ru>
Source: %f_pkg_name-%version.tar
Summary: Memory mapped files for POSIX and Windows

BuildRequires: ghc
BuildRequires(pre): rpm-build-haskell


%description
This library provides a wrapper to mmap(2) or MapViewOfFile, allowing
files or devices to be lazily loaded into memory as strict or lazy
ByteStrings, ForeignPtrs or plain Ptrs, using the virtual memory
subsystem to do on-demand loading.  Modifications are also supported.


%prep
%setup -n %h_pkg_name-%version


%build


%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

cd %buildroot/%_datadir/doc/%hsc_namever-%f_pkg_name-%version
rm -rf doc LICENSE README


%files  -f %name-files.nonprof
%hs_pkgconfdir/%f_pkg_name-%version.conf
%doc dist/doc/html
%doc LICENSE


%changelog
* Wed Nov 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.7-alt1
- 0.5.7

* Sat Aug 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.4.1-alt6.1.1
- rebuild with shared objects support

* Tue Dec 07 2010 Denis Smirnov <mithraen@altlinux.ru> 0.4.1-alt6.1
- rebuild with ghc 7.0/var/lib/altlinux/sisyphus/files/SRPMS/ghc-ansi-terminal-0.5.3-alt1.src.rpm

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.4.1-alt6
- auto rebuild

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 0.4.1-alt5
- auto rebuild

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 0.4.1-alt2
- ghc 6.12.3

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 0.4.1-alt1.1.1
- rebuild with new haskell

* Wed Mar 17 2010 Denis Smirnov <mithraen@altlinux.ru> 0.4.1-alt1.1
- rebuild with new haskell

* Tue Oct 06 2009 Alexey Voinov <voins@altlinux.ru> 0.4.1-alt1
- Initial build for Sisyphus.
