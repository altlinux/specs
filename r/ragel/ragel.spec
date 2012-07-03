# vim: set ft=spec: -*- rpm-spec -*-

Name: ragel
Version: 6.6
Release: alt1

Summary: Ragel State Machine Compiler
Group: Development/Other
License: GPLv2
Url: http://www.complang.org/ragel/

Packager: Sir Raorn <raorn@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Fri Jul 25 2008
BuildRequires: gcc-c++ ghostscript-classic tetex-context tetex-latex transfig vim-devel

%description
Ragel compiles executable finite state machines from regular
languages. Ragel targets C, C++, Objective-C, D, Java and Ruby.
Ragel state machines can not only recognize byte sequences as
regular expression machines do, but can also execute code at
arbitrary points in the recognition of a regular language. Code
embedding is done using inline operators that do not disrupt the
regular language syntax.

%package -n vim-plugin-%name-syntax
Summary: Vim syntax for Ragel
Group: Editors
PreReq: vim-common

%description -n vim-plugin-%name-syntax
Vim syntax for Ragel.

%prep
%setup
%patch -p1

%build
%configure
%make_build
%make_build -C doc

%install
mkdir -p %buildroot{%vim_syntax_dir,%vim_ftdetect_dir}
%makeinstall_std
%makeinstall_std docdir=%_docdir/%name-%version -C doc
cp CREDITS README TODO %buildroot%_docdir/%name-%version

install -p -m644 ragel.vim %buildroot%vim_syntax_dir/
cat <<EOF >%buildroot%vim_ftdetect_dir/ragel.vim
au BufNewFile,BufRead *.rl  setf ragel
EOF

%check
%make -C test check

%files
%doc %_docdir/%name-%version
%_bindir/*
%_man1dir/*

%files -n vim-plugin-%name-syntax
%vim_syntax_dir/ragel.vim
%vim_ftdetect_dir/ragel.vim

%changelog
* Thu Apr 15 2010 Alexey I. Froloff <raorn@altlinux.org> 6.6-alt1
- [6.6]

* Fri Jul 25 2008 Sir Raorn <raorn@altlinux.ru> 6.2-alt1
- Built for Sisyphus

