%define cid            firefox-tabgroups@mozilla.com
%define cid_dir        %palemoon_noarch_extensionsdir/%cid

#%define sids_dir       %sm_prefixr/%cid
#%define cidf_dir       %firefox_noarch_extensionsdir/%cid

%define pname palemoon-tabgroups

Name: palemoon-tabgroups
Version: 0.2.1
Release: alt1.1
Summary: Provides tab groups (Panorama)

License: GPL2
Group: Networking/WWW
Url: https://github.com/wolfbeast/palemoon-tabgroups.git
BuildArch: noarch

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %pname.tar.bz2

BuildRequires(pre):	rpm-build-palemoon

# Automatically added by buildreq on Wed Jul 29 2015
BuildRequires: libdb4-devel
Requires: palemoon

%description
Create and manage tab groups in a side-by-side
list-view interface, or "Groups Bar" toolbar interface.
Single or multi-tab close, bookmark, or move across groups.
Search for tabs by title or content in current or all groups.

%description -l ru_RU.utf8
Создание и управление табулируемыми группами
Поиск позаголовкам или содержанию в текущей, или во всех группах

%prep
%setup -c -n %pname/%cid

%install
mkdir -p %buildroot/%cid_dir
pushd  %name/src

cp -r * %buildroot/%cid_dir

mkdir -p %buildroot/%cidf_dir

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%cid_dir" ] || rm -rf "%cid_dir"
fi

%files
%cid_dir

%changelog
* Sun Nov 22 2015 Hihin Ruslan <ruslandh@altlinux.ru> 0.2.1-alt1.1
- New version

* Fri Jul 31 2015 Hihin Ruslan <ruslandh@altlinux.ru> 0.2-alt1.1
- Fix requires

* Wed Jul 29 2015 Hihin Ruslan <ruslandh@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
