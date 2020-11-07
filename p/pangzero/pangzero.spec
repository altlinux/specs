# test requires homedir and sound environment
%define _without_test 1

Name: pangzero
Version: 1.4.1
Release: alt1

Summary: Clone of Super Pang, a fast-paced action game
License: GPLv2
Group: Games/Arcade
Url: http://apocalypse.rulez.org/pangzero

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires: perl-SDL perl-Module-Build
# due to conflict perl-SDL <-> perl-SDL_Perl
%filter_from_requires /^perl(SDL/d
Requires:       perl-SDL

%description
Pang Zero is a clone of Super Pang, a fast-paced action game that involves
popping balloons with a harpoon. The intention of our effort is to create a
fun, open-source game that many (currently up to 6) people can play
together.

For more info, please visit our website at
http://apocalypse.rulez.org/pangzero

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*
%perl_vendor_privlib/Games*
%perl_vendor_privlib/auto/share/dist/*

%changelog
* Sat Nov 07 2020 Igor Vlasenko <viy@altlinux.ru> 1.4.1-alt1
- new version
- picked up from orphaned

* Tue Jun 14 2016 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1.1
- NMU: perl-SDL -> perl-SDL_Perl

* Fri Jan 25 2008 Igor Zubkov <icesik@altlinux.org> 1.3-alt1
- 0.13 -> 1.3
- buildreq
- add Url

* Thu Aug 31 2006 Igor Zubkov <icesik@altlinux.org> 0.13-alt1
- Initial build for Sisyphus
