Name: libtalloc
Version: 2.0.7
Release: alt1

Summary: The talloc library

License: LGPLv3+
Group: System/Libraries
Url: http://talloc.samba.org/

Source: http://samba.org/ftp/talloc/talloc-%version.tar.gz

# Automatically added by buildreq on Thu Jan 26 2012
BuildRequires: docbook-dtds docbook-style-xsl libacl-devel libcap-devel python-devel xsltproc

%description
A library that implements a hierarchical allocator with destructors.

%package devel
Group: Development/C
Summary: Developer tools for the Talloc library
Requires: %name = %version-%release

%package -n libpytalloc
Group: Development/Tools
Summary: Developer tools for the Talloc library
Requires: libtalloc = %version-%release

%description -n libpytalloc
Pytalloc libraries for creating python bindings using talloc

%package -n libpytalloc-devel
Group: Development/C
Summary: Developer tools for the Talloc library
Requires: libpytalloc = %version-%release

%description -n libpytalloc-devel
Development libraries for libpytalloc

%description devel
Header files needed to develop programs that link against the Talloc library.

%prep
%setup -q -n talloc-%version

%build
./configure --prefix=%_usr --libdir=%_libdir --disable-rpath
%make_build

%install
%makeinstall_std

rm -f %buildroot%_libdir/libtalloc.a
rm -f %buildroot%_datadir/swig/*/talloc.i

%files
%_libdir/libtalloc.so.*

%files devel
%_includedir/talloc.h
%_libdir/libtalloc.so
%_libdir/pkgconfig/talloc.pc
%_mandir/man3/talloc.3.*

%files -n libpytalloc
%_libdir/libpytalloc-util.so.*
%python_sitelibdir/talloc.so

%files -n libpytalloc-devel
%_includedir/pytalloc.h
%_libdir/pkgconfig/pytalloc-util.pc
%_libdir/libpytalloc-util.so


%changelog
* Thu Jan 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Wed Mar 09 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.5-alt2
- disable rpath

* Wed Mar 09 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Mon Nov 22 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt2
- rebuild to gain set-provides

* Tue Jul 06 2010 Ilya Shpigor <elly@altlinux.org> 2.0.1-alt1
- new version 2.0.1

* Tue Nov 24 2009 Ilya Shpigor <elly@altlinux.org> 2.0.0-alt1
- initial build for ALT Linux Sisyphus

* Tue Sep  8 2009 Simo Sorce <ssorce@redhat.com> - 2.0.0-0
- New version from upstream.
- Build also sover 1 compat library to ease packages migration

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Simo Sorce <ssorce@redhat.com> - 1.3.1-1
- Original tarballs had a screw-up, rebuild with new fixed tarballs from
  upstream.

* Tue Jun 16 2009 Simo Sorce <ssorce@redhat.com> - 1.3.1-0
- New Upstream release.

* Wed May 6 2009 Simo Sorce <ssorce@redhat.com> - 1.3.0-0
- First public independent release from upstream
