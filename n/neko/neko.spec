Name: neko
Version: 2.0.0
Release: alt3

Summary: The Neko Programming Language

License: LGPL
Group: Development/Other
Url: http://haxe.org

# https://github.com/HaxeFoundation/neko.git
Source: %name-%version.tar

# manually removed:  python3 ruby ruby-stdlibs
# Automatically added by buildreq on Tue Aug 06 2013
# optimized out: fontconfig fontconfig-devel glib2-devel libapr1-devel libaprutil1-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libssl-devel pkg-config python3-base zlib-devel
BuildRequires: apache2-devel libgc-devel libgtk+2-devel libmysqlclient-devel libpcre-devel libsqlite3-devel

%description
Neko is an intermediate programming language. It has been designed to
provide a common runtime for several different languages. Learning and
using Neko is very easy, but you're not supposed to directly program in
Neko. Instead, you can write a generator from your preferred language to
Neko and then use the Neko runtime to compile, run, and access libraries.

Neko is a good way for language designers to focus on design and reuse a
fast and well-designed runtime, as well as existing libraries for
 accessing filesystem, network, databases, xml...

%prep
%setup

%build
%__make

%install
mkdir -p %buildroot{%_libdir,%_bindir,%_libexecdir}
make install INSTALL_PREFIX=%buildroot%prefix LIBDIRNAME=%_lib

%files
%_bindir/%name
%_bindir/nekoc
%_bindir/nekoml
%_bindir/nekoml.std
%_bindir/nekotools
%_libdir/*.so
%_libexecdir/%name/
%_includedir/*.h

%changelog
* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt3
- Fixed build with new glibc.

* Thu May 05 2016 Sergey Alembekov <rt@altlinux.ru> 2.0.0-alt2
- backport apache-2.4 support

* Mon Aug 05 2013 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALTLinux Sisyphus
