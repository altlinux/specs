%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%def_enable ocaml
%def_enable perl
%def_enable python
%def_disable ruby
%def_disable static

Name: hivex
Version: 1.3.23
Release: alt1
Summary: Read and write Windows Registry binary hive files

Group: Development/Other
License: LGPLv2
Url: http://libguestfs.org/

Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: perl-Test-Pod
BuildRequires: perl-Test-Pod-Coverage
BuildRequires: perl-libintl
%{?_enable_ocaml:BuildRequires: ocaml ocaml-findlib ocaml-ocamldoc ocaml-ocamlbuild}
%{?_enable_ruby:BuildRequires: ruby rpm-build-ruby ruby-rake ruby-mkrf libruby-devel rubygems}
%{?_enable_perl:BuildRequires: perl(Test/More.pm) perl(ExtUtils/MakeMaker.pm) perl(IO/Stringy.pm)}
%{?_enable_python:BuildRequires: python3-devel}
%{?_enable_python:BuildPreReq:rpm-build-python3}
BuildRequires: libreadline-devel
BuildRequires: libxml2-devel
BuildRequires: gperf

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

For Python bindings, see 'python3-module-hivex'.

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

%package -n perl-%name
Summary: Perl bindings for %name
Group: Development/Perl
Requires: %name = %version-%release

%description -n perl-%name
perl-%name contains Perl bindings for %name.

%package -n python3-module-%name
Summary: Python bindings for %name
Group: Development/Python
Requires: %name = %version-%release

%description -n python3-module-%name
python3-%name contains Python bindings for %name.

%package -n ruby-%name
Summary: Ruby bindings for %name
Group: Development/Ruby
Requires: %name = %version-%release

%description -n ruby-%name
ruby-%name contains Ruby bindings for %name.

%prep
%setup
%patch1 -p1

%build
%autoreconf
./generator/generator.ml
%configure PYTHON=%__python3 \
	%{subst_enable static} \
	%{subst_enable ruby} \
	%{subst_enable ocaml} \
	%{subst_enable perl} \
	%{subst_enable python} \
	--disable-rpath

%make INSTALLDIRS=vendor

%check
make check

%install
%make install INSTALLDIRS=vendor DESTDIR=%buildroot

%if_disabled ocaml
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
rm -f %buildroot%python3_sitelibdir/libhivexmod.la

%find_lang %name

%files -f %name.lang
%doc README.md LICENSE
%_bindir/hivexget
%_bindir/hivexml
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

%if_enabled ocaml
%files -n ocaml-%name
%doc README.md
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

%if_enabled perl
%files -n perl-%name
%_bindir/hivexregedit
%perl_vendor_archlib/*
%endif

%if_enabled python
%files -n python3-module-%name
%python3_sitelibdir/*
%endif

%if_enabled ruby
%files -n ruby-%name
%doc ruby/doc/site/*
%ruby_sitelibdir/hivex.rb
%ruby_sitearchdir/_hivex.so
%endif

%changelog
* Fri Jan 20 2023 Anton Farygin <rider@altlinux.ru> 1.3.23-alt1
- 1.3.23

* Sun Oct 03 2021 Anton Farygin <rider@altlinux.ru> 1.3.21-alt2
- fixed build with LTO

* Wed Aug 18 2021 Anton Farygin <rider@altlinux.ru> 1.3.21-alt1
- 1.3.21 (Fixes: CVE-2021-3622)

* Fri May 21 2021 Anton Farygin <rider@altlinux.ru> 1.3.20-alt1
- 1.3.20

* Mon Sep 21 2020 Anton Farygin <rider@altlinux.ru> 1.3.19-alt1
- 1.3.19

* Wed Mar 11 2020 Anton Farygin <rider@altlinux.ru> 1.3.18-alt2
- removed python2 support

* Mon Jul 01 2019 Anton Farygin <rider@altlinux.ru> 1.3.18-alt1
- 1.3.18

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.15-alt3.1
- rebuild with new perl 5.28.1

* Fri Oct 19 2018 Anton Farygin <rider@altlinux.ru> 1.3.15-alt3
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 1.3.15-alt2
- rebuilt with ocaml 4.07

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 1.3.15-alt1
- 1.3.15

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.14-alt1.1
- rebuild with new perl 5.26.1

* Thu May 04 2017 Anton Farygin <rider@altlinux.ru> 1.3.14-alt1
- new version

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.3.13-alt4
- rebuild with ocaml 4.04.1

* Thu Apr 06 2017 Anton Farygin <rider@altlinux.ru> 1.3.13-alt3
- rebuild with ocaml-4.04.0

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.13-alt2.1
- rebuild with new perl 5.24.1

* Fri Jun 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.13-alt2
- rebuild with ocaml4-4.03.0

* Thu May 26 2016 Alexey Shabalin <shaba@altlinux.ru> 1.3.13-alt1
- 1.3.13

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.3.12-alt1.1
- rebuild with new perl 5.22.0

* Wed Oct 21 2015 Alexey Shabalin <shaba@altlinux.ru> 1.3.12-alt1
- 1.3.12

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.11-alt1.1
- rebuild with new perl 5.20.1

* Fri Nov 14 2014 Alexey Shabalin <shaba@altlinux.ru> 1.3.11-alt1
- 1.3.11
- build with ocaml4

* Tue Sep 02 2014 Alexey Shabalin <shaba@altlinux.ru> 1.3.10-alt1
- 1.3.10

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 1.3.6-alt3
- built for perl 5.18

* Mon Dec 10 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.6-alt2
- Move %_bindir/hivexregedit to perl-%name (ALT#28210)

* Tue Sep 04 2012 Alexey Shabalin <shaba@altlinux.ru> 1.3.6-alt1
- 1.3.6

* Thu Dec 15 2011 Alexey Shabalin <shaba@altlinux.ru> 1.3.3-alt1
- initial build for ALT Linux Sisyphus
