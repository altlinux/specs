Name: picolisp
Version: 3.1.4
Release: alt1

Summary: Interpreted Lisp
License: MIT
Group: Development/Lisp

Url: http://picolisp.com
Source: http://software-lab.de/picoLisp-%version.tgz
Source100: picolisp.watch

# 64-bit build bootstraps using 32-bit one or Java
BuildRequires: java /proc

# trickery inside
%set_verify_elf_method textrel=none

# pretty much hardwired
%define _libdir %_usr/lib

%description
PicoLisp can be viewed from two different aspects:
        as a general purpose programming language,
     and a dedicated application server framework.

%prep
%setup -n picoLisp

%build
%ifarch x86_64 ia64 ppc64 sparc64 s390x
cd src64
%else
cd src
%endif
make
cd ..

%install
mkdir -p %buildroot{%_bindir,%_libdir/%name,%_datadir}
cp -a bin/{picolisp,pil} %buildroot%_bindir/
# TODO: emacs subpackage
rm -rf lib/el
# lib/ and lib.l
cp -a lib* %buildroot%_libdir/%name/
# as per INSTALL
ln -s ../lib/%name %buildroot%_datadir/%name

%files
%doc CHANGES CREDITS README
%_bindir/*
%_libdir/%name/
%_datadir/%name/

%changelog
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
