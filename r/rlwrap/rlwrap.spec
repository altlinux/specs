Name: rlwrap
Version: 0.37
Release: alt1
Serial: 1

Summary: Line editor - readline wrapper
License: GCL
Group: Editors
Url: http://utopia.knoware.nl/~hlub/uck/rlwrap

Source0: %name-%version.tar.gz
Source1: rlwrap_cmucl_completions

BuildRequires: libreadline-devel libncurses-devel
%add_perl_lib_path %_datadir/%name/filters

%description
rlwrap is a 'readline wrapper', a small utility that uses the GNU
readline library to allow the editing of keyboard input for any
command.

%prep
%setup

%build
%configure
%make

%install
%makeinstall

# Extra complition tables
#   cmucl & sbcl
install -D -m644 %SOURCE1 %buildroot/%_datadir/%name/completions/lisp
install -D -m644 %SOURCE1 %buildroot/%_datadir/%name/completions/sbcl

%files
%_bindir/*
%_man1dir/*
%_man3dir/*
%_datadir/%name

%changelog
* Tue Aug 20 2013 Fr. Br. George <george@altlinux.ru> 1:0.37-alt1
- Autobuild version bump to 0.37
- Introducing perl filters

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1:0.30-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Jan 08 2009 Ilya Mashkin <oddity@altlinux.ru> 1:0.30-alt1
- 0.30

* Fri Sep 21 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:0.21-alt2
- Remove Russian summary and translation.

* Tue Oct 10 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:0.21-alt1
- Rollback to 0.21 - latest version which seems to be compatible
  with current readline and/or toolchain.

* Sat Sep 30 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.26-alt1
- New version.

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.24-alt1.1
- Rebuilt with libreadline.so.5.

* Sun Oct 23 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.24-alt1
- New version.

* Sat Feb 19 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.18-alt3
- Reduild with gcc 3.4.

* Mon Dec 13 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.18-alt2
- Fix directories.

* Sun May 09 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.18-alt1
- New version.

* Sat Aug 30 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.16-alt1
- Initial ALT Linux release

