Name: openjade
Version: 1.3.2
Release: alt12

%def_disable static
%def_enable http

%define sgmlbase %_datadir/sgml
%define sgmlconfdir %_sysconfdir/sgml

Summary: DSSSL processor
Group: Publishing
License: BSD
URL: http://openjade.sourceforge.net/

%define sp_ver 1.5.2

PreReq: docbook-dtds
Requires: sgml-common >= 0.2
Requires(post,postun,triggerun): sgml-common >= 0.2
Requires: libOpenSP >= %sp_ver

Provides: jade = %version
Obsoletes: jade
Provides: libopenjade
Obsoletes: libopenjade

Source0: http://download.sourceforge.net/openjade/%name-%version.tar.bz2
Patch0: %name-1.3.1-manlink.patch
Patch1: %name-1.3.2-libosp-without-lt.patch
# Fedora patches
Patch2: %name-1.3.1-nsl.patch
Patch3: %name-deplibs.patch
# from fedora
Patch4: openjade-1.3.2-gcc46.patch

BuildRequires: gcc-c++ libOpenSP-devel >= %sp_ver perl-Perl4-CoreLibs chrpath

%description
OpenJade is an implementation of the ISO/IEC 10179:1996 standard DSSSL
(Document Style Semantics and Specification Language).  OpenJade is
based on James Clark's Jade implementation of DSSSL.  OpenJade is a
commmand-line application and a set of components.  The DSSSL engine
inputs an SGML or XML document and can output a variety of formats:
XML, RTF, TeX, MIF (FrameMaker), SGML, or XML.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cp config/configure.in ./
%configure \
    --disable-static \
    --datadir=%sgmlbase/%name-%version \
    --enable-spincludedir=%_includedir/OpenSP \
    --enable-splibdir=%_libdir \
    --enable-default-catalog=%sgmlconfdir/catalog \
    --enable-default-search-path=%sgmlbase \
    %{subst_enable http}
%make_build

%install
%makeinstall datadir=$RPM_BUILD_ROOT%sgmlbase/%name-%version
%make install-man mandir=$RPM_BUILD_ROOT%_mandir

install -m644 dsssl/catalog $RPM_BUILD_ROOT%sgmlbase/%name-%version/
install -m644 dsssl/*.dtd $RPM_BUILD_ROOT%sgmlbase/%name-%version/
install -m644 dsssl/extensions.dsl $RPM_BUILD_ROOT%sgmlbase/%name-%version/

mkdir -p $RPM_BUILD_ROOT%sgmlconfdir
install -m644 /dev/null $RPM_BUILD_ROOT%sgmlconfdir/dsssl-%version.cat

# oMy, othis ois osilly.
ln -s openjade $RPM_BUILD_ROOT%_bindir/jade
echo ".so man1/openjade.1" > $RPM_BUILD_ROOT%_man1dir/jade.1

#for compatibility with alternatives
ln -s dsssl-%version.cat $RPM_BUILD_ROOT%sgmlconfdir/dsssl.cat

# remove RPATHs
chrpath --delete %buildroot%_libdir/libo{spgrove,style}.so.* \
		%buildroot%_bindir/%name

%post
%_bindir/install-catalog --add \
    %sgmlconfdir/dsssl-%version.cat \
    %sgmlbase/%name-%version/catalog >/dev/null 2>&1

/bin/find %sgmlconfdir -type f \
	\( -name 'sgml-docbook-*.cat' -o -name 'xml-docbook-*.cat' \) -print |
    while read -r catalog; do
	%_bindir/install-catalog --add "$catalog" \
	    %sgmlbase/%name-%version/catalog >/dev/null 2>&1
    done

%postun
if [ "$1" = 0 -o ! -f %sgmlbase/%name-%version/catalog ]; then
    /bin/find %sgmlconfdir -type f \
	 \( -name 'sgml-docbook-*.cat' -o -name 'xml-docbook-*.cat' \) -print |
	while read -r catalog; do
	    %_bindir/install-catalog --remove "$catalog" \
		%sgmlbase/%name-%version/catalog >/dev/null 2>&1
	done
fi
if [ "$1" != 0 -a ! -f %sgmlbase/%name-%version/catalog ]; then
    %_bindir/install-catalog --remove \
        %sgmlconfdir/dsssl-%version.cat \
        %sgmlbase/%name-%version/catalog >/dev/null 2>&1
fi

%triggerun -- openjade < 1.3.2-alt2
OJCATALOGS=$(echo %sgmlbase/%name-*/catalog)
[ "$OJCATALOGS" = '%sgmlbase/%name-*/catalog' ] ||
/bin/find %sgmlconfdir -type f \
	\( -name 'sgml-docbook-*.cat' -o -name 'xml-docbook-*.cat' \) -print |
    while read -r catalog; do
	for ojcatalog in $OJCATALOGS; do
	    [ "$ojcatalog" = %sgmlbase/%name-%version/catalog ] ||
	    %_bindir/install-catalog --remove "$catalog" \
		$ojcatalog >/dev/null 2>&1
	done
    done

