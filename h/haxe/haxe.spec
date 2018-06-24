Name: haxe
Version: 3.4.7
Release: alt1

Summary: Haxe is an open source programming language

License: GPLv2
Group: Development/Other
Url: http://haxe.org

# Source-git: https://github.com/HaxeFoundation/haxe.git
Source: %name-%version.tar
Source1: haxe-postsubmodules-%version.tar

BuildRequires: rpm-build-intro zlib-devel libpcre-devel neko
BuildRequires: ocaml-camlp4-devel >= 4.02

%define haxelib %_prefix/lib/%name

%description
Haxe (pronounced as hex) is an open source programming language.

While most other languages are bound to their own platform
(Java to the JVM, C# to .Net, ActionScript to the Flash Player),
Haxe is a multiplatform language.

The idea behind Haxe is to let the developer choose the best platform
for a given job. In general, this is not easy to do,
because every new platform comes with its own programming language.

What Haxe provides you with is:
* a standardized language with many good features
* a standard library (including Date, Xml, Math...) that works the same on all platforms
* platform-specific libraries : the full APIs for a given platform are accessible from Haxe

%prep
%setup -a1
%__subst "s|-I pcre|-I %_includedir/pcre|" libs/pcre/Makefile

%build
export OCAMLPARAM="safe-string=0,_"
#export CFLAGS="%optflags -I%_includedir/pcre"
%__make

%install
%makeinstall_std
# hack due broken make
rm -f %buildroot%_bindir/{haxe,haxelib}
%__ln_sr %buildroot%haxelib/haxe  %buildroot%_bindir/haxe
%__ln_sr %buildroot%haxelib/haxelib  %buildroot%_bindir/haxelib

%files
%_bindir/haxe
%_bindir/haxelib
%haxelib/

%changelog
* Sun Jun 24 2018 Vitaly Lipatov <lav@altlinux.ru> 3.4.7-alt1
- build 3.4.7 version

* Mon Aug 05 2013 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt1
- merge with tag v3-00, real 3.0.0 version

* Fri Mar 29 2013 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt0.1
- Initial build for ALTLinux Sisyphus

