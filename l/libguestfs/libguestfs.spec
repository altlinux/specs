%define _unpackaged_files_terminate_build 1

# Temporarily disable tests on i586 due to kvm bug
# see:  https://www.mail-archive.com/qemu-devel@nongnu.org/msg928879.html
# 1.48.6: Test suite fails on armh and ppc64le
%ifarch i586 armh ppc64le
%def_without check
%else
%def_with check
%endif

%def_enable daemon
%def_disable appliance
%def_enable fuse
%def_enable ocaml
%def_enable perl
%def_enable python
%def_disable ruby
%def_disable haskell
%def_disable php
%def_disable erlang
%def_disable lua
%def_disable golang
%def_enable introspection
%def_enable vala
%def_disable rust
%def_disable static
%def_enable bash_completion

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: libguestfs
Version: 1.48.6
Release: alt1

Summary: Library for accessing and modifying virtual machine disk images
License: LGPLv2+
Group: System/Libraries
Url: http://libguestfs.org/

Source: %name-%version.tar
Source2: %name-%version-common.tar
Patch1: %name-1.46.0-alt-fixes.patch
Patch2: %name-1.46.0-alt-fixes-common.patch

BuildRequires: /proc
BuildRequires: gcc gcc-c++ flex
BuildRequires: rpcgen
BuildRequires: glibc-utils libselinux-devel libaugeas-devel
BuildRequires: libgio-devel libgtk+3-devel
BuildRequires: gtk-doc
BuildRequires: gettext-tools
BuildRequires: cpio gperf xorriso xml-utils db4-utils zip unzip
BuildRequires: qemu-kvm qemu-system >= 1.3.0
BuildRequires: libncurses-devel libtinfo-devel libreadline-devel
BuildRequires: libpcre2-devel libmagic-devel libvirt-devel libxml2-devel libconfig-devel hivex-devel
BuildRequires: libacl-devel libcap-devel
BuildRequires: netpbm
BuildRequires: libyajl-devel >= 2.0.4
BuildRequires: libjansson-devel
BuildRequires: libsystemd-journal-devel >= 196
BuildRequires: librpm-devel
BuildRequires: libyara-devel
BuildRequires: libtsk-devel
BuildRequires: liblzma-devel
BuildRequires: libdbus-devel
BuildRequires: libtirpc-devel
BuildRequires: java-devel-default jpackage-utils

%if_enabled introspection
BuildRequires: gobject-introspection-devel libgjs-devel
%endif

%if_enabled vala
BuildRequires(pre): rpm-build-vala
BuildRequires: vala-tools
%endif

%if_enabled fuse
BuildRequires: libfuse-devel
%endif

%if_enabled ocaml
BuildRequires(pre): rpm-build-ocaml
BuildRequires: ocaml ocaml-findlib ocaml-gettext-devel ocaml-ounit-devel ocaml-ocamldoc ocaml-ocamlbuild ocaml-hivex-devel
%endif

%if_enabled python
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-libvirt
%endif

%if_enabled ruby
BuildRequires: ruby rpm-build-ruby ruby-rake ruby-mkrf libruby-devel rubygems
%endif

%if_enabled haskell
BuildRequires: ghc
%endif

%if_enabled php
BuildRequires: php7-devel
%endif

%if_enabled erlang
BuildRequires: erlang-devel
%endif

%if_enabled perl
BuildRequires: perl-Pod-Parser perl-Sys-Virt perl-libintl perl-hivex perl-Module-Build perl-ExtUtils-CBuilder perl-devel
%endif

%if_enabled golang
BuildRequires(pre): rpm-macros-golang
%endif

%if_enabled rust
BuildRequires: rust rust-cargo
%endif

%if_enabled bash_completion
BuildRequires: bash-completion >= 2.0
%endif

%if_with check
BuildRequires: /dev/kvm
BuildRequires: rpm-build-guestfs
%endif

%description
libguestfs is a set of tools for accessing and modifying virtual
machine (VM) disk images. You can use this for viewing and editing
files inside guests, scripting changes to VMs, monitoring disk
used/free statistics, P2V, V2V, performing partial backups, cloning
VMs, and much else besides.

%package -n guestfsd
Summary: Provides guestfsd for the appliance
Group: File tools

%description -n guestfsd
guestfsd runs within the appliance. It receives commands from the host
and performs the requested action by calling the helper binaries.
This package is only required for building the appliance.

%package rescue
Summary: virt-rescue shell
Group: System/Base

%description rescue
This adds the virt-rescue shell which is a "rescue disk" for virtual
machines, and additional tools to use inside the shell such as ssh,
network utilities, editors and debugging utilities.


