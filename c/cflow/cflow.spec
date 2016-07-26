Name: cflow
Version: 1.5
Release: alt1

Summary: Analyzes C files charting control flow within the program

License: GPLv2+
Group: Development/Other
Url: http://www.gnu.org/software/cflow/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://ftp.gnu.org/gnu/cflow/%name-%version.tar.bz2

# to install lisp files
#BuildRequires: emacs

Requires(post):  info
Requires(preun): info

Source44: import.info
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
GNU cflow analyzes a collection of C source files and prints a graph,
charting control flow within the program.

GNU cflow is able to produce both direct and inverted flowgraphs for C
sources. Optionally a cross-reference listing can be generated. Two
output formats are implemented: POSIX and GNU (extended).

%prep
%setup

%build
# fix broken configure.am logic
export EMACS=yes
%configure --with-lispdir=%_datadir/emacs/site-lisp/
%make_build

%install
%makeinstall_std
%find_lang %name
rm -f %buildroot/%_infodir/dir

%check
make check

%files -f %name.lang
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%_bindir/%name
%_infodir/%name.info.*
%_man1dir/*
%_datadir/emacs/site-lisp/%name-mode.el

%changelog
* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- new version 1.5 (with rpmrb script)

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.4-alt2.1
- NMU: added BR: texinfo

* Tue Nov 17 2015 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt2
- initial manual build for ALT Linux Sisyphus

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_9
- new version

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_5
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3
- update to new release by fcimport

* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_2
- fc import

