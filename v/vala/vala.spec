# Vala is written in Vala itself. To solve bootstrap problem we pre-compile it to C
# and use those C sources during bootstrap phase. Next package rebuilds must be done
# without bootstrap define.
%def_with bootstrap
%define api_ver 0.16

Name: vala
Version: 0.16.0
Release: alt1
Group: Development/C
Summary: Vala is a programming language which makes GNOME programming easy
License: LGPL
Url: http://live.gnome.org/Vala
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %name-%version.tar
%if_with bootstrap
Patch: %name-%version-%release-pregenerated.patch
%endif
Patch1: %name-%version-%release-fixes.patch
PreReq: rpm-build-vala vapi-common
BuildRequires: flex glib2-devel libgio-devel xsltproc dbus-tools-gui gobject-introspection-devel
BuildPreReq: /proc rpm-build-vala
%if_without bootstrap
BuildRequires: vala
%endif

%description
Vala is a programming language that aims to bring modern programming language
features to GNOME developers without imposing any additional runtime requirements and
without using a different ABI compared to applications and libraries written in C.

Vala is designed to allow access to existing C libraries, especially GObject-based
libraries, without the need for runtime bindings. Each to be used library requires a Vala
API file at compile-time, containing the class and method declarations in Vala
syntax. Vala currently comes with experimental bindings for GLib and GTK+. It's planned to
provide generated bindings for the full GNOME Platform at a later stage.

%package -n vapi-common
Summary: Common empty package with dir for vapi files
Group: Development/Other
Provides: %_datadir/vala/vapi

%description -n vapi-common
Common empty package with dir for vapi files.

%package -n lib%name-devel
Summary: Development files for embedding Vala translator
Group: Development/C
Requires: %name = %version-%release

%description -n lib%name-devel
Vala is a programming language that aims to bring modern programming language
features to GNOME developers without imposing any additional runtime requirements and
without using a different ABI compared to applications and libraries written in C.

This package contains infrastructure files to embed Vala translator into your programs

%package doc
Summary: Documentation for Vala programming language
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description doc
Vala is a programming language that aims to bring modern programming language
features to GNOME developers without imposing any additional runtime requirements and
without using a different ABI compared to applications and libraries written in C.

This package contains Vala documentation for GNOME DevHelp.

%package tools
Summary: Tools for creating Vala API specifications and new projects
Group: Development/C
Requires: %name = %version-%release

%description tools
Vala is a programming language that aims to bring modern programming language
features to GNOME developers without imposing any additional runtime requirements and
without using a different ABI compared to applications and libraries written in C.

This packages contains additional tools to generate Vala projects and API specifications
for existing C and C++ libraries.

%prep
%setup -q
%patch1 -p1

# Automake now requires to have ChangeLog and m4, fake them
touch ChangeLog
mkdir -p m4

# version in .tarball-version file
echo "%version" > .tarball-version

# whether external bootstrapping is in use or not we always want to build
# a compiler with the compiler itself. So first compile an intermediate
# (bootstrapping) compiler in a separate directory

%if_with bootstrap
# create a copy of sources. it's not that neat but otherwise
# our bootstrapping patch would "taint" sources used for
# the final build

mkdir bootstrap-build
# copy everythig but bootstrap-build recursively to bootstrap-build
find ./ -mindepth 1 -maxdepth 1 \( -name 'bootstrap-*' -prune -o \
	-exec cp -pr {} bootstrap-build \; \)
cd bootstrap-build
# apply pregenerated patch
%patch0 -p1
cd ..
%else
# use the directory for the "off-source" build
mkdir bootstrap-build
%endif

%build

autoreconf -v --install

# build an intermediate version of the compiler
BSINSTALL=$(pwd)/bootstrap-install
mkdir "$BSINSTALL"

cd bootstrap-build

%if_with bootstrap
autoreconf -v --install
./configure --enable-vapigen --prefix="$BSINSTALL"

# Make stamps for pregenerated source code so that Vala build system would not run valac again
for i in vala codegen ccode gee ; do
    touch $i/$i.vala.stamp
done
touch vapigen/{vapigen,vapicheck}.vala.stamp
touch compiler/valac.vala.stamp
%else
../configure --enable-vapigen --prefix="$BSINSTALL"
%endif

%make
make install
cd ..

# now build a pristine variant of the compiler to be packaged
OLD_PATH="$PATH"
export PATH="$BSINSTALL/bin:$PATH"
%configure --enable-vapigen
# Delete stamps to force re-generation of C code with bootstrapped valac
find . -name '*.stamp' | xargs -r rm
%make
rm -rf bootstrap-build "$BSINSTALL"
export PATH="$OLD_PATH"

# Perform language environment tests
%check
%make check

%install
%make DESTDIR=%buildroot install
# own this directory for third-party *.vapi files
mkdir -p %buildroot%_datadir/vala/vapi

