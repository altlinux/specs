Name: fonts-otf-pelagy-sg
Version: 1.0
Release: alt1

Summary: Pelagy SG(tm) Regular font
License: ALT-Public-Domain
Group: System/Fonts/True type

Url: http://fonts-online.ru/fonts/pelagy-sg
Source: Pelagy_SG.zip

BuildArch: noarch
BuildRequires: unzip
BuildRequires: rpm-build-fonts >= 0.4

%description
Decorative Old Slavic font by dpstarco@yandex.ru;
see also http://t.me/solono_stihi/3944

%prep
%setup -c

%install
%otf_fonts_install pelagy_sg

%files -f pelagy_sg.files
%doc COPYRIGHT.txt

%changelog
* Sat Sep 03 2022 Michael Shigorin <mike@altlinux.org> 1.0-alt1
- initial release (spec based on fonts-otf-mozilla-fira somewhat)
