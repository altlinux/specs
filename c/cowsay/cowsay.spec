Name: cowsay
Version: 3.03
Release: alt4
Summary: Configurable speaking/thinking cow
Group: Games/Other
License: Artistic or GPL
Url: http://www.nog.net/~tony/warez/
Source0: http://www.nog.net/~tony/warez/%name-%version.tar.gz
Source1: cowsay.bashcomp
Source2: cowsay-convert
Source3: mech-and-cow.cow
Source4: animalsay
BuildArch: noarch
Requires: %name-offensive = %version-%release %name-soft = %version-%release

%description
cowsay is a configurable talking cow, written in Perl.  It operates
much as the figlet program does, and it written in the same spirit
of silliness.
It generates ASCII pictures of a cow with a message. It can also generate
pictures of other animals.

%package offensive
Summary: Potentially offensive %name ASCIIart
Group: Games/Other
%description offensive
Potentially offensive %name ASCIIart

%package soft
Summary: Non-offensive %name ASCIIart and binary
Group: Games/Other
%description soft
Non-offensive %name ASCIIart and binary

%prep
%setup -q
sed -e 's#%%PREFIX%%/share/cows#%_datadir/%name''#' \
         -e 's#%%BANGPERL%%#!/usr/bin/perl#' -i %name
sed -e 's#%%PREFIX%%/share/cows#%_datadir/%name''#' \
         -e 's#/usr/local/share/cows#%_datadir/%name''#' -i %name.1
cp %SOURCE2 %SOURCE4 .
%build
echo No need to build anything

%install
# using install.sh is not a good idea so let's make the install manually
mkdir -p %buildroot{%_bindir,%_mandir/man1,%_datadir/%name,%_sysconfdir/bash_completion.d}
cp -p %name %name-convert %buildroot%_bindir
cp -p cows/* %buildroot%_datadir/%name
cp %SOURCE3 %buildroot%_datadir/%name
rm %buildroot%_datadir/%name/mech-and-cow
cp -p %name.1 %buildroot%_mandir/man1
install -m755 %SOURCE2 %buildroot%_bindir
install -m755 %SOURCE4 %buildroot%_bindir

chmod +x %buildroot%_bindir/animalsay
ln -s %name %buildroot%_bindir/cowthink
ln -s %name.1 %buildroot%_mandir/man1/cowthink.1

cp %SOURCE1 %buildroot%_sysconfdir/bash_completion.d

%define offensivelist head-in.cow sodomized.cow telebears.cow
for f in %offensivelist; do echo "%_datadir/%name/$f"; done > offensivelist.files
%define offexclude %(for f in %offensivelist; do echo %%exclude %_datadir/%name/$f; done)

%files
%doc ChangeLog LICENSE README

%files offensive -f offensivelist.files

%files soft
%offexclude
%_bindir/*
%_mandir/man1/cow*
%_datadir/%name
%_sysconfdir/bash_completion.d/*

%changelog
* Tue Nov 20 2012 Fr. Br. George <george@altlinux.ru> 3.03-alt4
- They said a man inserted something to a cow from behind; separate this
- Closes: 27757

* Tue Jan 24 2012 Fr. Br. George <george@altlinux.ru> 3.03-alt3
- Remove bash_completion.d from file list

* Sat Mar 21 2009 Fr. Br. George <george@altlinux.ru> 3.03-alt2
- Fix #18840 (invalid cow file)
- new tool for converting files between cow and ascii

* Sun Jun 15 2008 Fr. Br. George <george@altlinux.ru> 3.03-alt1
- Initial build from FC

* Tue Jan 02 2007 Michał Bentkowski <mr.ecik at gmail.com> - 3.03-2
- Use cp -p to keep timestamps
- Fix paths in manpage
- Add animalsay

* Sun Dec 31 2006 Michał Bentkowski <mr.ecik at gmail.com> - 3.03-1
- Initial release
