%define m_distro Padre
Name: perl-Padre
Version: 0.92
Release: alt1
Summary: Padre - Perl Application Development and Refactoring Environment

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~plaven/Padre/

Source: %m_distro-%version.tar
Patch0: %name-%version-%release.patch

%add_findreq_skiplist */Padre/Wx/About.pm
%add_findreq_skiplist */auto/share/dist/Padre/*
%define _perl_req_method relaxed

BuildArch: noarch
BuildRequires: perl-HTML-Parser perl-pod perl-Text-FindIndent perl-List-MoreUtils perl-Test-NoWarnings perl-File-HomeDir perl-Test-Script perl-Parse-ErrorString-Perl perl-YAML-Tiny perl-threads perl-Class-Adapter perl-Wx perl-Class-Unload perl-Pod-POM perl-File-Find-Rule perldoc perl-Class-XSAccessor perl-PPI perl-File-Remove perl-Probe-Perl perl-Devel-Refactor perl-devel perl-Encode perl-Parse-ExuberantCTags perl-Debug-Client perl-Text-Balanced perl-Format-Human-Bytes perl-ack perl-File-Copy-Recursive perl-Pod-Abstract perl-ORLite perl-Term-ReadLine-Gnu perl-Module-Refresh perl-Test-Exception perl-Pod-Simple perl-File-ShareDir perl-IO-String perl-Module-Starter perl-Module-CoreList perl-Params-Util perl-Devel-Dumpvar perl-DBD-SQLite perl-File-Next perl-Text-Diff perl-File-Which perl-IO-stringy perl-Wx-Perl-ProcessStream perl-Template-Tiny perl-DBI perl-Capture-Tiny perl-URI perl-pip perl-PPIx-EditorTools perl-Locale-Msgfmt perl-Alien-wxWidgets perl-App-cpanminus perl-Readonly-XS perl-PPIx-Regexp perl-JSON-XS perl-Test-MockObject perl-IPC-Run perl-Module-Manifest perl-POD2-Base perl-File-Slurp perl-Wx-Scintilla perl-ORLite-Migrate
BuildRequires: xvfb-run /usr/bin/convert

# With relaxed perl.req method some deps are lost
Requires: perl-POD2-Base perl(CGI.pm) perl(CPAN.pm) perl(Capture/Tiny.pm) perl(Class/Adapter/Builder.pm) perl(Class/Unload.pm) perl(Data/Dumper.pm) perl(Debug/Client.pm) perl(Devel/Dumpvar.pm) perl(Devel/Refactor.pm) perl(Digest/MD5.pm) perl(Encode/Guess.pm) perl(ExtUtils/Manifest.pm) perl(File/Copy.pm) perl(File/Find/Rule.pm) perl(File/Remove.pm) perl(File/Which.pm) perl(File/pushd.pm) perl(Getopt/Long.pm) perl(HTTP/Date.pm) perl(HTTP/Request.pm) perl(IO/Socket.pm) perl(IPC/Open2.pm) perl(IPC/Open3.pm) perl(IPC/Run.pm) perl(List/MoreUtils.pm) perl(Module/CoreList.pm) perl(Module/Manifest.pm) perl(PPI/Find.pm) perl(PPIx/EditorTools.pm) perl(PPIx/Regexp.pm) perl(Parse/ExuberantCTags.pm) perl(Probe/Perl.pm) perl(Template/Tiny.pm) perl(Text/Diff.pm) perl(Text/FindIndent.pm) perl(Wx.pm) perl(Wx/Perl/ProcessStream.pm) perl(warnings.pm)

%description
%summary

%prep
%setup -q -n %m_distro-%version
%patch -p1

%build
xvfb-run -a perl Makefile.PL PREFIX=/usr INSTALLDIRS=vendor
make
xvfb-run -a make test

%install
%perl_vendor_install
mkdir -p %buildroot{%_miconsdir,%_niconsdir,%_liconsdir,%_desktopdir}
convert %buildroot%perl_vendor_privlib/auto/share/dist/Padre/icons/padre/64x64/logo.png \
    -scale 48x48 %buildroot%_liconsdir/padre.png
convert %buildroot%perl_vendor_privlib/auto/share/dist/Padre/icons/padre/64x64/logo.png \
    -scale 32x32 %buildroot%_niconsdir/padre.png
convert %buildroot%perl_vendor_privlib/auto/share/dist/Padre/icons/padre/64x64/logo.png \
    -scale 16x16 %buildroot%_miconsdir/padre.png
cp padre.desktop %buildroot%_desktopdir

%files
%_bindir/padre
%_miconsdir/padre.png
%_niconsdir/padre.png
%_liconsdir/padre.png
%_desktopdir/padre.desktop
%perl_vendor_privlib/Padre*
%perl_vendor_privlib/auto/share/dist/Padre
%doc Changes README Artistic COPYING

%changelog
* Mon Nov 14 2011 Vladimir Lettiev <crux@altlinux.ru> 0.92-alt1
- New version 0.92
- New builddeps: perl-File-Slurp, perl-Wx-Scintilla, perl-ORLite-Migrate

* Tue Aug 23 2011 Vladimir Lettiev <crux@altlinux.ru> 0.90-alt1
- New version 0.90

* Mon Mar 21 2011 Vladimir Lettiev <crux@altlinux.ru> 0.84-alt1
- New version 0.84

* Sun Feb 27 2011 Vladimir Lettiev <crux@altlinux.ru> 0.82-alt1
- New version 0.82
- Relaxed perl_req_method (due to failures while deparsing `use Wx')
- Fixed requires

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 0.80-alt1
- New version 0.80

* Tue Jan 25 2011 Vladimir Lettiev <crux@altlinux.ru> 0.78-alt1
- New version 0.78
- Updated buildrequires

* Mon Dec 13 2010 Vladimir Lettiev <crux@altlinux.ru> 0.76-alt1
- New version 0.76
- Updated buildrequires

* Tue Nov 23 2010 Vladimir Lettiev <crux@altlinux.ru> 0.74-alt2
- Updated russian translation

* Mon Nov 22 2010 Vladimir Lettiev <crux@altlinux.ru> 0.74-alt1
- New version 0.74
- Fixed and enabled tests
- Enabled normal method for dependency tracking for perl.req

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.72-alt1
- New version 0.72

* Sun Sep 12 2010 Vladimir Lettiev <crux@altlinux.ru> 0.70-alt1
- New version 0.70

* Tue Aug 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.69-alt1
- New version 0.69

* Mon Aug 02 2010 Vladimir Lettiev <crux@altlinux.ru> 0.68-alt1
- New version 0.68
- Updated russian translation

* Mon Jul 26 2010 Vladimir Lettiev <crux@altlinux.ru> 0.66-alt1
- New version 0.66

* Tue Jun 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.64-alt1
- New version 0.64

* Thu Jun 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.63-alt1
- New version 0.63

* Mon Apr 26 2010 Vladimir Lettiev <crux@altlinux.ru> 0.60-alt1
- New version 0.60

* Tue Apr 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.59-alt1
- New version 0.59

* Fri Jan 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.55-alt1
- initial build
