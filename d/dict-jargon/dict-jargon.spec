Name: dict-jargon
Version: 4.3.1
Release: alt2.1
Group: Text tools
License: GPL
Url: www.jargon.org
Packager: Alexey Dyachenko <alexd@altlinux.ru>

Summary: Hackers Dictionary
Summary(ru_RU.KOI8-R): Словарь Хакеров

BuildArch: noarch
BuildRequires: dict-tools
PreReq: dictd

Obsoletes: jargon-dict

Source: dict-jargon_%version.tgz

%description
Dictionary of hacker community. You'll find here abbreviatures,
slang and other unuseful information.

%description -l ru_RU.KOI8-R
Словарь сообщества хакеров. Здесь вы найдете непонятные аббревиатуры,
слова, выражения и кучу другой совершенно ненужной информации.


%prep
%setup -c

%install
mkdir -p %buildroot%_datadir/dictd
cp jargon.dict.dz jargon.index %buildroot%_datadir/dictd

%post
%_sbindir/dictdconfig -w
%_initdir/dictd condreload

%postun
%_sbindir/dictdconfig -w
%_initdir/dictd condreload

%files
%_datadir/dictd/*

%changelog
* Sun Jun 03 2007 Slava Semushin <php-coder@altlinux.ru> 4.3.1-alt2.1
- NMU
- Fixed incomplete locale specification in Summary tag (#11841)
- Set packager tag to previous maintainer
- Spec cleanup:
  + s/%%setup -q/%%setup/
  + s/BuildArchitectures/BuildArch/
  + s/$$RPM_BUILD_ROOT/%%buildroot/
  + Use macroses %%_datadir and %%_sbindir instead of appropriate paths
  + Removed some tabs

* Thu Jan 30 2003 Alexey Dyachenko <alexd@altlinux.ru> 4.3.1-alt2
- fix bug #0001706: service dictd condreload would be more appropriate
  than condrestart

* Tue Oct 15 2002 Alexey Dyachenko <alexd@altlinux.ru> 4.3.1-alt1
- new version

* Wed Feb 21 2001 Peter 'Nidd' Novodvorsky <petya@logic.ru> ipl2
- Added /usr/sbin before dictdconfig in case that user doesn't have
/usr/sbin in path.

* Mon Feb  5 2001 Peter 'Nidd' Novodvorsky<petya@logic.ru> ipl1
- initial release
