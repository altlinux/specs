Name: mosml
Version: 2.10.1
Release: alt1

Summary:  Moscow ML
License: GPL
Group: Development/ML
Url: http://mosml.org/

Packager: %packager
Source: %name-%version.tar
Patch: %name-alt-header.patch

# Automatically added by buildreq on Sat Sep 03 2016
BuildRequires: libgmp-devel

%description
Moscow ML provides a light-weight implementation of full Standard ML,
including Modules and some extensions.  Standard ML is a strict
functional language widely used in teaching and research.

Moscow ML is based on the Caml Light system, which gives fast
compilation and modest storage consumption.

   * The full SML Modules language (structures, signatures, and functors)
     is now supported, thanks to Claudio Russo.
   * Also, several extensions to the SML Modules language are provided:
      - higher-order functors: functors may be defined within structures
        and functors
      - first-class modules: structures and functors may be packed and
        then handled as Core language values, which may then be unpacked
        as structures or functors again
      - recursive modules: signatures and structures may be recursively
        defined
   * Despite that improvements, Moscow ML remains backwards compatible.
   * Value polymorphism has become friendlier: non-generalizable free
     type variables are left free, and become instantiated (once only)
     when the bound variable is used
   * Added facilities for creating and communicating with subprocesses
     (structure Unix and Signal from SML Basis Library).
   * Added facilities for efficient functional generation of HTML code
     (structure Msp); also supports the writing of ML Server Page scripts.
   * Added facilities setting and accessing `cookies' in CGI scripts
     (structure Mosmlcookie), thanks to Hans Molin, Uppsala, Sweden.
   * The Gdimage structure now produces PNG images (using Thomas
     Boutell's gd library).

%set_verify_elf_method rpath=relaxed unresolved=relaxed

%prep
%setup
%patch0 -p1

%build
%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir

cd src
make PREFIX=%_datadir BINDIR=%_bindir LIBDIR=%_libdir/mosml DOCDIR=%buildroot/%docdir world
cd compiler
make promote
cd ../
make PREFIX=%_datadir BINDIR=%_bindir LIBDIR=%_libdir/mosml DOCDIR=%buildroot/%docdir again

%install
cd src
make PREFIX=%buildroot/usr BINDIR=%buildroot/%_bindir LIBDIR=%buildroot/%_libdir/mosml DOCDIR=%buildroot/%docdir install

#cd dynlibs
#make MOSMLHOME=${RPM_BUILD_ROOT}/usr/mosml
#make MOSMLHOME=${RPM_BUILD_ROOT}/usr/mosml install
#cd ..
#cd ..

#cp -a tools/Makefile.stub ${RPM_BUILD_ROOT}/usr/mosml/tools

# Put installed doc in an rpm manner
#cp -a ${RPM_BUILD_ROOT}/usr/mosml/doc .
#rm -rf ${RPM_BUILD_ROOT}/usr/mosml/doc

# Alternatively, you can move bin out of mosml:
# mkdir -p ${RPM_BUILD_ROOT}/usr
# mv ${RPM_BUILD_ROOT}/usr/mosml/bin ${RPM_BUILD_ROOT}/usr/bin

# dynamic load path is extended to include /usr/mosml/lib,
# Instead you can move libraries to the standard dynamic loadpath /usr/lib
# mkdir -p ${RPM_BUILD_ROOT}/usr/lib
# cd ${RPM_BUILD_ROOT}/usr/mosml/lib
# for x in lib*.so
# do
#   mv ${RPM_BUILD_ROOT}/usr/mosml/lib/${x} ${RPM_BUILD_ROOT}/usr/lib/${x}
#   # to link instead: ln -sf ../mosml/lib/${x}  ${RPM_BUILD_ROOT}/usr/lib/${x}
# done

# Fix minor install problem:
rm -f %buildroot/%_libdir/mosml/camlrunm

%files
%_bindir/*
%_includedir/*
%_libdir/mosml
%doc README copyrght doc/* examples

%changelog
* Sat Sep 03 2016 Andrey Bergman <vkni@altlinux.org> 2.10.1-alt1
- Initial release for Sisyphus.

