%def_with ocaml
%def_disable ruby
%def_disable static

Name: hivex
Version: 1.3.3
Release: alt1
Summary: Read and write Windows Registry binary hive files

Group: Development/Other
License: LGPLv2
Url: http://libguestfs.org/

Source: %name-%version.tar
Source1: gnulib-%name-%version.tar
Patch1: %name-%version-%release.patch

BuildRequires: perl-Test-Pod
BuildRequires: perl-Test-Pod-Coverage
BuildRequires: perl-IO-stringy
BuildRequires: perl-libintl
%if_with ocaml
BuildRequires: ocaml findlib ocamldoc ocamlbuild
%endif
%if_enabled ruby
BuildRequires: ruby rpm-build-ruby ruby-rake ruby-mkrf libruby-devel rubygems
%endif
BuildRequires: python-devel
BuildRequires: libreadline-devel
BuildRequires: libxml2-devel

%description
Hive files are the undocumented binary blobs that Windows uses to
store the Windows Registry on disk.  Hivex is a library that can read
and write to these files.

'hivexsh' is a shell you can use to interactively navigate a hive
binary file.

'hivexregedit' lets you export and merge to the textual regedit
format.

'hivexml' can be used to convert a hive file to a more useful XML
format.

In order to get access to the hive files themselves, you can copy them
from a Windows machine.  They are usually found in
%%systemroot%%\system32\config.  For virtual machines we recommend
using libguestfs or guestfish to copy out these files.  libguestfs
also provides a useful high-level tool called 'virt-win-reg' (based on
hivex technology) which can be used to query specific registry keys in
an existing Windows VM.

For OCaml bindings, see 'ocaml-hivex-devel'.

For Perl bindings, see 'perl-hivex'.

For Python bindings, see 'python-module-hivex'.

For Ruby bindings, see 'ruby-hivex'.

%package devel
Summary: Development tools and libraries for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
%name-devel contains development tools and libraries
for %name.

%package static
Summary: Statically linked library for %name
Group: Development/Other
Requires: %name = %version-%release

%description static
%name-static contains the statically linked library
for %name.

%if_with ocaml
%package -n ocaml-%name
Summary: OCaml bindings for %name
Group: Development/Other
Requires: %name = %version-%release

%description -n ocaml-%name
ocaml-%name contains OCaml bindings for %name.

This is for toplevel and scripting access only.  To compile OCaml
programs which use %name you will also need ocaml-%name-devel.

%package -n ocaml-%name-devel
Summary: OCaml bindings for %name
Group: Development/Other
Requires: ocaml-%name = %version-%release

%description -n ocaml-%name-devel
ocaml-%name-devel contains development libraries
required to use the OCaml bindings for %name.
%endif

%package -n perl-%name
Summary: Perl bindings for %name
Group: Development/Perl
Requires: %name = %version-%release

%description -n perl-%name
perl-%name contains Perl bindings for %name.

%package -n python-module-%name
Summary: Python bindings for %name
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-%name
python-%name contains Python bindings for %name.

%package -n ruby-%name
Summary: Ruby bindings for %name
Group: Development/Ruby
Requires: %name = %version-%release

%description -n ruby-%name
ruby-%name contains Ruby bindings for %name.

%prep
%setup -a1
%patch1 -p1
# git and rsync aren't needed for build.
sed -i '/^\(git\|rsync\)[[:space:]]/d' bootstrap
rmdir .gnulib
ln -s gnulib-%name-%version .gnulib

%build
./bootstrap
./generator/generator.ml
%configure \
	%{subst_enable static} \
	%{subst_enable ruby} \
	--disable-rpath \
	--disable-silent-rules
%make INSTALLDIRS=vendor

%check
make check

%install
%make install INSTALLDIRS=vendor DESTDIR=%buildroot

%if_without ocaml
# Delete OCaml files, in case the user had OCaml installed and it was
# picked up by the configure script.
# XXX Add ./configure --disable-ocaml upstream.
rm -rf %buildroot%_libdir/ocaml/hivex
rm -f  %buildroot%_libdir/ocaml/stublibs/*hivex*
%endif

# Remove unwanted libtool *.la file:
rm -f %buildroot%_libdir/libhivex.la

# Remove unwanted Perl files:
find %buildroot -name perllocal.pod -delete
find %buildroot -name .packlist -delete
find %buildroot -name '*.bs' -delete

# Remove unwanted Python files:
rm -f %buildroot%python_sitelibdir/libhivexmod.la

%find_lang %name

%files -f %name.lang
%doc README LICENSE
%_bindir/hivexget
%_bindir/hivexml
%_bindir/hivexregedit
%_bindir/hivexsh
%_libdir/libhivex.so.*
%_man1dir/hivexget.1*
%_man1dir/hivexml.1*
%_man1dir/hivexregedit.1*
%_man1dir/hivexsh.1*

%files devel
%doc LICENSE
%_libdir/libhivex.so
%_man3dir/hivex.3*
%_includedir/hivex.h
%_pkgconfigdir/hivex.pc

%if_enabled static
%files static
%doc LICENSE
%_libdir/libhivex.a
%endif

%if_with ocaml
%files -n ocaml-%name
%doc README
%_libdir/ocaml/hivex
%exclude %_libdir/ocaml/hivex/*.a
%exclude %_libdir/ocaml/hivex/*.cmxa
%exclude %_libdir/ocaml/hivex/*.cmx
%exclude %_libdir/ocaml/hivex/*.mli
%_libdir/ocaml/stublibs/*.so
%_libdir/ocaml/stublibs/*.so.owner

%files -n ocaml-%name-devel
%_libdir/ocaml/hivex/*.a
%_libdir/ocaml/hivex/*.cmxa
%_libdir/ocaml/hivex/*.cmx
%_libdir/ocaml/hivex/*.mli
%endif

%files -n perl-%name
%perl_vendor_archlib/*

%files -n python-module-%name
%python_sitelibdir/*

%if_enabled ruby
%files -n ruby-%name
%doc ruby/doc/site/*
%ruby_sitelibdir/hivex.rb
%ruby_sitearchdir/_hivex.so
%endif

%changelog
* Thu Dec 15 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3.3-alt1
- initial build for ALT Linux Sisyphus
