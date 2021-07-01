Name: nxscramble
Version: 0.2
Release: alt1

Summary: Utility which scrambles password string same way as Nomachine NX client

License: GPLv2
Group: Text tools
Url: http://www.nomachine.com/ar/view.php?ar_id=AR01C00125

Source: %name-%version.tar

Packager: Lenar Shakirov <snejok@altlinux.org>

BuildRequires: rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libxml2-devel
BuildRequires: qt5-base-devel

%description
Small tool which scrambles an plain text string the same way as Nomachine
NX Client does it.

%prep
%setup

%build
%cmake_insource
%make

%install
%makeinstall_std

%files
%_bindir/nxscramble

%changelog
* Thu Jul 01 2021 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- cleanup spec, build with Qt5

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1-alt4.qa1
- NMU: rebuilt for debuginfo.

* Tue May 26 2009 Lenar Shakirov <snejok@altlinux.ru> 0.1-alt4
- Url added. Thanks to repocop!

* Fri Dec 26 2008 Lenar Shakirov <snejok@altlinux.ru> 0.1-alt3
- BuildRequires updated

* Fri Dec 26 2008 Lenar Shakirov <snejok@altlinux.ru> 0.1-alt2
- New packager

* Wed Mar 26 2008 Maxim Ivanov <redbaron@altlinux.ru> 0.1-alt1
- Initial build for Sisyphus

