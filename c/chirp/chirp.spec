%define _localstatedir %_var
%global src_name chirp-daily

Name: chirp
Version: 20171104
Release: alt1
Summary: A tool for programming two-way radio equipment

Group: Communications
License: GPLv3+
Url: http://chirp.danplanet.com/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: http://trac.chirp.danplanet.com/chirp_daily/daily-%version/%{src_name}-%version.tar.gz
Source1: %name.desktop

BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildRequires: %_bindir/desktop-file-install
BuildRequires: python-devel
BuildRequires: desktop-file-utils
BuildRequires: python-module-libxml2
BuildRequires: python-module-serial
#Requires: python-module-suds-jurko

%description
Chirp is a tool for programming two-way radio equipment
It provides a generic user interface to the programming
data and process that can drive many radio models under
the hood.

%prep
%setup -n %src_name-%version

%build
%python_build

%install
%python_install

# Wrong .desktop config lets install the correct .desktop
desktop-file-install \
        --dir=%buildroot%_desktopdir %SOURCE1

%files
%doc COPYING
%exclude %_docdir/%name
%_bindir/*
%python_sitelibdir_noarch/%{src_name}_%version-py2.7.egg-info
%python_sitelibdir_noarch/%name/
%_desktopdir/%name.desktop
%_datadir/%name/
%_man1dir/chirpw.1*
%_pixmapsdir/%name.png

%changelog
* Tue Nov 14 2017 Anton Midyukov <antohami@altlinux.org> 20171104-alt1
- Initial build for ALT Sisyphus.
