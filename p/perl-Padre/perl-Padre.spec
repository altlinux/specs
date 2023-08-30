%define _unpackaged_files_terminate_build 1
# we need a font
BuildRequires: fonts-ttf-liberation
%define dist Padre
Name: perl-Padre
Version: 1.02
Release: alt1


Summary: Padre - Perl Application Development and Refactoring Environment
License: Perl
Group: Development/Perl

Url: %CPAN %dist
VCS: git+https://github.com/PadreIDE/Padre.git
Source: %name-%version.tar

%add_findreq_skiplist */Padre/Wx/About.pm
%add_findreq_skiplist */Padre/Wx/FunctionList.pm
%add_findreq_skiplist */auto/share/dist/Padre/*

BuildArch: noarch
BuildRequires: perl-Parse-Functions perl-unicore perl-HTML-Parser perl-pod perl-Text-FindIndent perl-List-MoreUtils perl-Test-NoWarnings perl-File-HomeDir perl-Test-Script perl-Parse-ErrorString-Perl perl-YAML-Tiny perl-threads perl-Class-Adapter perl-Wx perl-Class-Unload perl-Pod-POM perl-File-Find-Rule perldoc perl-Class-XSAccessor perl-PPI perl-File-Remove perl-Probe-Perl perl-Devel-Refactor perl-devel perl-Encode perl-Parse-ExuberantCTags perl-Debug-Client perl-Text-Balanced perl-Format-Human-Bytes perl-ack perl-File-Copy-Recursive perl-Pod-Abstract perl-ORLite perl-Term-ReadLine-Gnu perl-Module-Refresh perl-Test-Exception perl-Pod-Simple perl-File-ShareDir perl-IO-String perl-Module-Starter perl-Module-CoreList perl-Params-Util perl-Devel-Dumpvar perl-DBD-SQLite perl-File-Next perl-Text-Diff perl-File-Which perl-IO-stringy perl-Wx-Perl-ProcessStream perl-Template-Tiny perl-DBI perl-Capture-Tiny perl-URI perl-PPIx-EditorTools perl-Locale-Msgfmt perl-Alien-wxWidgets perl-App-cpanminus perl-Readonly-XS perl-PPIx-Regexp perl-JSON-XS perl-Test-MockObject perl-IPC-Run perl-Module-Manifest perl-POD2-Base perl-File-Slurp perl-Wx-Scintilla perl-ORLite-Migrate perl-App-cpanminus perl-CGI perl-Test-Warn perl-Text-Patch perl(HTTP/Cookies.pm)
BuildRequires: xvfb-run /usr/bin/convert

Requires: perl-unicore perl-POD2-Base
Provides: padre = %EVR

%description
%summary

%prep
%setup -q

%build
xvfb-run -a perl Makefile.PL PREFIX=/usr INSTALLDIRS=vendor
make

%check
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

cat << EOF > %buildroot%_desktopdir/padre.desktop
[Desktop Entry]
Type=Application
Name=Padre
Comment=Perl Application Development and Refactoring Environment
Icon=padre
Exec=/usr/bin/padre
Categories=Development;IDE;TextTools;
EOF

%{expand:%%global __find_requires xvfb-run -a %__find_requires}

%files
%doc README.md Build_locallib_debian_ubuntu14.10.md Build_perlbrew_debian_ubuntu14.10.md Changes PACKAGING.md LICENSE COPYING Artistic
%_bindir/padre
%_miconsdir/padre.png
%_niconsdir/padre.png
%_liconsdir/padre.png
%_desktopdir/padre.desktop
%perl_vendor_privlib/Padre*
%perl_vendor_privlib/auto/share/dist/Padre
%doc Changes README* Artistic

%changelog
* Wed Aug 30 2023 Igor Vlasenko <viy@altlinux.org> 1.02-alt1
- new version

* Fri Jul 28 2023 Igor Vlasenko <viy@altlinux.org> 1.00-alt8.dac1134
- added VCS: tag

* Mon Apr 04 2022 Igor Vlasenko <viy@altlinux.org> 1.00-alt7.dac1134
- fixed build

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.00-alt6.dac1134
- NMU: drop unused BR: perl-pip

* Thu Jan 03 2019 Igor Vlasenko <viy@altlinux.ru> 1.00-alt5.dac1134
- resurrected to Sisyphus
- switched to https://github.com/PadreIDE/Padre.git
- added Provides: padre

* Mon Mar 14 2016 Vladimir Lettiev <crux@altlinux.ru> 1.00-alt4.df25a95
- commit df25a95 (Closes: #31841)
- restored auto requires

* Fri Oct 30 2015 Vladimir Lettiev <crux@altlinux.ru> 1.00-alt3.be9d0b8
- commit be9d0b8

* Fri Apr 04 2014 Vladimir Lettiev <crux@altlinux.ru> 1.00-alt2
- Fixed build with Pod::Perldoc >= 3.21

* Thu Nov 14 2013 Vladimir Lettiev <crux@altlinux.ru> 1.00-alt1
- 1.00

* Fri Jul 26 2013 Vladimir Lettiev <crux@altlinux.ru> 0.98-alt1
- 0.98

* Mon Feb 18 2013 Vladimir Lettiev <crux@altlinux.ru> 0.97-alt1
- 0.97 (r19692)

* Mon Oct 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.96-alt1
- 0.92 -> 0.96
- built as plain srpm

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
