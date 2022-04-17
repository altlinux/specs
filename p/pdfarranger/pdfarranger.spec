Name: pdfarranger
Version: 1.8.2
Release: alt1
Url: https://github.com/pdfarranger/pdfarranger
Group: Publishing
License: GPLv3
BuildArch: noarch
Source: %name-%version.tar.gz
Summary: Split pdf documents and rotate, crop and rearrange their pages
Requires: python3-module-%name = %version-%release, python3-module-pikepdf

# Automatically added by buildreq on Tue Dec 29 2020
# optimized out: perl perl-Encode perl-XML-Parser perl-parent python2-base python3 python3-base python3-dev python3-module-paste python3-module-pkg_resources sh4
BuildRequires: intltool python3-module-distutils-extra python3-module-setuptools python3-module-sphinxcontrib

%description
Pdfarranger is a small python-gtk application, which helps the user to
merge or split pdf documents and rotate, crop and rearrange their pages
using an interactive and intuitive graphical interface. It is a frontend
for pikepdf.

%package -n python3-module-%name
Summary: Supplemental module for %name
Group: Development/Python3
%description -n python3-module-%name
Supplemental module for %name, %summary

%prep
%setup

%build
%python3_build

%install
%python3_install
install -d %buildroot%_iconsdir
cp -a data/icons/* %buildroot/%_iconsdir/

%files
%_bindir/*
%_desktopdir/*%{name}*.desktop
%_man1dir/*
%_datadir/metainfo/*%{name}*
%_datadir/%name
%_iconsdir/hicolor/*/*/*%{name}*

%files -n python3-module-%name
%python3_sitelibdir_noarch/*

%changelog
* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 1.8.2-alt1
- Autobuild version bump to 1.8.2

* Sat Jun 19 2021 Fr. Br. George <george@altlinux.ru> 1.7.1-alt1
- Autobuild version bump to 1.7.1

* Tue Dec 29 2020 Fr. Br. George <george@altlinux.ru> 1.6.2-alt1
- Initial build fo ALT

