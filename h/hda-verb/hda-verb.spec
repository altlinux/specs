Name:		hda-verb
Version:	0.3
Release:	alt1
Summary:	Tool to send commands (verbs) to HD-Audio codecs
License:	%gpl2plus
Group:		System/Configuration/Hardware
URL:		ftp://ftp.kernel.org/pub/linux/kernel/people/tiwai/misc/

Packager: Michael Pozhidaev <msp@altlinux.org>
BuildRequires:	rpm-build-licenses

Source0:	ftp://ftp.kernel.org/pub/linux/kernel/people/tiwai/misc/hda-verb-%{version}.tar.bz2

%description
hda-verb is a tiny program that allows you to access the HD-audio
codecs directly, allowing you to send commands (verbs) to them. For
hda-verb to work you must be running a linux kernel with
CONFIG_SND_HDA_HWDEP option enabled.

%prep
%setup -q

%build
%make_build CFLAGS="%{optflags}"

%install
%__install -pD -m755 hda-verb %buildroot%_sbindir/hda-verb

%files
%doc ChangeLog README
%{_sbindir}/hda-verb

%changelog
* Fri Sep 04 2009 Michael Pozhidaev <msp@altlinux.ru> 0.3-alt1
- First rpm for ALT Linux Sisyphus

* Wed Jan 28 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.3-1mdv2009.1
+ Revision: 334965
- import hda-verb


