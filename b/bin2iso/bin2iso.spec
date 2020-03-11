Name:          bin2iso
Version:       1.9b
Release:       alt1
Summary:       Convert ".bin" files into ISO or WAV
Summary(ru_RU.UTF-8): Преобразователь файлов ".bin" в формат ISO и/или WAV.
License:       Unlicense
Group:         File tools
Url:           http://users.andara.com/~doiron/bin2iso/
Vcs:           https://github.com/einsteinx2/bin2iso.git
Source:        %name-%version.tar

%description
A program to convert ".bin" images into iso or wav files.

%description -l ru_RU.UTF8
Средство преобразования образов компакт-дисков ".bin" в формат ISO и/или набор
WAV-файлов.


%prep
%setup

%build
cd src/linux_macos
%__cc $RPM_OPT_FLAGS -o %name %{name}_v%{version}_linux.c

%install
cd src/linux_macos
%__mkdir_p $RPM_BUILD_ROOT%_bindir
%__install -m 0755 %name $RPM_BUILD_ROOT/%_bindir

%files
%_bindir/%name


%changelog
* Wed Mar 11 2020 Pavel Skrylev <majioa@altlinux.org> 1.9b-alt1
- ^ 1.9 -> 1.9b
- > sources at upstream
- ! spec tags

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.9-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Feb 12 2006 Vyacheslav Dikonov <slava@altlinux.ru> 1.9-alt1
- ALTLinux build
