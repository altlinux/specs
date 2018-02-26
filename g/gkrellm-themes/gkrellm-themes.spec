Name: gkrellm-themes
Version: 1.0
Release: alt1

Summary: Gkrellm themes
Summary(ru_RU.KOI8-R): Темы для gkrellm
License: GPL
Group: Monitoring
Url: http://www.muhri.net/gkrellm/
Buildarch: noarch

Source0: http://www.muhri.net/gkrellm/GKrellM-Skins.tar.bz2

Requires: gkrellm >= 2.2.0

Summary(ru_RU.KOI8-R): Темы для gkrellm

%description
Gkrellm themes

%description -l ru_RU.KOI8-R
Темы для gkrellm

%prep
%setup -q -n GKrellM-skins

%build

%install
mkdir -p %buildroot%_datadir/gkrellm2/themes
for i in *.tar.gz; do tar xzv -C %buildroot%_datadir/gkrellm2/themes -f $i; done

%files
%_datadir/gkrellm2/themes

%changelog
* Mon Jan 10 2005 Serge Pavlovsky <pal@altlinux.ru> 1.0-alt1
- built for Sisyphus

