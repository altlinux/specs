Name: nomarch
Version: 1.4
Release: alt1

Summary: GPLed Arc de-archiver

Group: Archiving/Compression
License: GPLv2+
Url: http://www.svgalib.org/rus/nomarch.html
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source: ftp://ftp.ibiblio.org/pub/Linux/utils/compress/%name-%version.tar.gz

%description
nomarch lists/extracts/tests `.arc' archives. (It also handles `.ark'
files, they're exactly the same.) This is a *very* outdated file
format which should never be used for anything new, but unfortunately,
you can still run into it every so often.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%optflags"

%install

%makeinstall \
    BINDIR="%buildroot%_bindir" \
    MANDIR="%buildroot%_mandir/man1"


%files
%defattr(0644, root, root, 0755)
%doc ChangeLog NEWS README TODO
%doc %_mandir/man?/*
%attr(0755,root,root) %_bindir/*

%changelog
* Sun Dec 12 2010 Ilya Mashkin <oddity@altlinux.ru> 1.4-alt1
- Build for ALT Linux

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 1.4-5
- Rebuild against gcc 4.4 and rpm 4.6

* Wed Sep 3 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.4-4
- Update URL

* Fri Feb 08 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.4-3
- gcc 4.3 rebuild
- License fix

* Sat Sep 02 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.4-2
- FE6 Rebuild

* Sun Jun 30 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.4-1
- upstream made a new release! Packager nirvana ends...

* Mon Feb 13 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.3-5
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 16 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.3-4
- me is gcc4.1-proof

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com>
- 1.3-3
- rebuild on all arches

* Fri Apr 7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Apr 18 2004 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net>
- 0:1.3-0.fdr.1
- Fedorization

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- 1.3-0
- Initial package. (using DAR)
