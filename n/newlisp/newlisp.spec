%def_with readline
%def_with utf8
%def_with ext_pcre
%def_disable check

%define Name newLISP
Name: newlisp
Version: 10.2.8
Release: alt1
Summary: Lisp-like, general purpose scripting language
License: %gpl3only
Group: Development/Lisp
URL: http://www.%name.org
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: http://%name.nfshost.com/downloads/development/%name-%version.tgz
Source1: Makefile.alt
Patch0: %name-9.4.4-test.patch
Patch1: %name-9.4.4-shebang.patch
Patch2: %name-9.4.4-ext_pcre.patch

# Automatically added by buildreq on Sat Aug 02 2008
#BuildRequires: libpcre-devel libreadline-devel
%{?_with_readline:BuildRequires: libreadline-devel}
%{?_with_ext_pcre:BuildRequires: libpcre-devel}
BuildRequires: rpm-build-licenses vim-devel

%description
%Name is a LISP-like scripting language for doing things you
typically do with scripting languages: programming for the internet,
system administration, text processing, gluing other programs together,
etc. %Name is a scripting LISP for people who are fascinated by
LISP's beauty and power of expression, but who need it stripped down to
easy-to-learn essentials. %Name is small on resources like disk space
and memory but has a deep, practical API.


%package modules
Summary: %Name modules
Group: Development/Lisp
Requires: %name = %version-%release
BuildArch: noarch

%description modules
%Name is a LISP-like scripting language for doing things you
typically do with scripting languages: programming for the internet,
system administration, text processing, gluing other programs together,
etc. %Name is a scripting LISP for people who are fascinated by
LISP's beauty and power of expression, but who need it stripped down to
easy-to-learn essentials. %Name is small on resources like disk space
and memory but has a deep, practical API.
This package contains standard modules for %Name.


%package guiserver
Summary: Application for generating GUIs and 2D graphics for %Name
Group: Development/Lisp
Requires: %name-modules = %version-%release
Requires: jre
BuildArch: noarch

%description guiserver
guiserver.lsp is a module for interfacing to guiserver.jar a Java
server application for generating GUIs (graphical user interfaces) and
2D graphics for %Name applications. The guiserver.lsp module
implements a %Name API much smaller and more abstract than the APIs
of the Java Swing libraries which it interfaces with. Because of this,
GUI applications can be built much faster than when using the original
Java APIs.


%package doc
Summary: %Name documentation and samples
Group: Documentation
License: %fdl
BuildArch: noarch
Provides: %name-examples = %version-%release

%description doc
%Name is a LISP-like scripting language for doing things you
typically do with scripting languages: programming for the internet,
system administration, text processing, gluing other programs together,
etc. %Name is a scripting LISP for people who are fascinated by
LISP's beauty and power of expression, but who need it stripped down to
easy-to-learn essentials. %Name is small on resources like disk space
and memory but has a deep, practical API.
This package contains %Name documentation and examples.


%package -n vim-plugin-%name-syntax
Summary: VIm syntax for %Name
Group: Development/Lisp
BuildArch: noarch
Requires: vim-common

%description -n vim-plugin-%name-syntax
This package contains VIm syntax for %Name.


%package -n nano-%name-syntax
Summary: nano syntax for %Name
Group: Development/Lisp
BuildArch: noarch
Requires: nano

%description -n nano-%name-syntax
This package contains nano syntax for %Name.


%prep
%setup
#patch0 -p1
%patch1 -p1
%patch2 -p1
install -m 0644 %SOURCE1 ./Makefile.alt


%build
%add_optflags %{?_with_readline:-DREADLINE} %{?_with_utf8:-DSUPPORT_UTF8}
%ifarch x86_64 k8 opteron nocona
%add_optflags -DNEWLISP64
%endif
%if_with ext_pcre
%add_optflags -I%_includedir/pcre
%else
%add_optflags -I.
%endif
cat > config.mk <<__EOF__
CFLAGS = %optflags
LIBS=%{?_with_readline:-lreadline} %{?_with_ext_pcre:-lpcre}
OBJS=%{?_with_utf8:nl-utf8.o} %{!?_with_ext_pcre:pcre.o}
__EOF__
%make_build -f Makefile.alt
%{?_enable_check:%make_build test}


%install
install -d -m 0755 %buildroot{%_bindir,%vim_syntax_dir,%_datadir/nano}
%make_install bindir=%buildroot%_bindir datadir=%buildroot%_datadir install
chmod 755 %buildroot%_datadir/%name/guiserver/*
mv %buildroot%_docdir/%name{,-%version}
mv %buildroot{%_datadir/%name/util,%vim_syntax_dir}/%name.vim
mv %buildroot%_datadir/{%name/util/,nano/%name.}nanorc
rm -f %buildroot%_docdir/%name-%version/{,*/}COPYING

rm -f %buildroot%_bindir/%name
cd %buildroot%_bindir
ln -s %name-%version %name

%files
%_bindir/*
%dir %_datadir/%name
%_datadir/%name/util


%files modules
%_datadir/%name/modules


%files guiserver
%_datadir/%name/guiserver.*
%_datadir/%name/*.png


%files doc
%_docdir/%name-%version
%dir %_datadir/%name
%_datadir/%name/guiserver
%_datadir/%name/init.lsp.example


%files -n vim-plugin-%name-syntax
%vim_syntax_dir/*


%files -n nano-%name-syntax
%_datadir/nano/*


%changelog
* Sat Dec 18 2010 Ilya Mashkin <oddity@altlinux.ru> 10.2.8-alt1
- 10.2.8

* Wed Sep 24 2008 Led <led@altlinux.ru> 9.9.4-alt1
- 9.9.4

* Mon Sep 22 2008 Led <led@altlinux.ru> 9.9.2-alt1
- 9.9.2

* Tue Sep 02 2008 Led <led@altlinux.ru> 9.4.8-alt1
- 9.4.8

* Mon Aug 25 2008 Led <led@altlinux.ru> 9.4.7-alt1
- 9.4.7

* Tue Aug 19 2008 Led <led@altlinux.ru> 9.4.6-alt1
- 9.4.6

* Sat Aug 02 2008 Led <led@altlinux.ru> 9.4.4-alt1
- initial build
