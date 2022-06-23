Name: podiff
Version: 1.3
Release: alt2

Summary: Program for comparing *.po files
Summary(ru_RU.UTF-8): Сравнение файлов *.po
License: GPLv3
Group: Editors

Url: https://puszcza.gnu.org.ua/projects/podiff

# Source-url:   ftp://download.gnu.org.ua/pub/release/podiff/%name-%version.tar.gz
Source:	%name-%version.tar

%description
Program for comparing *.po files.

%description -l ru_RU.UTF-8
Приложение, предназначенное для сравнения файлов с расширением .po

%prep
%setup -q -n %name-%version

%build
%make_build CFLAGS="%{optflags}"

%install
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_mandir/man1
%makeinstall_std

%files
%doc README NEWS
%_bindir/podiff
%_man1dir/podiff.1*

%changelog
* Thu Jun 23 2022 Artem Proskurnev <tema@altlinux.org> 1.3-alt2
- Add optflags

* Wed Apr 20 2022 Artem Proskurnev <tema@altlinux.org> 1.3-alt1
- Initial build for Sisyphus
