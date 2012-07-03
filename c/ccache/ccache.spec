Name: ccache
Version: 3.0.1
Release: alt1

Summary: Compiler cache
License: GPLv3+
Group: Development/Tools
Url: http://ccache.samba.org/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Packager: Andrey Rahmatullin <wrar@altlinux.org>

Provides: ccache3 = %version-%release
Obsoletes: ccache3

BuildPreReq: asciidoc-a2x zlib-devel

%description
ccache is a compiler cache. It acts as a caching pre-processor to
C/C++ compilers, using the -E compiler switch and a hash to detect
when a compilation can be satisfied from cache. This often results in
a 5 to 10 times speedup in common compilations.

%prep
%setup
%patch -p1
rm -rfv zlib/
%autoreconf

%build
%configure --enable-dev
%make_build all docs

%install
%makeinstall

mkdir -p %buildroot%_sysconfdir/buildreqs/packages/ignore.d
cat > %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name << EOF
%name
EOF

%files
%doc *.txt *.html
%_mandir/man1/ccache.1*
%_bindir/ccache
%_sysconfdir/buildreqs/packages/ignore.d/*

%changelog
* Sat Jul 17 2010 Andrey Rahmatullin <wrar@altlinux.org> 3.0.1-alt1
- 3.0.1

* Mon Jun 21 2010 Andrey Rahmatullin <wrar@altlinux.ru> 3.0-alt2
- 3.0
- rename back to ccache
- remove obsoletes/provides for ccache-bte

* Fri May 14 2010 Andrey Rahmatullin <wrar@altlinux.ru> 3.0-alt1.pre1
- 3.0pre1

* Wed Mar 31 2010 Andrey Rahmatullin <wrar@altlinux.ru> 3.0-alt1.pre0
- package 3.0pre0 as ccache3

* Mon Sep 08 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.4-alt3
- add Debian patches:
  + respect LDFLAGS when linking
  + use utimes(2) instead of utime(2) when possible
  + zlib compression of cache, enabled by default
  + --long-options
  + don't cache compilations with profiling on
  + fix dependencies when using -o
  + fix hyphens in the manpage
  + add CACHEDIR.TAG support
  + improve LRU-based cache cleanup
  + don't try to use caching when HOME is unset
  + check for errors when setting cache limits
  + behave more reliably when the cache is on NFS
- spec fixes

* Tue Oct 04 2005 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt2
- fix bug #2910

* Sun Nov 07 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt1
- new version

* Fri Jul 23 2004 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt1
- new version
- patch adopted

* Wed Oct 22 2003 Alexey Tourbin <at@altlinux.ru> 1.9-alt3.3
- fixed segfault in env-alt.patch (introduced by ab in 1.9-alt3)

* Thu Oct 16 2003 Stanislav Ievlev <inger@altlinux.ru> 1.9-alt3.2
- removed bte subpackage: ccache now supported by gcc_wrapper

* Mon Jan 06 2003 Alexander Bokovoy <ab@altlinux.ru> 1.9-alt3.1
- Fix dependency loop for post-install and pre-uninstall scriptlets

* Sun Nov 24 2002 Alexander Bokovoy <ab@altlinux.ru> 1.9-alt3
- Update CC/CXX environment patch to better fit BTE

* Wed Oct 23 2002 Alexander Bokovoy <ab@altlinux.ru> 1.9-alt2
- Integrate BTE support

* Thu Oct 10 2002 Victor Forsyuk <force@altlinux.ru> 1.9-alt1
- Add ignore.d files for buildreq.

* Wed May 29 2002 Victor Forsyuk <force@altlinux.ru> 1.9-alt0.1
- Initial build for Sysiphus.
