%def_with lua_compat
Name: lua5.1
Version: 5.1.5
Release: alt8

Summary: Embeddable programming language
License: MIT
Group: Development/Other

URL: http://www.lua.org
Source: lua-%version.tar

Patch00: lua5.1-5.1.5-alt-at-ABI-compat.patch
Patch01: lua5.1-5.1.5-alt-at-ldo-abort.patch
Patch02: lua5.1-5.1.5-alt-at-luaconf.patch
Patch03: lua5.1-5.1.5-alt-at-luaconf-LUA_USE_LINUX.patch
Patch04: lua5.1-5.1.5-alt-at-restore-lua_version.patch
Patch05: lua5.1-5.1.5-alt-at-symbol-map.patch
Patch06: lua5.1-5.1.5-alt-doc.patch
Patch07: lua5.1-5.1.5-alt-pkgconfig.patch
Patch08: lua5.1-5.1.5-alt-safe-stack.patch
Patch09: lua5.1-5.1.5-lua.org-bugs-5.1.5-1.patch
Patch10: lua5.1-5.1.5-lua.org-bugs-5.1.5-2.patch
Patch11: lua5.1-5.1.5-alt-vseleznv-gcc6.patch
Patch12: lua-5.1.4-idsize.patch
Patch13: lua-5.1.4-lunatic.patch

Requires: lib%{name} = %EVR
Provides: lua = %version
Provides: lua5 = %version-%release
Obsoletes: lua5 <= 5.1.5-alt2
Conflicts: lua4

# Automatically added by buildreq on Mon Sep 28 2009
BuildRequires: libreadline-devel

%package -n lib%{name}
Summary: Embeddable programming language
Group: System/Libraries
# for smooth upgrade against lua5.1-alt-compat
Provides: %_libdir/lua/5.1
Provides: %_datadir/lua/5.1
Requires: lib%{name}-preinstall = %EVR
Requires(pre): lib%{name}-preinstall = %EVR
Conflicts: lua5.1-alt-compat = 1.0-alt1

%package -n lib%{name}-devel
Summary: Embeddable programming language
Group: Development/Other
Provides: %{name}-devel = %EVR
Requires: lib%{name} = %EVR
Conflicts: liblua4-devel

%package -n lib%{name}-devel-static
Summary: Embeddable programming language
Group: Development/Other
Provides: liblua5-devel-static = %version-%release
Requires: lib%{name}-devel = %EVR
Conflicts: liblua4-devel-static

%package -n lib%{name}-preinstall
Summary: preinstall package for lib%{name}
Group: Development/Other
Provides: lua5.1-alt-compat = %version
Conflicts: lua5.1-alt-compat = 1.0-alt1

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

%description -n lib%{name}
Lua is a powerful, light-weight programming language designed for extending
applications.  The language engine is accessible as a library, having a C
API which allows the application to exchange data with Lua programs and also
to extend Lua with C functions.  Lua is also used as a general-purpose,
stand-alone language through the simple command line interpreter provided.

%description -n lib%{name}-devel
Lua is a powerful, light-weight programming language designed for extending
applications.  The language engine is accessible as a library, having a C
API which allows the application to exchange data with Lua programs and also
to extend Lua with C functions.  Lua is also used as a general-purpose,
stand-alone language through the simple command line interpreter provided.

%description -n lib%{name}-devel-static
Lua is a powerful, light-weight programming language designed for extending
applications.  The language engine is accessible as a library, having a C
API which allows the application to exchange data with Lua programs and also
to extend Lua with C functions.  Lua is also used as a general-purpose,
stand-alone language through the simple command line interpreter provided.

%description -n lib%{name}-preinstall
virtual preinstall package for lib%{name} to resolve installation conflicts.

%description doc
Lua is a powerful, light-weight programming language designed for extending
applications.  The language engine is accessible as a library, having a C
API which allows the application to exchange data with Lua programs and also
to extend Lua with C functions.  Lua is also used as a general-purpose,
stand-alone language through the simple command line interpreter provided.

%prep
%setup -n lua-%version
%patch00 -p1
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch04 -p1
%patch05 -p1
%patch06 -p1
%patch07 -p1
%patch08 -p1
%patch09 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
%def_enable Werror

cd ./src
# from Makefile
core='lapi lcode ldebug ldo ldump lfunc lgc llex lmem lobject lopcodes lparser lstate lstring ltable ltm lundump lvm lzio'
lib='lauxlib lbaselib ldblib liolib lmathlib loslib ltablib lstrlib loadlib linit'

for f in $core $lib; do gcc %optflags -c $f.c; done
ar rcu liblua-5.1.a *.o
ranlib liblua-5.1.a

%define soffix -5.1.so.0
for f in $core $lib; do gcc %optflags %optflags_shared -c $f.c; done
gcc -shared -o liblua%soffix -Wl,-soname=liblua%soffix -Wl,--version-script=liblua.map -Wl,-z,defs *.o -lm -ldl

gcc -o lua %optflags lua.c ./liblua%soffix -lreadline
gcc -o luac %optflags luac.c print.c ./liblua%soffix

LD_LIBRARY_PATH=$PWD ./lua ../test/hello.lua 

%install
%define pkgdocdir %_docdir/lua-5.1
mkdir -p %buildroot{%_libdir,%_bindir,%_includedir/lua-5.1,%_man1dir,%pkgdocdir/html}

