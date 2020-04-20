# coccinelle.spec
Name:		coccinelle
Version:	1.0.8
Release:	alt5
Summary:	Semantic patching for Linux (spatch)

Group:		Development/Kernel
License:	GPL-2.0-only
Url:		http://coccinelle.lip6.fr/

Source:		%name-%version.tar
Provides:	spatch

BuildRequires(pre): rpm-build-ocaml
BuildRequires(pre): rpm-build-python3
BuildRequires:	ocaml >= 3.12.1
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-ocamldoc
BuildRequires:	ocaml-menhir
BuildRequires:	ocaml-stdcompat-devel
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-num-devel
BuildRequires:	ocaml-parmap-devel
BuildRequires:	python3-dev

# Bogus internal name
%filter_from_requires /^python.*(coccinelle)/d
# Bogus dependencies to OCaml
AutoReqProv: noocaml
# Only what's matter
Provides: ocaml-cmi(Coccilib) = %version-%release
Provides: ocaml-cmx(Coccilib) = %version-%release
# No cocciguis (pida for vim, gtk output), yet
%add_findreq_skiplist %python3_sitelibdir/coccilib/coccigui/*
# No trac integraion
%add_findreq_skiplist %python3_sitelibdir/coccilib/trac.py

%description
Coccinelle is a tool to utilize semantic patches for manipulating
C code. It was originally designed to ease maintenance of device
drivers in the Linux kernel.

%prep
%setup -q -n %{name}-%{version}
sed -i '1s:^#!/usr/bin/env python$:#!/usr/bin/python3:' tools/pycocci

%build
./autogen
%configure \
	--with-python=%_bindir/python3 \

make EXTLIBDIR=`ocamlc -where`/extlib

%install
make DESTDIR=%buildroot install

# relocate python module
install -d %buildroot%python3_sitelibdir
mv %buildroot%_libdir/coccinelle/python/coccilib %buildroot%python3_sitelibdir/
rm -rf %buildroot%_libdir/coccinelle/python

# Somebody forgot to install this
install ./tools/pycocci %buildroot%_bindir/pycocci

%check
export COCCINELLE_HOME=%buildroot%_libdir/coccinelle
export LD_LIBRARY_PATH=.
%buildroot%_bindir/spatch -sp_file demos/simple.cocci demos/simple.c

%files
%doc authors.txt bugs.txt changes.txt copyright.txt credits.txt
%doc license.txt readme.txt
%_bindir/pycocci
%_bindir/spatch
%_bindir/spgen
%_libdir/%name/
%python3_sitelibdir/coccilib
%_man1dir/*.1*
%_man3dir/Coccilib.3cocci*
/usr/share/bash-completion/completions/spatch

%changelog
* Mon Apr 20 2020 Vitaly Chikunov <vt@altlinux.org> 1.0.8-alt5
- spec: Fix `Cannot infer Python version'.

* Sat Apr 18 2020 Vitaly Chikunov <vt@altlinux.org> 1.0.8-alt4
- Convert to python3, add spgen, delete spatch.opt, clean up reqs.

* Sat Apr 18 2020 Vitaly Chikunov <vt@altlinux.org> 1.0.8-alt3
- Install coccinelle ocaml libs (for coccicheck).

* Thu Mar 05 2020 Anton Farygin <rider@altlinux.ru> 1.0.8-alt2
- removed unsafe-string build flag to avoid problems with ocaml-4.10
- built with external stdcompat
- removed chrpath from build dependencies (it is no longer required)

* Mon Feb 17 2020 Vitaly Chikunov <vt@altlinux.org> 1.0.8-alt1
- Update to 1.0.8.

* Wed Aug 07 2019 Vitaly Chikunov <vt@altlinux.org> 1.0.7.0.217.ged1eb8e0-alt1
- Update to 1.0.7-217-ged1eb8e0.

* Sun Jun 10 2018 Vitaly Chikunov <vt@altlinux.ru> 1.0.6-alt1
- Initial build for ALT.
