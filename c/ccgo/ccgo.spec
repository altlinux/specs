Group: Games/Boards
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       ccgo
Version:    0.3.6.5
Release:    alt1_7
Summary:    An IGS (Internet Go Server) client written in C++
License:    GPLv3+
URL:        http://ccdw.org/~cjj/prog/%{name}/
Source0:    %{url}src/%{name}-%{version}.tar.gz
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
# See <http://www.freedesktop.org/software/appstream/docs/> for more details.
Source1:    %{name}.appdata.xml
# Fix building against libsigc++-2.6.0, bug #1304679
Patch0:     ccgo-0.3.6.5-Port-to-libsigc-2.6.0.patch
# Adapt to assert() macro changes in glibc > 2.26, bug #1482990
Patch1:     ccgo-0.3.6.5-Adapt-to-glibc-assert-change.patch
# Update config.sub to support aarch64, bug #925132
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext gettext-tools
BuildRequires:  gettext-tools libasprintf-devel
BuildRequires:  libappstream-glib
BuildRequires:  libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel
BuildRequires:  pkgconfig(gconfmm-2.6)
BuildRequires:  pkgconfig(gtkmm-2.4)
BuildRequires:  sed
# Optional, but ccgo does not signal missing gnugo through GUI
Requires:       gnugo
Source44: import.info

%description
ccGo allows you to play go with GNU Go on your computer or with other players
on an Internet Go Server (IGS) on the Internet. It supports smart game format
(SGF) suitable for exchanging game records.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
# Make XDG desktop file compliant
sed -i -e '/^Encoding/d' -e '/^Categories/s/Application;//' \
    %{name}.desktop.in
# Update config.sub to support aarch64, bug #925132
autoreconf -i -f

%build
%configure
%make_build

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet \
    %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%install
make install DESTDIR=%{buildroot}

# Register as an application to be visible in the software center
install -d %{buildroot}%{_datadir}/appdata
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING
%doc AUTHORS README
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.6.5-alt1_7
- update to new version by fcimport

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.6.4-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Mon Feb 16 2015 Ilya Mashkin <oddity@altlinux.ru> 0.3.6.4-alt1
- 0.3.6.4

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.3.6.3-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Oct 25 2009 Timur Batyrshin <erthad@altlinux.org> 0.3.6.3-alt1
- 0.3.6.3

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.3.6.2-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for ccgo

* Wed Feb 08 2006 Alex V. Myltsev <avm@altlinux.ru> 0.3.6.2-alt1
- Initial build for ALT Linux Sisyphus.

