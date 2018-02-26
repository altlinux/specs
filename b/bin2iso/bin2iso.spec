Name: bin2iso
Version: 1.9
Release: alt1

Summary: Convert ".bin" files into ISO or WAV
Summary(ru_RU.UTF-8): Преобразователь файлов ".bin" в формат ISO и/или WAV.
License: Distributable (Unknown)
Group: File tools
Url: http://users.andara.com/~doiron/bin2iso/
Source0: http://users.eastlink.ca/~doiron/bin2iso/linux/bin2iso19b_linux.c

%description
A program to convert ".bin" images into iso or wav files.

%description -l ru_RU.UTF8
Средство преобразования образов компакт-дисков ".bin" в формат ISO и/или набор WAV-файлов.

%prep
%setup -c -T

%build
%__cc $RPM_OPT_FLAGS -o %name %SOURCE0

%install
%__mkdir_p $RPM_BUILD_ROOT%_bindir
%__install -m 0755 %name $RPM_BUILD_ROOT/%_bindir

%files
%_bindir/%name

%changelog
* Sun Feb 12 2006 Vyacheslav Dikonov <slava@altlinux.ru> 1.9-alt1
- ALTLinux build