%files
%doc README COPYING NEWS releasenotes.html ChangeLog
%doc dsssl/demo.*
%doc jadedoc/* contrib
%_bindir/*
%_libdir/*.so.*
%sgmlbase/%name-%version
%_man1dir/*
%ghost %sgmlconfdir/dsssl-%version.cat
%sgmlconfdir/dsssl.cat

%exclude %_libdir/libogrove.so
%exclude %_libdir/libospgrove.so
%exclude %_libdir/libostyle.so

%changelog
* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt12
- fixed RPATH

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt11
- updated buildreqs
- prepared for gcc-4.6 (patch from fedora)

* Tue Dec 16 2008 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt10
- removed obsolete %%post{,un}_ldconfig
- %%exclude for non-packaged files

* Tue Sep 16 2008 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt9
- Fixed build, tnks Fedora for patches (2,3)

* Sat Jun 03 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.2-alt8
- Rebuilt with OpenSP 1.5.2

* Sun Apr 09 2006 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.2-alt7
- Patch2: correct library linkage to withstand ld --as-needed
- Patch3: use g++ for linking

* Mon Jan 17 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.2-alt6
- Abolished the libopenjade package
- Run autoconf to recognize new architectures like pentium4

* Tue Jun 15 2004 Stanislav Ievlev <inger@altlinux.org> 1.3.2-alt5.1
- NMU: remove alternatives support, and use symlink instead,
  'cause we have only one candidate for this alternative

* Sun Jan 18 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.2-alt5
- Provide jade with version
- HTTP is made optional

* Thu Dec 18 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.2-alt4
- Build without libosp.la installed in the system [Patch1]

* Fri Dec 12 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.2-alt3
- Streamlined install scripts
- PreReq docbook-dtds
- Split requires for sgml-common
- Admitted dsssl-%version.cat into the filelist as %%config(noreplace)

* Fri Oct 17 2003 Dmitry V. Levin <ldv@altlinux.org> 1.3.2-alt2
- Requires(post,preun): %_sbindir/update-alternatives.

* Sun Mar 30 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.2-alt1
- New version
- OpenSP is now separate
- Classified the license as BSD (correct me if I'm wrong)
- Abolished -devel and -devel-static because no headers are installed
  officially. libOpenSP-devel now provides support for OpenSP libraries.

* Mon Nov 18 2002 AEN <aen@altlinux.ru> 1.3.1-alt3
- rebuilt with gcc-3.2

* Wed Mar 27 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.1-alt2
- Moved extensions.dsl from the doc list to the main dir,
  excluded blanket dsssl/ from the doc list, of there left only
  README.jadetex and demo.*

* Sun Mar 10 2002 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.1-alt1
- 1.3.1
- Spec cleanup
- Sync with RedHat openjade-1.3.1-2
- libification
- bedevelment
- Shutup install-catalog and make it always happy
- update-alternatives instead of symlink hackwork
- Patched symlink for sgmlnorm(1)
- BuildRequires

* Tue Jan 23 2001 AEN <aen@logic.ru>
- %files fixed
- cleanup spec

* Sun Dec 10 2000 Peter 'Nidd' Novodvorsky <petya@logic.ru> ipl1mdk
- changed from 10mdk to ipl10mdk. Now IPLabs Linux Team supports this
Package.

* Mon Nov 27 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3-10mdk
- Don't compile with optimisations.

* Wed Nov 08 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3-9mdk
- RH patch merge.
- Compile with gcc2.96.

* Sun Sep 03 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.3-8mdk
- Rebuilt as jade is not finding the new version of docbook-style-dsssl it is
  still looking for the old one.

* Mon Aug 28 2000 Camille Begnis <camille@mandrakesoft.com> 1.3-7mdk
- relocate builtins.dsl

* Thu Aug 24 2000 Camille Begnis <camille@mandrakesoft.com> 1.3-6mdk
- Requires: sgml-common >= 0.2

* Wed Aug 23 2000 Camille Begnis <camille@mandrakesoft.com> 1.3-5mdk
- Pre-LSB compliance

* Mon Jul 03 2000 Camille Begnis <camille@mandrakesoft.com> 1.3-4mdk
- Add %post -p ldconfig and %postun -p ldconfig

* Fri Jun 30 2000 Camille Begnis <camille@mandrakesoft.com> 1.3-3mdk
- recompile with newer libstdc++

* Tue Jun 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3-2mdk
- User makeinstall macros.

* Tue May 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3-1mdk
- Set -fexecpltions to CFLAGS when compiling on ia32.
- Rename package to openjade (add Provides: Obsoletes: jade).
- compile with egcs.
- Clean up specs.

* Tue Mar 21 2000 Camille Begnis <camille@mandrakesoft.com> 1.2.1-9mdk
- major spec update
- remove sources from rpm
- fixed doc

* Sun Dec 19 1999 John Buswell <johnb@mandrakesoft.com>
- Fixed docs

* Tue Dec 14 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix build with gcc2.95.

* Sun Nov 07 1999 John Buswell <johnb@mandrakesoft.com>
- Added Url and updated source url
- Build Release

* Tue Jul 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- bzip2 source

* Thu Jul 08 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- First version with the help of author.
