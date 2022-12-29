Name: picolisp
Version: 22.12
Release: alt1

Summary: Interpreted Lisp
License: MIT
Group: Development/Lisp

Url: http://picolisp.com
Source: http://software-lab.de/picoLisp-%version.tgz
Source100: picolisp.watch



BuildRequires:  clang llvm libreadline-devel libssl-devel libffi-devel
# 64-bit build bootstraps using 32-bit one or Java
#BuildRequires: java /proc
# armh-alt-linux-gnueabi-gcc: error: unrecognized command line option '-m32'; did you mean '-mbe32'?
ExcludeArch: armh %ix86

# trickery inside
%set_verify_elf_method textrel=none

# pretty much hardwired
#define _libdir %_usr/lib
#- undefine usrlib (Closes: #32231)

%description
PicoLisp can be viewed from two different aspects:
        as a general purpose programming language,
     and a dedicated application server framework.

%prep
%setup -n pil21

%build
# :)
#if [ %_lib = lib64 ]; then
cd src
#else
#	cd src
#fi
make
cd ..

%install
mkdir -p %buildroot{%_bindir,%_libdir/%name,%_datadir,%_man1dir}
cp -a bin/{picolisp,pil} %buildroot%_bindir/
# TODO: emacs subpackage
rm -rf lib/el
# lib/ and lib.l
cp -a lib* %buildroot%_libdir/%name/
# as per INSTALL
ln -s ../lib64/%name %buildroot%_datadir/%name
#ln -s ../lib64/%name %buildroot%_datadir/%name
cp man/man1/* %buildroot%_man1dir

%files
%doc README
%_bindir/*
%_libdir/%name/
%_datadir/%name/
%_man1dir/*

%changelog
* Thu Dec 29 2022 Ilya Mashkin <oddity@altlinux.ru> 22.12-alt1
- 22.12

* Mon Oct 03 2022 Ilya Mashkin <oddity@altlinux.ru> 22.9-alt1
- 22.9

* Sat Jul 02 2022 Ilya Mashkin <oddity@altlinux.ru> 22.6-alt1
- 22.6

* Wed Mar 23 2022 Ilya Mashkin <oddity@altlinux.ru> 22.3-alt1
- 22.3

* Sun Jan 02 2022 Ilya Mashkin <oddity@altlinux.ru> 21.12-alt1
- 21.12

* Fri Aug 27 2021 Ilya Mashkin <oddity@altlinux.ru> 21.6-alt1
- 21.6
- build with clang, llvm etc
- undefine usrlib (Closes: #32231)

* Tue Jun 30 2020 Michael Shigorin <mike@altlinux.org> 20.6-alt2
- ExcludeArch: armh

* Mon Jun 29 2020 Michael Shigorin <mike@altlinux.org> 20.6-alt1
- new version (watch file uupdate)

* Sun Dec 29 2019 Michael Shigorin <mike@altlinux.org> 19.12-alt1
- new version (watch file uupdate)

* Mon Jul 01 2019 Michael Shigorin <mike@altlinux.org> 19.6-alt1
- new version (watch file uupdate)

* Sat Jan 19 2019 Michael Shigorin <mike@altlinux.org> 18.12-alt2
- fix 64-bitness test

* Sun Dec 30 2018 Michael Shigorin <mike@altlinux.org> 18.12-alt1
- new version (watch file uupdate)

* Thu Jun 28 2018 Michael Shigorin <mike@altlinux.org> 18.6-alt1
- new version (watch file uupdate)

* Tue Dec 26 2017 Michael Shigorin <mike@altlinux.org> 17.12-alt1
- new version (watch file uupdate)

* Thu Jun 29 2017 Michael Shigorin <mike@altlinux.org> 17.6-alt1
- new version (watch file uupdate)

* Thu Dec 08 2016 Michael Shigorin <mike@altlinux.org> 16.12-alt1
- new version (watch file uupdate)

* Wed Jun 29 2016 Michael Shigorin <mike@altlinux.org> 16.6-alt1
- new version (watch file uupdate)

* Thu Feb 18 2016 Michael Shigorin <mike@altlinux.org> 16.2-alt1
- new version (watch file uupdate)

* Tue Nov 24 2015 Michael Shigorin <mike@altlinux.org> 15.11-alt1
- new version (watch file uupdate)

* Mon Jun 22 2015 Michael Shigorin <mike@altlinux.org> 3.1.11-alt1
- new version (watch file uupdate)

* Sat Apr 18 2015 Michael Shigorin <mike@altlinux.org> 3.1.10-alt1
- new version (watch file uupdate)

* Sun Mar 22 2015 Michael Shigorin <mike@altlinux.org> 3.1.9-alt1
- new version (watch file uupdate)

* Wed Oct 01 2014 Michael Shigorin <mike@altlinux.org> 3.1.8-alt1
- new version (watch file uupdate)

* Mon Jun 30 2014 Michael Shigorin <mike@altlinux.org> 3.1.7-alt1
- new version (watch file uupdate)

* Wed Apr 02 2014 Michael Shigorin <mike@altlinux.org> 3.1.6-alt1
- new version (watch file uupdate)

* Thu Jan 02 2014 Michael Shigorin <mike@altlinux.org> 3.1.5-alt1
- new version (watch file uupdate)

* Fri Dec 06 2013 Michael Shigorin <mike@altlinux.org> 3.1.4-alt1
- added watch file
- new version (watch file uupdate)

* Mon Nov 26 2012 Michael Shigorin <mike@altlinux.org> 3.1.0-alt2
- actually working package for Sisyphus

* Wed Jun 27 2012 Michael Shigorin <mike@altlinux.org> 3.1.0-alt1
- 3.1.0
- spec based on fedora proposed one (rhbz#783294) and cleaned up

* Thu Jan 19 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 3.0.9-1
- initial packaging
