%define        _unpackaged_files_terminate_build 1

Name:          rvm
Version:       1.29.12.125
Release:       alt0.3
Summary:       Ruby enVironment Manager (RVM)
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://rvm.io
Vcs:           https://github.com/rvm/rvm.git
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-macros-valgrind
BuildRequires: /proc /dev
BuildRequires: curl
BuildRequires: gnupg2

Requires:      %name-devel
Requires:      gem(gem-wrappers)
Requires:      gem(rubygems-bundler)
Requires:      gem(rake)
Requires:      gem(rvm)
Requires:      gem(bundler)
Requires:      gem(openssl)

%description
RVM is the acronym of Ruby enVironment Manager. It manages Ruby application
environments and enables switching between them.

Homepage and more info at https://rvm.io

Currently supported following ruby interpreters:

* ruby - MRI ruby (The Gold Standard)
* ironruby - a .NET ruby
* jruby - Java implementation of the ruby
* macruby - implementation of ruby 1.9 directly on top of macOS core
  technologies
* maglev - 64-bit implementation on top of VMware's GemStone
* mruby - lightweight ruby
* opal - ruby to JavaScript compiler
* rbx - Rubinius - a next generation virtual machine VM for ruby
* topaz - high performance ruby, written in RPython
* truffleruby - high performance ruby using GraalVM

%package       devel
Summary:       Ruby enVironment Manager (RVM) pure development package with RVM code
Group:         Development/Ruby
Autoreq:       yes,noshell

Requires:      setup
Requires:      curl
Requires:      gnupg2
Requires:      gperf
Requires:      gcc
Requires:      gcc-c++
Requires:      doxygen
Requires:      autoconf
Requires:      groff-base
Requires:      rust
Requires:      libssl-devel
Requires:      libgmp-devel
Requires:      libreadline-devel
Requires:      libdb4-devel
Requires:      libffi-devel
Requires:      libgdbm-devel
Requires:      libncursesw-devel
Requires:      zlib-devel
Requires:      libyaml-devel
%ifarch %valgrind_arches
Requires:      valgrind-devel
%endif

%description   devel
RVM is the acronym of Ruby enVironment Manager. It manages Ruby application
environments and enables switching between them.

Homepage and more info at https://rvm.io

Currently supported following ruby interpreters:

* ruby - MRI ruby (The Gold Standard)
* ironruby - a .NET ruby
* jruby - Java implementation of the ruby
* macruby - implementation of ruby 1.9 directly on top of macOS core
  technologies
* maglev - 64-bit implementation on top of VMware's GemStone
* mruby - lightweight ruby
* opal - ruby to JavaScript compiler
* rbx - Rubinius - a next generation virtual machine VM for ruby
* topaz - high performance ruby, written in RPython
* truffleruby - high performance ruby using GraalVM

Development code package.


%prep
%setup
%autopatch -p1

%install
./install --auto-dotfiles --path %buildroot%_libexecdir/%name
mkdir -p %buildroot%_bindir/ %buildroot%_sysconfdir/%name/ %buildroot%_sysconfdir/bashrc.d %buildroot%_localstatedir/%name
pushd %buildroot%_libexecdir/%name
ls -d tmp wrappers environments src archives rubies gems user |while read i; do \
      cp -rf "$i" %buildroot%_localstatedir/%name/; \
      rm -rf $i; \
      ln -s %_localstatedir/%name/$i $i; \
   done
mkdir -p %buildroot%{_var}/log/%name
ls -d log |while read i; do rm -rf $i; ln -s %{_var}/$i/%name $i; done
popd
ls %buildroot%_libexecdir/%name/bin/*| while read f; do fn="$(basename "$f")"; ln -s %_libexecdir/%name/bin/"$fn" %buildroot%_bindir/"$fn"; done
cp -rp %buildroot%_libexecdir/%name/config/* %buildroot%_sysconfdir/%name/
cat > %buildroot%_sysconfdir/bashrc.d/%name.sh << PROFILE
[[ -s "%_libexecdir/%name/scripts/rvm" ]] && source "%_libexecdir/%name/scripts/rvm" # Load RVM into a shell session *as a function*
PROFILE

%pre           devel
ln -sf /proc/self/fd /dev/fd >/dev/null 2>&1 || exit 0

%files
%doc README* CHANGELOG* CONTRIBUTING* FORMATTING* HACKING* VERSION

%files         devel
%attr(755,root,root) %config(noreplace) %_sysconfdir/bashrc.d/%name.sh
%config(noreplace) %_sysconfdir/%name
%_bindir/*
%_libexecdir/%name
%attr(775,root,rvm) %_localstatedir/%name
%attr(775,root,rvm) %_localstatedir/%name/wrappers
%attr(775,root,rvm) %_localstatedir/%name/environments
%attr(775,root,rvm) %_localstatedir/%name/src
%attr(775,root,rvm) %_localstatedir/%name/archives
%attr(775,root,rvm) %_localstatedir/%name/rubies
%attr(775,root,rvm) %_localstatedir/%name/gems
%attr(775,root,rvm) %_localstatedir/%name/user
%attr(775,root,rvm) %_localstatedir/%name/tmp
%dir %attr(775,root,rvm) %_logdir/%name

%changelog
* Fri May 17 2024 Pavel Skrylev <majioa@altlinux.org> 1.29.12.125-alt0.3
- ! fixed dep to true binary for devel in per section (closes #50385)

* Thu Apr 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.29.12.125-alt0.2
- - removed PATH variable from bashrc

* Wed Feb 07 2024 Pavel Skrylev <majioa@altlinux.org> 1.29.12.125-alt0.1
- ^ 1.29.12 -> 1.29.12p125
- ! clean up pre script
- ! minor fixed

* Thu Dec 14 2023 Pavel Skrylev <majioa@altlinux.org> 1.29.12-alt2
- ! fixed rvm build for custom user-space rubies

* Wed Aug 02 2023 Pavel Skrylev <majioa@altlinux.org> 1.29.12-alt1
- Initial build v1.29.12 for Sisyphus.