cd ./src
cp -p liblua-5.1.a liblua%soffix %buildroot%_libdir/
ln -s liblua%soffix %buildroot%_libdir/liblua-5.1.so
ln -s liblua%soffix %buildroot%_libdir/liblua5.1.so
cp -p lua %buildroot%_bindir/lua-5.1
cp -p luac %buildroot%_bindir/luac-5.1
ln -s lua-5.1 %buildroot%_bindir/lua5.1
ln -s luac-5.1 %buildroot%_bindir/luac5.1
cp -p lua.h luaconf.h lualib.h lauxlib.h ../etc/lua.hpp %buildroot%_includedir/lua-5.1
ln -s lua-5.1 %buildroot%_includedir/lua5.1
install -pD -m644 ../etc/lua.pc %buildroot%_pkgconfigdir/lua-5.1.pc
ln -s lua-5.1.pc %buildroot%_pkgconfigdir/lua5.1.pc

# Fix paths in lua-5.1.pc:
sed -i 's|/usr/lib|%_libdir|g;s|/usr/share|%_datadir|g;' %buildroot%_pkgconfigdir/lua-5.1.pc

%if_with lua_compat
# compat symlinks that conflicts with other lua's -devels
ln -s liblua-5.1.so %buildroot%_libdir/liblua.so
ln -s lua-5.1.pc %buildroot%_pkgconfigdir/lua.pc
pushd %buildroot%_includedir/lua-5.1
for i in *.*; do
    ln -s lua-5.1/$i %buildroot%_includedir/$i
done
popd
%endif

cd ..
cp -av COPYRIGHT HISTORY README etc test %buildroot%pkgdocdir/
cd ./doc
cp -p lua.1 %buildroot%_man1dir/lua5.1.1
cp -p luac.1 %buildroot%_man1dir/luac5.1.1
cp -p *.html *.css *.gif *.png %buildroot%pkgdocdir/html/
mv %buildroot%pkgdocdir/html/{readme,index}.html

mkdir -p %buildroot{%_libdir,%_datadir}/lua/5.1

%pre -n lib%{name}
# ----------- begin update from old lua5 to lua5.1 ----
if [ -L %_libdir/lua/5.1 ]; then
    echo "removing lua5.1-alt-compat symlink..."
    rm -f %_libdir/lua/5.1
    if [ -d %_libdir/lua5 ] && [ ! -e %_libdir/lua/5.1 ]; then
	mkdir -p %_libdir/lua
	mv %_libdir/lua5 %_libdir/lua/5.1
    fi
fi
# ----------- end update from old lua5 to lua5.1 ----

%files
%_bindir/lua*
%_man1dir/lua*

%files -n lib%{name}
%_libdir/liblua%soffix
%dir %_libdir/lua
%dir %_datadir/lua
%dir %_libdir/lua/5.1
%dir %_datadir/lua/5.1
%dir %pkgdocdir
%pkgdocdir/COPYRIGHT
%pkgdocdir/HISTORY
%pkgdocdir/README

%files -n lib%{name}-devel
%_includedir/lua-5.1
%_includedir/lua5.1
%_libdir/liblua*5.1.so
%_pkgconfigdir/lua*5.1.pc
%if_with lua_compat
%_libdir/liblua.so
%_pkgconfigdir/lua.pc
%_includedir/*.h
%_includedir/*.hpp
%endif

%files -n lib%{name}-devel-static
%_libdir/liblua-5.1.a

%files -n lib%{name}-preinstall

%files doc
%dir %pkgdocdir
%pkgdocdir/html
%pkgdocdir/etc
%pkgdocdir/test

%changelog
* Sat Feb 11 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.5-alt8
- added Requires: on preinstall subpackage
- upgrade script made more forceful (should help #33104)
					    
* Fri Feb 10 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.5-alt7
- added %_includedir/lua5.1 (seen in boswars, for better compatibility)

* Thu Feb 09 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.5-alt6
- added lua5.1.pc and liblua5.1.so as packages expect them
- added if_with lua_compat to group conflicting files

* Thu Feb 09 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.5-alt5
- added preinstall subpackage to help apt dist-upgrade.

* Wed Feb 08 2017 Igor Vlasenko <viy@altlinux.ru> 5.1.5-alt4
- restored luaconf.h LUA_CDIR / LUA_LDIR defaults
- split cummulative diff into separate patches
- added lua-5.1.4-idsize.patch (fc)
- added lua-5.1.4-lunatic.patch (fc)
- returned LUA_CDIR and LUA_LDIR definitions to luaconf.h

* Wed Feb 08 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.1.5-alt3
- added lua-5.1.pc, liblua-5.1.so and related files (thx Igor Vlasenko).
- removed liblua5-devel provides to avoid clash with liblua5.3-devel (thx Igor
  Vlasenko).
- renamed lua5 package to lua5.1.
- added %%pre for 5->5.1 upgrade (thx Igor Vlasenko).
- added symlinks for fedora (thx Igor Vlasenko).
- removed %%_bindir/lua %%_bindir/luac %%_man1dir/lua.1*
  %%_man1dir/luac.1*.
- reverted LUA_LDIR and LUA_CDIR in luaconf.h and paths in lua.pc.
- fixed build with gcc6.

* Tue Dec 20 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 5.1.5-alt2
- renamed liblua5-devel package to liblua5.1-devel
- renamed liblua5-devel-static package to liblua5.1-devel-static

* Sun Sep  7 2014 Terechkov Evgenii <evg@altlinux.org> 5.1.5-alt1
- Patch for CVE-2014-5461 applied
- 5.1.4 -> 5.1.5
- lua-5.1.4 patches reverted
- applied official pathes #1/#2 from lua.org/bugs.html

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
