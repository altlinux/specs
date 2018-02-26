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
%def_disable static

Summary: Tools for accessing and modifying virtual machine disk images
Name: libguestfs
Version: 1.15.16
Release: alt1
License: LGPLv2+
Group: Development/Other
Url: http://libguestfs.org/

Source: %name-%version.tar
Source1: gnulib-%name-%version.tar
Patch1: %name-%version-alt-fixes.patch

# libguestfs live service
#%%Source2: guestfsd.service
#%%Source3: 99-guestfsd.rules

BuildPreReq: /proc
BuildRequires: gcc gcc-c++
BuildRequires: glibc-utils libselinux-devel libaugeas-devel
BuildRequires: cpio gperf perl-podlators perl-devel genisoimage xml-utils db4-utils
# po4a 
BuildRequires: qemu-kvm qemu-system
BuildRequires: libncurses-devel libreadline-devel
BuildRequires: libpcre-devel libmagic-devel libvirt-devel libxml2-devel libconfig-devel hivex-devel
%if_enabled fuse
BuildRequires: libfuse-devel
%endif
%if_enabled ocaml
BuildRequires: ocaml findlib ocamldoc ocamlbuild
%endif
%if_enabled python
BuildRequires: python-devel
%endif
%if_enabled ruby
BuildRequires: ruby rpm-build-ruby ruby-rake ruby-mkrf libruby-devel rubygems
%endif
BuildRequires: java-devel-default jpackage-utils
%if_enabled haskell
BuildRequires: ghc
%endif
%if_enabled php
BuildRequires: php5-devel
%endif
%if_enabled erlang
BuildRequires: erlang-devel
%endif
%if_enabled perl
BuildRequires: perl-Pod-Parser perl-Sys-Virt perl-libintl perl-hivex perl-String-ShellQuote
%endif

%description
libguestfs is a set of tools for accessing and modifying virtual
machine (VM) disk images. You can use this for viewing and editing
files inside guests, scripting changes to VMs, monitoring disk
used/free statistics, P2V, V2V, performing partial backups, cloning
VMs, and much else besides.

%package devel
Summary: Header files for libguestfs library
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for libguestfs library.

%package tools
Summary: System administration tools for virtual machines
Group: Development/Tools
License: GPLv2+
Requires: %name = %version-%release

# for virt-make-fs:
Requires: qemu-img

# for virt-sysprep:
Requires: %_bindir/fusermount
Requires: %_bindir/getopt
Requires: %_bindir/guestmount
Requires: %_bindir/virt-inspector

%description tools
This package contains miscellaneous system administrator command line
tools for virtual machines.

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

%package -n perl-Sys-Guestfs
Summary: Perl bindings for %name (Sys::Guestfs)
Group: Development/Other
Requires: %name = %version-%release
Provides: perl-%name = %version-%release

%description -n perl-Sys-Guestfs
perl-Sys-Guestfs contains Perl bindings for %name (Sys::Guestfs).

%package -n python-module-%name
Summary: Python bindings for %name
Group: Development/Other
Requires: %name = %version-%release

%description -n python-module-%name
python-module-%name contains Python bindings for %name.

%package -n ruby-%name
Summary: Ruby bindings for %name
Group: Development/Other
Requires: %name = %version-%release

%description -n ruby-%name
ruby-%name contains Ruby bindings for %name.

%package java
Summary: Java bindings for %name
Group: Development/Other
Requires: %name = %version-%release
Requires: jpackage-utils

%description java
%name-java contains Java bindings for %name.

If you want to develop software in Java which uses %name, then
you will also need %name-java-devel.

%package java-devel
Summary: Java development package for %name
Group: Development/Other
Requires: %name = %version-%release
Requires: %name-java = %version-%release

%description java-devel
%name-java-devel contains the tools for developing Java software
using %name.

See also %name-javadoc.

%package javadoc
Summary: Java documentation for %name
Group: Development/Other
Requires: %name = %version-%release
Requires: %name-java = %version-%release
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
%name-javadoc contains the Java documentation for %name.

%package -n php5-%name
Summary: PHP bindings for %name
Group: Development/Other
Requires: %name = %version-%release

%description -n php5-%name
php-%name contains PHP bindings for %name.

%package -n erlang-%name
Summary: Erlang bindings for %name
Group: Development/Other
Requires: %name = %version-%release

%description -n erlang-%name
erlang-%name contains Erlang bindings for %name.

%package -n bash-completion-libguestfs
Summary: bash-completion for libguestfs tools
Group: Shells
Requires: bash-completion
BuildArch: noarch

%description -n bash-completion-libguestfs
bash-completion for guestfish tool.

%prep
%setup -a1
%patch1 -p1

# git and rsync aren't needed for build.
sed -i '/^\(git\|rsync\)[[:space:]]/d' bootstrap
rmdir .gnulib
ln -s gnulib-%name-%version .gnulib

%build
mkdir -p daemon/m4
./bootstrap

