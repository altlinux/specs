Name: clive
Version: 0.4.5
Release: alt3

Summary: clive is a console client for LiveJournal.com
License: BSD-like
Group: Networking/Other
Url: http://sourceforge.net/projects/ljclive
Packager: Pavlov Konstantin <thresh@altlinux.ru>

Source0: %name-%version.tar.gz

Patch0: clive-0.4.5-alt-warning.patch

%description
clive is a console client for LiveJournal.com.

%prep
%setup -q
%patch0 -p1

%build
%__autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS BUGS ChangeLog
%_bindir/clive
%_man1dir/clive.*
%dir %_datadir/clive
%_datadir/clive/cliverc-example.conf

%changelog
* Sat Jan 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.4.5-alt3
- Changed packager field.
- Added autoreconf macro.
- Fixed package URL.

* Sat Nov 19 2005 Igor Zubkov <icesik@altlinux.ru> 0.4.5-alt2
- add url to package
- add docs

* Wed Jun 29 2005 Igor Zubkov <icesik@altlinux.ru> 0.4.5-alt1
- Initial build for Sisyphus
