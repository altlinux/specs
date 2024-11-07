Name:          hp4600-scan
Version:       0.2
Release:       alt1
Summary:       Scanning utility for HP Scanjet 4600 and 4670 scanners
Summary(ru_RU.UTF-8): Утилитка для оцифровки сканерами HP Scanjet 4600 и 4670
License:       Unlicenced
Group:         Graphics
Url:           http://www.chmil.org/hp4600linux/
Vcs:           https://github.com/Triften/hp4600.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-perl
BuildRequires: libusb-compat-devel
BuildRequires: perl-Tk-devel
Requires:      udev

%description
Scanning utilities for HP Scanjet 46xx series scanners. They support
4600 and 4670 models. For now, only a fullpage scan with 600 dpi as
a resolution is available.

%description -l ru_RU.UTF-8
Утилитки для оцифровки сканерами серии HP Scanjet 46xx. Поддерживаются
модели 4600 и 4670. На данное время доступно сканирование только полной
страницы с разрешением 600 тнд (dpi).

%prep
%setup

%build
echo %_udevrulesdir/
%make_build

%install
%makeinstall_std

%files
%doc README.md
%_bindir/*
%_udevrulesdir/*


%changelog
* Thu Nov 07 2024 Pavel Skrylev <majioa@altlinux.org> 0.2-alt1
- ^ 0.1 -> 0.2 (on 2024.05)
- + makefile, and rules fiels
- ! some fixes

* Sat Jun 24 2023 Pavel Skrylev <majioa@altlinux.org> 0.1-alt4
- ! fixed spec for udev rules setup, and some other things
- * relicensed

* Tue Apr 05 2011 Malo Skryleve <malo@altlinux.org> 0.1-alt3
- Fixed spec file

* Thu Mar 31 2011 Malo Skryleve <malo@altlinux.org> 0.1-alt2
- Added udev rules file to the %%files section

* Wed Feb 16 2011 Malo Skryleve <malo@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus

