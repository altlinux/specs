Name: lua5
Version: 5.1.4
Release: alt5

Summary: Embeddable programming language
License: MIT
Group: Development/Other

URL: http://www.lua.org
Source: lua-%version.tar
Patch: %name-%version-%release.patch

Requires: liblua5.1 = %version-%release
Provides: lua = %version
Conflicts: lua4

# Automatically added by buildreq on Mon Sep 28 2009
BuildRequires: libreadline-devel

%package -n liblua5.1
Summary: Embeddable programming language
Group: System/Libraries
Provides: %_libdir/lua5
Provides: %_datadir/lua5

%package -n liblua5-devel
Summary: Embeddable programming language
Group: Development/Other
Requires: liblua5.1 = %version-%release
Conflicts: liblua4-devel

%package -n liblua5-devel-static
Summary: Embeddable programming language
Group: Development/Other
Requires: liblua5-devel = %version-%release
Conflicts: liblua4-devel-static

%package doc
Summary: Embeddable programming language
Group: Development/Documentation
Conflicts: lua5 < 5.1.1-alt2
BuildArch: noarch

%description
Lua is a powerful, light-weight programming language designed for extending
applications.  The language engine is accessible as a library, having a C
API which allows the application to exchange data with Lua programs and also
to extend Lua with C functions.  Lua is also used as a general-purpose,
stand-alone language through the simple command line interpreter provided.

%description -n liblua5.1
Lua is a powerful, light-weight programming language designed for extending
applications.  The language engine is accessible as a library, having a C
API which allows the application to exchange data with Lua programs and also
to extend Lua with C functions.  Lua is also used as a general-purpose,
stand-alone language through the simple command line interpreter provided.

%description -n liblua5-devel
Lua is a powerful, light-weight programming language designed for extending
applications.  The language engine is accessible as a library, having a C
API which allows the application to exchange data with Lua programs and also
to extend Lua with C functions.  Lua is also used as a general-purpose,
stand-alone language through the simple command line interpreter provided.

%description -n liblua5-devel-static
Lua is a powerful, light-weight programming language designed for extending
applications.  The language engine is accessible as a library, having a C
API which allows the application to exchange data with Lua programs and also
to extend Lua with C functions.  Lua is also used as a general-purpose,
stand-alone language through the simple command line interpreter provided.

%description doc
Lua is a powerful, light-weight programming language designed for extending
applications.  The language engine is accessible as a library, having a C
API which allows the application to exchange data with Lua programs and also
to extend Lua with C functions.  Lua is also used as a general-purpose,
stand-alone language through the simple command line interpreter provided.

%prep
%setup -n lua-%version
%patch -p1

%build
%def_enable Werror

cd ./src
# from Makefile
core='lapi lcode ldebug ldo ldump lfunc lgc llex lmem lobject lopcodes lparser lstate lstring ltable ltm lundump lvm lzio'
lib='lauxlib lbaselib ldblib liolib lmathlib loslib ltablib lstrlib loadlib linit'

for f in $core $lib; do gcc %optflags -c $f.c; done
ar rcu liblua.a *.o
ranlib liblua.a

%define soffix -5.1.so.0
for f in $core $lib; do gcc %optflags %optflags_shared -c $f.c; done
gcc -shared -o liblua%soffix -Wl,-soname=liblua%soffix -Wl,--version-script=liblua.map -Wl,-z,defs *.o -lm -ldl

gcc -o lua %optflags lua.c ./liblua%soffix -lreadline
gcc -o luac %optflags luac.c print.c ./liblua%soffix

LD_LIBRARY_PATH=$PWD ./lua ../test/hello.lua 

%install
%define pkgdocdir %_docdir/lua-5.1
mkdir -p %buildroot{%_libdir,%_bindir,%_includedir,%_man1dir,%pkgdocdir/html}

cd ./src
cp -p liblua.a liblua%soffix %buildroot%_libdir/
ln -s liblua%soffix %buildroot%_libdir/liblua.so
cp -p lua %buildroot%_bindir/lua5.1
cp -p luac %buildroot%_bindir/luac5.1
ln -s lua5.1 %buildroot%_bindir/lua
ln -s luac5.1 %buildroot%_bindir/luac
cp -p lua.h luaconf.h lualib.h lauxlib.h ../etc/lua.hpp %buildroot%_includedir/
install -pD -m644 ../etc/lua.pc %buildroot%_pkgconfigdir/lua.pc

# Fix paths in lua.pc:
sed -i 's|/usr/lib|%_libdir|g;s|/usr/share|%_datadir|g' %buildroot%_pkgconfigdir/lua.pc

cd ..
cp -av COPYRIGHT HISTORY README etc test %buildroot%pkgdocdir/
cd ./doc
cp -p lua.1 %buildroot%_man1dir/lua5.1.1
cp -p luac.1 %buildroot%_man1dir/luac5.1.1
ln -s lua5.1.1 %buildroot%_man1dir/lua.1
ln -s luac5.1.1 %buildroot%_man1dir/luac.1
cp -p *.html *.css *.gif *.png %buildroot%pkgdocdir/html/
mv %buildroot%pkgdocdir/html/{readme,index}.html

mkdir -p %buildroot{%_libdir,%_datadir}/lua5

%files
%_bindir/lua*
%_man1dir/lua*

%files -n liblua5.1
%_libdir/liblua%soffix
%dir %_libdir/lua5
%dir %_datadir/lua5
%dir %pkgdocdir
%pkgdocdir/COPYRIGHT
%pkgdocdir/HISTORY
%pkgdocdir/README

%files -n liblua5-devel
%_includedir/*.*
%_libdir/liblua.so
%_pkgconfigdir/lua.pc

%files -n liblua5-devel-static
%_libdir/liblua.a

%files doc
%dir %pkgdocdir
%pkgdocdir/html
%pkgdocdir/etc
%pkgdocdir/test

%changelog
* Tue May  3 2011 Terechkov Evgenii <evg@altlinux.org> 5.1.4-alt5
- Add more info in lua.pc (ALT#25368)

* Sat Feb 26 2011 Dmitry V. Levin <ldv@altlinux.org> 5.1.4-alt4
- Rebuilt for debuginfo.

* Thu Nov 04 2010 Dmitry V. Levin <ldv@altlinux.org> 5.1.4-alt3
- Applied official patches #7 and #8 from lua.org/bugs.html (by at@).

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 5.1.4-alt2
- applied official patch #6 from lua.org/bugs.html

* Mon Sep 28 2009 Alexey Tourbin <at@altlinux.ru> 5.1.4-alt1
- 5.1.3 -> 5.1.4
- applied 3 official patches from lua.org/bugs.html
- reverted lua-5.0 compatibility hacks
- disabled APICHECK to workaround assertion failures (#18557)

* Tue Jun 24 2008 Alexey Tourbin <at@altlinux.ru> 5.1.3-alt2.1
- spec: removed "BuildArch: %%_target_cpu"

* Sun Jun 22 2008 Alexey Tourbin <at@altlinux.ru> 5.1.3-alt2
- http://www.lua.org/ftp/patch-lua-5.1.3 (20080508)
- made lua5-doc package noarch

* Sat Mar 01 2008 Alexey Tourbin <at@altlinux.ru> 5.1.3-alt1
- 5.1.2 -> 5.1.3

* Wed Oct 24 2007 Alexey Tourbin <at@altlinux.ru> 5.1.2-alt4
- luaconf.h (lua_popen): call fflush(NULL) before popen()
- applied 1 more official patch from lua.org/bugs.html:
  + An error in a module loaded through the '-l' option shows no traceback.

* Sun Aug 12 2007 Alexey Tourbin <at@altlinux.ru> 5.1.2-alt3
- applied 2 more official patches from lua.org/bugs.html:
  + Very small numbers all collide in the hash function.
  + Too many variables in an assignment may cause a C stack overflow.
- changed src.rpm packaging to keep unmodified upstream tarball

* Sun Jun 17 2007 Alexey Tourbin <at@altlinux.ru> 5.1.2-alt2
- applied official patches from lua.org/bugs.html:
  + Code generated for "-nil", "-true", and "-false" is wrong.
  + Count hook may be called without being set.
  + Wrong error message in some concatenations.
- ldo.c (luaD_throw): abort() instead of exit(EXIT_FAILURE)
- relaxed lua5-doc dependencies

* Wed Apr 04 2007 Alexey Tourbin <at@altlinux.ru> 5.1.2-alt1
- updated to 5.1.2
- installed %_pkgconfigdir/lua.pc

* Mon Mar 19 2007 Alexey Tourbin <at@altlinux.ru> 5.1.1-alt3
- applied 3 more official patches from lua.org/bugs.html
- in the COPYRIGHT file, added notice about readline/GPL

* Sat Oct 14 2006 Alexey Tourbin <at@altlinux.ru> 5.1.1-alt2
- imported sources into git and built with gear
- applied 3 official patches from lua.org/bugs.html
- added version script for the shared library to avoid static luac linkage
- split html documentation and examples into separate lua5-doc subpackage

* Mon Jun 12 2006 Alexey Tourbin <at@altlinux.ru> 5.1.1-alt1
- 5.1 -> 5.1.1

* Tue May 16 2006 Alexey Tourbin <at@altlinux.ru> 5.1-alt1
- 5.0.2 -> 5.1
- changed soname to liblua-5.1.so.0
- applied fixes for known bugs from lua.org
- removed alternatives, lua4 goes obsolete

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 5.0.2-alt5.1
- Rebuilt with libreadline.so.5.

* Wed Jun 29 2005 Alexey Tourbin <at@altlinux.ru> 5.0.2-alt5
- fixed segfaults introduced in previous release (type casts)
- fixed linkage (linked liblualib.so with liblua.so)

* Sat Jun 11 2005 Alexey Tourbin <at@altlinux.ru> 5.0.2-alt4
- compat-5.1r2 -> compat-5.1r3
- in sync with Debian: lua50_5.0.2-5.diff.gz
- fixed invalid type casts on x86_64 (Kachalov Anton, #6539)

* Mon May 09 2005 Alexey Tourbin <at@altlinux.ru> 5.0.2-alt3
- packaged Compat-5.1 (implementation of Lua-5.1 package proposal)
- applied 3 official patches from http://www.lua.org/bugs.html
- removed old dependencies

* Sat Sep 18 2004 Alexey Tourbin <at@altlinux.ru> 5.0.2-alt2
- %_datadir/lua5/loadlib.lua -- implemented require()-like path search
  for loadlib(); compiled extensions should reside in %_libdir/lua5
- added %_datadir/lua5 to default LUA_PATH
- enabled os.tmpname()
- upgraded to new alternatives format

* Fri Mar 19 2004 Alexey Tourbin <at@altlinux.ru> 5.0.2-alt1
- updated to 5.0.2 release
- enabled partial compatibility with old upvalue syntax
- pedro-openbsd-snprintf.patch: use snprintf(3) instead of sprintf(3)

* Sun Mar 07 2004 Alexey Tourbin <at@altlinux.ru> 5.0.2-alt0.1
- updated to 5.0.2 pre-release, with all official patches in

* Mon Feb 23 2004 Alexey Tourbin <at@altlinux.ru> 5.0-alt7.2
- %_docdir/lua5-%version -> %_docdir/lua-%version
- fixed luac symilnk (alternatives)

* Mon Feb 02 2004 Alexey Tourbin <at@altlinux.ru> 5.0-alt7.1
- fixed %_docdir/lua5-%version ownership

* Fri Jan 30 2004 Alexey Tourbin <at@altlinux.ru> 5.0-alt7
- fixed _customdocdir misusage
- Werror mode enabled

* Tue Nov 18 2003 Alexey Tourbin <at@altlinux.ru> 5.0-alt6
- 5 more official patches applied

* Sun Aug 24 2003 Alexey Tourbin <at@altlinux.ru> 5.0-alt5
- moved lua4 (weight=10) and lua5 (weight=20) packages under alternatives control
- in sync with debian (deb-paths.patch):
  + Added support for -C to load compatibility library on startup
  + Added an initial LUA_PATH to support /usr/share/lua5 etc.
  + Added a -P switch to suppress the LUA_PATH code if need-be
  + Updated the manpage lua.1 for the -C and -P switches

* Fri Jun 20 2003 Alexey Tourbin <at@altlinux.ru> 5.0-alt4
- packages renamed: s/lua/lua5/
- lua4 will be kept; thus Provides/Obsoletes reconsidered, Conflicts added
- two patches from http://www.lua.org/bugs.html
- Sisyphus release

* Wed May 07 2003 Alexey Tourbin <at@altlinux.ru> 5.0-alt3
- added Provides and Obsoletes for smooth upgrade

* Mon May 05 2003 Alexey Tourbin <at@altlinux.ru> 5.0-alt2
- desert Makefile/config/patches; custom build with direct commands
- features enabled: dlopen (loadlib), popen, fastround, libreadline
- new package layout: lua, liblua, liblua-devel, liblua-devel-static

* Mon Apr 28 2003 Alexey Tourbin <at@altlinux.ru> 5.0-alt1
- 5.0; API changes; soname changed; license: MIT
- loadlib now implemented, so drop that stuff borrowed from PLD

* Sun Jan 19 2003 Alexey Tourbin <at@altlinux.ru> 4.0.1-alt6
- minor enhancements

* Thu Dec 26 2002 Alexey Tourbin <at@altlinux.ru> 4.0.1-alt5
- corrected s/-lc/-lc -lm -ldl/ for liblualib.so in alt-soname patch
- shared optimization flags

* Tue Dec 24 2002 Alexey Tourbin <at@altlinux.ru> 4.0.1-alt4
- error in previous build: *.so files are binary copy of *.so.* files,
  not symlinks; fixed
- really shared build (s/ld -shared/ld -shared -lc/ in alt-soname patch)
- post and postun sections added (ldconfig)

* Fri Dec 20 2002 Alexey Tourbin <at@altlinux.ru> 4.0.1-alt3
- shared build; alt-soname patch; lua-devel-static subpackage
- reference manual and code samples included in lua-devel package
- additional features from XTG Systems (loadlib files) and
  PLD Team (pld-loadlib-require patch)
- buildreq applied (none)

* Mon Oct 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.0.1-alt2
- Rebuilt in new environment

* Wed Aug 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.0.1-alt1
- First build for Sisyphus
