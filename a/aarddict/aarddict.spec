Name: aarddict
Version: 0.9.3
Release: alt1
Summary: Aard Dictionary is a multiplatform dictionary and offline Wikipedia reader

Packager: Ildar Mulyukov <ildar@altlinux.ru>

BuildArch: noarch
Group: System/Internationalization
Url: http://aarddict.org
License: GPL3

Source: %name.tar
Source1: %name.desktop

# Automatically added by buildreq on Mon Apr 01 2013
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-email python-modules-logging
BuildRequires: python-module-distribute python-module-PyQt4

%description
Aard Dictionary is a free, fast, easy to use word lookup program that

* looks up words fast even with huge dictionaries like English Wikipedia
* looks up words in multiple dictionaries in multiple languages without switching
* works great as offline Wikipedia reader
* is keyboard navigation friendly
* has efficient, highly compressed dictionary data storage format with ability to verify data integrity built-in

%prep
%setup -n %name

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir --record=INSTALLED_FILES
install -D %SOURCE1 %buildroot%_desktopdir

%files
%_bindir/aard*
%python_sitelibdir/%name
%python_sitelibdir/%{name}*egg-info
%_desktopdir/%name.desktop
%_iconsdir/hicolor/64x64/apps/%name.*
%doc doc/*
%exclude %python_sitelibdir/tests

%changelog
* Mon Apr 01 2013 Ildar Mulyukov <ildar@altlinux.ru> 0.9.3-alt1
- initial build for ALT Linux Sisyphus
