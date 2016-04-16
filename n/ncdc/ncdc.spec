Name: ncdc
Version: 1.19.1
Release: alt2.qa1
Summary: A modern and lightweight direct connect client
License: MIT
Group: Networking/File transfer
Url: http://dev.yorhel.nl/ncdc
Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: http://dev.yorhel.nl/download/%name-%version.tar.gz
BuildRequires: bzip2-devel
BuildRequires: glib2-devel
BuildRequires: libgnutls-devel
BuildRequires: ncurses-devel
BuildRequires: libncursesw-devel
BuildRequires: perl-podlators
BuildRequires: libsqlite3-devel
BuildRequires: zlib-devel

%description
Ncdc is a modern and lightweight direct connect client with a
friendly ncurses interface.

%prep
%setup

%build
%configure --disable-silent-rules
%make_build #{?_smp_flags}

%install
%makeinstall_std

%files
%doc ChangeLog COPYING README
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Sat Apr 16 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.19.1-alt2.qa1
- NMU: rebuilt with libgnutls.so.28 -> libgnutls.so.30.

* Thu Aug 06 2015 Konstantin Artyushkin <akv@altlinux.org> 1.19.1-alt2
- new version

* Thu Aug 06 2015 Konstantin Artyushkin <akv@altlinux.org> 1.19.1-alt1
- initial build for ALT Linux Sisyphus

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Christopher Meng <rpm@cicku.me> - 1.19.1-1
- Update to 1.19.1

* Mon Oct 07 2013 Christopher Meng <rpm@cicku.me> - 1.18.1-1
- Initial Package(BZ#1016170).
