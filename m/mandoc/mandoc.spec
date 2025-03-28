%def_with check

Name: mandoc
Version: 1.14.6
Release: alt1

Summary: mandoc (formerly mdocml) UNIX manpage compiler toolset
License: ISC
Group: System/Base
Url: http://mandoc.bsd.lv/

Source0: %name-%version.tar
Source1: configure.local

BuildRequires: zlib-devel less

%if_with check
BuildRequires: perl
%endif

%description
mandoc is a suite of tools compiling mdoc, the roff macro language of choice
for BSD manual pages, and man, the predominant historical language for UNIX
manuals. It is small, ISO C, ISC-licensed, and quite fast. The main component
of the toolset is the mandoc utility program, based on the libmandoc validating
compiler, to format output for UTF-8 and ASCII UNIX terminals, HTML 5,
PostScript, and PDF.

%prep
%setup
cp %SOURCE1 .

%build
# Not GNU Autotools
./configure
%make_build

%install
%make DESTDIR=%buildroot base-install

# To avoid conflicts with soelim from GNU
mv %buildroot%_bindir/soelim %buildroot%_bindir/soelim.%name
mv %buildroot%_man1dir/soelim.1 %buildroot%_man1dir/soelim.%name.1

# To avoid conflict in case of man appearing in another package
mv %buildroot%_man7dir/roff.7 %buildroot%_man7dir/roff.%name.7

# Remove unnecessary symlinks to mandoc
rm -v %buildroot%_bindir/man
rm -v %buildroot%_bindir/apropos
rm -v %buildroot%_bindir/whatis
rm -v %buildroot%_sbindir/makewhatis

# Remove unnecessary man pages
rm -v %buildroot%_man1dir/apropos.1
rm -v %buildroot%_man1dir/man.1
rm -v %buildroot%_man1dir/whatis.1
rm -v %buildroot%_man7dir/eqn.7
rm -v %buildroot%_man7dir/man.7
rm -v %buildroot%_man7dir/tbl.7
rm -v %buildroot%_man8dir/makewhatis.8

%check
%make_build regress

%files
%_bindir/de%name
%_bindir/%name
%_bindir/soelim.%name
%_man1dir/de%name.1.xz
%_man1dir/%name.1.xz
%_man1dir/soelim.%name.1.xz
%_man5dir/%name.db.5.xz
%_man5dir/%name.conf.5.xz
%_man7dir/%{name}_char.7.xz
%_man7dir/mdoc.7.xz
%_man7dir/roff.%name.7.xz

%changelog
* Mon Mar 17 2025 Ulysses Apokin <ulysses@altlinux.org> 1.14.6-alt1
- Initial build for Sisyphus.