%package devel
Summary: Header files for libguestfs library
Group: Development/Other
Requires: %name = %EVR
Requires: %name-gobject = %EVR
Requires: %name-gir = %EVR
Provides: %name-gobject-devel = %EVR
Obsoletes: %name-gobject-devel < %EVR
Provides: %name-gir-devel = %EVR
Obsoletes: %name-gir-devel < %EVR

%description devel
Header files for libguestfs library.

%package gobject
Summary: GObject'ified version of libguestfs API
Group: System/Libraries
Requires: %name = %EVR

%description gobject
GObject'ified version of libguestfs API

%package gir
Summary: GObject introspection data for the libguestf library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the libguestfs library

%package -n golang-guestfs
Summary: Golang bindings for %name
Group: Development/Other
Requires: %name = %EVR
Requires: golang

%description -n golang-guestfs
golang-%name contains Go language bindings for %name.

%package -n ocaml-%name
Summary: OCaml bindings for %name
Group: Development/Other
Requires: %name = %EVR
Provides: ocaml4-%name = %EVR
Obsoletes: ocaml4-%name < %EVR

%description -n ocaml-%name
ocaml-%name contains OCaml bindings for %name.

This is for toplevel and scripting access only.  To compile OCaml
programs which use %name you will also need ocaml-%name-devel.

%package -n ocaml-%name-devel
Summary: OCaml bindings for %name
Group: Development/Other
Requires: ocaml-%name = %EVR
Provides: ocaml4-%name-devel = %EVR
Obsoletes: ocaml4-%name-devel < %EVR

%description -n ocaml-%name-devel
ocaml-%name-devel contains development libraries
required to use the OCaml bindings for %name.

%package -n perl-Sys-Guestfs
Summary: Perl bindings for %name (Sys::Guestfs)
Group: Development/Other
Requires: %name = %EVR
Provides: perl-%name = %EVR

%description -n perl-Sys-Guestfs
perl-Sys-Guestfs contains Perl bindings for %name (Sys::Guestfs).

%package -n python3-module-%name
Summary: Python3 bindings for %name
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-%name
python3-module-%name contains Python3 bindings for %name.

%package -n ruby-%name
Summary: Ruby bindings for %name
Group: Development/Other
Requires: %name = %EVR

%description -n ruby-%name
ruby-%name contains Ruby bindings for %name.

%package java
Summary: Java bindings for %name
Group: Development/Other
Requires: %name = %EVR
Requires: jpackage-utils

%description java
%name-java contains Java bindings for %name.

If you want to develop software in Java which uses %name, then
you will also need %name-java-devel.

%package java-devel
Summary: Java development package for %name
Group: Development/Other
Requires: %name = %EVR
Requires: %name-java = %EVR

%description java-devel
%name-java-devel contains the tools for developing Java software
using %name.

See also %name-javadoc.

%package javadoc
Summary: Java documentation for %name
Group: Development/Other
Requires: %name = %EVR
Requires: %name-java = %EVR
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
%name-javadoc contains the Java documentation for %name.

%package -n php7-%name
Summary: PHP bindings for %name
Group: Development/Other
Requires: %name = %EVR

%description -n php7-%name
php-%name contains PHP bindings for %name.

%package -n erlang-%name
Summary: Erlang bindings for %name
Group: Development/Other
Requires: %name = %EVR

%description -n erlang-%name
erlang-%name contains Erlang bindings for %name.

%prep
%setup -a2
tar -xf %SOURCE2 -C common


# test_cap_set_file_0 fails becaues we still have old libcap
# see: d4ab4ff683807dc42525c38dee8016ea9f4fab3f
sed -i -e 's/"cap_chown=ep"/"= cap_chown+ep"/' generator/actions_core.ml

%patch1 -p1
pushd common
%patch2 -p1
popd

%build
%autoreconf
export PYTHON=%__python3
%configure \
	vmchannel_test=no \
	%{subst_enable daemon} \
	--enable-install-daemon \
	%{subst_enable appliance} \
	%{subst_enable fuse} \
	%{subst_enable ocaml} \
	%{subst_enable perl} \
	%{subst_enable python} \
	%{subst_enable ruby} \
	%{subst_enable haskell} \
	%{subst_enable php} \
	%{subst_enable erlang} \
	%{subst_enable lua} \
	%{subst_enable goolang} \
	%{subst_enable introspection} \
	%{subst_enable vala} \
	%{subst_enable rust} \
	%{subst_enable static} \
	--with-default-backend=direct \
	--with-extra="ALTLinux,release=%version-%release,libvirt" \
	--with-qemu="qemu-kvm qemu-system-%_build_arch qemu" \
	--disable-silent-rules \
	--disable-probes \
	--disable-rpath

