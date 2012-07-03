%define languagelocal	deutsch
%define languageeng	german
%define languagecode	de

Summary: German and Swiss dictionaries for ispell
Name: ispell-%{languagecode}
Epoch:1
Version: 20090107
Release: alt1

Packager: Igor Vlasenko <viy@altlinux.ru>

Url: http://j3e.de/ispell/igerman98/
Source:	http://j3e.de/ispell/igerman98/dict/%name-%version.tar
License: GPL2
Group: System/Internationalization

# Can't be noarch due to the byte order
#BuildArch: noarch

Requires: ispell
# the binary format changed with ispell 3.2.06
PreReq: ispell >= 3.2.06
Provides: ispell-dictionary
BuildRequires: ispell

%description
ispell-de is spelling data in German to be used by ispell program.
With this extension, you can compose a document in German and check
for the typos easily.

Ispell can be used directly from command line to check a file;
or used by several text dealing programs, like LyX, etc.

%prep
%setup -q 

%build
for lang in de_DE de_AT de_CH; do
	make ispell/${lang}{.aff,.hash}
done

%install
mkdir -p $RPM_BUILD_ROOT%_libdir/ispell

# Copyright 1999-2008 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: /var/cvsroot/gentoo-x86/app-dicts/ispell-de/ispell-de-20071211.ebuild,v 1.2 2008/11/01 11:56:19 pva Exp $

pushd ispell
for lang in de_DE de_AT de_CH; do
    install -m 644 $lang.aff $lang.hash $RPM_BUILD_ROOT%_libdir/ispell/
done
popd

pushd $RPM_BUILD_ROOT%_libdir/ispell/
  ln -s de_DE.aff %languagelocal.aff
  ln -s de_DE.hash %languagelocal.hash
popd

# LaTeX babel
if [ "%languagelocal" != "%languageeng" ];then
 cd $RPM_BUILD_ROOT%_libdir/ispell
 ln -s %languagelocal.aff %languageeng.aff
 ln -s %languagelocal.hash %languageeng.hash
fi

#%post
#cd %_libdir/ispell
#mv -f %languagelocal.hash %languagelocal.ispell
#buildhash %languagelocal.ispell %languagelocal.aff %languagelocal.hash &> /dev/null
#rm -f %languagelocal.ispell.stat %languagelocal.ispell.cnt %languagelocal.ispell

%files
%doc Documentation/*
%_libdir/ispell/*

%changelog
* Sun Apr 12 2009 Igor Vlasenko <viy@altlinux.ru> 1:20090107-alt1
- new version; built as a separate package now

