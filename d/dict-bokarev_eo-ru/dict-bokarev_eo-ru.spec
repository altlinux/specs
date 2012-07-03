%define dict_name bokarjoveoru

Name: dict-bokarev_eo-ru
Version: 1.0
Release: alt1

Summary: Dictionary: Esperanto-Russian Bokarev dictionary 
Group: Text tools
License: GPL

Url: http://vicerveza.homeunix.net/~viric/dict/
Source: dictd-bokarjoveoru.tar.gz
Packager: Sergey Alembekov <rt@altlinux.org>

Requires(post,postun): dictd
BuildArch: noarch

Summary(ru_RU.UTF-8): Эсперанто-Русский словарь Бокарева.

%description
Revo Esperanto-Russian and Russian-Esperanto dictionary for dictd

%description -l ru_RU.UTF-8
Рево Эсперанто-Русский Руский-Эсперанто словарь для dictd

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

