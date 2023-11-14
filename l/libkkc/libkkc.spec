Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/valadoc pkgconfig(gio-2.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global dataversion 0.2.7

Name:		libkkc
Version:	0.3.5
Release:	alt1_24
Summary:	Japanese Kana Kanji conversion library

License:	GPLv3+
URL:		https://github.com/ueno/libkkc
Source0:	https://github.com/ueno/libkkc/releases/download/v%{version}/%{name}-%{version}.tar.gz
# remove for next release:
Source1:        README.md
Patch0:		libkkc-HEAD.patch
Patch1:         libkkc-POT.skip.patch
Patch2:         libkkc-vala-abstract-create.patch

BuildRequires(pre): rpm-macros-valgrind
BuildRequires:  gcc-c++
BuildRequires:	marisa-devel
BuildRequires:	vala vala-tools valadoc-devel
BuildRequires:	pkgconfig(gee-0.8) libgee0.8-gir-devel
BuildRequires:	libjson-glib libjson-glib-devel libjson-glib-gir-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	python3-devel
BuildRequires:	python3-module-marisa
BuildRequires: chrpath
%ifarch %valgrind_arches
BuildRequires: /usr/bin/valgrind
%endif

Requires:	skkdic
Requires:	%{name}-data >= %{dataversion}
Requires:	%{name}-common = %{version}-%{release}
Source44: import.info

%description
libkkc provides a converter from Kana-string to
Kana-Kanji-mixed-string.  It was named after kkc.el in GNU Emacs, a
simple Kana Kanji converter, while libkkc tries to convert sentences
in a bit more complex way using N-gram language models.


%package	devel
Group: Other
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Group: Other
Summary:	Tools for %{name}
Requires:	%{name} = %{version}-%{release}

%description	tools
The %{name}-tools package contains tools for developing applications
that use %{name}.


%package	common
Group: Other
Summary:	Common data files for %{name}
BuildArch:	noarch
AutoReq: yes,nopython
AutoProv: yes,nopython

%description	common
The %{name}-common package contains the arch-independent data that
%{name} uses at run time.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1


[ -f README.md ] || cp -p %SOURCE1 .
autoreconf -f


%build
%configure --disable-static --disable-silent-rules PYTHON=python3
%make_build


%check
make check


%install
%makeinstall_std

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# https://bugzilla.redhat.com/show_bug.cgi?id=1987650
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/kkc

%find_lang %{name}





%files -f %{name}.lang
%doc README data/rules/README.rules COPYING
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib

%files common
%{_datadir}/libkkc

%files devel
#doc %_docdir/%name
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*

%files tools
%{_bindir}/kkc*


%changelog
* Tue Nov 14 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.3.5-alt1_24
- NMU: fixed FTBFS on LoongArch

* Thu Sep 29 2022 Igor Vlasenko <viy@altlinux.org> 0.3.5-alt1_23
- new version

