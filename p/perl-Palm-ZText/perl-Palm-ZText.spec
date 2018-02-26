# SPEC file for Palm-ZText - perl module and utility for converting
# plain text files into zTXT Palm databases

Name: perl-Palm-ZText
Version: 0.1
Release: alt1.1

Summary: Perl module and command line interface for work with zTXT documents of Palm readers
Summary(ru_RU.KOI8-R): модуль Perl и утилита perlztxt для работы с документами Palm в формате zTXT

%define real_name Palm-ZText
License: GPL
Group: Development/Perl
URL: http://gutenpalm.sourceforge.net/

Packager: Nikolay Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: http://gutenpalm.sourceforge.net/files/%real_name-%version.tar.gz

AutoReqProv: perl, yes
BuildPreReq: perl-devel, perl-p5-Palm >= 1.1.5, perl-Compress-Zlib >= 1.12
BuildRequires: perl-Pod-Parser

%description
Palm-ZText - Perl module for reading/writing zTXT documents.
This is a native format of Weasel reader for Palm Pilot.
A command line utility perlztxt is utilizes this module for
convert text files into zTXT databases.

%description -l ru_RU.KOI8-R
Palm-ZText - модуль Perl для чтения/записи документов в
формате zTXT. Документы в этом формате предназначены для
просмотра утилитой Weasel для PalmOS. Кроме того, в
состав пакета входит утилита perlztxt для преобразования
текстовых файлов в базы zTXT.

%prep
%setup -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Palm/ZText.pm
%_bindir/perlztxt
%doc README Changes Changelog

%changelog
* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.1-alt1.1
- rebuilt with perl 5.12

* Wed Feb 09 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.1-alt1
- First build for ALT Linux
* Mon Feb 07 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.1-alt0.1
- Adding automatic dependence searching by rpm-build-perl 
* Sun Jan 30 2005 Nikolay Fetisov <naf@altlinux.ru> 0.1-alt0
- SPEC-file cleanup to meet Sisyphus requirements
- manual pages not packaged (use perldoc)
* Sun Feb 08 2004 Nikolay Fetisov <naf@ssc.ru> 0.1-ssc1
- First build

