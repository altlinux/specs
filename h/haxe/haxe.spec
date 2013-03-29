Name: haxe
Version: 3.0.0
Release: alt0.1

Summary: Haxe is an open source programming language

License: GPLv2
Group: Development/Other
Url: http://haxe.org

# https://github.com/haxe-mirrors/haxe.git
Source: %name-%version.tar

# Automatically added by buildreq on Fri Mar 29 2013
# optimized out: ocaml ocaml-runtime
BuildRequires: camlp4 zlib-devel

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
%setup

%build
%__make

%install
#makeinstall_std INSTALL_DIR=%buildroot%_prefix
install -D haxe %buildroot%_bindir/haxe
mkdir -p %buildroot/%haxelib/
cp -a std %buildroot/%haxelib/
# FIXME: haxelib dir
mkdir -p %buildroot/%haxelib/lib/
#mkdir %buildroot/%_localstatedir/haxe/
#chmod 755 $(INSTALL_DIR)/lib/haxe/lib
install -D std/tools/haxelib/haxelib.sh %buildroot%_bindir/haxelib
install -D std/tools/haxedoc/haxedoc.sh %buildroot%_bindir/haxedoc

%files
%_bindir/%name
%_bindir/haxedoc
%_bindir/haxelib
%haxelib/

%changelog
* Fri Mar 29 2013 Vitaly Lipatov <lav@altlinux.ru> 3.0.0-alt0.1
- Initial build for ALTLinux Sisyphus