%make INSTALLDIRS=vendor

%install
%make install INSTALLDIRS=vendor DESTDIR=%buildroot

# Delete static libraries, libtool files.
rm -f %buildroot%_libdir/libguestfs.{la,a}

find %buildroot -name perllocal.pod -delete
find %buildroot -name .packlist -delete
find %buildroot -name '*.bs' -delete
find %buildroot -name 'bindtests.pl' -delete

# Remove static-linked Java bindings.
rm %buildroot%_libdir/libguestfs_jni.la

# Remove Japanese manpages, since these are not translated fully at
# the moment.  When these are translated properly we intend to add
# them back.
rm -rf %buildroot%_mandir/ja/man{1,3}/


# delete unneeded
rm -f %buildroot%_man1dir/guestfs-release-notes*

%find_lang %name

%check
# TODO: create test-data/phony-guests/fedora.img
# needs fedora.img
export SKIP_TEST_JOURNAL_PL=1
# needs fedora-btrfs.img
export SKIP_TEST_MOUNTABLE_INSPECT_SH=1

# error: luks_close: cryptsetup exited with status 5: Device
# lukstest is still in use.
export SKIP_TEST_LUKS_SH=1

# needs network
export SKIP_TEST_RSYNC_SH=1

# get_tmpdir error: libguestfs-1.46.0-alt-fixes.patch
sed -i -e  '2i exit 77 if $ENV{SKIP_TEST_TMPDIRS_PL};' \
    tests/tmpdirs/test-tmpdirs.pl
export SKIP_TEST_TMPDIRS_PL=1

# log_messages does not contain magic string 'abcdefgh9876543210'
export SKIP_TEST_CONSOLE_DEBUG_PL=1

# hangs with our appliance
export SKIP_TEST_RHBZ914931=1

# needs x perm for /usr/bin/fusermount
export SKIP_TEST_GUESTUNMOUNT_FD=1

export LIBGUESTFS_PATH="%_libdir/guestfs"
export LIBGUESTFS_DEBUG=1
export LIBGUESTFS_TRACE=1

if ! make quickcheck check; then
    cat tests/test-suite.log ||:
    exit 1
fi

%files -f %name.lang
%doc COPYING README
%config(noreplace) %_sysconfdir/libguestfs-tools.conf
%_bindir/guestfish
%_bindir/guestmount
%_bindir/guestunmount
%_bindir/libguestfs-test-tool
%_bindir/virt-copy-in
%_bindir/virt-copy-out
%_bindir/virt-tar-in
%_bindir/virt-tar-out
%_libdir/libguestfs.so.*
%_man1dir/guestfish.1*
%_man1dir/guestfs-faq.1*
%_man1dir/guestfs-hacking.1*
%_man1dir/guestfs-internals.1*
%_man1dir/guestfs-performance.1*
%_man1dir/guestfs-security.1*
%_man1dir/guestmount.1*
%_man1dir/guestunmount.1*
%_man1dir/guestfs-testing.1*
%_man1dir/virt-copy-in.1*
%_man1dir/virt-copy-out.1*
%_man1dir/virt-tar-in.1*
%_man1dir/virt-tar-out.1*
%_man1dir/libguestfs-test-tool.1*
%_man5dir/libguestfs-tools.conf.5*
%dir %_datadir/bash-completion/completions
%_datadir/bash-completion/completions/guestfish
%_datadir/bash-completion/completions/guestmount
%_datadir/bash-completion/completions/guestunmount
%_datadir/bash-completion/completions/libguestfs-test-tool
%_datadir/bash-completion/completions/virt-copy-in
%_datadir/bash-completion/completions/virt-copy-out
%_datadir/bash-completion/completions/virt-rescue
%_datadir/bash-completion/completions/virt-tar-in
%_datadir/bash-completion/completions/virt-tar-out


%files -n guestfsd
%_sbindir/guestfsd
%_man8dir/guestfsd.*

%files rescue
%_bindir/virt-rescue
%_man1dir/virt-rescue.1*

