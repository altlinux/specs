%def_enable tests

Name: libtalloc
Version: 2.1.10
Release: alt1%ubt
Epoch:   1

Summary: The talloc library

License: LGPLv3+
Group: System/Libraries
Url: http://talloc.samba.org/

Source: http://samba.org/ftp/talloc/talloc-%version.tar.gz
Patch1: talloc-fix-tests.patch

BuildRequires: docbook-dtds docbook-style-xsl libacl-devel libcap-devel python-devel xsltproc

BuildRequires(pre):rpm-build-ubt

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
Header files needed to develop programs that link against the Talloc
library.

%prep
%setup -q -n talloc-%version
%patch1 -p2

%build
%undefine _configure_gettext
%configure	--disable-rpath \
		--disable-rpath-install \
		--bundled-libraries=NONE \
		--builtin-libraries=replace \
		--disable-silent-rules
%make_build

%install
%makeinstall_std

rm -f %buildroot%_libdir/*.a
rm -f %buildroot%_datadir/swig/*/talloc.i

%if_enabled tests
%check
export LD_LIBRARY_PATH=./bin/shared:$LD_LIBRARY_PATH
make test
%endif

%files
%_libdir/libtalloc.so.*

%files devel
%_includedir/talloc.h
%_libdir/libtalloc.so
%_pkgconfigdir/talloc.pc
%_man3dir/talloc.3.*

%files -n libpytalloc
%_libdir/libpytalloc-util.so.*
%python_sitelibdir/talloc.so

%files -n libpytalloc-devel
%_includedir/pytalloc.h
%_pkgconfigdir/pytalloc-util.pc
%_libdir/libpytalloc-util.so


%changelog
* Thu Aug 17 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1:2.1.10-alt1%ubt
- Update to release for samba-4.7.0 with tevent-0.9.33

* Sat Jul 15 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1:2.1.9-alt2%ubt
- Rebuild with universal build tag (aka ubt macros) for p7 and c7

* Tue Mar 07 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1:2.1.9-alt1%ubt
- Update to release for samba-4.6.0

* Thu Sep 08 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1:2.1.8-alt1
- 2.1.8

* Mon Mar 14 2016 Andrey Cherepanov <cas@altlinux.org> 1:2.1.6-alt2
- Build 2.1.6

* Sun Mar 13 2016 Andrey Cherepanov <cas@altlinux.org> 1:2.1.5-alt2
- Downgrade to 2.1.5

* Wed Mar 09 2016 Andrey Cherepanov <cas@altlinux.org> 2.1.6-alt1
- 2.1.6

* Fri Nov 13 2015 Andrey Cherepanov <cas@altlinux.org> 2.1.5-alt1
- 2.1.5
- Enable tests

* Fri Oct 23 2015 Alexey Shabalin <shaba@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Tue Aug 18 2015 Alexey Shabalin <shaba@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Mon Mar 23 2015 Alexey Shabalin <shaba@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Wed Jun 04 2014 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Mon Dec 16 2013 Alexey Shabalin <shaba@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Fri Dec 21 2012 Alexey Shabalin <shaba@altlinux.ru> 2.0.8-alt1
- 2.0.8

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
