%def_enable git

%define cid            \{e4a8a97b-f2ed-450b-b12d-ee082ba24781\}
%define cid_dir        %palemoon_noarch_extensionsdir/%cid


Name: greasemonkey
Version: 3.9.2
Release: alt1

Summary: greasemonkey: an efficient blocker extension for your browser. Fast, potent, and lean
License: GPLv3
Group: Other
Url: https://github.com/chrisaljoudi/greasemonkey
BuildArch: noarch

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar
Source1: META-INF.tar

# Automatically added by buildreq on Sat Nov 05 2016
# optimized out: python-base python-modules
BuildRequires: python-modules-compiler python-modules-encodings python-modules-json


%package -n palemoon-greasemonkey
Group: System/Libraries
Summary: Plugin  greasemonkey for Pale Moon
Requires: palemoon


BuildRequires(pre):	rpm-build-palemoon


%description
An efficient blocker: easy on memory and CPU footprint, and yet can load and enforce
thousands more filters than other popular blockers out there.


%description -l ru_RU.utf8
uBock-origin - эффективный блокировщик: он использует меньше оперативной памяти и меньше нагружает ЦП, 
чем другие популярные блокировщики, при этом используя больше фильтров.

%description -n palemoon-greasemonkey
Plugin greasemonkey: an efficient blocker extension for palemoon. Fast, potent, and lean.

%description  -l ru_RU.utf8 -n palemoon-greasemonkey
Плагин greasemonkey  эффективный блокировщик: он использует меньше оперативной памяти и меньше нагружает ЦП, 
чем другие популярные блокировщики, при этом используя больше фильтров.


%prep
%setup -n %name-%version

%if_enabled git
%build
./build.sh
tar -x -f  %SOURCE1
%endif


%install
pushd META-INF/
install -d -m755  %buildroot/%cid_dir/META-INF/
install -Dp -m644  ./* %buildroot/%cid_dir/META-INF/
popd



mkdir -p %buildroot/%cid_dir
cp -r * %buildroot/%cid_dir



%files -n palemoon-greasemonkey
%cid_dir
%exclude %cid_dir/*.sh 

%changelog
* Sun Mar 26 2017 Hihin Ruslan <ruslandh@altlinux.ru> 3.9.2-alt1
- initial build for ALT Linux Sisyphus
