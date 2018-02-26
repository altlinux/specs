%define dict_name bokarjovrueo

Name: dict-bokarev_ru-eo
Version: 1.0
Release: alt1

Summary: Dictionary: Russian-Esperanto Bokarev dictionary 
Group: Text tools
License: GPL

Url: http://vicerveza.homeunix.net/~viric/dict/
Source: dictd-bokarjovrueo.tar.gz
Packager: Sergey Alembekov <rt@altlinux.org>

Requires(post,postun): dictd
BuildArch: noarch

Summary(ru_RU.UTF-8): Русско-Эсперантский словарь Бокарева.

%description
Bokarev Russian-Esperanto dictionary for dictd

%description -l ru_RU.UTF-8
Русско-Эсперантский словарь Бокарева для dictd

%prep
%setup -q -c

%install
mkdir -p $RPM_BUILD_ROOT%_datadir/dictd
cp %dict_name.dict.dz $RPM_BUILD_ROOT%_datadir/dictd/
cp %dict_name.index $RPM_BUILD_ROOT%_datadir/dictd/

%post -n %name
/usr/sbin/dictdconfig -w
%_initdir/dictd condreload

%postun -n %name
/usr/sbin/dictdconfig -w
%_initdir/dictd condreload

%files
%_datadir/dictd/%{dict_name}*

%changelog
* Thu Feb 15 2007 Sergey Alembekov <rt@altlinux.ru> 1.0-alt1
- initial release

