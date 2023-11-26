# Spec file for pv - Pipe Viewer 

Name: pv
Version: 1.8.5
Release: alt1

Summary: Pipe Viewer

License: %gpl3plus
Group: Text tools
URL: http://www.ivarch.com/programs/pv.shtml

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

%description
pv - Pipe Viewer - is a terminal-based tool for monitoring the
progress of data through a pipeline. It can be inserted into
any normal pipeline between two processes to give a visual
indication of how quickly data is passing through, how long it
has taken, how near to completion it is, and an estimate of
how long it will be until completion.

Additional support is available for multiple instances working
in tandem, to given a visual indicator of relative throughput
in a complex pipeline.

%prep
%setup -q

%build
%autoreconf

%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang %name
pushd docs
mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-3.0+ %_docdir/%name/COPYING) COPYING
popd

%files -f %name.lang
%doc docs/NEWS.md docs/TODO.md docs/ACKNOWLEDGEMENTS.md docs/DEVELOPERS.md
%doc --no-dereference docs/COPYING

%_bindir/%name
%_man1dir/%name.*
%exclude %_datadir/doc

%changelog
* Sun Nov 26 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.8.5-alt1
- New version

* Sat Oct 21 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.8.0-alt1
- New version
- Licensing change from Artistic 2.0 to GPLv3+

* Sun Aug 06 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.7.0-alt1
- New version

* Wed Oct 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.6.20-alt1
- New version

* Tue Jul 04 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.6.6-alt1
- New version

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.6.0-alt1
- New version

* Sun Aug 31 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.7-alt1
- New version

* Sun Feb 23 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.2-alt1
- New version

* Sat Aug 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.12-alt1
- New version

* Sun Apr 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.4.6-alt1
- New version

* Sun Nov 04 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.3.8-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.3.4-alt1
- New version

* Mon May 19 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.1.4-alt1
- Initial build for ALT Linux Sisyphus
