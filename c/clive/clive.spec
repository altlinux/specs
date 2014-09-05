Name: clive
Version: 0.4.10
Release: alt1

Summary: clive is a console client for LiveJournal.com
License: BSD-like
Group: Networking/Other
Url: http://sourceforge.net/projects/ljclive

Source0: %name-%version.tar.gz

BuildPreReq: libbsd-devel

%description
clive is a console client for LiveJournal.com.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS BUGS ChangeLog README
%_bindir/clive
%_man1dir/clive.*
%dir %_datadir/clive
%_datadir/clive/cliverc-example.conf

%changelog
* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.10-alt1
- Version 0.4.10

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.5-alt3.qa1
- NMU: rebuilt for debuginfo.

* Sat Jan 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.4.5-alt3
- Changed packager field.
- Added autoreconf macro.
- Fixed package URL.

* Sat Nov 19 2005 Igor Zubkov <icesik@altlinux.ru> 0.4.5-alt2
- add url to package
- add docs

* Wed Jun 29 2005 Igor Zubkov <icesik@altlinux.ru> 0.4.5-alt1
- Initial build for Sisyphus