%files
%_bindir/valac
%_bindir/valac-%api_ver
%_bindir/vala
%_bindir/vala-%api_ver
%_libdir/libvala-%api_ver.so.*
%_man1dir/valac*
%dir %_datadir/vala-%api_ver
%dir %_datadir/vala-%api_ver/vapi
%_datadir/vala-%api_ver/vapi/*
%doc AUTHORS COPYING NEWS README THANKS

%files -n vapi-common
%dir %_datadir/vala
%dir %_datadir/vala/vapi

%files -n lib%name-devel
%_includedir/vala-%api_ver
%_pkgconfigdir/*.pc
%_libdir/*.so
%_datadir/aclocal/*.m4

%files doc
%_datadir/devhelp/books/%name-%api_ver

%files tools
%_bindir/vapigen
%_bindir/vapigen-%api_ver
%_bindir/vala-gen-introspect
%_bindir/vala-gen-introspect-%api_ver
%_bindir/vapicheck
%_bindir/vapicheck-%api_ver
%_datadir/pkgconfig/vapigen*.pc
%_datadir/vala/Makefile.vapigen
%_libdir/vala-%api_ver/gen-introspect-%api_ver
%_man1dir/vala-gen-introspect*
%_man1dir/vapigen*

%changelog
* Mon Mar 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Mar 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.2-alt2
- add vapi-common package

* Wed Feb 01 2012 Alexey Shabalin <shaba@altlinux.ru> 0.14.2-alt1
- 0.14.2

* Wed Dec 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.1-alt1
- 0.14.1

* Mon Oct 24 2011 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Fri Jun 03 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt2
- rebuild with rpm-build-vala
- own directory %%_datadir/vala/vapi for third-party *.vapi files

* Thu Jun 02 2011 Alexey Shabalin <shaba@altlinux.ru> 0.12.1-alt1
- 0.12.1
- replace vala0.12

* Wed Mar 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.4-alt1
- 0.10.4

* Tue Jan 25 2011 Alexey Shabalin <shaba@altlinux.ru> 0.10.3-alt1
- 0.10.3
- update buildreq

* Mon Oct 04 2010 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Wed Sep 08 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Wed Sep 08 2010 Alexey Shabalin <shaba@altlinux.ru> 0.9.1-alt1
- 0.9.1
- package doc as noarch

* Thu Apr 22 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Sun Mar 14 2010 Alexey Shabalin <shaba@altlinux.ru> 0.7.10-alt1
- new version

* Fri Jan 15 2010 Ildar Mulyukov <ildar@altlinux.ru> 0.7.9-alt1
- pull Alexey Morozov's changes to build process

* Wed Jan 06 2010 Alexey Morozov <morozov@altlinux.org> 0.7.9-alt0.2
- re-work build process, package the compiler built with the
  bootstrapping compiler of the same version

* Wed Jan 06 2010 Alexey Morozov <morozov@altlinux.org> 0.7.9-alt0.1
- new version

* Mon Dec 07 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.7.8_67_g3c53cbc-alt1
- most current GIT version

* Sun Dec 06 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.7.8-alt1
- new version

* Mon Oct 05 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.7.7-alt1
- new version

* Fri Sep 18 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.7.6-alt2
- get bootstrapping/pregenerated back (with new auto generation script)

* Fri Sep 18 2009 Ildar Mulyukov <ildar@altlinux.ru> 0.7.6-alt1
- 0.7.6
- new GEAR repo layout
- turn bootstrapping off (temporary)

* Mon Jun 29 2009 Alexander Bokovoy <ab@altlinux.org> 0.7.4-alt2
- 0.7.4
  + Final upstream 0.7.4

* Sat Jun 13 2009 Alexander Bokovoy <ab@altlinux.org> 0.7.4-alt1
- 0.7.4
  + merge upstream git after switching from svn
  + remove lua5.1.vapi as it is merged upstream already as lua.vapi

* Sun Jan 18 2009 Alexander Bokovoy <ab@altlinux.org> 0.5.7-alt1.r2389
- 0.5.7
  + post-release fixes

* Sun Jan 04 2009 Alexander Bokovoy <ab@altlinux.org> 0.5.4-alt3.r2262
- r2262

* Sat Dec 20 2008 Alexander Bokovoy <ab@altlinux.org> 0.5.4-alt2.r2232
- As vala-gen-project is now part of Vala Toys for gEdit, remove it from the package

* Sat Dec 20 2008 Alexander Bokovoy <ab@altlinux.org> 0.5.4-alt1.r2232
- 0.5.3
  + post-release r2232
  + owned/unowned keywords to mark passing ownership for method returns
    and getters. Syntax might evolve a bit in a future

* Tue Dec 02 2008 Alexander Bokovoy <ab@altlinux.org> 0.5.3-alt1.r2113
- 0.5.2
  + post-release r2113

* Sun Nov 16 2008 Alexander Bokovoy <ab@altlinux.org> 0.5.2-alt2.r2023
- Switch off bootstrap

* Sun Nov 16 2008 Alexander Bokovoy <ab@altlinux.org> 0.5.2-alt1.r2023
- Updated to r2023

* Sat Oct 25 2008 Alexander Bokovoy <ab@altlinux.org> 0.5.1-alt1.r1912
- Updated to r1912
    + Move to post-0.4.0
    + Use bootstrap again (0.4.0+ can't be built with 0.3.6 valac)

* Wed Oct 01 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.6-alt0.6
- Updated to r1816

* Sat Sep 27 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.6-alt0.5
- Updated to r1803
  + Merged upstream dependencies patch (#547569 in GNOME Bugzilla)

* Thu Sep 04 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.6-alt0.4
- Bootstrap is finished, switch to self-hosting builds

* Wed Sep 03 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.6-alt0.3
- Fix GTK+ VAPI (courtesy of Val(a)IDE project)

* Fri Aug 29 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.6-alt0.2
- Always perform language self-check tests

* Fri Aug 29 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.6-alt0.1
- Use correct version and release to signify in-progress version

* Fri Aug 29 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.5-alt6
- Fix package maintainership

* Fri Aug 29 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.5-alt5
- Remove unneeded now bootstrap patch

* Fri Aug 29 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.5-alt4
- Optimize build requires
- Support build with system-wide valac for future releases

* Fri Aug 29 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.5-alt3
- Clarify directories' layout
- Add essential documentation

* Fri Aug 29 2008 Alexander Bokovoy <ab@altlinux.org> 0.3.5-alt2
- First build for Sisyphus

