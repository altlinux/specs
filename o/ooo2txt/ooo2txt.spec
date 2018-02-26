Name: ooo2txt
Version: 0.0.6
Release: alt2

Summary: Convert OpenOffice documents to simple text
Group: Text tools
License: LGPL

URL: http://ooo2txt.fr.st/

Source0: http://oootools.free.fr/ooo2txt/download/source/ooo2txt.006.pl
Source1: http://oootools.free.fr/ooo2txt/download/source/update.txt
Source2: http://oootools.free.fr/ooo2txt/download/source/readme.txt
Source3: http://oootools.free.fr/ooo2txt/download/licence/LGPL.txt
Source4: %name.pod

Patch0: ooo2txt.006.pl.diff

BuildArch: noarch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sat Jan 13 2007 (-bi)
BuildRequires: perl-Archive-Zip perl-XML-Twig

%description
ooo2txt converts OpenOffice documents to simple text.

%prep
%setup -q -T -c
cp %SOURCE0 %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 .
sed -i -e 's/\r//' ooo2txt.006.pl
%patch0

%build
pod2man ooo2txt.pod > ooo2txt.1

%install
install -d -m755 %buildroot%_bindir/ %buildroot%_man1dir/
install ooo2txt.006.pl %buildroot%_bindir/ooo2txt
install -m644 ooo2txt.1 %buildroot%_man1dir/

%files
%doc update.txt readme.txt LGPL.txt
%_bindir/ooo2txt
%_man1dir/ooo2txt.*

%changelog
* Mon Jul 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt2
- Removed packages-info-i18n-common from BuildRequires

* Sat Jan 13 2007 Igor Zubkov <icesik@altlinux.org> 0.0.6-alt1
- initial build for Sisphus on spec from FC6 extra

* Wed Sep  6 2006 Patrice Dumas <pertusus@free.fr> - 0.0.6-2
- rebuild for FC-6

* Mon Jul 10 2006 Patrice Dumas <pertusus@free.fr> - 0.0.6-1
- initial packaging