%configure \
	vmchannel_test=no \
	%{subst_enable daemon} \
	%{subst_enable appliance} \
	%{subst_enable fuse} \
	%{subst_enable ocaml} \
	%{subst_enable perl} \
	%{subst_enable python} \
	%{subst_enable ruby} \
	%{subst_enable haskell} \
	%{subst_enable php} \
	%{subst_enable erlang} \
	%{subst_enable static} \
	--with-extra="ALTLinux,release=%version-%release" \
	--with-qemu="qemu-kvm qemu-system-%_build_arch qemu" \
	--disable-silent-rules \
	--disable-rpath

#   --enable-install-daemon \

%make INSTALLDIRS=vendor

%install
%make install INSTALLDIRS=vendor DESTDIR=%buildroot

# Delete static libraries, libtool files.
rm -f %buildroot%_libdir/libguestfs.{la,a}
rm -f %buildroot%python_sitelibdir/libguestfsmod.la

find %buildroot -name perllocal.pod -delete
find %buildroot -name .packlist -delete
find %buildroot -name '*.bs' -delete
find %buildroot -name 'bindtests.pl' -delete

# Remove static-linked Java bindings.
rm %buildroot%_libdir/libguestfs_jni.la

# Move installed documentation back to the source directory so
# we can install it using a %%doc rule.
mv %buildroot%_docdir/libguestfs installed-docs

# Remove Japanese manpages, since these are not translated fully at
# the moment.  When these are translated properly we intend to add
# them back.
rm -rf %buildroot%_mandir/ja/man{1,3}/

# For the libguestfs-live-service subpackage install the systemd
# service and udev rules.
#mkdir -p %buildroot%systemd_unitdir
#mkdir -p %buildroot%_sysconfdir/udev/rules.d
#install -m 0644 %%SOURCE2 %buildroot%systemd_unitdir
#install -m 0644 %%SOURCE3 %buildroot%_sysconfdir/udev/rules.d

%find_lang %name

%files -f %name.lang
%doc COPYING README
%_bindir/libguestfs-test-tool
%_libdir/libguestfs.so.*
%_man1dir/guestfs-testing.1*
%_man1dir/libguestfs-test-tool.1*

%files devel
%doc AUTHORS BUGS HACKING TODO README RELEASE-NOTES ROADMAP
%doc examples/*.c
%doc installed-docs/*
%_libdir/libguestfs.so
%_man1dir/guestfs-recipes.1*
%_man3dir/guestfs.3*
%_man3dir/guestfs-examples.3*
%_man3dir/libguestfs.3*
%_includedir/guestfs.h
%_pkgconfigdir/libguestfs.pc

%files tools
%doc README
%config(noreplace) %_sysconfdir/libguestfs-tools.conf
%_bindir/guestfish
%_man1dir/guestfish.1*
%_bindir/guestmount
%_man1dir/guestmount.1*
%_bindir/virt-alignment-scan
%_man1dir/virt-alignment-scan.1*
%_bindir/virt-cat
%_man1dir/virt-cat.1*
%_bindir/virt-copy-in
%_man1dir/virt-copy-in.1*
%_bindir/virt-copy-out
%_man1dir/virt-copy-out.1*
%_bindir/virt-df
%_man1dir/virt-df.1*
%_bindir/virt-edit
%_man1dir/virt-edit.1*
%_bindir/virt-filesystems
%_man1dir/virt-filesystems.1*
%_bindir/virt-inspector
%_man1dir/virt-inspector.1*
%_bindir/virt-ls
%_man1dir/virt-ls.1*
%_bindir/virt-rescue
%_man1dir/virt-rescue.1*
%_bindir/virt-resize
%_man1dir/virt-resize.1*
%_bindir/virt-sparsify
%_man1dir/virt-sparsify.1*
%_bindir/virt-tar-in
%_man1dir/virt-tar-in.1*
%_bindir/virt-tar-out
%_man1dir/virt-tar-out.1*
%_bindir/virt-list-filesystems
%_man1dir/virt-list-filesystems.1*
%_bindir/virt-list-partitions
%_man1dir/virt-list-partitions.1*
%_bindir/virt-make-fs
%_man1dir/virt-make-fs.1*
%_bindir/virt-sysprep
%_man1dir/virt-sysprep.1*
%_bindir/virt-tar
%_man1dir/virt-tar.1*
%_bindir/virt-win-reg
%_man1dir/virt-win-reg.1*

#%files live-service
#%doc COPYING README
#%_sbindir/guestfsd
#%systemd_unitdir/guestfsd.service
#%_sysconfdir/udev/rules.d/99-guestfsd.rules

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
#%_man3dir/Sys::Guestfs.3pm*
#%_man3dir/Sys::Guestfs::Lib.3pm*
%_man3dir/guestfs-perl.3*
%endif #perl

%if_enabled python
%files -n python-module-%name
%doc python/examples/*.py
%python_sitelibdir/*
%python_sitelibdir/*.py
%python_sitelibdir/*.pyc
%python_sitelibdir/*.pyo
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
%_datadir/javadoc/%name-java-%version

%if_enabled php
%files -n php5-%name
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

%files -n bash-completion-libguestfs
%_sysconfdir/bash_completion.d/guestfish-bash-completion.sh

%changelog
* Thu Jan 12 2012 Alexey Shabalin <shaba@altlinux.ru> 1.15.16-alt1
- initial build