%files devel
%doc AUTHORS HACKING TODO README
%doc examples/*.c
%_libdir/libguestfs.so
%_man1dir/guestfs-building.1*
%_man1dir/guestfs-recipes.1*
%_man3dir/guestfs.3*
%_man3dir/guestfs-examples.3*
%_man3dir/libguestfs.3*
%_includedir/guestfs.h
%_pkgconfigdir/libguestfs.pc

%if_enabled introspection
%_libdir/libguestfs-gobject-*.so
%_includedir/guestfs-gobject
%_includedir/guestfs-gobject.h
%_pkgconfigdir/libguestfs-gobject-1.0.pc
%_man3dir/guestfs-gobject.3.*
%_girdir/*.gir

%if_enabled vala
%_datadir/vala/vapi/libguestfs-gobject-1.0.*
%endif

%files gobject
%_libdir/libguestfs-gobject-*.so.*

%files gir
%_typelibdir/*.typelib
%endif #introspection

%if_enabled golang
%files -n golang-guestfs
%doc golang/examples/*.go
%doc golang/examples/LICENSE
%_libdir/golang/src/libguestfs.org
%_man3dir/guestfs-golang.3*
%endif

%if_enabled ocaml
%files -n ocaml-%name
%_libdir/ocaml/guestfs
%exclude %_libdir/ocaml/guestfs/*.a
%exclude %_libdir/ocaml/guestfs/*.cmxa
%exclude %_libdir/ocaml/guestfs/*.cmx
%exclude %_libdir/ocaml/guestfs/*.mli
%_libdir/ocaml/stublibs/*.so
%_libdir/ocaml/stublibs/*.so.owner

%files -n ocaml-%name-devel
%doc ocaml/examples/*.ml
%_libdir/ocaml/guestfs/*.a
%_libdir/ocaml/guestfs/*.cmxa
%_libdir/ocaml/guestfs/*.cmx
%_libdir/ocaml/guestfs/*.mli
%_man3dir/guestfs-ocaml.3*
%endif #ocaml

%if_enabled perl
%files -n perl-Sys-Guestfs
%doc perl/examples
%perl_vendor_archlib/*
%_man3dir/guestfs-perl.3*
%endif #perl

%if_enabled python
%files -n python3-module-%name
%doc python/examples/*.py
%python3_sitelibdir/*
%_man3dir/guestfs-python.3*
%endif #python

%if_enabled ruby
%files -n ruby-%name
%doc ruby/examples/*.rb
%doc ruby/doc/site/*
%ruby_sitelibdir/guestfs.rb
%ruby_sitearchdir/_guestfs.so
%_man3dir/guestfs-ruby.3*
%endif #ruby

%files java
%_libdir/libguestfs_jni*.so.*
%_datadir/java/*.jar

%files java-devel
%_libdir/libguestfs_jni*.so
%_man3dir/guestfs-java.3*

%files javadoc
%_datadir/javadoc/%name

%if_enabled php
%files -n php7-%name
%doc php/README-PHP
%dir %_sysconfdir/php.d
%_sysconfdir/php.d/guestfs_php.ini
%_libdir/php/modules/guestfs_php.so
%endif #php

%if_enabled erlang
%files -n erlang-%name
%doc erlang/README
%doc erlang/examples/*.erl
%doc erlang/examples/LICENSE
%_bindir/erl-guestfs
%_libdir/erlang/lib/%name-%version
%_man3dir/guestfs-erlang.3*
%endif #erlang

%changelog
* Wed Nov 30 2022 Egor Ignatov <egori@altlinux.org> 1.48.6-alt1
- 1.48.6
- enable tests

* Wed Nov 23 2022 Egor Ignatov <egori@altlinux.org> 1.48.5-alt1
- 1.48.5

* Mon Sep 12 2022 Egor Ignatov <egori@altlinux.org> 1.48.4-alt2
- enable basic tests

* Mon Sep 05 2022 Egor Ignatov <egori@altlinux.org> 1.48.4-alt1
- 1.48.4
- update libguestfs-1.46.0-alt-fixes patch

* Sat Feb 05 2022 Anton Farygin <rider@altlinux.ru> 1.46.2-alt2
- the default backend switched to direct (closes: #41783)

* Mon Jan 10 2022 Anton Farygin <rider@altlinux.ru> 1.46.2-alt1
- 1.46.1 -> 1.46.2

* Thu Dec 16 2021 Anton Farygin <rider@altlinux.ru> 1.46.1-alt1
- 1.46.0 -> 1.46.1
- built with enabled librpm, yara and sleuthkit support

* Thu Nov 04 2021 Anton Farygin <rider@altlinux.ru> 1.46.0-alt1
- 1.46.0

* Mon Oct 04 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.44.1-alt2
- Fix build via -ffat-lto-objects

* Mon Apr 05 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.44.1-alt1
- 1.44.1

* Wed Feb 10 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.44.0-alt1
- 1.44.0

* Tue Dec 26 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.42.0-alt4
- Add requires to db4-utils (Closes: 39365)

* Thu Dec 24 2020 Anton Farygin <rider@altlinux.ru> 1.42.0-alt3
- added rpcgen to build requires against glibc 2.32

* Tue Jun 30 2020 Alexey Shabalin <shaba@altlinux.org> 1.42.0-alt2
- Set default guestfs appliance path to $libdir/guestfs

* Fri Apr 24 2020 Alexey Shabalin <shaba@altlinux.org> 1.42.0-alt1
- 1.42.0
- build with vala support
- drop virt-p2v and virt-v2v

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 1.40.2-alt3
- removed python-2 support
- fixed build with python-3.8 by patch from upstream

* Thu Jul 18 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.40.2-alt2
- %%build: changed to always pass distro name to configure script in case
  /etc/os-release file is missing.
- %name: added R: guestfs-data on aarch64.

* Wed Apr 03 2019 Alexey Shabalin <shaba@altlinux.org> 1.40.2-alt1
- 1.40.2

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.38.6-alt3.1
- rebuild with new perl 5.28.1

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 1.38.6-alt3
- build python3 package
- build bash-completion package

* Sat Oct 20 2018 Anton Farygin <rider@altlinux.ru> 1.38.6-alt2
- rebuilt with ocaml-4.07.1

* Thu Oct 18 2018 Alexey Shabalin <shaba@altlinux.org> 1.38.6-alt1
- 1.38.6

* Tue Oct 09 2018 Alexey Shabalin <shaba@altlinux.org> 1.36.15-alt1
- 1.36.15

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 1.36.9-alt2
- rebuilt with ocaml 4.07

* Mon May 21 2018 Anton Farygin <rider@altlinux.ru> 1.36.9-alt1
- rebuilt for ocaml 4.06.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.36.5-alt1.1
- rebuild with new perl 5.26.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.36.5-alt1
- new version

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.36.3-alt3
- rebuild with ocaml 4.04.1

* Thu Apr 27 2017 Anton Farygin <rider@altlinux.ru> 1.36.3-alt2
- using /var/tmp for tmppath in virt-* tools instead of TMPDIR
- added ubt tag
- added /lib/systemd/systemd-machined  requires to guestfs-tools 

* Mon Apr 03 2017 Anton Farygin <rider@altlinux.ru> 1.36.3-alt2
- rebuild with ocaml-4
- ocaml modules renamed back to ocaml-*

* Tue Mar 28 2017 Alexey Shabalin <shaba@altlinux.ru> 1.36.3-alt1
- 1.36.3

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.33.38-alt1.1
- rebuild with new perl 5.24.1

* Wed Jun 22 2016 Alexey Shabalin <shaba@altlinux.ru> 1.33.38-alt1
- 1.33.38

* Thu May 26 2016 Alexey Shabalin <shaba@altlinux.ru> 1.32.4-alt1
- 1.32.4

* Mon Jan 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.32.0-alt1
- 1.32.0

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.31.17-alt1.1
- rebuild with new perl 5.22.0

* Tue Oct 20 2015 Alexey Shabalin <shaba@altlinux.ru> 1.31.17-alt1
- 1.31.17

* Thu Sep 17 2015 Alexey Shabalin <shaba@altlinux.ru> 1.31.6-alt1
- 1.31.6

* Thu Jul 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.29.6-alt2
- vkni@: Rebuild with new rpm-build-ocaml4. Renamed ocaml packages to ocaml4-.

* Thu Feb 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1.29.6-alt1
- 1.29.6

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.29.2-alt1.1
- rebuild with new perl 5.20.1

* Tue Oct 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1.29.2-alt1
- 1.29.2

* Tue Sep 03 2013 Vladimir Lettiev <crux@altlinux.ru> 1.23.19-alt2
- built for perl 5.18

* Fri Aug 30 2013 Alexey Shabalin <shaba@altlinux.ru> 1.23.19-alt1
- 1.23.19

* Tue Dec 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.19.66-alt1
- 1.19.66

* Thu Sep 06 2012 Vladimir Lettiev <crux@altlinux.ru> 1.19.38-alt2
- rebuilt for perl-5.16

* Tue Sep 04 2012 Alexey Shabalin <shaba@altlinux.ru> 1.19.38-alt1
- 1.19.38

* Thu Jan 12 2012 Alexey Shabalin <shaba@altlinux.ru> 1.15.16-alt1
- initial build

