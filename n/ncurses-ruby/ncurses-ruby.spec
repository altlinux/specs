Name: ncurses-ruby
Version: 1.2.4
Release: alt2

Summary: A Ruby module for accessing the ncurses library
License: LGPLv2.1
Group: Development/Ruby
Url: http://ncurses-ruby.berlios.de/

Source0: %name-%version.tar.bz2
Patch0: ncurses-ruby-alt-STR2CSTR.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sat Dec 12 2009 (-bi)
BuildRequires: libncurses-devel libruby-devel

%description
This ruby extension makes most functions, constants, and external variables of
the C library ncurses accessible from the Ruby programming language.

The panel library (for support of overlapping windows) and the form library
(providing simple ui-widgets) are also wrapped.

%prep
%setup -q
%patch0 -p2

%build
%ruby_configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc Changes README THANKS TODO
%ruby_sitelibdir/ncurses.rb
%ruby_sitearchdir/ncurses_bin.so

%changelog
* Sun Sep 26 2010 Alexey I. Froloff <raorn@altlinux.org> 1.2.4-alt2
- Rebuilt with Ruby 1.9.2

* Sat Dec 12 2009 Igor Zubkov <icesik@altlinux.org> 1.2.4-alt1
- build for Sisyphus

